// -*- C++ -*-
//
// Package:    TrackingPFG/Utilities
// Class:      RefittedTrackCoupler
// 
/**\class RefittedTrackCoupler RefittedTrackCoupler.cc TrackingPFG/Utilities/plugins/RefittedTrackCoupler.cc


 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Mon Dec 17 09:05:45 CET 2010
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/Common/interface/OneToOne.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "UserCode/TrackerTrackMixing/interface/TrackMixingAssociator.h"

//
// class decleration
//

class RefittedTrackCoupler : public edm::EDProducer {
   public:
      explicit RefittedTrackCoupler(const edm::ParameterSet&);
      ~RefittedTrackCoupler();

  typedef edm::AssociationMap<edm::OneToOne<reco::TrackCollection,reco::TrackCollection> > TrackPairCollection;

private:
  virtual void beginJob() ;
  virtual void beginRun(edm::Run&, const edm::EventSetup&);
  virtual void endRun(edm::Run&, const edm::EventSetup&);
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  const edm::InputTag m_firstTrackCollection;
  const edm::InputTag m_secondTrackCollection;
  const edm::InputTag m_stripClusterCollection;
  const edm::InputTag m_pixelClusterCollection;

};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
RefittedTrackCoupler::RefittedTrackCoupler(const edm::ParameterSet& iConfig):
  m_firstTrackCollection(iConfig.getParameter<edm::InputTag>("firstTrackCollection")),
  m_secondTrackCollection(iConfig.getParameter<edm::InputTag>("secondTrackCollection")),
  m_stripClusterCollection(iConfig.getParameter<edm::InputTag>("stripClusterCollection")),
  m_pixelClusterCollection(iConfig.getParameter<edm::InputTag>("pixelClusterCollection"))
{

  produces<TrackPairCollection,edm::InEvent>();

   //now do what ever other initialization is needed

}


RefittedTrackCoupler::~RefittedTrackCoupler()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
RefittedTrackCoupler::beginRun(edm::Run& iRun, const edm::EventSetup& iSetup) 
{
}

void 
RefittedTrackCoupler::endRun(edm::Run&, const edm::EventSetup&)
{
}


void
RefittedTrackCoupler::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  using namespace edm;
  
  std::auto_ptr<TrackPairCollection> trackpairs(new TrackPairCollection() );
  
  Handle<reco::TrackCollection> trkcoll1;
  iEvent.getByLabel(m_firstTrackCollection,trkcoll1);

  Handle<reco::TrackCollection> trkcoll2;
  iEvent.getByLabel(m_secondTrackCollection,trkcoll2);

  Handle<edmNew::DetSetVector<SiStripCluster> > stripclusters;
  iEvent.getByLabel(m_stripClusterCollection,stripclusters);

  Handle<edmNew::DetSetVector<SiPixelCluster> > pixelclusters;
  iEvent.getByLabel(m_pixelClusterCollection,pixelclusters);

  TrackMixingAssociator associator;

  associator.registerTrackEvent(0,*trkcoll2);
  associator.registerClusterEvent(0,*pixelclusters,*stripclusters);

  /*
  for(reco::TrackCollection::const_iterator trk1= trkcoll1->begin();trk1!=trkcoll1->end();++trk1) {
    for(reco::TrackCollection::const_iterator trk2= trkcoll2->begin();trk2!=trkcoll2->end();++trk2) {

      bool match = false;

      if(match) {
	const reco::TrackRef trkref1(trkcoll1,trk1-trkcoll1->begin());
	const reco::TrackRef trkref2(trkcoll2,trk2-trkcoll2->begin());
	trackpairs->insert(trkref1,trkref2);
      }

    }
  }
  */

  for(reco::TrackCollection::const_iterator trk1= trkcoll1->begin();trk1!=trkcoll1->end();++trk1) {

    std::vector<TrackMixingAssociator::TrackAssociation> trackAssos;
    associator.associateToTracks(*trk1, trackAssos);

    for(std::vector<TrackMixingAssociator::TrackAssociation>::const_iterator trka = trackAssos.begin(); trka!=trackAssos.end(); ++trka) {

      bool match = trka->sharedHits > 0.8 * std::min(trka->track->numberOfValidHits(), trk1->numberOfValidHits());

      if(match) {
	const reco::TrackRef trkref1(trkcoll1,trk1-trkcoll1->begin());
	const reco::TrackRef trkref2(trkcoll2,trka->track-&*(trkcoll2->begin()));
	trackpairs->insert(trkref1,trkref2);
      }

    }

  }  

  iEvent.put(trackpairs);

}

// ------------ method called once each job just before starting event loop  ------------
void 
RefittedTrackCoupler::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
RefittedTrackCoupler::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(RefittedTrackCoupler);
