// -*- C++ -*-
//
// Package:    TPAnalyzer
// Class:      TPAnalyzer
// 
/**\class TPAnalyzer TPAnalyzer.cc DebugTools/OverlapProblem/plugins/TPAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Thu Dec 16 16:32:56 CEST 2010
// $Id: TPAnalyzer.cc,v 1.1 2013/04/18 18:17:11 venturia Exp $
//
//


// system include files
#include <memory>
#include <numeric>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/UtilAlgos/interface/DetIdSelector.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TProfile2D.h"
//
// class decleration
//


class TPAnalyzer : public edm::EDAnalyzer {
public:
  explicit TPAnalyzer(const edm::ParameterSet&);
  ~TPAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  edm::InputTag m_tpcollection;
  std::vector<DetIdSelector> m_detsels;
  std::vector<std::string> m_selnames;
  std::vector<std::string> m_seltitles;

  TH1F* m_ptp;
  TH1F* m_etatp;
  TH1F* m_nhits;
  TH1F* m_pdgid;
  TH1F* m_llbit;
  TH1F* m_statustp;

  std::vector<TH1F*> m_selnhits;
  std::vector<TProfile*> m_selnhitsvseta;
  std::vector<TProfile2D*> m_selnhitsvsetavsphi;

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
TPAnalyzer::TPAnalyzer(const edm::ParameterSet& iConfig):
  m_tpcollection(iConfig.getParameter<edm::InputTag>("trackingParticlesCollection")),
  m_detsels(),m_selnames(),m_seltitles()

{
   //now do what ever initialization is needed



  edm::Service<TFileService> tfserv;

  m_ptp = tfserv->make<TH1F>("tpmomentum","Tracking Particle momentum",100,0.,200.);
  m_etatp = tfserv->make<TH1F>("tpeta","Tracking Particle pseudorapidity",100,-4.,4.);
  m_nhits = tfserv->make<TH1F>("nhits","Tracking Particle associated hits",100,-0.5,99.5);
  m_pdgid = tfserv->make<TH1F>("pdgid","Tracking Particle PDG id",1000,-500.5,499.5);
  m_llbit = tfserv->make<TH1F>("llbit","Tracking Particle LongLived bit",2,-0.5,1.5);
  m_statustp = tfserv->make<TH1F>("statustp","Tracking Particle status",2000,-1000.5,999.5);

  std::vector<edm::ParameterSet> wantedsubds(iConfig.getParameter<std::vector<edm::ParameterSet> >("wantedSubDets"));
					     
  std::cout << "selections found: " << wantedsubds.size() << std::endl;

  for(std::vector<edm::ParameterSet>::iterator ps=wantedsubds.begin();ps!=wantedsubds.end();++ps) {
    m_selnames.push_back(ps->getParameter<std::string>("name"));
    m_seltitles.push_back(ps->getParameter<std::string>("title"));
    m_detsels.push_back(DetIdSelector(ps->getParameter<std::vector<std::string> >("selection")));

    std::string name = "nhits_" + ps->getParameter<std::string>("name");
    std::string title = "Number of Sim Hits per Track " + ps->getParameter<std::string>("title");
    m_selnhits.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),50,-0.5,49.5));
    name = "nhitsvseta_" + ps->getParameter<std::string>("name");
    title = "Average Number of Sim Hits per Track vs eta " + ps->getParameter<std::string>("title");
    m_selnhitsvseta.push_back(tfserv->make<TProfile>(name.c_str(),title.c_str(),120,-3.,3.));
    name = "nhitsvsetavsphi_" + ps->getParameter<std::string>("name");
    title = "Average Number of Sim Hits per Track vs eta and phi " + ps->getParameter<std::string>("title");
    m_selnhitsvsetavsphi.push_back(tfserv->make<TProfile2D>(name.c_str(),title.c_str(),30,-3.,3.,120,-acos(-1.),acos(-1.)));
    
  }
}


TPAnalyzer::~TPAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
TPAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

   // reco track Handle

  Handle<TrackingParticleCollection> tpcoll;
  iEvent.getByLabel(m_tpcollection,tpcoll);
    
  // loop on Handle with index and use find
  
  for(unsigned int index=0 ; index != tpcoll->size() ; ++index) {
    
    // get TrackingParticleRef
    
    const TrackingParticleRef tp(tpcoll,index);
    
    if(std::abs(tp->pdgId())!=13) continue;
    
    // get the SimHIt from tracker only
    
    //    std::vector<PSimHit> tksimhits = tp->trackPSimHit(DetId::Tracker);
    
    
    m_ptp->Fill(tp->p());
    m_etatp->Fill(tp->eta());
    //    m_nhits->Fill(tksimhits.size());
    m_nhits->Fill(tp->numberOfTrackerHits());
    
    
    m_pdgid->Fill(tp->pdgId());
    m_llbit->Fill(tp->longLived());
    m_statustp->Fill(tp->status());
    
    // loop on sim hits

    std::vector<int> nhits(m_detsels.size(),0);

    // This loop is no more possible with the new TP's    
    /*
    for( std::vector<PSimHit>::const_iterator sh = tksimhits.begin(); sh!= tksimhits.end(); ++sh) {

      for(unsigned int i=0;i<m_detsels.size();++i) {
	if(m_detsels[i].isSelected(sh->detUnitId())) ++nhits[i];
      }
      
    }
    */

    for(unsigned int i=0;i<nhits.size();++i) {
      m_selnhits[i]->Fill(nhits[i]);
      m_selnhitsvseta[i]->Fill(tp->eta(),nhits[i]);
      m_selnhitsvsetavsphi[i]->Fill(tp->eta(),tp->phi(),nhits[i]);
    }
  }
  
}

void 
TPAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{
}

void 
TPAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup&)
{
}



// ------------ method called once each job just before starting event loop  ------------
void 
TPAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TPAnalyzer::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(TPAnalyzer);
