// -*- C++ -*-
//
// Package:    Utilities
// Class:      JetSpectrumAnalyzer
// 
/**\class JetSpectrumAnalyzer JetSpectrumAnalyzer.cc TrackingPFG/Utilities/JetSpectrumAnalyzer.cc

 Description: 

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Tue Oct 21 20:55:22 CEST 2008
//
//


// system include files
#include <memory>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESWatcher.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/JetReco/interface/JetID.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/strbitset.h"

#include "TH1F.h"
#include "TH2F.h"

//
// class declaration
//

class JetSpectrumAnalyzer : public edm::EDAnalyzer {
   public:
      explicit JetSpectrumAnalyzer(const edm::ParameterSet&);
      ~JetSpectrumAnalyzer();

   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

  edm::InputTag m_jetCollection;
  edm::InputTag m_jetIDMap;
  const double m_etamaxcut;
  JetIDSelectionFunctor m_jetIDfunc;

  TH1F* m_hjetpt;
  TH2F* m_hjetptvseta;

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
JetSpectrumAnalyzer::JetSpectrumAnalyzer(const edm::ParameterSet& iConfig):
  m_jetCollection(iConfig.getParameter<edm::InputTag>("jetCollection")),
  m_jetIDMap(iConfig.getParameter<edm::InputTag>("jetIDMap")),
  m_etamaxcut(iConfig.getParameter<double>("maxRapidityCut")),
  m_jetIDfunc(JetIDSelectionFunctor::PURE09,JetIDSelectionFunctor::LOOSE)
{
   //now do what ever initialization is needed

  edm::Service<TFileService> tfserv;

  m_hjetpt = tfserv->make<TH1F>("jetpt","Max jet pt",200,0.,1000.);
  m_hjetptvseta = tfserv->make<TH2F>("jetptvseta","Max jet pt vs eta",20,-5.,5.,200,0.,1000.);

}

JetSpectrumAnalyzer::~JetSpectrumAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
JetSpectrumAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<reco::CaloJetCollection> jetcoll;
  iEvent.getByLabel(m_jetCollection,jetcoll);
  
  Handle<reco::JetIDValueMap> jetIDmap;
  iEvent.getByLabel(m_jetIDMap,jetIDmap);
  
  double maxjetpt = -1.;
  double maxjetpteta = 0.;

  for(unsigned int ijet=0;ijet<jetcoll->size();++ijet) {
    
    const reco::CaloJetRef jet(jetcoll,ijet);

    LogDebug("JetUnderTest") << "Jet with eta = " << jet->eta() << " and pt = " << jet->pt() << " under test";

    if( !(std::abs(jet->eta()) < m_etamaxcut)) continue;

    LogDebug("JetUnderTest") << "kincut passed";

    if(jetIDmap->contains(jet.id())) {
      
      const reco::JetID & jetid = (*jetIDmap)[jet];
      pat::strbitset ret = m_jetIDfunc.getBitTemplate();
      ret.set(false);
      bool goodjet = m_jetIDfunc((*jetcoll)[ijet],jetid,ret);
      if(goodjet) { 
	LogDebug("JetUnderTest") << "JetID passed";
	if(jet->pt() > maxjetpt) {
	  maxjetpt = jet->pt();
	  maxjetpteta = jet->eta();
	}
      }
      
    } else {
      edm::LogWarning("JetIDNotFound") << "JetID not found ";
      
    }
    
  }

  m_hjetpt->Fill(maxjetpt);
  m_hjetptvseta->Fill(maxjetpteta,maxjetpt);
  
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetSpectrumAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetSpectrumAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetSpectrumAnalyzer);
