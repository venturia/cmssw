// -*- C++ -*-
//
// Package:    LogErrorAnalyzer
// Class:      LogErrorAnalyzer
// 
/**\class LogErrorAnalyzer LogErrorAnalyzer.cc TrackingPFG/Utilities/src/LogErrorAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Thu Dec 16 16:32:56 CEST 2010
// $Id: LogErrorAnalyzer.cc,v 1.2 2011/07/22 07:43:42 venturia Exp $
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
#include "FWCore/MessageLogger/interface/ErrorSummaryEntry.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "TH1F.h"
#include "TH2F.h"
//
// class decleration
//


class LogErrorAnalyzer : public edm::EDAnalyzer {
public:
  explicit LogErrorAnalyzer(const edm::ParameterSet&);
  ~LogErrorAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  TH1F* m_nese;
  TH1F* m_nerrors;

  TH1F* m_ncatmod;
  TH1F* m_ncountcatmod;

  /*
  TH2F* m_ncatvsmod;
  TH2F* m_ncountcatvsmod;
  */

  edm::InputTag m_logerrcollection;
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
LogErrorAnalyzer::LogErrorAnalyzer(const edm::ParameterSet& iConfig):
  m_logerrcollection(iConfig.getParameter<edm::InputTag>("logErrCollection"))

{
   //now do what ever initialization is needed



  edm::Service<TFileService> tfserv;

  m_nese = tfserv->make<TH1F>("nese","Number of ErrorSummaryEntries",50,-0.5,49.5);
  m_nerrors = tfserv->make<TH1F>("nerrors","Number of Errors",100,-0.5,100.5);

  m_ncatmod = tfserv->make<TH1F>("ncatmod","Error Categories and Modules",10,0.,10.);
  m_ncatmod->SetBit(TH1::kCanRebin);
  m_ncountcatmod = tfserv->make<TH1F>("ncountcatmod","Error Categories and Modules counts",10,0.,10.);
  m_ncountcatmod->SetBit(TH1::kCanRebin);
  
  /*
  m_ncatvsmod = tfserv->make<TH2F>("ncatvsmod","Error Categories and Modules",10,0.,10.,10,0.,10.);
  m_ncatvsmod->SetBit(TH1::kCanRebin);
  m_ncountcatvsmod = tfserv->make<TH2F>("ncountcatvsmod","Error Categories and Modules counts",10,0.,10.,10,0.,10.);
  m_ncountcatvsmod->SetBit(TH1::kCanRebin);
  */  

}


LogErrorAnalyzer::~LogErrorAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
LogErrorAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<std::vector<ErrorSummaryEntry> > errors;
   iEvent.getByLabel(m_logerrcollection,errors);

   //

   int nese = 0;
   int nerrors = 0;

   for(std::vector<ErrorSummaryEntry>::const_iterator err = errors->begin(); err!= errors->end() ; ++err) {

     if(err->severity.getLevel() == edm::ELseverityLevel::ELsev_error // ||
	//	err->severity.getLevel() == edm::ELseverityLevel::ELsev_warning ||
	//	err->severity.getLevel() == edm::ELseverityLevel::ELsev_error2  
	) {

       ++nese;
       nerrors += err->count;

       std::string catmod = err->category + ":" + err->module;

       m_ncatmod->Fill(catmod.c_str(),1.);
       m_ncountcatmod->Fill(catmod.c_str(),err->count);

       /*
       m_ncatvsmod->Fill(err->module.c_str(),err->category.c_str(),1.);
       m_ncountcatvsmod->Fill(err->module.c_str(),err->category.c_str(),err->count);
       */

     }

   }

   m_nese->Fill(nese);
   m_nerrors->Fill(nerrors);


}

void 
LogErrorAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{
}

void 
LogErrorAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup&)
{
}



// ------------ method called once each job just before starting event loop  ------------
void 
LogErrorAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LogErrorAnalyzer::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(LogErrorAnalyzer);
