// -*- C++ -*-
//
// Package:    V0CandProducer
// Class:      V0CandProducer
// 
/**\class V0CandProducer V0CandProducer.cc myProducers/V0CandProducer/src/V0CandProducer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Brian Drell
//         Created:  Mon Sep 28 16:32:58 MDT 2009
// $Id: V0CandProducer.cc,v 1.5 2010/03/19 09:42:34 drell Exp $
//
//


// system include files
#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/V0Candidate/interface/V0Candidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/PatCandidates/interface/GenericParticle.h"

#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include "DataFormats/TrackReco/interface/HitPattern.h"


class V0CandProducer : public edm::EDProducer {
public:
  explicit V0CandProducer(const edm::ParameterSet&);
  ~V0CandProducer();
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      
  edm::InputTag k0sCollection;
  edm::InputTag lamCollection;
};

V0CandProducer::V0CandProducer(const edm::ParameterSet& iConfig):
  k0sCollection( iConfig.getParameter<edm::InputTag>("kShortCollection")),
  lamCollection( iConfig.getParameter<edm::InputTag>("lambdaCollection")) {

  produces< std::vector<reco::V0Candidate> >("allVees");
  produces< pat::CompositeCandidateCollection >("allVees");
  
}


V0CandProducer::~V0CandProducer() {
}

void V0CandProducer::produce(edm::Event& iEvent, 
			     const edm::EventSetup& iSetup) {
   using namespace edm;
   using namespace std;

   ESHandle<TransientTrackBuilder> ttBuilder;

   Handle<reco::VertexCompositeCandidateCollection> theKshorts;
   Handle<reco::VertexCompositeCandidateCollection> theLambdas;

   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", ttBuilder);

   iEvent.getByLabel(k0sCollection, theKshorts);
   iEvent.getByLabel(lamCollection, theLambdas);

   std::vector<reco::V0Candidate> theVeeCands;
   std::auto_ptr<pat::CompositeCandidateCollection> 
     patOut(new pat::CompositeCandidateCollection);

   // Loop over the K0s collection, find which tracks have which charge, and push back
   //  V0Candidate objects
   for( reco::VertexCompositeCandidateCollection::const_iterator iKS = theKshorts->begin();
	iKS != theKshorts->end();
	iKS++ ) {
     reco::VertexCompositeCandidate theKS(*iKS);
     reco::VertexCompositeCandidate* iKS_ = &theKS;
     reco::CompositeCandidate* iKSptr 
       = dynamic_cast<reco::CompositeCandidate *> (iKS_);
     pat::CompositeCandidate ksPatCand(*iKSptr);
     ksPatCand.clearDaughters();
     //ksPatCand.daughter(0)->embedTrack();
     //ksPatCand.daughter(1)->embedTrack();

     int numOfPosDaughter = -1;
     int numOfNegDaughter = -1;
     if( iKS->daughter(0)->charge() > 0. && iKS->daughter(1)->charge() < 0. ) {
       numOfPosDaughter = 0;
       numOfNegDaughter = 1;
     }
     else if( iKS->daughter(1)->charge() > 0. && iKS->daughter(0)->charge() < 0. ){
       numOfPosDaughter = 1;
       numOfNegDaughter = 0;
     }
     if( numOfPosDaughter >= 0 && numOfNegDaughter >= 0 ) {
       // PAT
       pat::GenericParticle patPosDau( *(iKS->daughter(numOfPosDaughter)) );
       pat::GenericParticle patNegDau( *(iKS->daughter(numOfNegDaughter)) );

       //cout << "patPosDau_eta: " << patPosDau.eta() << endl;
       //cout << "patPosDau_track_chi2: " << patPosDau.track()->chi2() << endl;
       //patPosDau.embedTrack();
       //patNegDau.embedTrack();
       //ksPatCand.addDaughter( patPosDau, "posTk" );
       //ksPatCand.addDaughter( patNegDau, "negTk" );

       //pat::GenericParticle patPosDau();
       //pat::GenericParticle patNegDau();

       // Non-PAT
       reco::RecoChargedCandidate posCand1 
	 = *(dynamic_cast<const reco::RecoChargedCandidate*>(iKS->daughter(numOfPosDaughter)));
       reco::RecoChargedCandidate negCand1
	 = *(dynamic_cast<const reco::RecoChargedCandidate*>(iKS->daughter(numOfNegDaughter)));
       patPosDau.setTrack( posCand1.track(), true );
       patNegDau.setTrack( negCand1.track(), true );

       ksPatCand.addDaughter( patPosDau );
       ksPatCand.addDaughter( patNegDau );

       //cout << "Tk Chi2: " 
       //   << (dynamic_cast<const reco::RecoCandidate*>(ksPatCand.daughter(0)))->track()->chi2() << endl;
       reco::V0Candidate temp( *iKS, 
			       *(posCand1.track()), 
			       *(negCand1.track()) );

       const reco::HitPattern& posHitPatt = posCand1.track()->hitPattern();
       const reco::HitPattern& negHitPatt = negCand1.track()->hitPattern();
       reco::TransientTrack posDaughterTT 
	 = ttBuilder->build( temp.getPosTrack() );
       reco::TransientTrack negDaughterTT 
	 = ttBuilder->build( temp.getNegTrack() );
       GlobalPoint vtxpos( temp.getVtxCC().vx(), 
			   temp.getVtxCC().vy(), 
			   temp.getVtxCC().vz() );

       temp.setPosNPixelHits( posHitPatt.numberOfValidPixelHits() );
       temp.setNegNPixelHits( negHitPatt.numberOfValidPixelHits() );
       temp.setPosNStripHits( posHitPatt.numberOfValidStripHits() );
       temp.setNegNStripHits( negHitPatt.numberOfValidStripHits() );

       ksPatCand.addUserInt( "posTkNPixelHits",
			     posHitPatt.numberOfValidPixelHits() );
       ksPatCand.addUserInt( "negTkNPixelHits",
			     negHitPatt.numberOfValidPixelHits() );
       ksPatCand.addUserInt( "posTkNStripHits", 
			     posHitPatt.numberOfValidStripHits() );
       ksPatCand.addUserInt( "negTkNStripHits",
			     negHitPatt.numberOfValidStripHits() );

       TrajectoryStateClosestToPoint posDaughterTSCP 
	 = posDaughterTT.trajectoryStateClosestToPoint(vtxpos);
       TrajectoryStateClosestToPoint negDaughterTSCP
	 = negDaughterTT.trajectoryStateClosestToPoint(vtxpos);
       temp.setPosMomentum( posDaughterTSCP.momentum() );
       temp.setNegMomentum( negDaughterTSCP.momentum() );

       ksPatCand.addUserFloat( "posTkPX",
			       posDaughterTSCP.momentum().x() );
       ksPatCand.addUserFloat( "posTkPY",
			       posDaughterTSCP.momentum().y() );
       ksPatCand.addUserFloat( "posTkPZ",
			       posDaughterTSCP.momentum().z() );
       ksPatCand.addUserFloat( "negTkPX",
			       negDaughterTSCP.momentum().x() );
       ksPatCand.addUserFloat( "negTkPY",
			       negDaughterTSCP.momentum().y() );
       ksPatCand.addUserFloat( "negTkPZ",
			       negDaughterTSCP.momentum().z() );

       ksPatCand.addUserFloat( "vtxCov00",
			       iKS->vertexCovariance(0,0) );
       ksPatCand.addUserFloat( "vtxCov01",
			       iKS->vertexCovariance(0,1) );
       ksPatCand.addUserFloat( "vtxCov11",
			       iKS->vertexCovariance(1,1) );
       ksPatCand.addUserFloat( "vtxCov02",
			       iKS->vertexCovariance(0,2) );
       ksPatCand.addUserFloat( "vtxCov12",
			       iKS->vertexCovariance(1,2) );
       ksPatCand.addUserFloat( "vtxCov22",
			       iKS->vertexCovariance(2,2) );
       ksPatCand.addUserFloat( "vtxChi2",
			       iKS->vertexChi2() );
       ksPatCand.addUserFloat( "vtxNormChi2",
			       iKS->vertexNormalizedChi2() );

       theVeeCands.push_back( temp );
       patOut->push_back( ksPatCand );
     }
   }

   // Rinse and repeat for Lambda collection
   for( reco::VertexCompositeCandidateCollection::const_iterator iLM = theLambdas->begin();
	iLM != theLambdas->end();
	iLM++ ) {
     // PAT stuff
     reco::VertexCompositeCandidate theLM(*iLM);
     reco::VertexCompositeCandidate* iLM_ = &theLM;
     reco::CompositeCandidate* iLMptr 
       = dynamic_cast<reco::CompositeCandidate *> (iLM_);
     pat::CompositeCandidate lamPatCand(*iLMptr);
     lamPatCand.clearDaughters();
     //lamPatCand.daughter(0)->embedTrack();
     //lamPatCand.daughter(1)->embedTrack();

     // Non-PAT
     int numOfPosDaughter = -1;
     int numOfNegDaughter = -1;
     if( iLM->daughter(0)->charge() > 0. && iLM->daughter(1)->charge() < 0. ) {
       numOfPosDaughter = 0;
       numOfNegDaughter = 1;
     }
     else if( iLM->daughter(1)->charge() > 0. && iLM->daughter(0)->charge() < 0. ) {
       numOfPosDaughter = 1;
       numOfNegDaughter = 0;
     }
     if( numOfPosDaughter >= 0 && numOfNegDaughter >= 0 ) {
       // PAT
       pat::GenericParticle patPosDau( *(iLM->daughter(numOfPosDaughter)) );
       pat::GenericParticle patNegDau( *(iLM->daughter(numOfNegDaughter)) );
       //patPosDau.embedTrack();
       //patNegDau.embedTrack();
       //lamPatCand.addDaughter( patPosDau, "posTk" );
       //lamPatCand.addDaughter( patNegDau, "negTk" );
       //pat::GenericParticle patPosDau();
       //pat::GenericParticle patNegDau();

       // Non-PAT
       reco::RecoChargedCandidate posCand2 
	 = *(dynamic_cast<const reco::RecoChargedCandidate*>(iLM->daughter(numOfPosDaughter)));
       reco::RecoChargedCandidate negCand2
	 = *(dynamic_cast<const reco::RecoChargedCandidate*>(iLM->daughter(numOfNegDaughter)));

       patPosDau.setTrack( posCand2.track(), true );
       patNegDau.setTrack( negCand2.track(), true );

       lamPatCand.addDaughter( patPosDau );
       lamPatCand.addDaughter( patNegDau );

       reco::V0Candidate temp( *iLM,
			       *(posCand2.track()),
			       *(negCand2.track()) );
       const reco::HitPattern& posHitPatt = posCand2.track()->hitPattern();
       const reco::HitPattern& negHitPatt = negCand2.track()->hitPattern();
       reco::TransientTrack posDaughterTT 
	 = ttBuilder->build( temp.getPosTrack() );
       reco::TransientTrack negDaughterTT 
	 = ttBuilder->build( temp.getNegTrack() );
       GlobalPoint vtxpos( temp.getVtxCC().vx(), 
			   temp.getVtxCC().vy(), 
			   temp.getVtxCC().vz() );

       temp.setPosNPixelHits( posHitPatt.numberOfValidPixelHits() );
       temp.setNegNPixelHits( negHitPatt.numberOfValidPixelHits() );
       temp.setPosNStripHits( posHitPatt.numberOfValidStripHits() );
       temp.setNegNStripHits( negHitPatt.numberOfValidStripHits() );

       lamPatCand.addUserInt( "posTkNPixelHits",
			      posHitPatt.numberOfValidPixelHits() );
       lamPatCand.addUserInt( "negTkNPixelHits",
			      negHitPatt.numberOfValidPixelHits() );
       lamPatCand.addUserInt( "posTkNStripHits", 
			      posHitPatt.numberOfValidStripHits() );
       lamPatCand.addUserInt( "negTkNStripHits",
			      negHitPatt.numberOfValidStripHits() );

       TrajectoryStateClosestToPoint posDaughterTSCP 
	 = posDaughterTT.trajectoryStateClosestToPoint(vtxpos);
       TrajectoryStateClosestToPoint negDaughterTSCP
	 = negDaughterTT.trajectoryStateClosestToPoint(vtxpos);
       temp.setPosMomentum( posDaughterTSCP.momentum() );
       temp.setNegMomentum( negDaughterTSCP.momentum() );

       lamPatCand.addUserFloat( "posTkPX",
				posDaughterTSCP.momentum().x() );
       lamPatCand.addUserFloat( "posTkPY",
				posDaughterTSCP.momentum().y() );
       lamPatCand.addUserFloat( "posTkPZ",
				posDaughterTSCP.momentum().z() );
       lamPatCand.addUserFloat( "negTkPX",
				negDaughterTSCP.momentum().x() );
       lamPatCand.addUserFloat( "negTkPY",
				negDaughterTSCP.momentum().y() );
       lamPatCand.addUserFloat( "negTkPZ",
				negDaughterTSCP.momentum().z() );

       lamPatCand.addUserFloat( "vtxCov00",
			       iLM->vertexCovariance(0,0) );
       lamPatCand.addUserFloat( "vtxCov01",
			       iLM->vertexCovariance(0,1) );
       lamPatCand.addUserFloat( "vtxCov11",
			       iLM->vertexCovariance(1,1) );
       lamPatCand.addUserFloat( "vtxCov02",
			       iLM->vertexCovariance(0,2) );
       lamPatCand.addUserFloat( "vtxCov12",
			       iLM->vertexCovariance(1,2) );
       lamPatCand.addUserFloat( "vtxCov22",
			       iLM->vertexCovariance(2,2) );

       theVeeCands.push_back( temp );
       patOut->push_back( lamPatCand );
     }
   }

   // Allocate vector and put it into the event
   std::auto_ptr< std::vector<reco::V0Candidate> > 
     veesOut( new std::vector<reco::V0Candidate> );
   veesOut->reserve( theVeeCands.size() );
   std::copy( theVeeCands.begin(),
	      theVeeCands.end(),
	      std::back_inserter( *veesOut ) );
   iEvent.put( veesOut, std::string("allVees") );

   iEvent.put( patOut, std::string("allVees") );
 
}

void V0CandProducer::beginJob() {
}

void V0CandProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(V0CandProducer);
