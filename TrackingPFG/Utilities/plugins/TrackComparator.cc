// -*- C++ -*-
//
// Package:    TrackComparator
// Class:      TrackComparator
// 
/**\class TrackComparator TrackComparator.cc TrackingPFG/Utilities/src/TrackComparator.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Thu Dec 16 16:32:56 CEST 2010
// $Id: TrackComparator.cc,v 1.1 2011/02/03 22:35:27 venturia Exp $
//
//


// system include files
#include <memory>
#include <numeric>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/Common/interface/OneToOne.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"


#include "TH1F.h"
#include "TProfile.h"
#include "TProfile2D.h"

//
// class decleration
//


class TrackComparator : public edm::EDAnalyzer {
public:
  explicit TrackComparator(const edm::ParameterSet&);
  ~TrackComparator();
  
  typedef edm::AssociationMap<edm::OneToOne<reco::TrackCollection,reco::TrackCollection> > TrackPairCollection;
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  TH1F* m_hdpoverp;
  TH1F* m_hdqoverp;
  TH1F* m_hdptoverpt;
  TH1F* m_hdqoverpt;

  TProfile* m_hdpoverpvseta;
  TProfile* m_hdqoverpvseta;
  TProfile* m_hdptoverptvseta;
  TProfile* m_hdqoverptvseta;

  TProfile2D* m_hdpoverpvsetaphi;
  TProfile2D* m_hdqoverpvsetaphi;
  TProfile2D* m_hdptoverptvsetaphi;
  TProfile2D* m_hdqoverptvsetaphi;

  edm::InputTag m_trkpaircollection;
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
TrackComparator::TrackComparator(const edm::ParameterSet& iConfig):
  m_trkpaircollection(iConfig.getParameter<edm::InputTag>("trackPairCollection"))

{
   //now do what ever initialization is needed



  edm::Service<TFileService> tfserv;

  m_hdpoverp = tfserv->make<TH1F>("dpoverp","#Delta(p)/p",400,-0.01,0.01);
  m_hdqoverp = tfserv->make<TH1F>("dqoverp","#Delta(q/p)",400,-0.0001,0.0001);
  m_hdptoverpt = tfserv->make<TH1F>("dptoverpt","#Delta(pt)/pt",400,-0.01,0.01);
  m_hdqoverpt = tfserv->make<TH1F>("dqoverpt","#Delta(q/pt)",400,-0.0001,0.0001);

  m_hdpoverpvseta = tfserv->make<TProfile>("dpoverpvseta","#Delta(p)/p vs #eta",30,-3.,3.);
  m_hdqoverpvseta = tfserv->make<TProfile>("dqoverpvseta","#Delta(q/p) vs #eta",30,-3.,3.);
  m_hdptoverptvseta = tfserv->make<TProfile>("dptoverptvseta","#Delta(pt)/pt vs #eta",30,-3.,3.);
  m_hdqoverptvseta = tfserv->make<TProfile>("dqoverptvseta","#Delta(q/pt) vs #eta",30,-3.,3.);

  m_hdpoverpvsetaphi = tfserv->make<TProfile2D>("dpoverpvsetaphi","#Delta(p)/p vs #eta vs #phi",20,-M_PI,M_PI,30,-3.,3.);
  m_hdqoverpvsetaphi = tfserv->make<TProfile2D>("dqoverpvsetaphi","#Delta(q/p) vs #eta vs #phi",20,-M_PI,M_PI,30,-3.,3.);
  m_hdptoverptvsetaphi = tfserv->make<TProfile2D>("dptoverptvsetaphi","#Delta(pt)/pt vs #eta vs #phi",20,-M_PI,M_PI,30,-3.,3.);
  m_hdqoverptvsetaphi = tfserv->make<TProfile2D>("dqoverptvsetaphi","#Delta(q/pt) vs #eta vs #phi",20,-M_PI,M_PI,30,-3.,3.);

}


TrackComparator::~TrackComparator()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
TrackComparator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<TrackPairCollection> trackpairs;
   iEvent.getByLabel(m_trkpaircollection,trackpairs);

   //

   for(TrackPairCollection::const_iterator pair=trackpairs->begin();pair!=trackpairs->end();++pair) {

     const reco::TrackRef & trk1 = pair->key;
     const reco::TrackRef & trk2 = pair->val;

     double dpoverp = trk1->p()!=0 ? (trk2->p()-trk1->p())/trk1->p() : 0.;
     double dptoverpt = trk1->pt()!=0 ? (trk2->pt()-trk1->pt())/trk1->pt() : 0.;

     double dqoverp = trk1->p()!=0 && trk2->p()!=0 ? (trk2->qoverp()-trk1->qoverp()) : 0.;
     double dqoverpt = trk1->pt()!=0 && trk2->pt()!=0 ? ((trk2->charge()/trk2->pt())-(trk1->charge()/trk1->pt())) : 0.;

     double eta = trk1->eta();
     double phi = trk1->phi();

     m_hdpoverp->Fill(dpoverp);
     m_hdqoverp->Fill(dqoverp);
     m_hdptoverpt->Fill(dptoverpt);
     m_hdqoverpt->Fill(dqoverpt);

     m_hdpoverpvseta->Fill(eta,dpoverp);
     m_hdqoverpvseta->Fill(eta,dqoverp);
     m_hdptoverptvseta->Fill(eta,dptoverpt);
     m_hdqoverptvseta->Fill(eta,dqoverpt);
     
     m_hdpoverpvsetaphi->Fill(phi,eta,dpoverp);
     m_hdqoverpvsetaphi->Fill(phi,eta,dqoverp);
     m_hdptoverptvsetaphi->Fill(phi,eta,dptoverpt);
     m_hdqoverptvsetaphi->Fill(phi,eta,dqoverpt);
     
   }



}

void 
TrackComparator::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{
}

void 
TrackComparator::endRun(const edm::Run& iRun, const edm::EventSetup&)
{
}



// ------------ method called once each job just before starting event loop  ------------
void 
TrackComparator::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TrackComparator::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackComparator);
