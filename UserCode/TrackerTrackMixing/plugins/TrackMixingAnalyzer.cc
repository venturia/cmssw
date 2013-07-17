#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "UserCode/TrackerTrackMixing/interface/TrackMixingAssociator.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

#include <algorithm>

class TrackMixingAnalyzer : public edm::EDProducer {
    public:
        TrackMixingAnalyzer(const edm::ParameterSet &pset) ;
        ~TrackMixingAnalyzer() ;

        virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup) ;

    private:
        edm::InputTag tracksSignal_; 
        edm::InputTag pixelsSignal_; 
        edm::InputTag stripsSignal_; 
        edm::InputTag mixData_;
        edm::InputTag tracksMix_;
        edm::InputTag pixelsMix_;
        edm::InputTag stripsMix_;
        uint32_t      pileupEvents_;

        StringCutObjectSelector<reco::Track> cut_;
        double minFraction_;

        bool debug_;
};

TrackMixingAnalyzer::TrackMixingAnalyzer(const edm::ParameterSet &iConfig) :
    tracksSignal_(iConfig.getParameter<edm::InputTag>("tracksSignal")),
    pixelsSignal_(iConfig.getParameter<edm::InputTag>("pixelsSignal")),
    stripsSignal_(iConfig.getParameter<edm::InputTag>("stripsSignal")),
    mixData_(iConfig.getParameter<edm::InputTag>("mixData")),
    tracksMix_(iConfig.getParameter<edm::InputTag>("tracksMix")),
    pileupEvents_(iConfig.getParameter<uint32_t>("pileupEvents")),
    cut_(iConfig.getParameter<std::string>("cut")),
    minFraction_(iConfig.getParameter<double>("minSharedHitFraction")),
    debug_(iConfig.getUntrackedParameter<bool>("debug", false))
{
    produces<reco::TrackCollection>("stable");
    produces<reco::TrackCollection>("gained");
    produces<reco::TrackCollection>("lost");
}

TrackMixingAnalyzer::~TrackMixingAnalyzer()
{
}

void
TrackMixingAnalyzer::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) 
{
    TrackMixingAssociator associator, backassociator;
    edm::Handle<reco::TrackCollection> tracksHandle;
    edm::Handle<edmNew::DetSetVector<SiPixelCluster> > pixelsHandle;
    edm::Handle<edmNew::DetSetVector<SiStripCluster> > stripsHandle;

    iEvent.getByLabel(tracksSignal_, tracksHandle);
    iEvent.getByLabel(pixelsSignal_, pixelsHandle);
    iEvent.getByLabel(stripsSignal_, stripsHandle);
    associator.registerTrackEvent(0, *tracksHandle);
    associator.registerClusterEvent(0, *pixelsHandle, *stripsHandle);

    for (size_t i = 0; i < pileupEvents_; ++i) {
        char buff[10]; sprintf(buff,"e%lu", i);
        iEvent.getByLabel(edm::InputTag(mixData_.label(), buff, mixData_.process()), tracksHandle);
        iEvent.getByLabel(edm::InputTag(mixData_.label(), buff, mixData_.process()), stripsHandle);
        iEvent.getByLabel(edm::InputTag(mixData_.label(), buff, mixData_.process()), pixelsHandle);
        associator.registerTrackEvent(i+1, *tracksHandle);
        associator.registerClusterEvent(i+1, *pixelsHandle, *stripsHandle);
    }

    iEvent.getByLabel(tracksMix_, tracksHandle);
    std::vector<TrackMixingAssociator::TrackAssociation> trackAssos;
    std::vector<TrackMixingAssociator::TrackClusterAssociation> clusterAssos;
    backassociator.registerTrackEvent(0, *tracksHandle);

    std::auto_ptr<reco::TrackCollection> stable(new reco::TrackCollection());
    std::auto_ptr<reco::TrackCollection> gained(new reco::TrackCollection());
    std::auto_ptr<reco::TrackCollection> lost(new reco::TrackCollection());

    if (debug_) printf("\nMixed Event\n");
    for (reco::TrackCollection::const_iterator it = tracksHandle->begin(), ed = tracksHandle->end(); it != ed; ++it) {
        if (!cut_(*it)) continue;

        if (debug_) {
            printf("Track pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                    it->pt(), it->eta(), it->phi(),
                    it->numberOfValidHits(), it->hitPattern().numberOfValidPixelHits(), 
                    it->hitPattern().trackerLayersWithMeasurement(), it->hitPattern().numberOfLostHits(),
                    it->normalizedChi2());
        }

        associator.associateToTracks(*it, trackAssos);
        bool associated = false;
        for (std::vector<TrackMixingAssociator::TrackAssociation>::const_iterator ita = trackAssos.begin(), eda = trackAssos.end(); ita != eda; ++ita) {
            if (debug_) {
                printf(" - assoc. track (event %d, %2d hits): pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                        ita->eventId, ita->sharedHits,
                        ita->track->pt(), ita->track->eta(), ita->track->phi(),
                        ita->track->numberOfValidHits(), ita->track->hitPattern().numberOfValidPixelHits(), 
                        ita->track->hitPattern().trackerLayersWithMeasurement(), ita->track->hitPattern().numberOfLostHits(),
                        ita->track->normalizedChi2());
            }
            if (ita->sharedHits >= 3 && (ita->sharedHits >= minFraction_ * std::min(ita->track->numberOfValidHits(), it->numberOfValidHits()))) {
               stable->push_back(*it); 
               associated = true;
            }
        }
        if (associated == false) gained->push_back(*it);

        if (debug_) {
            associator.associateToClusters(*it, clusterAssos);
            for (std::vector<TrackMixingAssociator::TrackClusterAssociation>::const_iterator ita = clusterAssos.begin(), eda = clusterAssos.end(); ita != eda; ++ita) {
                printf(" - assoc. clusters (event %d, %2d exclusive hits, %2d merged hits)\n",
                    ita->eventId, int(ita->exclusiveHits), int(ita->sharedHits));
            }
        }

    }
    
    for (size_t i = 0; i <= pileupEvents_; ++i) {
        if (i == 0) {
            iEvent.getByLabel(tracksSignal_, tracksHandle);
        } else {
            char buff[10]; sprintf(buff,"e%lu", i-1);
            iEvent.getByLabel(edm::InputTag(mixData_.label(), buff, mixData_.process()), tracksHandle);
        }
        if (debug_) printf("\nSource Event %lu\n", i);

        for (reco::TrackCollection::const_iterator it = tracksHandle->begin(), ed = tracksHandle->end(); it != ed; ++it) {
            if (!cut_(*it)) continue;
        
            if (debug_) {
                printf("Track pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                        it->pt(), it->eta(), it->phi(),
                        it->numberOfValidHits(), it->hitPattern().numberOfValidPixelHits(), 
                        it->hitPattern().trackerLayersWithMeasurement(), it->hitPattern().numberOfLostHits(),
                        it->normalizedChi2());
            }

            backassociator.associateToTracks(*it, trackAssos);
            bool associated = false;
            for (std::vector<TrackMixingAssociator::TrackAssociation>::const_iterator ita = trackAssos.begin(), eda = trackAssos.end(); ita != eda; ++ita) {
                if (debug_) {
                    printf(" - assoc. track (%2d hits): pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                            ita->sharedHits,
                            ita->track->pt(), ita->track->eta(), ita->track->phi(),
                            ita->track->numberOfValidHits(), ita->track->hitPattern().numberOfValidPixelHits(), 
                            ita->track->hitPattern().trackerLayersWithMeasurement(), ita->track->hitPattern().numberOfLostHits(),
                            ita->track->normalizedChi2());
                }
                if (ita->sharedHits >= 3 && (ita->sharedHits >= minFraction_ * std::min(ita->track->numberOfValidHits(), it->numberOfValidHits()))) {
                    associated = true;
                    break;
                }
            }
            if (associated == false) lost->push_back(*it);
        }

    }

    iEvent.put(lost,"lost");
    iEvent.put(gained,"gained");
    iEvent.put(stable,"stable");
}


DEFINE_FWK_MODULE(TrackMixingAnalyzer);
