// -*- C++ -*-
//
// Package:    SiPixelRecHitsDump
// Class:      SiPixelRecHitsDump
// 
/**\class SiPixelRecHitsDump SiPixelRecHitsDump.cc DebugTools/RecHits/plugins/SiPixelRecHitsDump.cc

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

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"


//
// class decleration
//

class SiPixelRecHitsDump : public edm::EDAnalyzer {
public:
  explicit SiPixelRecHitsDump(const edm::ParameterSet&);
  ~SiPixelRecHitsDump();
  
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  edm::InputTag m_sipixrhcollection;

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
SiPixelRecHitsDump::SiPixelRecHitsDump(const edm::ParameterSet& iConfig):
  m_sipixrhcollection(iConfig.getParameter<edm::InputTag>("siPixelRHCollection"))

{
   //now do what ever initialization is needed

  edm::LogInfo("SiPixelRecHitCollection") << "Using collection " << m_sipixrhcollection.label().c_str() ;

}


SiPixelRecHitsDump::~SiPixelRecHitsDump()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
SiPixelRecHitsDump::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   Handle<SiPixelRecHitCollection> rechits;
   iEvent.getByLabel(m_sipixrhcollection,rechits);

   //

   edm::LogInfo("RecHitDump") << "Dump of SiPixelRecHits";
   for(SiPixelRecHitCollection::const_iterator det = rechits->begin();det!=rechits->end();++det) {
     
     for(edmNew::DetSet<SiPixelRecHit>::const_iterator hit = det->begin(); hit!= det->end() ; ++hit) {

       edm::LogVerbatim("RecHitDump") << hit->geographicalId().rawId() << " " 
				      << hit->localPosition().x() << " " 
				      << hit->localPosition().y() << " " 
				      << hit->localPosition().z() << " "
				      << hit->localPositionError().xx() << " " 
				      << hit->localPositionError().xy() << " " 
				      << hit->localPositionError().yy() << " "
				      << sqrt(hit->localPositionError().xx()) << " " 
				      << sqrt(hit->localPositionError().yy());
     }
   }


}

void 
SiPixelRecHitsDump::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{}

void 
SiPixelRecHitsDump::endRun(const edm::Run& iRun, const edm::EventSetup&)
{}



// ------------ method called once each job just before starting event loop  ------------
void 
SiPixelRecHitsDump::beginJob()
{}

// ------------ method called once each job just after ending the event loop  ------------
void 
SiPixelRecHitsDump::endJob() 
{}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelRecHitsDump);
