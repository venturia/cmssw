// -*- C++ -*-
//
// Package:    OverlapProblemTSOSAnalyzer
// Class:      OverlapProblemTSOSAnalyzer
// 
/**\class OverlapProblemTSOSAnalyzer OverlapProblemTSOSAnalyzer.cc DebugTools/OverlapProblem/plugins/OverlapProblemTSOSAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Thu Dec 16 16:32:56 CEST 2010
// $Id: OverlapProblemTSOSAnalyzer.cc,v 1.2 2013/04/10 21:08:01 venturia Exp $
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

#include "FWCore/Utilities/interface/InputTag.h"

#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "TrackingTools/PatternTools/interface/TrajectoryMeasurement.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryStateCombiner.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"

#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "TH1F.h"

#include "tracking/TrackRecoMonitoring/interface/TSOSHistogramMaker.h"
//
// class decleration
//


class OverlapProblemTSOSAnalyzer : public edm::EDAnalyzer {
public:
  explicit OverlapProblemTSOSAnalyzer(const edm::ParameterSet&);
  ~OverlapProblemTSOSAnalyzer();
  
private:
  virtual void beginJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  virtual void endRun(const edm::Run&, const edm::EventSetup&);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  TH1F* m_ptrk;
  TH1F* m_etatrk;


  std::vector<TH1F*> m_tsosytecr;
  std::vector<TH1F*> m_ttrhytecr;
  std::vector<TH1F*> m_tsosdytecr;
  bool m_validOnly;
  edm::InputTag m_ttacollection;

  TSOSHistogramMaker m_tsoshm;

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
OverlapProblemTSOSAnalyzer::OverlapProblemTSOSAnalyzer(const edm::ParameterSet& iConfig):
  m_tsosytecr(),m_ttrhytecr(),m_tsosdytecr(),
  m_validOnly(iConfig.getParameter<bool>("onlyValidRecHit")),
  m_ttacollection(iConfig.getParameter<edm::InputTag>("trajTrackAssoCollection")),
  m_tsoshm(iConfig.getParameter<edm::ParameterSet>("tsosHMConf"))

{
   //now do what ever initialization is needed



  edm::Service<TFileService> tfserv;

  m_ptrk = tfserv->make<TH1F>("trkmomentum","Refitted Track  momentum",100,0.,200.);
  m_etatrk = tfserv->make<TH1F>("trketa","Refitted Track pseudorapidity",100,-4.,4.);

  for(unsigned int ring=0;ring<7;++ring) {

    char name[100];
    char title[100];

    sprintf(name,"tsosytecr_%d",ring+1);
    sprintf(title,"TSOS local Y TEC ring %d",ring+1);
    m_tsosytecr.push_back(tfserv->make<TH1F>(name,title,200,-20.,20.));

    sprintf(name,"ttrhytecr_%d",ring+1);
    sprintf(title,"Transient Tracking RecHit local Y TEC ring %d",ring+1);
    m_ttrhytecr.push_back(tfserv->make<TH1F>(name,title,200,-20.,20.));

    sprintf(name,"tsosdytecr_%d",ring+1);
    sprintf(title,"TSOS local Y - TTRH local Y TEC ring %d",ring+1);
    m_tsosdytecr.push_back(tfserv->make<TH1F>(name,title,200,-20.,20.));

  }

}


OverlapProblemTSOSAnalyzer::~OverlapProblemTSOSAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
OverlapProblemTSOSAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  // loop on trajectories and plot TSOS local coordinate
  
  TrajectoryStateCombiner tsoscomb;
  
  // Trajectory Handle
  
  Handle<TrajTrackAssociationCollection> ttac;
  iEvent.getByLabel(m_ttacollection,ttac);
  
  for(TrajTrackAssociationCollection::const_iterator pair=ttac->begin();pair!=ttac->end();++pair) {
    
    const edm::Ref<std::vector<Trajectory> > & traj = pair->key;
    const reco::TrackRef & trk = pair->val;
    const std::vector<TrajectoryMeasurement> & tmcoll = traj->measurements();
    
    m_ptrk->Fill(trk->p());
    m_etatrk->Fill(trk->eta());


    for(std::vector<TrajectoryMeasurement>::const_iterator meas = tmcoll.begin() ; meas!= tmcoll.end() ; ++meas) {
      
      if(!meas->updatedState().isValid()) continue;
      
      TrajectoryStateOnSurface tsos = tsoscomb(meas->forwardPredictedState(), meas->backwardPredictedState());
      TransientTrackingRecHit::ConstRecHitPointer hit = meas->recHit();
      
      m_tsoshm.fill(tsos,hit);

      if(!hit->isValid() && m_validOnly) continue;

      if(hit->geographicalId().det() != DetId::Tracker) continue;
      
      TECDetId det(hit->geographicalId());
      if(det.subDetector() != SiStripDetId::TEC) continue;
      
      unsigned int iring = det.ring() - 1;
      m_tsosytecr[iring]->Fill(tsos.localPosition().y());

      if(!hit->isValid()) continue;

      m_ttrhytecr[iring]->Fill(hit->localPosition().y());
      m_tsosdytecr[iring]->Fill(tsos.localPosition().y()-hit->localPosition().y());
      
      
    }
    
  }
  
  
}

void 
OverlapProblemTSOSAnalyzer::beginRun(const edm::Run& iRun, const edm::EventSetup&)
{
}

void 
OverlapProblemTSOSAnalyzer::endRun(const edm::Run& iRun, const edm::EventSetup&)
{
}



// ------------ method called once each job just before starting event loop  ------------
void 
OverlapProblemTSOSAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
OverlapProblemTSOSAnalyzer::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(OverlapProblemTSOSAnalyzer);
