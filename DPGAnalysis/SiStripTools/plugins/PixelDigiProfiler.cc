// -*- C++ -*-
//
// Package:    PixelDigiProfiler
// Class:      PixelDigiProfiler
//
/**\class PixelDigiProfiler PixelDigiProfiler.cc DPGAnalysis/SiStripTools/plugins/PixelDigiProfiler.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Mon Jul 03 10:37:00 CET 2017
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

#include <vector>
#include "TH1D.h"
#include "TH2D.h"
#include "TProfile2D.h"
#include "CommonTools/UtilAlgos/interface/DetIdSelector.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/SiPixelDigi/interface/PixelDigi.h"

//
// class decleration
//

class PixelDigiProfiler : public edm::EDAnalyzer {
   public:
      explicit PixelDigiProfiler(const edm::ParameterSet&);
      ~PixelDigiProfiler();


   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

      // ----------member data ---------------------------

  edm::EDGetTokenT<edm::DetSetVector<PixelDigi> > m_collectionToken;

  std::vector<DetIdSelector> m_selections;
  std::vector<TH1D*> m_hitadc;
  std::vector<TH2D*> m_histhit;
  std::vector<TProfile2D*> m_hitadcprof;
  //  std::vector<TH2D*> m_histhitpair;
  //  std::vector<TProfile2D*> m_hprofhit;
  //  std::vector<TProfile2D*> m_hprofhitpair;


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
PixelDigiProfiler::PixelDigiProfiler(const edm::ParameterSet& iConfig):
  m_collectionToken(consumes<edm::DetSetVector<PixelDigi> >(iConfig.getParameter<edm::InputTag>("collection")))

{
   //now do what ever initialization is needed

  std::vector<edm::ParameterSet> selconfigs = iConfig.getParameter<std::vector<edm::ParameterSet> >("selections");

  for(std::vector<edm::ParameterSet>::const_iterator selconfig=selconfigs.begin();selconfig!=selconfigs.end();++selconfig) {
    DetIdSelector selection(*selconfig);
    m_selections.push_back(selection);

  }

  edm::Service<TFileService> tfserv;

    //book histos

  unsigned int nxbins =52*8; // number of ROCs in half modules, times number of columns
  unsigned int nybins =80*2; // number of ROC rows, times number of rows

  for(std::vector<edm::ParameterSet>::const_iterator selconfig=selconfigs.begin();selconfig!=selconfigs.end();++selconfig) {

    std::string label = selconfig->getParameter<std::string>("label");

    std::string hname = label + "histhit";
    std::string htitle = label + " number of hits";
    m_histhit.push_back(tfserv->make<TH2D>(hname.c_str(),htitle.c_str(),nxbins,-0.5,nxbins-0.5,nybins,-0.5,nybins-0.5));
    hname = label + "hitadcprof";
    htitle = label + " average ADC";
    m_hitadcprof.push_back(tfserv->make<TProfile2D>(hname.c_str(),htitle.c_str(),nxbins,-0.5,nxbins-0.5,nybins,-0.5,nybins-0.5));
    hname = label + "hitadc";
    htitle = label + " hit ADC ";
    m_hitadc.push_back(tfserv->make<TH1D>(hname.c_str(),htitle.c_str(),300,-0.5,299.5));
    /*
    hname = label + "histhitpair";
    htitle = label + " number of hits in pixel pairs";
    m_histhitpair.push_back(tfserv->make<TH2D>(hname.c_str(),htitle.c_str(),nxbins,-0.5,nxbins-0.5,nybins,-0.5,nybins-0.5));
    */
  }
}

PixelDigiProfiler::~PixelDigiProfiler()
{


   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
PixelDigiProfiler::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<edm::DetSetVector<PixelDigi> > digis;
  iEvent.getByToken(m_collectionToken,digis);
  
  for(edm::DetSetVector<PixelDigi>::const_iterator det = digis->begin();det!=digis->end();++det) {

    DetId detid(det->detId());

    std::vector<DetIdSelector>::const_iterator detsel;
    std::vector<TH2D*>::const_iterator histhit;
    std::vector<TProfile2D*>::const_iterator hitadcprof;
    std::vector<TH1D*>::const_iterator hitadc;
    for(detsel=m_selections.begin(),histhit=m_histhit.begin(),hitadcprof=m_hitadcprof.begin(),hitadc=m_hitadc.begin();
	detsel!=m_selections.end();
	++detsel,++histhit,++hitadcprof,++hitadc) {
      if(detsel->isValid() && detsel->isSelected(detid)) {
	for(edm::DetSet<PixelDigi>::const_iterator digi = det->begin();digi!=det->end();++digi) {
	  (*histhit)->Fill(digi->column(),digi->row());
	  (*hitadcprof)->Fill(digi->column(),digi->row(),digi->adc());
	  (*hitadc)->Fill(digi->adc());
	}
      }
    }

  }
  
}

//define this as a plug-in
DEFINE_FWK_MODULE(PixelDigiProfiler);
