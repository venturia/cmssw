// -*- C++ -*-
//
// Package:    Utilities
// Class:      BoolAnalyzer
// 
/**\class BoolAnalyzer BoolAnalyzer.cc TrackingPFG/Utilities/BoolAnalyzer.cc

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

#include "TH1F.h"

//
// class declaration
//

class BoolAnalyzer : public edm::EDAnalyzer {
   public:
      explicit BoolAnalyzer(const edm::ParameterSet&);
      ~BoolAnalyzer();

   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

  edm::InputTag m_src;

  TH1F* m_hbool;

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
BoolAnalyzer::BoolAnalyzer(const edm::ParameterSet& iConfig):
  m_src(iConfig.getParameter<edm::InputTag>("src"))
{
   //now do what ever initialization is needed

  edm::Service<TFileService> tfserv;

  m_hbool = tfserv->make<TH1F>("bool","bool value",2,-0.5,1.5);

}

BoolAnalyzer::~BoolAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
void
BoolAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<bool> bools;
  iEvent.getByLabel(m_src,bools);

  m_hbool->Fill(*bools);
  
  
}

// ------------ method called once each job just before starting event loop  ------------
void 
BoolAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BoolAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(BoolAnalyzer);
