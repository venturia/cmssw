// -*- C++ -*-
//
// Package:    SiStripTools
// Class:      FillingSchemeEDFilter
// 
/**\class FillingSchemeEDFilter FillingSchemeEDFilter.cc DPGAnalysis/SiStripTools/plugins/FillingSchemeEDFilter.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Tue Dec  9 18:33:42 CET 2008
// $Id: FillingSchemeEDFilter.cc,v 1.2 2009/09/25 12:03:27 venturia Exp $
//
//


// system include files
#include <memory>

#include <vector>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CondFormats/RunInfo/interface/FillInfo.h"
#include "CondFormats/DataRecord/interface/FillInfoRcd.h"

//
// class declaration
//

class FillingSchemeEDFilter : public edm::EDFilter {
public:
  explicit FillingSchemeEDFilter(const edm::ParameterSet&);
  ~FillingSchemeEDFilter();
  
private:
  
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ----------member data ---------------------------
  
  const int m_bxoff;
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
FillingSchemeEDFilter::FillingSchemeEDFilter(const edm::ParameterSet& iConfig):
  m_bxoff(iConfig.getParameter<int>("bxOffset"))
{
   //now do what ever initialization is needed

}


FillingSchemeEDFilter::~FillingSchemeEDFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
FillingSchemeEDFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  bool selected = false;

  edm::ESHandle<FillInfo> fillInfo;
  iSetup.get<FillInfoRcd>().get(fillInfo);

  int eventbx = iEvent.bunchCrossing()==0 ? 3564 : iEvent.bunchCrossing();
  const int bx = (eventbx - m_bxoff - 1)%3564 < 0 ? (eventbx - m_bxoff -1)%3564 + 1 + 3564 : (eventbx - m_bxoff - 1)%3564 + 1;

  selected = fillInfo->isBunchInBeam1(bx) && fillInfo->isBunchInBeam2(bx);
 
  return selected;

}

// ------------ method called once each job just before starting event loop  ------------
void 
FillingSchemeEDFilter::beginJob()
{}

// ------------ method called once each job just after ending the event loop  ------------
void 
FillingSchemeEDFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(FillingSchemeEDFilter);
