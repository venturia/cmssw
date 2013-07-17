#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "UserCode/TrackerTrackMixing/interface/TrackMixingAssociator.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

class TrackDiff : public edm::EDProducer {
    public:
        TrackDiff(const edm::ParameterSet &pset) ;
        ~TrackDiff() ;

        virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup) ;

    private:
        edm::InputTag tracksBefore_; 
        edm::InputTag tracksAfter_;

        StringCutObjectSelector<reco::Track> cut_;
        float minFraction_;
};

TrackDiff::TrackDiff(const edm::ParameterSet &iConfig) :
    tracksBefore_(iConfig.getParameter<edm::InputTag>("tracksBefore")),
    tracksAfter_(iConfig.getParameter<edm::InputTag>("tracksAfter")),
    cut_(iConfig.getParameter<std::string>("cut")),
    minFraction_(iConfig.getParameter<double>("minFraction"))
{
    produces<reco::TrackCollection>("gained");
    produces<reco::TrackCollection>("lost");
    produces<reco::TrackCollection>("stable");
}

TrackDiff::~TrackDiff()
{
}

void
TrackDiff::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) 
{
    TrackMixingAssociator associator;

    std::auto_ptr<reco::TrackCollection> gained(new reco::TrackCollection());
    std::auto_ptr<reco::TrackCollection> stable(new reco::TrackCollection());
    std::auto_ptr<reco::TrackCollection> lost(new reco::TrackCollection());

    edm::Handle<reco::TrackCollection> tracksBefore, tracksAfter;

    iEvent.getByLabel(tracksBefore_, tracksBefore);
    iEvent.getByLabel(tracksAfter_,  tracksAfter);

    associator.registerTrackEvent(0, *tracksBefore);
    associator.registerTrackEvent(1, *tracksAfter);

    std::vector<TrackMixingAssociator::TrackAssociation> trackAssos;

    for (reco::TrackCollection::const_iterator it = tracksAfter->begin(), ed = tracksAfter->end(); it != ed; ++it) {
        if (!cut_(*it)) continue;
            associator.associateToTracks(*it, trackAssos);
        bool found = false;
        for (std::vector<TrackMixingAssociator::TrackAssociation>::const_iterator ita = trackAssos.begin(), eda = trackAssos.end(); ita != eda; ++ita) {
            if (ita->eventId == 1) continue;
            if (ita->sharedHits >= minFraction_ * it->numberOfValidHits()) { found = true; break; }
        }

        if (found == false) {
            gained->push_back(*it); 
            printf("Gained track pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                    it->pt(), it->eta(), it->phi(),
                    it->numberOfValidHits(), it->hitPattern().numberOfValidPixelHits(), 
                    it->hitPattern().trackerLayersWithMeasurement(), it->hitPattern().numberOfLostHits(),
                    it->normalizedChi2());
        } else {
            stable->push_back(*it);
        }

    }
    for (reco::TrackCollection::const_iterator it = tracksBefore->begin(), ed = tracksBefore->end(); it != ed; ++it) {
        if (!cut_(*it)) continue;
        associator.associateToTracks(*it, trackAssos);
        bool found = false;
        for (std::vector<TrackMixingAssociator::TrackAssociation>::const_iterator ita = trackAssos.begin(), eda = trackAssos.end(); ita != eda; ++ita) {
            if (ita->eventId == 0) continue;
            if (ita->sharedHits >= minFraction_ * it->numberOfValidHits()) { found = true; break; }
        }

        if (found == false) {
            lost->push_back(*it); 
            printf("Lost track pt %4.1f, eta %-4.2f, phi %-4.2f; hits %2d (pixel %1d), layers %2d, lost hits %2d; c2/ndf %5.1f\n",
                    it->pt(), it->eta(), it->phi(),
                    it->numberOfValidHits(), it->hitPattern().numberOfValidPixelHits(), 
                    it->hitPattern().trackerLayersWithMeasurement(), it->hitPattern().numberOfLostHits(),
                    it->normalizedChi2());
        }

    }

    iEvent.put(gained, "gained");
    iEvent.put(stable, "stable");
    iEvent.put(lost,   "lost");
    
}


DEFINE_FWK_MODULE(TrackDiff);
