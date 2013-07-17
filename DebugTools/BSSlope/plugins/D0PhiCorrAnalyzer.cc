// -*- C++ -*-
//
// Package:    D0PhiCorrAnalyzer
// Class:      D0PhiCorrAnalyzer
// 
/**\class D0PhiCorrAnalyzer D0PhiCorrAnalyzer.cc DebugTools/BSSlope/plugins/D0PhiCorrAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  2011/04/06
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// my includes

#include "TH2D.h"
#include "TProfile.h"
#include "TProfile2D.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

//
// class decleration
//

class D0PhiCorrAnalyzer : public edm::EDAnalyzer {
public:
  explicit D0PhiCorrAnalyzer(const edm::ParameterSet&);
  ~D0PhiCorrAnalyzer();
  
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  TProfile2D* m_hdxyvsphivsz;
  TProfile2D* m_hdxyvsphivsznocorr;
  TProfile* m_hdxyvsphi;
  TProfile* m_hdxyvsphinocorr;
  TH2D* m_hdxyvsphi2D;
  TH2D* m_hdxyvsphinocorr2D;
  TH1D* m_hdxy;
  TH1D* m_hdxynocorr;

  edm::InputTag m_trkcollection;
  edm::InputTag m_bscollection;
  const bool m_weightError;

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
D0PhiCorrAnalyzer::D0PhiCorrAnalyzer(const edm::ParameterSet& iConfig):
  m_trkcollection(iConfig.getParameter<edm::InputTag>("trackCollection")),
  m_bscollection(iConfig.getParameter<edm::InputTag>("bsCollection")),
  m_weightError(iConfig.getParameter<bool>("errorAsWeight"))
  

{
   //now do what ever initialization is needed

  edm::LogInfo("TrackCollection") << "Using collection " << m_trkcollection.label().c_str() ;


  edm::Service<TFileService> tfserv;

  m_hdxyvsphivsz = tfserv->make<TProfile2D>("hdxyvsphivsz","Impact parameter vs phi vs z",180,-M_PI,M_PI,24,-20.,20.,-.1,.1);
  m_hdxyvsphivsznocorr = tfserv->make<TProfile2D>("hdxyvsphivsznocorr","Impact parameter vs phi vs z (no slope correction)",180,-M_PI,M_PI,24,-20.,20.,-.1,.1);

  m_hdxyvsphi = tfserv->make<TProfile>("hdxyvsphi","Impact parameter vs phi",180,-M_PI,M_PI,-.1,.1);
  m_hdxyvsphinocorr = tfserv->make<TProfile>("hdxyvsphinocorr","Impact parameter vs phi (no slope correction)",180,-M_PI,M_PI,-.1,.1);

  m_hdxyvsphi2D = tfserv->make<TH2D>("hdxyvsphi2D","Impact parameter vs phi",180,-M_PI,M_PI,500,-.05,.05);
  m_hdxyvsphinocorr2D = tfserv->make<TH2D>("hdxyvsphinocorr2D","Impact parameter vs phi (no slope correction)",180,-M_PI,M_PI,500,-.05,.05);

  m_hdxy = tfserv->make<TH1D>("hdxy","Impact parameter",2000,-1.,1.);
  m_hdxynocorr = tfserv->make<TH1D>("hdxynocorr","Impact parameter (no slope correction)",2000,-1.,1.);


}


D0PhiCorrAnalyzer::~D0PhiCorrAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
D0PhiCorrAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   edm::Service<TFileService> tfserv;

   Handle<reco::TrackCollection> tracks;
   iEvent.getByLabel(m_trkcollection,tracks);

   Handle<reco::BeamSpot> bs;
   iEvent.getByLabel(m_bscollection,bs);

   //

   for(reco::TrackCollection::const_iterator it = tracks->begin();it!=tracks->end();it++) {
     
     double weight = 1.;
     if(m_weightError) weight = 1/(it->dxyError()*it->dxyError());

     m_hdxyvsphivsz->Fill(it->phi(),it->vz(),it->dxy(*bs),weight);
     m_hdxyvsphivsznocorr->Fill(it->phi(),it->vz(),it->dxy(bs->position()),weight);
     m_hdxyvsphi->Fill(it->phi(),it->dxy(*bs),weight);
     m_hdxyvsphinocorr->Fill(it->phi(),it->dxy(bs->position()),weight);
     m_hdxyvsphi2D->Fill(it->phi(),it->dxy(*bs),weight);
     m_hdxyvsphinocorr2D->Fill(it->phi(),it->dxy(bs->position()),weight);
     m_hdxy->Fill(it->dxy(*bs),weight);
     m_hdxynocorr->Fill(it->dxy(bs->position()),weight);

   }


}

void 
D0PhiCorrAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{}

void 
D0PhiCorrAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup&)
{}



// ------------ method called once each job just before starting event loop  ------------
void 
D0PhiCorrAnalyzer::beginJob()
{}

// ------------ method called once each job just after ending the event loop  ------------
void 
D0PhiCorrAnalyzer::endJob() 
{}

//define this as a plug-in
DEFINE_FWK_MODULE(D0PhiCorrAnalyzer);
