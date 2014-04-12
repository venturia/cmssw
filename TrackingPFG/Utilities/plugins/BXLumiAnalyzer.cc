// -*- C++ -*-
//
// Package:    BXLumiAnalyzer
// Class:      BXLumiAnalyzer
// 
/**\class BXLumiAnalyzer BXLumiAnalyzer.cc TrackingPFG/Utilities/src/BXLumiAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Thu Dec 16 16:32:56 CEST 2010
// $Id: BXLumiAnalyzer.cc,v 1.3 2011/11/15 10:00:18 venturia Exp $
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
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Luminosity/interface/LumiDetails.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DPGAnalysis/SiStripTools/interface/RunHistogramManager.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
//
// class decleration
//


class BXLumiAnalyzer : public edm::EDAnalyzer {
public:
  explicit BXLumiAnalyzer(const edm::ParameterSet&);
  ~BXLumiAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  RunHistogramManager m_rhm;
  const unsigned int m_maxLS;
  const bool m_runHisto;
  TH1F* m_hlumi;
  TProfile** m_hlumivsorbrun;
  edm::InputTag m_lumicollection;
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
BXLumiAnalyzer::BXLumiAnalyzer(const edm::ParameterSet& iConfig):
  m_rhm(consumesCollector()),m_maxLS(iConfig.getParameter<unsigned int>("maxLSBeforeRebin")),
  m_runHisto(iConfig.getParameter<bool>("runHisto")),
  m_lumicollection(iConfig.getParameter<edm::InputTag>("lumiCollection"))

{
   //now do what ever initialization is needed



  edm::Service<TFileService> tfserv;

  m_hlumi = tfserv->make<TH1F>("lumi","BX luminosity",250,0.,10.);
  m_hlumi->GetXaxis()->SetTitle("BX lumi [10^{30}cm^{-2}s^{-1}]");

  if(m_runHisto) {
    m_hlumivsorbrun = m_rhm.makeTProfile("lumivsorbrun","BX lumi vs orbit number",m_maxLS,0.5,m_maxLS*262144+0.5);
  }

}


BXLumiAnalyzer::~BXLumiAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
BXLumiAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

  edm::Handle<LumiDetails> ld;
  iEvent.getLuminosityBlock().getByLabel(m_lumicollection,ld);

  float bxlumi = -1.;

  if(ld.isValid()) {
    if(ld->isValid()) {
      bxlumi = ld->lumiValue(LumiDetails::kOCC1,iEvent.bunchCrossing())*6.37;
      m_hlumi->Fill(bxlumi);
      if(m_runHisto) {
	if(m_hlumivsorbrun && *m_hlumivsorbrun) (*m_hlumivsorbrun)->Fill(iEvent.orbitNumber(),bxlumi);
      }
    }
  }

}

void 
BXLumiAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{

  m_rhm.beginRun(iRun);

  if(m_runHisto) {
    (*m_hlumivsorbrun)->GetXaxis()->SetTitle("time [orbit#]");   (*m_hlumivsorbrun)->GetYaxis()->SetTitle("BX lumi [10^{30}cm^{-2}s^{-1}]"); 
    (*m_hlumivsorbrun)->SetBit(TH1::kCanRebin);
  }

}

void 
BXLumiAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup&)
{
}



// ------------ method called once each job just before starting event loop  ------------
void 
BXLumiAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BXLumiAnalyzer::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(BXLumiAnalyzer);
