#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"

#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"


#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit1D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"

#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

#include <algorithm>

#include <boost/ptr_container/ptr_vector.hpp>
#include <boost/unordered_set.hpp>
#include <boost/foreach.hpp>
#define foreach BOOST_FOREACH

class TrackerOccupancyAnalyzer : public edm::EDProducer {
    public:
        TrackerOccupancyAnalyzer(const edm::ParameterSet &pset) ;
        ~TrackerOccupancyAnalyzer() ;

        virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup) ;

        class Classifier {
            public:
                Classifier(const char *det="ALL", int layer=0) : 
                    name_(det), 
                    layer_(layer) 
                {
                    if (layer != 0) {
                        char buff[25];
                        sprintf(buff, "%s%d",  det, layer);
                        name_ = buff;
                    }
                }

                virtual ~Classifier() {}
                virtual int layer(DetId detid) const { return 0; }

                void push(DetId detid, bool ontrack) {
                    int l = layer(detid);
                    if (layer_ == 0 ? l >= 0 : l == layer_) {
                        (*all_)++;
                        if (ontrack) (*on_)++;
                        else (*off_)++;
                    }
                }
                    
                void doProduces(edm::ProducerBase &prod) {
                    prod.produces<int>(name_);
                    prod.produces<int>(name_+"on");
                    prod.produces<int>(name_+"off");
                }

                void init() {
                    on_.reset(new int(0));
                    off_.reset(new int(0));
                    all_.reset(new int(0));
                }

                void out(edm::Event &iEvent) {
                    iEvent.put(all_, name_);
                    iEvent.put(on_,  name_+"on");
                    iEvent.put(off_, name_+"off");
                }

            private:
                std::string name_;
                int         layer_;
                std::auto_ptr<int> on_, off_, all_;
        };

        struct PIXELClassifier : public Classifier { 
            PIXELClassifier() : Classifier("PIXEL",0) {}
            virtual int layer(DetId detid) const { return detid.subdetId() <= 2 ? 0 : -1; }
        };
        struct STRIPClassifier : public Classifier { 
            STRIPClassifier() : Classifier("STRIP",0) {}
            virtual int layer(DetId detid) const { return detid.subdetId() >= 3 ? 0 : -1; }
        };
        struct PXBClassifier : public Classifier { 
            PXBClassifier(int layer=0) : Classifier("PXB",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 1 ? PXBDetId(detid).layer() : -1; }
        };
        struct PXFClassifier : public Classifier { 
            PXFClassifier(int layer=0) : Classifier("PXF",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 2 ? PXFDetId(detid).disk() : -1; }
        };
        struct TIBClassifier : public Classifier { 
            TIBClassifier(int layer=0) : Classifier("TIB",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 3 ? TIBDetId(detid).layer() : -1; }
        };
        struct TIDClassifier : public Classifier { 
            TIDClassifier(int layer=0) : Classifier("TID",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 4 ? TIDDetId(detid).wheel() : -1; }
        };
        struct TOBClassifier : public Classifier { 
            TOBClassifier(int layer=0) : Classifier("TOB",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 5 ? TOBDetId(detid).layer() : -1; }
        };
        struct TECClassifier : public Classifier { 
            TECClassifier(int layer=0) : Classifier("TEC",layer) {}
            virtual int layer(DetId detid) const { return detid.subdetId() == 6 ? TECDetId(detid).wheel() : -1; }
        };

        class ScoreBoard {
            public:
                void clear() { board_.clear(); }
                void mark(const TrackingRecHit & hit) {
                    const void *p = id(hit);
                    if (p) board_.insert(p);
                }
                bool test(const TrackingRecHit & hit) {
                    const void *p = id(hit);
                    return (p == 0 ? false : board_.count(p));
                }
                bool test(const void *p) {
                    return board_.count(p);
                }
                
            private:
                template<typename T> 
                const void * id_(const TrackingRecHit &hit) const {
                    return (typeid(T) == typeid(hit) ? &*(static_cast<const T &>(hit)).cluster() : 0);
                }
                const void * id(const TrackingRecHit &hit) {
                    const void *p = 0;
                    if ((p = id_<SiPixelRecHit>(hit))) return p;
                    if ((p = id_<SiStripRecHit2D>(hit))) return p;
                    if ((p = id_<SiStripRecHit1D>(hit))) return p;
                    return p;
                }
                boost::unordered_set<const void *> board_;
        };
    private:
        edm::InputTag tracks_; 
        edm::InputTag pixels_; 
        edm::InputTag strips_; 

        boost::ptr_vector<Classifier> classes_;

        ScoreBoard onTrack_;

        typedef StringCutObjectSelector<reco::Track> TkSel;
        typedef std::pair<std::string, TkSel>        TkCounter;
        std::vector<TkCounter> trackCounters_;

};

TrackerOccupancyAnalyzer::TrackerOccupancyAnalyzer(const edm::ParameterSet &iConfig) :
    tracks_(iConfig.getParameter<edm::InputTag>("tracks")),
    pixels_(iConfig.getParameter<edm::InputTag>("pixels")),
    strips_(iConfig.getParameter<edm::InputTag>("strips"))
{
    classes_.push_back(new Classifier("ALL"));
    classes_.push_back(new PIXELClassifier());
    classes_.push_back(new STRIPClassifier());
    for (int i=0; i<=4; ++i) { classes_.push_back(new TIBClassifier(i)); }
    for (int i=0; i<=6; ++i) { classes_.push_back(new TOBClassifier(i)); }
    for (int i=0; i<=3; ++i) { classes_.push_back(new TIDClassifier(i)); }
    for (int i=0; i<=9; ++i) { classes_.push_back(new TECClassifier(i)); }
    for (int i=0; i<=3; ++i) { classes_.push_back(new PXBClassifier(i)); }
    for (int i=0; i<=2; ++i) { classes_.push_back(new PXFClassifier(i)); }

    foreach(Classifier &c, classes_) { c.doProduces(*this); }

    produces<int>("NTK");
    if (iConfig.existsAs<edm::ParameterSet>("countTracks")) {
        edm::ParameterSet counters = iConfig.getParameter<edm::ParameterSet>("countTracks");
        foreach(const std::string &name, counters.getParameterNames()) {
            trackCounters_.push_back(TkCounter(name, TkSel(counters.getParameter<std::string>(name))));
            produces<int>("NTK"+name);
        }
    }
}

TrackerOccupancyAnalyzer::~TrackerOccupancyAnalyzer()
{
}

void
TrackerOccupancyAnalyzer::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) 
{
    edm::Handle<reco::TrackCollection> tracks;
    edm::Handle<edmNew::DetSetVector<SiPixelCluster> > pixels;
    edm::Handle<edmNew::DetSetVector<SiStripCluster> > strips;

    iEvent.getByLabel(tracks_, tracks);
    iEvent.getByLabel(pixels_, pixels);
    iEvent.getByLabel(strips_, strips);

    foreach(Classifier &c, classes_) { c.init(); }

    onTrack_.clear();
    foreach(const reco::Track &tk, *tracks) {
        for (trackingRecHit_iterator it = tk.recHitsBegin(), ed = tk.recHitsEnd(); it != ed; ++it) {
            onTrack_.mark(**it);
        }
    }

    foreach(edmNew::DetSet<SiStripCluster> det, *strips) {
        DetId detid(det.detId());
        foreach(const SiStripCluster &clust, det) {
            bool ontr = onTrack_.test(&clust);
            foreach(Classifier &c, classes_) { c.push(detid, ontr); }
        }
    } 

    foreach(edmNew::DetSet<SiPixelCluster> det, *pixels) {
        DetId detid(det.detId());
        foreach(const SiPixelCluster &clust, det) {
            bool ontr = onTrack_.test(&clust);
            foreach(Classifier &c, classes_) { c.push(detid, ontr); }
        }
    } 

    foreach(Classifier &c, classes_) { c.out(iEvent); }

    std::auto_ptr<int> ntk(new int(tracks->size()));
    iEvent.put(ntk, "NTK");
    foreach(const TkCounter &counter, trackCounters_) {
        ntk.reset(new int(std::count_if(tracks->begin(), tracks->end(), counter.second)));
        iEvent.put(ntk, "NTK"+counter.first);
    }
    
}


DEFINE_FWK_MODULE(TrackerOccupancyAnalyzer);
