// -*- C++ -*-
//
// Package:    V0RecoAnalyzer
// Class:      V0RecoAnalyzer
// 
/**\class V0RecoAnalyzer V0RecoAnalyzer.cc myAnalyzers/V0RecoAnalyzer/src/V0RecoAnalyzer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Brian Drell
//         Created:  Wed Aug 26 13:34:28 MDT 2009
// $Id: V0RecoAnalyzer.cc,v 1.21 2010/04/09 23:36:44 drell Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Candidate/interface/VertexCompositeCandidate.h"
#include "DataFormats/Candidate/interface/VertexCompositeCandidateFwd.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/V0Candidate/interface/V0Candidate.h"

#include "RecoVertex/VertexTools/interface/VertexDistance3D.h"

//#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
//#include "RecoVertex/VertexTools/interface/InvariantMassFromVertex.h"

//#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
//#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include <typeinfo>

// ROOT includes
#include "TFile.h"
#include "TTree.h"
#include "TF1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TGraphErrors.h"
#include "TMath.h"
#include "TCanvas.h"

#include <Math/Functions.h>
#include <Math/SVector.h>
#include <Math/SMatrix.h>

// Standard C++ includes
#include <sstream>

// Constants
const double piMass = 0.13957018;
const double piMass2 = piMass * piMass;
const double protonMass = 0.93827203;
const double protonMass2 = protonMass * protonMass;
const double ksMassConst = 0.497648;
const double lamMassConst = 1.115683;

class V0RecoAnalyzer : public edm::EDAnalyzer {
public:
  explicit V0RecoAnalyzer(const edm::ParameterSet&);
  ~V0RecoAnalyzer();


private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  TTree* theTree;
  TFile* theFile;

  // ***Tree variables***
  // V0 vertex position info
  std::vector<float> *v0VtxX;
  std::vector<float> *v0VtxY;
  std::vector<float> *v0VtxZ;
  std::vector<float> *v0VtxR;
  std::vector<float> *v0VtxChi2;
  std::vector<float> *v0VtxNormChi2;
  /*  std::vector<float> *v0VtxCXX;
  std::vector<float> *v0VtxCYY;
  std::vector<float> *v0VtxCZZ;
  std::vector<float> *v0VtxCYX;
  std::vector<float> *v0VtxCZX;
  std::vector<float> *v0VtxCZY;
  std::vector<float> *v0VtxChi2;
  std::vector<float> *v0VtxNormChi2;*/

  // V0 kinematics
  std::vector<float> *v0pX;
  std::vector<float> *v0pY;
  std::vector<float> *v0pZ;
  std::vector<float> *v0pT;
  std::vector<float> *v0p;
  std::vector<float> *v0Eta;
  std::vector<float> *v0Phi;

  // For the Armenteros plot:
  std::vector<float> *v0pTPlus;
  std::vector<float> *v0pTMinus;
  std::vector<float> *v0pLPlus;
  std::vector<float> *v0pLMinus;
  /*std::vector<float> *v0pXerr;
  std::vector<float> *v0pYerr;
  std::vector<float> *v0pZerr;*/

  // V0 mass and error
  //std::vector<float> *v0Mass;
  //std::vector<float> *v0Masserr;
  //std::vector<float> *v0Massnorm;
  std::vector<float> *v0CandMass;
  std::vector<float> *v0OtherCandMass;

  // V0 lifetime
  std::vector<float> *v0Lifetime;
  std::vector<float> *v03DLifetime;
  std::vector<int> *v0PDG;
  std::vector<float> *v0VtxSig;

  //std::vector<float> *priVtxChi2;
  //std::vector<float> *priVtxNdof;
  //std::vector<float> *nTracks;
  //std::vector<float> *nV0s;
  int nTracks;
  int nV0s;
  float priVtxChi2;
  float priVtxNdof;
  float priVtxX;
  float priVtxY;
  float priVtxZ;

  std::vector<float> *v0VtxPriDist;
  std::vector<float> *v0VtxPriDistErr;

  std::vector<float> *v0VtxBSTransDist;
  std::vector<float> *v0VtxBSTransDistErr;

  // V0 daughter track quantities
  std::vector<float> *v0DaupT;
  std::vector<float> *v0Daup;
  std::vector<float> *v0DaupX;
  std::vector<float> *v0DaupY;
  std::vector<float> *v0DaupZ;
  std::vector<float> *v0DauAtVtxpX;
  std::vector<float> *v0DauAtVtxpY;
  std::vector<float> *v0DauAtVtxpZ;
  std::vector<float> *v0DauEta;
  std::vector<float> *v0DauPhi;
  //std::vector<float> *v0DauNHits;
  std::vector<float> *v0DauNValidHits;
  std::vector<float> *v0DauNPixelHits;
  std::vector<float> *v0DauNStripHits;
  std::vector<float> *v0DauChi2;
  std::vector<float> *v0DauNormChi2;
  std::vector<float> *v0DauD0;

  // Quantities associated with daughter track that has lowest pT
  std::vector<float> *v0DaupT_lowestpT;
  std::vector<float> *v0DauEta_lowestpT;
  std::vector<float> *v0DauPhi_lowestpT;

  // Histograms
  TH1F* ksR;
  TH1F* ksRFull;
  TH1F* ksRSignal;
  TH1F* ksRBg;

  TH1F* ksZ;
  TH1F* ksZFull;
  TH1F* ksZSignal;
  TH1F* ksZBg;

  TH2F* ksZvsRFull;
  TH2F* ksZvsRBgSubt;
  TH2F* ksZvsRBg;
  TH2F* ksZvsRSignal;

  TH1F* ksEta;
  TH1F* ksEtaFull;
  TH1F* ksEtaSignal;
  TH1F* ksEtaBg;

  TH1F* ksPhi;
  TH1F* ksPhiFull;
  TH1F* ksPhiSignal;
  TH1F* ksPhiBg;

  TH1F* ksPt;
  TH1F* ksPtFull;
  TH1F* ksPtSignal;
  TH1F* ksPtBg;

  TH1F* ksMass;
  TH1F* ksNormMass;
  TH1F* ksCandMass;

  TH1F* ksDaup;
  TH1F* ksDaupT;
  TH1F* ksDauEta;
  TH1F* ksDauPhi;
  TH1F* ksDauNValidHits;
  TH1F* ksDauNPixelHits;
  TH1F* ksDauNStripHits;
  TH1F* ksDauChi2;
  TH1F* ksDauNormChi2;
  TH1F* ksDauD0;

  TH1F* lamR;
  TH1F* lamRFull;
  TH1F* lamRSignal;
  TH1F* lamRBg;

  TH1F* lamZ;
  TH1F* lamZFull;
  TH1F* lamZSignal;
  TH1F* lamZBg;

  TH2F* lamZvsRFull;
  TH2F* lamZvsRBgSubt;
  TH2F* lamZvsRBg;
  TH2F* lamZvsRSignal;

  TH1F* lamEta;
  TH1F* lamEtaFull;
  TH1F* lamEtaSignal;
  TH1F* lamEtaBg;

  TH1F* lamPhi;
  TH1F* lamPhiFull;
  TH1F* lamPhiSignal;
  TH1F* lamPhiBg;

  TH1F* lamPt;
  TH1F* lamPtFull;
  TH1F* lamPtSignal;
  TH1F* lamPtBg;

  TH1F* lamCandMass;

  TH1F* lamDaup;
  TH1F* lamDaupT;
  TH1F* lamDauEta;
  TH1F* lamDauPhi;
  TH1F* lamDauNValidHits;
  TH1F* lamDauNPixelHits;
  TH1F* lamDauNStripHits;
  TH1F* lamDauChi2;
  TH1F* lamDauNormChi2;
  TH1F* lamDauD0;

  /*TH1F* ksMass_pt_1;
  TH1F* ksMass_pt_2;
  TH1F* ksMass_pt_3;
  TH1F* ksMass_pt_4;
  TH1F* ksMass_pt_5;
  TH1F* ksMass_pt_6;*/
  std::vector<TH1F*> ksMass_pt; 
  std::vector<std::string> ksMass_pt_names_short;
  std::vector<std::string> ksMass_pt_names_long;
  std::vector<double> ksMass_pt_minima;

  /*TH1F* ksMass_phi_1;
  TH1F* ksMass_phi_2;
  TH1F* ksMass_phi_3;
  TH1F* ksMass_phi_4;
  TH1F* ksMass_phi_5;
  TH1F* ksMass_phi_6;*/
  std::vector<TH1F*> ksMass_phi;
  std::vector<std::string> ksMass_phi_names_short;
  std::vector<std::string> ksMass_phi_names_long;
  std::vector<double> ksMass_phi_minima;

  /*TH1F* ksMass_eta_2__2_5;
  TH1F* ksMass_eta_1_5__2;
  TH1F* ksMass_eta_1__1_5;
  TH1F* ksMass_eta_0_5__1;
  TH1F* ksMass_eta_0__0_5;*/
  std::vector<TH1F*> ksMass_eta;
  std::vector<std::string> ksMass_eta_names_short;
  std::vector<std::string> ksMass_eta_names_long;
  std::vector<double> ksMass_eta_minima;

  std::vector<TH1F*> ksMass_eta_phi;
  std::vector<std::string> ksMass_eta_phi_names_short;
  std::vector<std::string> ksMass_eta_phi_names_long;
  std::vector<double> ksMass_eta_phi_etaminima;
  std::vector<double> ksMass_eta_phi_phiminima;

  std::vector<TH1F*> lamMass_pt;
  std::vector<std::string> lamMass_pt_names_short;
  std::vector<std::string> lamMass_pt_names_long;
  std::vector<double> lamMass_pt_minima;

  std::vector<TH1F*> lamMass_phi;
  std::vector<std::string> lamMass_phi_names_short;
  std::vector<std::string> lamMass_phi_names_long;
  std::vector<double> lamMass_phi_minima;

  std::vector<TH1F*> lamMass_eta;
  std::vector<std::string> lamMass_eta_names_short;
  std::vector<std::string> lamMass_eta_names_long;
  std::vector<double> lamMass_eta_minima;

  /*TGraphErrors* ksMassInPtBins;
  TGraphErrors* trueKsMassInPtBins;
  TGraphErrors* ksMassInPhiBins;
  TGraphErrors* trueKsMassInPhiBins;
  TGraphErrors* ksMassInEtaBins;
  TGraphErrors* trueKsMassInEtaBins;*/
  TH1F* ksMassInPtBins;
  TH1F* ksMassInPhiBins;
  TH1F* ksMassInEtaBins;
  TH2F* ksMassBiasEtaVsPhi;

  TH1F* lamMassInPtBins;
  TH1F* lamMassInPhiBins;
  TH1F* lamMassInEtaBins;

  // Strings for algorithm names, etc.
  edm::InputTag v0Collection;

  bool writeTree;
  bool putTreeInTFile;
  bool writeHistos;
  std::string instanceName;

  bool pvAvailable;
  bool beamSpotAvailable;
  bool tracksAvailable;

  // Mass plot limits and binning
  double ksMassXmin, ksMassXmax;
  int ksMassNbins;
  double ksMassBinWidth;
  //double ksNormMassXmin, ksNormMassXmax;
  //double ksNormMassBinWidth;

  double lamMassXmin, lamMassXmax;
  int lamMassNbins;
  double lamMassBinWidth;
  //double lamNormMassXmin, lamNormMassXmax;
  //double lamNormMassBinWidth;

  // Parameters for mass bias plots
  int ksMass_eta_nBins;
  int ksMass_phi_nBins;
  //int ksMass_pt_nBins;
  double ksMass_pt_nBinSubdiv;

  int lamMass_eta_nBins;
  int lamMass_phi_nBins;
  //int lamMass_pt_nBins;
  double lamMass_pt_nBinSubdiv;



};


V0RecoAnalyzer::V0RecoAnalyzer(const edm::ParameterSet& iConfig) : 
  v0VtxX(0), v0VtxY(0), v0VtxZ(0), v0VtxR(0), v0VtxChi2(0), v0VtxNormChi2(0),
  /*v0VtxCXX(0), v0VtxCYY(0), v0VtxCZZ(0), v0VtxCYX(0), v0VtxCZX(0), v0VtxCZY(0),
    v0VtxChi2(0), v0VtxNormChi2(0),*/
  v0pX(0), v0pY(0), v0pZ(0), v0pT(0), v0p(0), v0Eta(0), v0Phi(0), //v0pXerr(0), v0pYerr(0), v0pZerr(0),
  v0pTPlus(0), v0pTMinus(0), v0pLPlus(0), v0pLMinus(0),
  v0CandMass(0), v0OtherCandMass(0),
  v0Lifetime(0), v03DLifetime(0), v0PDG(0), v0VtxSig(0),
  nTracks(0), nV0s(0), priVtxChi2(0), priVtxNdof(0), 
  priVtxX(0), priVtxY(0), priVtxZ(0), v0VtxPriDist(0), v0VtxPriDistErr(0),
  v0VtxBSTransDist(0), v0VtxBSTransDistErr(0),
  v0DaupT(0), v0Daup(0), v0DaupX(0), v0DaupY(0), v0DaupZ(0), 
  v0DauAtVtxpX(0), v0DauAtVtxpY(0), v0DauAtVtxpZ(0),
  v0DauEta(0), v0DauPhi(0), 
  v0DauNValidHits(0), v0DauNPixelHits(0), v0DauNStripHits(0),
  v0DauChi2(0), v0DauNormChi2(0), v0DauD0(0),
  v0DaupT_lowestpT(0), v0DauEta_lowestpT(0), v0DauPhi_lowestpT(0),
  v0Collection( iConfig.getParameter<edm::InputTag>("v0Collection") ),
  putTreeInTFile( iConfig.getParameter<bool>("writeTree") ),
  writeHistos( iConfig.getParameter<bool>("writeHistos") ),
  instanceName( iConfig.getParameter<std::string>("instanceName") ),
  pvAvailable( iConfig.getParameter<bool>("pvAvailable") ),
  beamSpotAvailable( iConfig.getParameter<bool>("beamSpotAvailable") ),
  tracksAvailable( iConfig.getParameter<bool>("tracksAvailable") ),
  ksMassXmin(iConfig.getParameter<double>("ksMassXmin")),
  ksMassXmax(iConfig.getParameter<double>("ksMassXmax")),
  ksMassNbins(iConfig.getParameter<int>("ksMassNbins")),
  ksMassBinWidth(0.),
  lamMassXmin(iConfig.getParameter<double>("lamMassXmin")),
  lamMassXmax(iConfig.getParameter<double>("lamMassXmax")),
  lamMassNbins(iConfig.getParameter<int>("lamMassNbins")),
  lamMassBinWidth(0.),
  ksMass_eta_nBins(iConfig.getParameter<int>("ksMass_eta_nBins")),
  ksMass_phi_nBins(iConfig.getParameter<int>("ksMass_phi_nBins")),
  //ksMass_pt_nBins(iConfig.getParameter<int>("ksMass_pt_nBins")),
  ksMass_pt_nBinSubdiv(iConfig.getParameter<int>("ksMass_pt_nBinSubdiv")),
  lamMass_eta_nBins(iConfig.getParameter<int>("lamMass_eta_nBins")), 
  lamMass_phi_nBins(iConfig.getParameter<int>("lamMass_phi_nBins")),
  //lamMass_pt_nBins(iConfig.getParameter<int>("lamMass_pt_nBins")),
  lamMass_pt_nBinSubdiv(iConfig.getParameter<int>("lamMass_pt_nBinSubdiv")) {
  //std::cout << "Constructor" << std::endl;
  //instanceName = v0Collection.instance();
  writeTree = true;

}

V0RecoAnalyzer::~V0RecoAnalyzer() {

}


void V0RecoAnalyzer::analyze(const edm::Event& iEvent, 
			     const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace reco;
  using namespace std;

  Handle<pat::CompositeCandidateCollection> patHandle;
  Handle<reco::BeamSpot> theBeamSpotH;
  Handle<reco::VertexCollection> priVtxs;
  Handle<reco::TrackCollection> theTracks;

  iEvent.getByLabel( v0Collection, patHandle );
  if( putTreeInTFile ) {
    //cout << "Crashy?" << endl;
    //nV0s->push_back( patHandle->size() );
    nV0s = patHandle->size();
    //cout << "Crash?" << endl;
  }
  if( beamSpotAvailable ) {
    iEvent.getByLabel( std::string("offlineBeamSpot"), theBeamSpotH );
  }

  reco::Vertex* thePrim = 0;
  if( putTreeInTFile && pvAvailable ) {
    iEvent.getByLabel( "offlinePrimaryVertices", priVtxs );
    if( priVtxs->size() > 0. ) {
      reco::VertexCollection::const_iterator bestVtx = priVtxs->begin();
      if( bestVtx->isValid() && !bestVtx->isFake() ) {
	thePrim = new reco::Vertex( *bestVtx );
	//priVtxChi2->push_back( bestVtx->normalizedChi2() );
	//priVtxNdof->push_back( bestVtx->ndof() );
	priVtxChi2 = bestVtx->normalizedChi2();
	priVtxNdof = bestVtx->ndof();
	priVtxX = bestVtx->position().x();
	priVtxY = bestVtx->position().y();
      }
    }
  }
  if( putTreeInTFile && tracksAvailable ) {
    iEvent.getByLabel( "generalTracks", theTracks );
    //nTracks->push_back( theTracks->size() );
    nTracks = theTracks->size();
  }

  GlobalPoint beamSpotPos;
  //GlobalPoint beamSpotPos(theBeamSpotH->position().x(),
  //			  theBeamSpotH->position().y(),
  //			  theBeamSpotH->position().z());
  if( beamSpotAvailable ) {
    beamSpotPos = GlobalPoint(theBeamSpotH->position().x(),
			      theBeamSpotH->position().y(),
			      theBeamSpotH->position().z());
  }
  
  typedef ROOT::Math::SMatrix<double, 3, 3, ROOT::Math::MatRepSym<double, 3> > SMatrixSym3D;
  typedef ROOT::Math::SVector<double, 3> SVector3;

  //cout << "Size: " << patHandle->size() << endl;
  /*for( pat::CompositeCandidateCollection::const_iterator iVEE = patHandle->begin();
       iVEE != patHandle->end();
       iVEE++ ) {
    cout << "PDG: " << iVEE->pdgId() << endl;
    }*/
  
  for( pat::CompositeCandidateCollection::const_iterator iV0 = patHandle->begin();
       iV0 != patHandle->end();
       iV0++ ) {
    
    reco::Track v0DauLowestpTTrack;

    std::vector<reco::Track> v0Daughters;
    std::vector<const reco::Candidate*> v0DauCands;
    //v0Daughters.push_back( iV0->getPosTrack() );
    v0Daughters.push_back( *((dynamic_cast<const reco::RecoCandidate*>(iV0->daughter(0)))->track()));
    v0Daughters.push_back( *((dynamic_cast<const reco::RecoCandidate*>(iV0->daughter(1)))->track()));
    if( iV0->daughter(0) ) {
      //cout << "Type of daughter(0): " << typeid(*(iV0->daughter(0))) << endl;
    }
    //cout << "Pushing back cands..." << endl;
    //v0DauCands.push_back( *(dynamic_cast<const reco::RecoChargedCandidate*>(iV0->daughter(0))) );
    //v0DauCands.push_back( *(dynamic_cast<const reco::RecoChargedCandidate*>(iV0->daughter(1))) );
    v0DauCands.push_back( iV0->daughter(0) );
    v0DauCands.push_back( iV0->daughter(1) );

    double tkpT = 100000.;
    bool wroteKsTreeHits = false;
    bool wroteKsHistoHits = false;
    bool wroteLamTreeHits = false;
    bool wroteLamHistoHits = false;

    GlobalVector v0Momentum;
    GlobalVector posDauMomentum;
    GlobalVector negDauMomentum;
    GlobalVector posDauCandMomentum;
    GlobalVector negDauCandMomentum;

    if( v0Daughters[0].charge() > 0 && v0Daughters[1].charge() < 0 ) {
      //cout << "Splat?" << endl;
      posDauMomentum = GlobalVector( v0Daughters[0].momentum().x(),
				     v0Daughters[0].momentum().y(),
				     v0Daughters[0].momentum().z() );
      negDauMomentum = GlobalVector( v0Daughters[1].momentum().x(),
				     v0Daughters[1].momentum().y(),
				     v0Daughters[1].momentum().z() );
      posDauCandMomentum = GlobalVector( v0DauCands[0]->momentum().x(),
				     v0DauCands[0]->momentum().y(),
				     v0DauCands[0]->momentum().z() );
      negDauCandMomentum = GlobalVector( v0DauCands[1]->momentum().x(),
				     v0DauCands[1]->momentum().y(),
				     v0DauCands[1]->momentum().z() );

    }
    else if (v0Daughters[0].charge() < 0. && v0Daughters[1].charge() > 0 ) {
      //cout << "Splat??" << endl;
      posDauMomentum = GlobalVector( v0Daughters[1].momentum().x(),
				     v0Daughters[1].momentum().y(),
				     v0Daughters[1].momentum().z() );
      negDauMomentum = GlobalVector( v0Daughters[0].momentum().x(),
				     v0Daughters[0].momentum().y(),
				     v0Daughters[0].momentum().z() );
      posDauCandMomentum = GlobalVector( v0DauCands[1]->momentum().x(),
				     v0DauCands[1]->momentum().y(),
				     v0DauCands[1]->momentum().z() );
      negDauCandMomentum = GlobalVector( v0DauCands[0]->momentum().x(),
				     v0DauCands[0]->momentum().y(),
				     v0DauCands[0]->momentum().z() );
    }
    else {
      posDauMomentum = GlobalVector( 0., 0., 0. );
      negDauMomentum = GlobalVector( 0., 0., 0. );
      posDauCandMomentum = GlobalVector( 0., 0., 0. );
      negDauCandMomentum = GlobalVector( 0., 0., 0.);
    }

    v0Momentum = GlobalVector( iV0->momentum().x(),
			       iV0->momentum().y(),
			       iV0->momentum().z() );

    double pTPlus = ( posDauCandMomentum.cross( v0Momentum.unit() ) ).mag();
    double pTMinus = ( negDauCandMomentum.cross( v0Momentum.unit() ) ).mag();
    double pLPlus = posDauCandMomentum.dot( v0Momentum.unit() );
    double pLMinus = negDauCandMomentum.dot( v0Momentum.unit() );
    //cout << "pTPlus = " << pTPlus << ", pTMinus = " << pTMinus << endl;

    if( pLPlus && iV0->pdgId() == 310 
	&& instanceName == string("Kshort") && putTreeInTFile) {
      v0pTPlus->push_back( pTPlus );
      v0pTMinus->push_back( pTMinus );
      v0pLPlus->push_back( pLPlus );
      v0pLMinus->push_back( pLMinus );
    }
    else if (pLPlus && abs(iV0->pdgId()) == 3122 
	     && instanceName == string("Lambda") && putTreeInTFile) {
      v0pTPlus->push_back( pTPlus );
      v0pTMinus->push_back( pTMinus );
      v0pLPlus->push_back( pLPlus );
      v0pLMinus->push_back( pLMinus );
    }


    for( std::vector<reco::Track>::iterator iDAU = v0Daughters.begin();
	 iDAU != v0Daughters.end();
	 iDAU++ ) {

      if( iDAU->pt() < tkpT ) {
	v0DauLowestpTTrack = *iDAU;
      }
      tkpT = iDAU->pt();
      // Fill daughter track branches
      if( iV0->pdgId() == 310 && instanceName == string("Kshort") ) {
	if( putTreeInTFile ) {
	  v0DaupT->push_back( iDAU->pt() );
	  v0Daup->push_back( iDAU->p() );
	  v0DaupX->push_back( iDAU->momentum().x() );
	  v0DaupY->push_back( iDAU->momentum().y() );
	  v0DaupZ->push_back( iDAU->momentum().z() );
	  v0DauEta->push_back( iDAU->eta() );
	  v0DauChi2->push_back( iDAU->chi2() );
	  v0DauNormChi2->push_back( iDAU->normalizedChi2() );
	  v0DauD0->push_back( iDAU->d0() );
	  if( !wroteKsTreeHits ) {
	    v0DauNValidHits->push_back( (float) (iV0->userInt("posTkNPixelHits") 
						 + iV0->userInt("posTkNStripHits") ) );
	    v0DauNValidHits->push_back( (float) (iV0->userInt("negTkNPixelHits")
						 + iV0->userInt("negTkNStripHits") ) );
	    v0DauNPixelHits->push_back( (float) iV0->userInt("posTkNPixelHits") );
	    v0DauNStripHits->push_back( (float) iV0->userInt("posTkNStripHits") );
	    v0DauNPixelHits->push_back( (float) iV0->userInt("negTkNPixelHits") );
	    v0DauNStripHits->push_back( (float) iV0->userInt("negTkNStripHits") );
	    wroteKsTreeHits = true;
	  }
	}
	if( (iV0->mass() > ksMassConst - 3*0.0058)
	    && (iV0->mass() < ksMassConst + 3*0.0058) 
	    && writeHistos ) {
	  ksDaupT->Fill( iDAU->pt() );
	  ksDaup->Fill( iDAU->p() );
	  ksDauEta->Fill( iDAU->eta() );
	  ksDauChi2->Fill( iDAU->chi2() );
	  ksDauNormChi2->Fill( iDAU->normalizedChi2() );
	  ksDauD0->Fill( iDAU->d0() );
	  if( !wroteKsHistoHits ) {
	    ksDauNValidHits->Fill( (float) (iV0->userInt("posTkNPixelHits")
				       + iV0->userInt("posTkNStripHits") ) );
	    ksDauNPixelHits->Fill( (float) iV0->userInt("posTkNPixelHits") );
	    ksDauNStripHits->Fill( (float) iV0->userInt("posTkNStripHits") );
	    ksDauNValidHits->Fill( (float) (iV0->userInt("negTkNPixelHits")
				       + iV0->userInt("negTkNStripHits") ) );
	    ksDauNPixelHits->Fill( (float) iV0->userInt("negTkNPixelHits") );
	    ksDauNStripHits->Fill( (float) iV0->userInt("negTkNStripHits") );
	    wroteKsHistoHits = true;
	  }
	}
      }
      // Lambda sigma = 0.002389 ~ 0.0024
      if( abs(iV0->pdgId()) == 3122 && instanceName == string("Lambda") ) {
	if( putTreeInTFile ) {
	  v0DaupT->push_back( iDAU->pt() );
	  v0Daup->push_back( iDAU->p() );
	  v0DaupX->push_back( iDAU->momentum().x() );
	  v0DaupY->push_back( iDAU->momentum().y() );
	  v0DaupZ->push_back( iDAU->momentum().z() );
	  v0DauEta->push_back( iDAU->eta() );
	  v0DauChi2->push_back( iDAU->chi2() );
	  v0DauNormChi2->push_back( iDAU->normalizedChi2() );
	  v0DauD0->push_back( iDAU->d0() );
	  if( !wroteLamTreeHits ) {
	    v0DauNValidHits->push_back( (float) (iV0->userInt("posTkNPixelHits") 
						 + iV0->userInt("posTkNStripHits") ) );
	    v0DauNValidHits->push_back( (float) (iV0->userInt("negTkNPixelHits")
						 + iV0->userInt("negTkNStripHits") ) );
	    v0DauNPixelHits->push_back( (float) iV0->userInt("posTkNPixelHits") );
	    v0DauNStripHits->push_back( (float) iV0->userInt("posTkNStripHits") );
	    v0DauNPixelHits->push_back( (float) iV0->userInt("negTkNPixelHits") );
	    v0DauNStripHits->push_back( (float) iV0->userInt("negTkNStripHits") );
	    wroteLamTreeHits = true;
	  }
	}
	if( (iV0->mass() > lamMassConst - 3*0.0024)
	    && (iV0->mass() < lamMassConst + 3*0.0024) 
	    && writeHistos ) {
	  lamDaupT->Fill( iDAU->pt() );
	  lamDaup->Fill( iDAU->p() );
	  lamDauEta->Fill( iDAU->eta() );
	  lamDauChi2->Fill( iDAU->chi2() );
	  lamDauNormChi2->Fill( iDAU->normalizedChi2() );
	  lamDauD0->Fill( iDAU->d0() );
	  if( !wroteLamHistoHits ) {
	    lamDauNValidHits->Fill( (float) (iV0->userInt("posTkNPixelHits")
					+ iV0->userInt("posTkNStripHits") ) );
	    lamDauNPixelHits->Fill( (float) iV0->userInt("posTkNPixelHits") );
	    lamDauNStripHits->Fill( (float) iV0->userInt("posTkNStripHits") );
	    lamDauNValidHits->Fill( (float) (iV0->userInt("negTkNPixelHits")
					+ iV0->userInt("negTkNStripHits") ) );
	    lamDauNPixelHits->Fill( (float) iV0->userInt("negTkNPixelHits") );
	    lamDauNStripHits->Fill( (float) iV0->userInt("negTkNStripHits") );
	    wroteLamHistoHits = true;
	  }
	}
      }
    }

    //cout << "They suck." << endl;
    double v0DauPhi_lowestpT_forHistos = 0.;
    // Fill daughter branches at vertex position
    GlobalVector posP( iV0->userFloat("posTkPX"),
		       iV0->userFloat("posTkPY"),
		       iV0->userFloat("posTkPZ") );
    GlobalVector negP( iV0->userFloat("negTkPX"),
		       iV0->userFloat("negTkPY"),
		       iV0->userFloat("negTkPZ") );
    double protonE = sqrt(posP.mag2() + protonMass2);
    double antiprotonE = sqrt(negP.mag2() + protonMass2);
    double posPiE = sqrt(posP.mag2() + piMass2);
    double negPiE = sqrt(negP.mag2() + piMass2);
    GlobalVector totalP = posP + negP;
    if( iV0->pdgId() == 310 && instanceName == string("Kshort") ) {

      //v0VtxChi2->push_back( iV0->UserFloat("vtxChi2") );
      //v0VtxNormChi2->push_back( iV0->UserFloat("vtxNormChi2") );

      double lamE = protonE + negPiE;
      double lamBarE = antiprotonE + posPiE;
      double lamMass = sqrt( lamE*lamE - totalP.mag2() );
      double lamBarMass = sqrt( lamBarE*lamBarE - totalP.mag2() );

      if( putTreeInTFile ) {
	if( (lamMass - lamMassConst) < (lamBarMass - lamMassConst) ) {
	  v0OtherCandMass->push_back( lamMass );
	}
	else {
	  v0OtherCandMass->push_back( lamBarMass );
	}
      }

      if( putTreeInTFile ) {
	v0DaupT_lowestpT->push_back( v0DauLowestpTTrack.pt() );
	v0DauEta_lowestpT->push_back( v0DauLowestpTTrack.eta() );
	v0VtxChi2->push_back( iV0->userFloat("vtxChi2") );
	v0VtxNormChi2->push_back( iV0->userFloat("vtxNormChi2") );
      }

      if( v0DauLowestpTTrack.charge() > 0. ) {
	if( putTreeInTFile ) v0DauPhi_lowestpT->push_back( posP.phi() );
	v0DauPhi_lowestpT_forHistos = posP.phi();
      }
      else {
	if( putTreeInTFile ) v0DauPhi_lowestpT->push_back( negP.phi() );
	v0DauPhi_lowestpT_forHistos = negP.phi();
      }
      if( putTreeInTFile ) {
	v0DauAtVtxpX->push_back( posP.x() );
	v0DauAtVtxpY->push_back( posP.y() );
	v0DauAtVtxpZ->push_back( posP.z() );
	v0DauPhi->push_back( posP.phi() );

	v0DauAtVtxpX->push_back( negP.x() );
	v0DauAtVtxpY->push_back( negP.y() );
	v0DauAtVtxpZ->push_back( negP.z() );
	v0DauPhi->push_back( negP.phi() );
      }
      if( (iV0->mass() > ksMassConst - 3*0.0058)
	  && (iV0->mass() < ksMassConst + 3*0.0058) 
	  && writeHistos ) {
	ksDauPhi->Fill( posP.phi() );
	ksDauPhi->Fill( negP.phi() );
      }
    }

    //cout << "They really do." << endl;
    if( abs(iV0->pdgId()) == 3122 && instanceName == string("Lambda") ) {

      double ksE = posPiE + negPiE;
      double ksM = sqrt( ksE*ksE - totalP.mag2() );

      if( putTreeInTFile ) {
	v0OtherCandMass->push_back( ksM );
      }
      if( putTreeInTFile ) {
	v0DaupT_lowestpT->push_back( v0DauLowestpTTrack.pt() );
	v0DauEta_lowestpT->push_back( v0DauLowestpTTrack.eta() );
	v0VtxChi2->push_back( iV0->userFloat("vtxChi2") );
	v0VtxNormChi2->push_back( iV0->userFloat("vtxNormChi2") );
      }

      if( v0DauLowestpTTrack.charge() > 0. ) {
	if( putTreeInTFile ) v0DauPhi_lowestpT->push_back( posP.phi() );
	v0DauPhi_lowestpT_forHistos = posP.phi();
      }
      else {
	if( putTreeInTFile ) v0DauPhi_lowestpT->push_back( negP.phi() );
	v0DauPhi_lowestpT_forHistos = negP.phi();
      }
      if( putTreeInTFile ) {
	v0DauAtVtxpX->push_back( posP.x() );
	v0DauAtVtxpY->push_back( posP.y() );
	v0DauAtVtxpZ->push_back( posP.z() );
	v0DauPhi->push_back( posP.phi() );

	v0DauAtVtxpX->push_back( negP.x() );
	v0DauAtVtxpY->push_back( negP.y() );
	v0DauAtVtxpZ->push_back( negP.z() );
	v0DauPhi->push_back( negP.phi() );
      }
      if( (iV0->mass() > lamMassConst - 3*0.0024)
	  && (iV0->mass() < lamMassConst + 3*0.0024) 
	  && writeHistos) {
	lamDauPhi->Fill( posP.phi() );
	lamDauPhi->Fill( negP.phi() );
      }
    }

    // Fill mass branch
    if( iV0->pdgId() == 310 && instanceName == string("Kshort") ) {
      if( putTreeInTFile ) {
	v0CandMass->push_back( iV0->mass() );
      }
      if( writeHistos ) {
	ksCandMass->Fill( iV0->mass() );
      }
    }
    if( abs(iV0->pdgId()) == 3122 && instanceName == string("Lambda") ) {
      if( putTreeInTFile ) {
	v0CandMass->push_back( iV0->mass() );
      }
      if( writeHistos ) {
	lamCandMass->Fill( iV0->mass() );
      }
    }

    // t = m(L - 15sigma)/p

    // Fill branches vertex quantities
    GlobalVector v0p_( iV0->momentum().x(),
		       iV0->momentum().y(),
		       iV0->momentum().z() );

    // Lifetime stuff
    if( beamSpotAvailable ) {    
      double cov00 = iV0->userFloat("vtxCov00");
      double cov01 = iV0->userFloat("vtxCov01");
      double cov11 = iV0->userFloat("vtxCov11");
      double cov02 = iV0->userFloat("vtxCov02");
      double cov12 = iV0->userFloat("vtxCov12");
      double cov22 = iV0->userFloat("vtxCov22");
      std::vector<double> covv;
      covv.push_back( cov00 );
      covv.push_back( cov01 );
      covv.push_back( cov11 );
      covv.push_back( cov02 );
      covv.push_back( cov12 );
      covv.push_back( cov22 );

      SMatrixSym3D vtxCov( covv.begin(), covv.end() );

      // Adding stuff for 3D lifetime.  This is the Vertex.
      //  Chi2 is BOGUS.  It shouldn't be needed for VertexDistance,
      //  so don't expect it to be right for any other purpose.
      reco::Vertex v0Vtx(iV0->vertex(), vtxCov, 1., 1., 2);
      //v0VtxPriDist(Err)
      if( pvAvailable && thePrim ) {
	//cout << "In new PV stuff" << endl;
	VertexDistance3D theDistCalculator;
	Measurement1D theDist1D =
	  theDistCalculator.signedDistance(*thePrim, v0Vtx, v0p_);
	//cout << "Just did distance calculation" << endl;
	double ltime3D = fabs( theDist1D.value() ) * iV0->mass() / v0p_.mag();

	//cout << "Found 3D lifetime: " << ltime3D << endl;

	if( putTreeInTFile && iV0->pdgId() == 310 
	    && instanceName == string("Kshort") && putTreeInTFile) {
	  //cout << "Putting into K0S vectors" << endl;
	  v0VtxPriDist->push_back( theDist1D.value() );
	  v0VtxPriDistErr->push_back( theDist1D.error() );
	  v03DLifetime->push_back( ltime3D ) ;
	}
	if( putTreeInTFile && abs(iV0->pdgId()) == 3122
	    && instanceName == string("Lambda") && putTreeInTFile) {
	  //cout << "Putting into Lambda vectors" << endl;
	  v0VtxPriDist->push_back( theDist1D.value() );
	  v0VtxPriDistErr->push_back( theDist1D.error() );
	  v03DLifetime->push_back( ltime3D );
	}

	//v03DLifetime->push_back( ltime3D );
	//cout << "Deleting primary we created before" << endl;
	//delete thePrim;
      }

      SMatrixSym3D totalCov = theBeamSpotH->covariance3D() + vtxCov;

      SVector3 distanceVector( iV0->vertex().x() - beamSpotPos.x(),
			       iV0->vertex().y() - beamSpotPos.y(),
			       0. );
      double rVtxMag = ROOT::Math::Mag(distanceVector);
      double sigmaRvtxMag = 
	sqrt(ROOT::Math::Similarity(totalCov, distanceVector)) / rVtxMag;


      //double sigmaR = (cov00*(iV0->vertex().x()*iV0->vertex().x())
      //	       + cov11*(iV0->vertex().y()*iV0->vertex().y())
      //	       + cov01*(iV0->vertex().x()*iV0->vertex().y())*2 );
      //double lifetime = v0p_.mag() * (iV0->vertex().Rho())/iV0->mass();
      //double ltime = (iV0->vertex().Rho() - 15.*sigmaR) 
      double ltime = ( rVtxMag - 15.*sigmaRvtxMag )
	//double ltime = (iV0->vertex().Rho())
	* iV0->mass()/v0p_.transverse();
      if( iV0->pdgId() == 310 && instanceName == string("Kshort") ) {
	if( putTreeInTFile ) {
	  v0Lifetime->push_back( ltime );
	  v0VtxSig->push_back( rVtxMag/sigmaRvtxMag );
	  v0VtxBSTransDist->push_back( rVtxMag );
	  v0VtxBSTransDistErr->push_back( sigmaRvtxMag );
	}
	if( writeHistos ) {
	  //  Nothing yet.
	}
      }
      if( abs(iV0->pdgId()) == 3122 && instanceName == string("Lambda") ) {
	if( putTreeInTFile ) {
	  v0Lifetime->push_back( ltime );
	  v0VtxSig->push_back( rVtxMag/sigmaRvtxMag );
	  v0VtxBSTransDist->push_back( rVtxMag );
	  v0VtxBSTransDistErr->push_back( sigmaRvtxMag );
	}
      }
    }//if(beamSpotAvailable)
    
    // Fill branches with vertex quantities
    if( iV0->pdgId() == 310 && instanceName == string("Kshort") ) {
      if( putTreeInTFile ) {
	v0VtxX->push_back( iV0->vertex().x() );
	v0VtxY->push_back( iV0->vertex().y() );
	v0VtxZ->push_back( iV0->vertex().z() );
	v0VtxR->push_back( iV0->vertex().Rho() );
	v0pX->push_back( v0p_.x() );
	v0pY->push_back( v0p_.y() );
	v0pZ->push_back( v0p_.z() );
	v0pT->push_back( v0p_.transverse() );
	v0p->push_back( v0p_.mag() );
	v0Eta->push_back( v0p_.eta() );
	v0Phi->push_back( v0p_.phi() );
	v0PDG->push_back( iV0->pdgId() );
      }
      if( writeHistos ) {
	ksRFull->Fill( iV0->vertex().Rho() );
	ksZFull->Fill( iV0->vertex().z() );
	ksZvsRFull->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	ksEtaFull->Fill( v0p_.eta() );
	ksPhiFull->Fill( v0p_.phi() );
	ksPtFull->Fill( v0p_.transverse() );
	if( iV0->mass() > (ksMassConst - 0.01) 
	    && iV0->mass() < (ksMassConst + 0.01) ) {
	  ksRSignal->Fill( iV0->vertex().Rho() );
	  ksZSignal->Fill( iV0->vertex().z() );
	  ksZvsRSignal->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	  ksEtaSignal->Fill( v0p_.eta() );
	  ksPhiSignal->Fill( v0p_.phi() );
	  ksPtSignal->Fill( v0p_.transverse() );
	}
	if( (iV0->mass() > 0.445 && iV0->mass() < 0.465) ||
	    (iV0->mass() > 0.55  && iV0->mass() < 0.57 ) ) {
	  ksRBg->Fill( iV0->vertex().Rho() );
	  ksZBg->Fill( iV0->vertex().z() );
	  //ksZvsRBg
	  ksEtaBg->Fill( v0p_.eta() );
	  ksPhiBg->Fill( v0p_.phi() );
	  ksPtBg->Fill( v0p_.transverse() );
	}
	if( (iV0->mass() < (ksMassConst - 0.01))
	    || (iV0->mass() > (ksMassConst + 0.01)) ) {
	  ksZvsRBg->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	}
      }
    }
    if( abs(iV0->pdgId()) == 3122 && instanceName == string("Lambda") ) {
      if( putTreeInTFile ) {
	v0VtxX->push_back( iV0->vertex().x() );
	v0VtxY->push_back( iV0->vertex().y() );
	v0VtxZ->push_back( iV0->vertex().z() );
	v0VtxR->push_back( iV0->vertex().Rho() );
	v0pX->push_back( v0p_.x() );
	v0pY->push_back( v0p_.y() );
	v0pZ->push_back( v0p_.z() );
	v0pT->push_back( v0p_.transverse() );
	v0p->push_back( v0p_.mag() );
	v0Eta->push_back( v0p_.eta() );
	v0Phi->push_back( v0p_.phi() );
	v0PDG->push_back( iV0->pdgId() );
      }
      if( writeHistos ) {
	lamRFull->Fill( iV0->vertex().Rho() );
	lamZFull->Fill( iV0->vertex().z() );
	lamZvsRFull->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	lamEtaFull->Fill( v0p_.eta() );
	lamPhiFull->Fill( v0p_.phi() );
	lamPtFull->Fill( v0p_.transverse() );
	if( iV0->mass() > (lamMassConst - 0.01) 
	    && iV0->mass() < (lamMassConst + 0.01) ) {
	  lamRSignal->Fill( iV0->vertex().Rho() );
	  lamZSignal->Fill( iV0->vertex().z() );
	  lamZvsRSignal->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	  lamEtaSignal->Fill( v0p_.eta() );
	  lamPhiSignal->Fill( v0p_.phi() );
	  lamPtSignal->Fill( v0p_.transverse() );
	}
	if( (iV0->mass() > 0.445 && iV0->mass() < 0.465) ||
	    (iV0->mass() > 0.55  && iV0->mass() < 0.57 ) ) {
	  lamRBg->Fill( iV0->vertex().Rho() );
	  lamZBg->Fill( iV0->vertex().z() );
	  //lamZvsRBg
	  lamEtaBg->Fill( v0p_.eta() );
	  lamPhiBg->Fill( v0p_.phi() );
	  lamPtBg->Fill( v0p_.transverse() );
	}
	if( (iV0->mass() < (lamMassConst - 0.01))
	    || (iV0->mass() > (lamMassConst + 0.01)) ) {
	  lamZvsRBg->Fill( iV0->vertex().z(), iV0->vertex().Rho(), 1. );
	}
      }
    }

    if( iV0->pdgId() == 310 
	&& instanceName == string("Kshort") 
	&& writeHistos) {
      double ksMass_eta_binWidth = 5. / (double) (ksMass_eta_nBins*2);
      double ksMass_eta_min = -2.5;
      for( vector<TH1F*>::iterator iETA = ksMass_eta.begin();
	   iETA != ksMass_eta.end();
	   iETA++ ) {
	if( v0DauLowestpTTrack.eta() > ksMass_eta_min 
	    && v0DauLowestpTTrack.eta() 
	    < (ksMass_eta_min + ksMass_eta_binWidth) ) {
	  (*iETA)->Fill( iV0->mass() );
	}
	ksMass_eta_min += ksMass_eta_binWidth;
      }

      double ksMass_phi_binWidth = 2*M_PI / (double) ksMass_phi_nBins;
      double ksMass_phi_min = -M_PI;
      for( vector<TH1F*>::iterator iPHI = ksMass_phi.begin();
	   iPHI != ksMass_phi.end();
	   iPHI++ ) {
	if( v0DauPhi_lowestpT_forHistos > ksMass_phi_min
	    && v0DauPhi_lowestpT_forHistos 
	    < (ksMass_phi_min + ksMass_phi_binWidth) ) {
	  (*iPHI)->Fill( iV0->mass() );
	}
	ksMass_phi_min += ksMass_phi_binWidth;
      }

      ksMass_phi_binWidth = 2*ksMass_phi_binWidth;
      ksMass_phi_min = -M_PI;
      ksMass_eta_min = -2.5;
      int phiCount = 0;
      int nPhi = ksMass_phi_nBins / 2;
      for( vector<TH1F*>::iterator iEP = ksMass_eta_phi.begin();
	   iEP != ksMass_eta_phi.end();
	   iEP++ ) {
	if( (v0DauPhi_lowestpT_forHistos > ksMass_phi_min
	     && v0DauPhi_lowestpT_forHistos < (ksMass_phi_min + ksMass_phi_binWidth))
	    && (v0DauLowestpTTrack.eta() > ksMass_eta_min
		&& v0DauLowestpTTrack.eta() < (ksMass_eta_min + ksMass_eta_binWidth) ) ) {
	  (*iEP)->Fill( iV0->mass() );
	}
	phiCount++;
	if( phiCount < nPhi ) {
	  ksMass_phi_min += ksMass_phi_binWidth;
	}
	else {
	  ksMass_phi_min = -M_PI;
	  ksMass_eta_min += ksMass_eta_binWidth;
	  phiCount = 0;
	}
      }

      // Need to do pT plots here
      int ptCounter = 0;
      for( vector<TH1F*>::iterator iPT = ksMass_pt.begin();
	   iPT != ksMass_pt.end();
	   iPT++ ) {
	if( ksMass_pt_minima[ptCounter] < 3. ) {
	  if( v0DauLowestpTTrack.pt() > ksMass_pt_minima[ptCounter]
	      && v0DauLowestpTTrack.pt() <= ksMass_pt_minima[ptCounter+1] ) {
	    (*iPT)->Fill( iV0->mass() );
	  }
	}
	else {
	  if( v0DauLowestpTTrack.pt() > 3. ) {
	    (*iPT)->Fill( iV0->mass() );
	  }
	}
	ptCounter++;
      }
    }

    if( abs(iV0->pdgId()) == 3122 
	&& instanceName == string("Lambda") 
	&& writeHistos ) {
      double lamMass_eta_binWidth = 5. / (double) (lamMass_eta_nBins*2);
      double lamMass_eta_min = -2.5;
      for( vector<TH1F*>::iterator iETA = lamMass_eta.begin();
	   iETA != lamMass_eta.end();
	   iETA++ ) {
	if( v0DauLowestpTTrack.eta() > lamMass_eta_min 
	    && v0DauLowestpTTrack.eta() 
	    < (lamMass_eta_min + lamMass_eta_binWidth) ) {
	  (*iETA)->Fill( iV0->mass() );
	}
	lamMass_eta_min += lamMass_eta_binWidth;
      }

      double lamMass_phi_binWidth = 2*M_PI / (double) lamMass_phi_nBins;
      double lamMass_phi_min = -M_PI;
      for( vector<TH1F*>::iterator iPHI = lamMass_phi.begin();
	   iPHI != lamMass_phi.end();
	   iPHI++ ) {
	if( v0DauPhi_lowestpT_forHistos > lamMass_phi_min
	    && v0DauPhi_lowestpT_forHistos 
	    < (lamMass_phi_min + lamMass_phi_binWidth) ) {
	  (*iPHI)->Fill( iV0->mass() );
	}
	lamMass_phi_min += lamMass_phi_binWidth;
      }

      // Need to do pT plots here
      int ptCounter2 = 0;
      for( vector<TH1F*>::iterator iPT = lamMass_pt.begin();
	   iPT != lamMass_pt.end();
	   iPT++ ) {
	if( lamMass_pt_minima[ptCounter2] < 3. ) {
	  if( v0DauLowestpTTrack.pt() > lamMass_pt_minima[ptCounter2]
	      && v0DauLowestpTTrack.pt() <= lamMass_pt_minima[ptCounter2+1] ) {
	    (*iPT)->Fill( iV0->mass() );
	  }
	}
	else {
	  if( v0DauLowestpTTrack.pt() > 3. ) {
	    (*iPT)->Fill( iV0->mass() );
	  }
	}
	ptCounter2++;
      }
    }
  
  }

  if( thePrim ) delete thePrim;

  // Fill the tree
  if( putTreeInTFile ) {
    theTree->Fill();
  }

  if( putTreeInTFile ) {
    v0VtxX->clear(); v0VtxY->clear(); v0VtxZ->clear(); v0VtxR->clear(); v0VtxChi2->clear(); v0VtxNormChi2->clear();
    //v0VtxCXX->clear(); v0VtxCYY->clear(); v0VtxCZZ->clear(); v0VtxCYX->clear(); v0VtxCZX->clear(); v0VtxCZY->clear();
    //v0VtxChi2->clear(); v0VtxNormChi2->clear();
    
    v0pX->clear(); v0pY->clear(); v0pZ->clear(); v0pT->clear(); v0p->clear(); v0Eta->clear(); v0Phi->clear();
    v0pTPlus->clear(); v0pTMinus->clear(); v0pLPlus->clear(); v0pLMinus->clear();
    //v0pXerr->clear(); v0pYerr->clear(); v0pZerr->clear();
    
    v0CandMass->clear(); v0OtherCandMass->clear();
    v0Lifetime->clear(); v03DLifetime->clear();
    v0PDG->clear(); v0VtxSig->clear();
    //priVtxChi2->clear(); 
    //priVtxNdof->clear(); nTracks->clear(); nV0s->clear();

    v0VtxPriDist->clear(); v0VtxPriDistErr->clear();
    v0VtxBSTransDist->clear(); v0VtxBSTransDistErr->clear();
    
    v0DaupT->clear(); v0Daup->clear(); v0DaupX->clear(); v0DaupY->clear(); v0DaupZ->clear();
    v0DauAtVtxpX->clear(); v0DauAtVtxpY->clear(); v0DauAtVtxpZ->clear();
    v0DauEta->clear(); v0DauPhi->clear();
    v0DauNValidHits->clear(); v0DauNStripHits->clear(); v0DauNPixelHits->clear();
    v0DauChi2->clear(); v0DauNormChi2->clear(); v0DauD0->clear();
    
    v0DaupT_lowestpT->clear(); v0DauEta_lowestpT->clear(); v0DauPhi_lowestpT->clear();
  }
}


void V0RecoAnalyzer::beginJob() {
  using namespace std;

  edm::Service<TFileService> fs;

  if( putTreeInTFile ) {
    theTree = fs->make<TTree>("ntuple", "vee ntuple");
    theTree->Branch("v0VtxX", &v0VtxX);
    theTree->Branch("v0VtxY", &v0VtxY);
    theTree->Branch("v0VtxZ", &v0VtxZ);
    theTree->Branch("v0VtxR", &v0VtxR);
    theTree->Branch("v0VtxChi2", &v0VtxChi2);
    theTree->Branch("v0VtxNormChi2", &v0VtxNormChi2);
  /*theTree->Branch("v0VtxCXX", &v0VtxCXX);
    theTree->Branch("v0VtxCYY", &v0VtxCYY);
    theTree->Branch("v0VtxCZZ", &v0VtxCZZ);
    theTree->Branch("v0VtxCYX", &v0VtxCYX);
    theTree->Branch("v0VtxCZX", &v0VtxCZX);
    theTree->Branch("v0VtxCZY", &v0VtxCZY);
    theTree->Branch("v0VtxChi2", &v0VtxChi2);
    theTree->Branch("v0VtxNormChi2", &v0VtxNormChi2);*/
    
    theTree->Branch("v0pX", &v0pX);
    theTree->Branch("v0pY", &v0pY);
    theTree->Branch("v0pZ", &v0pZ);
    theTree->Branch("v0pT", &v0pT);
    theTree->Branch("v0p", &v0p);
    theTree->Branch("v0Eta", &v0Eta);
    theTree->Branch("v0Phi", &v0Phi);
  /*theTree->Branch("v0pXerr", &v0pXerr);
    theTree->Branch("v0pYerr", &v0pYerr);
    theTree->Branch("v0pZerr", &v0pZerr);*/

    theTree->Branch("v0pTPlus", &v0pTPlus);
    theTree->Branch("v0pTMinus", &v0pTMinus);
    theTree->Branch("v0pLPlus", &v0pLPlus);
    theTree->Branch("v0pLMinus", &v0pLMinus);
  
    theTree->Branch("v0CandMass", &v0CandMass);
    theTree->Branch("v0OtherCandMass", &v0OtherCandMass);

    theTree->Branch("v0Lifetime", &v0Lifetime);
    theTree->Branch("v03DLifetime", &v03DLifetime);

    theTree->Branch("v0PDG", &v0PDG);

    theTree->Branch("v0VtxSig", &v0VtxSig);

    //theTree->Branch("priVtxChi2", &priVtxChi2);
    //theTree->Branch("priVtxNdof", &priVtxNdof);
    //theTree->Branch("nTracks", &nTracks);
    //theTree->Branch("nV0s", &nV0s);
    theTree->Branch("priVtxChi2", &priVtxChi2, "priVtxChi2/F");
    theTree->Branch("privtxNdof", &priVtxNdof, "priVtxNdof/F");
    theTree->Branch("priVtxX", &priVtxX, "priVtxX/F");
    theTree->Branch("priVtxY", &priVtxY, "priVtxY/F");
    theTree->Branch("priVtxZ", &priVtxZ, "priVtxZ/F");
    theTree->Branch("nTracks", &nTracks, "nTracks/I");
    theTree->Branch("nV0s", &nV0s, "nV0s/I");

    theTree->Branch("v0VtxPriDist", &v0VtxPriDist);
    theTree->Branch("v0VtxPriDistErr", &v0VtxPriDistErr);
    theTree->Branch("v0VtxBSTransDist", &v0VtxBSTransDist);
    theTree->Branch("v0VtxBSTransDistErr", &v0VtxBSTransDistErr);
  
    theTree->Branch("v0DaupT", &v0DaupT);
    theTree->Branch("v0Daup", &v0Daup);
    theTree->Branch("v0DaupX", &v0DaupX);
    theTree->Branch("v0DaupY", &v0DaupY);
    theTree->Branch("v0DaupZ", &v0DaupZ);
    theTree->Branch("v0DauAtVtxpX", &v0DauAtVtxpX);
    theTree->Branch("v0DauAtVtxpY", &v0DauAtVtxpY);
    theTree->Branch("v0DauAtVtxpZ", &v0DauAtVtxpZ);
    theTree->Branch("v0DauEta", &v0DauEta);
    theTree->Branch("v0DauPhi", &v0DauPhi);
    theTree->Branch("v0DauNValidHits", &v0DauNValidHits);
    theTree->Branch("v0DauNPixelHits", &v0DauNPixelHits);
    theTree->Branch("v0DauNStripHits", &v0DauNStripHits);
    theTree->Branch("v0DauChi2", &v0DauChi2);
    theTree->Branch("v0DauNormChi2", &v0DauNormChi2);
    theTree->Branch("v0DauD0", &v0DauD0);

    theTree->Branch("v0DaupT_lowestpT", &v0DaupT_lowestpT);
    theTree->Branch("v0DauEta_lowestpT", &v0DauEta_lowestpT);
    theTree->Branch("v0DauPhi_lowestpT", &v0DauPhi_lowestpT);
  }

    ksMassBinWidth = (ksMassXmax - ksMassXmin) / (double) ksMassNbins;
    lamMassBinWidth = (lamMassXmax - lamMassXmin) / (double) lamMassNbins;

  if( writeHistos ) {
    if( instanceName == string("Kshort") ) {
      ksR = fs->make<TH1F>("ksR", "K^{0}_{S} radial distance from beam line",
			   50, 0., 40.);
      ksRFull = fs->make<TH1F>("ksRFull", "K^{0}_{S} radial distance from beam line",
			       50, 0., 40.);
      ksRSignal = fs->make<TH1F>("ksRSignal", "K^{0}_{S} radial distance from beam line",
				 50, 0., 40.);
      ksRBg = fs->make<TH1F>("ksRBg", "K^{0}_{S} radial distance from beam line",
			     50, 0., 40.);
      
      ksZ = fs->make<TH1F>("ksZ", "K^{0}_{S} z position",
			   50, -150., 150.);
      ksZFull = fs->make<TH1F>("ksZFull", "K^{0}_{S} z position",
			       50, -150., 150.);
      ksZSignal = fs->make<TH1F>("ksZSignal", "K^{0}_{S} z position",
				 50, -150., 150.);
      ksZBg = fs->make<TH1F>("ksZBg", "K^{0}_{S} z position",
			     50, -150., 150.);

      ksZvsRFull = fs->make<TH2F>("ksZvsRFull", "K^{0}_{S} z position vs. decay radius",
				  120, -120., 120., 40, 0., 40.);
      ksZvsRBgSubt = fs->make<TH2F>("ksZvsRBgSubt", "K^{0}_{S} z position vs. decay radius",
				    120, -120., 120., 40, 0., 40.);
      ksZvsRBg = fs->make<TH2F>("ksZvsRBg", "K^{0}_{S} z position vs. decay radius",
				120, -120., 120., 40, 0., 40.);
      ksZvsRSignal = fs->make<TH2F>("ksZvsRSignal", "K^{0}_{S} z position vs. decay radius",
				    120, -120., 120., 40, 0., 40.);
    
      ksEta = fs->make<TH1F>("ksEta", "K^{0}_{S} momentum #eta",
			     40, -2.5, 2.5);
      ksEtaFull = fs->make<TH1F>("ksEtaFull", "K^{0}_{S} momentum #eta",
				 40, -2.5, 2.5);
      ksEtaSignal = fs->make<TH1F>("ksEtaSignal", "K^{0}_{S} momentum #eta",
				   40, -2.5, 2.5);
      ksEtaBg = fs->make<TH1F>("ksEtaBg", "K^{0}_{S} momentum #eta",
			       40, -2.5, 2.5);
    
      ksPhi = fs->make<TH1F>("ksPhi", "K^{0}_{S} momentum #phi",
			     60, -M_PI, M_PI);
      ksPhiFull = fs->make<TH1F>("ksPhiFull", "K^{0}_{S} momentum #phi",
				 60, -M_PI, M_PI);
      ksPhiSignal = fs->make<TH1F>("ksPhiSignal", "K^{0}_{S} momentum #phi",
				   60, -M_PI, M_PI);
      ksPhiBg = fs->make<TH1F>("ksPhiBg", "K^{0}_{S} momentum #phi",
			       60, -M_PI, M_PI);
      
      ksPt = fs->make<TH1F>("ksPt", "K^{0}_{S} p_{T}",
			    70, 0., 20.);
      ksPtFull = fs->make<TH1F>("ksPtFull", "K^{0}_{S} p_{T}",
				70, 0., 20.);
      ksPtSignal = fs->make<TH1F>("ksPtSignal", "K^{0}_{S} p_{T}",
				  70, 0., 20.);
      ksPtBg = fs->make<TH1F>("ksPtBg", "K^{0}_{S} p_{T}",
			      70, 0., 20.);

      ksCandMass = fs->make<TH1F>("ksCandMass", "K^{0}_{S} mass from Candidate",
				  ksMassNbins, ksMassXmin, ksMassXmax);
	
      ksDaup = fs->make<TH1F>("ksDaup", "p of K^{0}_{S} daughter tracks",
			      100, 0., 30.);
      ksDaupT = fs->make<TH1F>("ksDaupT", "p_{T} of K^{0}_{S} daughter tracks",
			       100, 0., 20.);
      ksDauEta = fs->make<TH1F>("ksDauEta", "#eta of K^{0}_{S} daughter tracks",
				100, -2.5, 2.5);
      ksDauPhi = fs->make<TH1F>("ksDauPhi", "#phi of K^{0}_{S} daughter track at vertex position",
				70, -M_PI, M_PI);
      ksDauNValidHits = fs->make<TH1F>("ksDauNValHits", 
				       "Number of valid hits on K^{0}_{S} daughter tracks", 
				       80, 0., 40.);
      ksDauNPixelHits = fs->make<TH1F>("ksDauNPixelHits", 
				       "Number of valid pixel hits on K^{0}_{S} daughter tracks",
				       30 , 0., 15.);
      ksDauNStripHits = fs->make<TH1F>("ksDauNStripHits", 
				       "Number of valid strip hits on K^{0}_{S} daughter tracks",
				       80, 0., 40.);
      ksDauChi2 = fs->make<TH1F>("ksDauChi2", "#chi^{2} of K^{0}_{S} daughter tracks",
				 100, 0., 100.);
      ksDauNormChi2 = fs->make<TH1F>("ksDauNormChi2", "#chi^{2}/ndof of K^{0}_{S} daughter tracks",
				     100, 0., 5.);
      ksDauD0 = fs->make<TH1F>("ksDauD0", "abs(d_{0}) of K^{0}_{S} daughter tracks",
			       100, 0., 15.);

      double ksMass_eta_binWidth = 5. / (double) (ksMass_eta_nBins*2);
      for( double ksMass_eta_min = -2.5;
	   ksMass_eta_min < 2.5;
	   ksMass_eta_min += ksMass_eta_binWidth ) {
	ostringstream etaNameShort;
	ostringstream etaNameLong;
	etaNameShort << "ksMass_eta_" << ksMass_eta_min;
	etaNameLong << "K^{0}_{S} invariant mass " << ksMass_eta_min
		    << " < #eta < " << ksMass_eta_min + ksMass_eta_binWidth;
	/*ksMass_eta.push_back( fs->make<TH1F>((string("ksMass_eta_") 
					      + string(ksMass_eta_min)).c_str(),
					     (string("K^{0}_{S} invariant mass eta min ")
					     + string(ksMass_eta_min)).c_str(),*/
	ksMass_eta.push_back( fs->make<TH1F>(etaNameShort.str().c_str(),
					     etaNameLong.str().c_str(),
					     ksMassNbins, ksMassXmin, ksMassXmax) );
	ksMass_eta_names_short.push_back( etaNameShort.str() );
	ksMass_eta_names_long.push_back( etaNameLong.str() );
	ksMass_eta_minima.push_back( ksMass_eta_min );
      }
      ksMassInEtaBins = fs->make<TH1F>("KsMassBiasVsEta", 
				       "K^{0}_{S} mass bias vs. #eta of lowest-p_{T} track",
				       ksMass_eta_nBins*2, -2.5, 2.5); 

      double ksMass_phi_binWidth = 2*M_PI / (double) ksMass_phi_nBins;
      for( double ksMass_phi_min = -M_PI;
	   ksMass_phi_min < M_PI - 0.0001;
	   ksMass_phi_min += ksMass_phi_binWidth ) {
	ostringstream phiNameShort;
	ostringstream phiNameLong;
	phiNameShort << "ksMass_phi_" << ksMass_phi_min;
	phiNameLong << "K^{0}_{S} invariant mass " << ksMass_phi_min
		    << " < #phi < " << ksMass_phi_min + ksMass_phi_binWidth;
	/*ksMass_phi.push_back( fs->make<TH1F>((string("ksMass_phi_")
					      + string(ksMass_phi_min)).c_str(),
					     (string("K^{0}_{S} invariant mass phi min ")
					     + string(ksMass_phi_min)).c_str(),*/
	ksMass_phi.push_back( fs->make<TH1F>(phiNameShort.str().c_str(),
					     phiNameLong.str().c_str(),
					     ksMassNbins, ksMassXmin, ksMassXmax) );
	ksMass_phi_names_short.push_back( phiNameShort.str() );
	ksMass_phi_names_long.push_back( phiNameLong.str() );
	ksMass_phi_minima.push_back( ksMass_phi_min );
      }
      ksMassInPhiBins = fs->make<TH1F>("KsMassBiasVsPhi", 
				       "K^{0}_{S} mass bias vs. #phi of lowest-p_{T} track",
				       ksMass_phi_nBins, -M_PI, M_PI); 

      for(double ksMass_eta_min = -2.5;
	  ksMass_eta_min < 2.5;
	  ksMass_eta_min += ksMass_eta_binWidth ) {
	for(double ksMass_phi_min = -M_PI;
	    ksMass_phi_min < M_PI - 0.0001;
	    ksMass_phi_min += ksMass_phi_binWidth*2 ) {
	  ostringstream shortNames2D;
	  ostringstream longNames2D;
	  shortNames2D << "ksMass_2D_" << ksMass_eta_min << "_" << ksMass_phi_min;
	  longNames2D << "Ks invariant mass, " << ksMass_eta_min << " < #eta < "
		      << ksMass_eta_min + ksMass_eta_binWidth << ", "
		      << ksMass_phi_min << " < #phi < " << ksMass_phi_min + ksMass_phi_binWidth;
	  ksMass_eta_phi.push_back( fs->make<TH1F>(shortNames2D.str().c_str(),
						   longNames2D.str().c_str(),
						   ksMassNbins/2, ksMassXmin, ksMassXmax) );
	  ksMass_eta_phi_names_short.push_back( shortNames2D.str() );
	  ksMass_eta_phi_names_long.push_back( longNames2D.str() );
	  ksMass_eta_phi_etaminima.push_back( ksMass_eta_min );
	  ksMass_eta_phi_phiminima.push_back( ksMass_phi_min );
	}
      }
      ksMassBiasEtaVsPhi = fs->make<TH2F>("KsMassBiasEtaVsPhi",
					  "K^{0}_{S} mass bias #eta vs. #phi",
					  ksMass_phi_nBins/2,
					  -M_PI, M_PI,
					  ksMass_eta_nBins*2,
					  -2.5, 2.5);

      double ksMass_pt_binWidth1 = 0.25 / (double) ksMass_pt_nBinSubdiv;//0. < pT < 0.25
      double ksMass_pt_binWidth2 = ksMass_pt_binWidth1;//0.25 < pT < 0.5
      double ksMass_pt_binWidth3 = 0.5 / (double) ksMass_pt_nBinSubdiv;//0.5 < pT < 1.
      double ksMass_pt_binWidth4 = ksMass_pt_binWidth3;//1. < pT < 1.5
      double ksMass_pt_binWidth5 = ksMass_pt_binWidth3;//1.5 < pT < 2.
      double ksMass_pt_binWidth6 = 1.0 / (double) ksMass_pt_nBinSubdiv;//2. < pT < 3.
      double ksMass_pt_min = 0.;
      //cout << "Making pT histos" << endl;
      while( ksMass_pt_min <= 3. ) {
	//cout << "ksMass_pt_min: " << ksMass_pt_min << endl;
	ostringstream ptNameShort;
	ostringstream ptNameLong;
	ptNameShort << "ksMass_pt_" << ksMass_pt_min;
	ptNameLong << "K^{0}_{S} invariant mass, p_{T} bin minimum = "
		   << ksMass_pt_min;
	ksMass_pt.push_back( fs->make<TH1F>(ptNameShort.str().c_str(),
					    ptNameLong.str().c_str(),
					    ksMassNbins, ksMassXmin, ksMassXmax) );
	ksMass_pt_names_short.push_back( ptNameShort.str() );
	ksMass_pt_names_long.push_back( ptNameLong.str() );
	ksMass_pt_minima.push_back( ksMass_pt_min );
	//cout << "Minima size is now " << ksMas
	if( ksMass_pt_min < 0.25
	    && (ksMass_pt_min + ksMass_pt_binWidth1) <= 0.25)  {
	  ksMass_pt_min += ksMass_pt_binWidth1;
	}
	else if( ksMass_pt_min < 0.25
		 && (ksMass_pt_min + ksMass_pt_binWidth1) > 0.25 ) {
	  ksMass_pt_min += ksMass_pt_binWidth2;
	}
	else if( ksMass_pt_min < 0.5
		 && (ksMass_pt_min + ksMass_pt_binWidth2) <= 0.5 ) {
	  ksMass_pt_min += ksMass_pt_binWidth2;
	}
	else if( ksMass_pt_min < 0.5
		 && (ksMass_pt_min + ksMass_pt_binWidth2) > 0.5 ) {
	  ksMass_pt_min += ksMass_pt_binWidth3;
	}
	else if( ksMass_pt_min < 1.
		 && (ksMass_pt_min + ksMass_pt_binWidth3) <= 1. ) {
	  ksMass_pt_min += ksMass_pt_binWidth3;
	}
	else if( ksMass_pt_min < 1.
		 && (ksMass_pt_min + ksMass_pt_binWidth3) > 1. ) {
	  ksMass_pt_min += ksMass_pt_binWidth4;
	}
	else if( ksMass_pt_min < 1.5
		 && (ksMass_pt_min + ksMass_pt_binWidth4) <= 1.5 ) {
	  ksMass_pt_min += ksMass_pt_binWidth4;
	}
	else if( ksMass_pt_min < 1.5
		 && (ksMass_pt_min + ksMass_pt_binWidth4) > 1.5 ) {
	  ksMass_pt_min += ksMass_pt_binWidth5;
	}
	else if( ksMass_pt_min < 2.
		 && (ksMass_pt_min + ksMass_pt_binWidth5) <= 2. ) {
	  ksMass_pt_min += ksMass_pt_binWidth5;
	}
	else if( ksMass_pt_min < 2.
		 && (ksMass_pt_min + ksMass_pt_binWidth5) > 2. ) {
	  ksMass_pt_min += ksMass_pt_binWidth6;
	}
	else if( ksMass_pt_min < 3.
		 && (ksMass_pt_min + ksMass_pt_binWidth6) <= 3. ) {
	  ksMass_pt_min += ksMass_pt_binWidth6;
	}
	else if( ksMass_pt_min < 3.) {
	  ksMass_pt_min = 3.;
	}
	else {
	  ksMass_pt_min = 4.;
	}

      }

      vector<float> minimaForTH1;
      unsigned int ndx = 0;
      for( vector<double>::iterator iMIN = ksMass_pt_minima.begin();
	   iMIN != ksMass_pt_minima.end();
	   iMIN++ ) {
	minimaForTH1.push_back(*iMIN);
	if( ndx == ksMass_pt_minima.size() - 1 ) {
	  //cout << "Pushed back a 15. " << endl;
	  minimaForTH1.push_back( 6. );
	}
	ndx++;
      }
      ksMassInPtBins = fs->make<TH1F>("KsMassBiasVsPt",
				      "K^{0}_{S} mass bias vs. p_{T} of lowest-p_{T} track",
				      ksMass_pt_minima.size(), &minimaForTH1[0]);

    }
    if( instanceName == string("Lambda") ) {
      lamR = fs->make<TH1F>("lamR", "#Lambda^{0} radial distance from beam line",
			    50, 0., 40.);
      lamRFull = fs->make<TH1F>("lamRFull", "#Lambda^{0} radial distance from beam line",
				50, 0., 40.);
      lamRSignal = fs->make<TH1F>("lamRSignal", "#Lambda^{0} radial distance from beam line",
				  50, 0., 40.);
      lamRBg = fs->make<TH1F>("lamRBg", "#Lambda^{0} radial distance from beam line",
			      50, 0., 40.);
      
      lamZ = fs->make<TH1F>("lamZ", "#Lambda^{0} z position",
			    50, -150., 150.);
      lamZFull = fs->make<TH1F>("lamZFull", "#Lambda^{0} z position",
				50, -150., 150.);
      lamZSignal = fs->make<TH1F>("lamZSignal", "#Lambda^{0} z position",
				  50, -150., 150.);
      lamZBg = fs->make<TH1F>("lamZBg", "#Lambda^{0} z position",
			      50, -150., 150.);

      lamZvsRFull = fs->make<TH2F>("lamZvsRFull", "#Lambda^{0} z position vs. decay radius",
				   120, -120., 120., 40, 0., 40.);
      lamZvsRBgSubt = fs->make<TH2F>("lamZvsRBgSubt", "#Lambda^{0} z position vs. decay radius",
				     120, -120., 120., 40, 0., 40.);
      lamZvsRBg = fs->make<TH2F>("lamZvsRBg", "#Lambda^{0} z position vs. decay radius",
				 120, -120., 120., 40, 0., 40.);
      lamZvsRSignal = fs->make<TH2F>("lamZvsRSignal", "#Lambda^{0} z position vs. decay radius",
				     120, -120., 120., 40, 0., 40.);
    
      lamEta = fs->make<TH1F>("lamEta", "#Lambda^{0} momentum #eta",
			      40, -2.5, 2.5);
      lamEtaFull = fs->make<TH1F>("lamEtaFull", "#Lambda^{0} momentum #eta",
				  40, -2.5, 2.5);
      lamEtaSignal = fs->make<TH1F>("lamEtaSignal", "#Lambda^{0} momentum #eta",
				    40, -2.5, 2.5);
      lamEtaBg = fs->make<TH1F>("lamEtaBg", "#Lambda^{0} momentum #eta",
				40, -2.5, 2.5);
      
      lamPhi = fs->make<TH1F>("lamPhi", "#Lambda^{0} momentum #phi",
			      60, -M_PI, M_PI);
      lamPhiFull = fs->make<TH1F>("lamPhiFull", "#Lambda^{0} momentum #phi",
				  60, -M_PI, M_PI);
      lamPhiSignal = fs->make<TH1F>("lamPhiSignal", "#Lambda^{0} momentum #phi",
				    60, -M_PI, M_PI);
      lamPhiBg = fs->make<TH1F>("lamPhiBg", "#Lambda^{0} momentum #phi",
				60, -M_PI, M_PI);
    
      lamPt = fs->make<TH1F>("lamPt", "#Lambda^{0} p_{T}",
			     70, 0., 20.);
      lamPtFull = fs->make<TH1F>("lamPtFull", "#Lambda^{0} p_{T}",
				 70, 0., 20.);
      lamPtSignal = fs->make<TH1F>("lamPtSignal", "#Lambda^{0} p_{T}",
				   70, 0., 20.);
      lamPtBg = fs->make<TH1F>("lamPtBg", "#Lambda^{0} p_{T}",
			       70, 0., 20.);

      lamCandMass = fs->make<TH1F>("lamCandMass", "#Lambda^{0} mass from Candidate",
				   lamMassNbins, lamMassXmin, lamMassXmax);
      
      lamDaup = fs->make<TH1F>("lamDaup", "p of #Lambda^{0} daughter tracks",
			       100, 0., 30.);
      lamDaupT = fs->make<TH1F>("lamDaupT", "p_{T} of #Lambda^{0} daughter tracks",
				100, 0., 20.);
      lamDauEta = fs->make<TH1F>("lamDauEta", "#eta of #Lambda^{0} daughter tracks",
				 100, -2.5, 2.5);
      lamDauPhi = fs->make<TH1F>("lamDauPhi", "#phi of #Lambda^{0} daughter track at vertex position",
				 70, -M_PI, M_PI);
      lamDauNValidHits = fs->make<TH1F>("lamDauNValHits", 
					"Number of valid hits on #Lambda^{0} daughter tracks", 
					80, 0., 40.);
      lamDauNPixelHits = fs->make<TH1F>("lamDauNPixelHits", 
					"Number of valid pixel hits on #Lambda^{0} daughter tracks",
					30 , 0., 15.);
      lamDauNStripHits = fs->make<TH1F>("lamDauNStripHits", 
					"Number of valid strip hits on #Lambda^{0} daughter tracks",
					80, 0., 40.);
      lamDauChi2 = fs->make<TH1F>("lamDauChi2", "#chi^{2} of #Lambda^{0} daughter tracks",
				  100, 0., 100.);
      lamDauNormChi2 = fs->make<TH1F>("lamDauNormChi2", "#chi^{2}/ndof of #Lambda^{0} daughter tracks",
				      100, 0., 5.);
      lamDauD0 = fs->make<TH1F>("lamDauD0", "abs(d_{0}) of #Lambda^{0} daughter tracks",
				100, 0., 15.);

      double lamMass_eta_binWidth = 5. / (double) (lamMass_eta_nBins*2);
      for( double lamMass_eta_min = -2.5;
	   lamMass_eta_min < 2.5;
	   lamMass_eta_min += lamMass_eta_binWidth ) {
	ostringstream etaNameShort;
	ostringstream etaNameLong;
	etaNameShort << "lamMass_eta_" << lamMass_eta_min;
	etaNameLong << "#Lambda^{0} invariant mass " << lamMass_eta_min
		    << " < #eta < " << lamMass_eta_min + lamMass_eta_binWidth;
	/*lamMass_eta.push_back( fs->make<TH1F>((string("lamMass_eta_") 
					       + string(lamMass_eta_min)).c_str(),
					      (string("#Lambda^{0} invariant mass eta min ")
					      + string(lamMass_eta_min)).c_str(),*/
	lamMass_eta.push_back( fs->make<TH1F>(etaNameShort.str().c_str(),
					      etaNameLong.str().c_str(),
					      lamMassNbins, lamMassXmin, lamMassXmax) );
	lamMass_eta_names_short.push_back( etaNameShort.str() );
	lamMass_eta_names_long.push_back( etaNameLong.str() );
	lamMass_eta_minima.push_back( lamMass_eta_min );
      }
      lamMassInEtaBins = fs->make<TH1F>("LamMassBiasVsEta", 
					"#Lambda^{0} mass bias vs. #eta of lowest-p_{T} track",
					lamMass_eta_nBins*2, -2.5, 2.5); 

      double lamMass_phi_binWidth = 2*M_PI / (double) lamMass_phi_nBins;
      for( double lamMass_phi_min = -M_PI;
	   lamMass_phi_min < M_PI - 0.001;
	   lamMass_phi_min += lamMass_phi_binWidth ) {
	ostringstream phiNameShort;
	ostringstream phiNameLong;
	phiNameShort << "lamMass_phi_" << lamMass_phi_min;
	phiNameLong << "#Lambda^{0} invariant mass " << lamMass_phi_min
		    << " < #phi < " << lamMass_phi_min + lamMass_phi_binWidth;
	/*lamMass_phi.push_back( fs->make<TH1F>((string("lamMass_phi_")
					       + string(lamMass_phi_min)).c_str(),
					      (string("#Lambda^{0} invariant mass phi min ")
					      + string(lamMass_phi_min)).c_str(),*/
	lamMass_phi.push_back( fs->make<TH1F>(phiNameShort.str().c_str(),
					      phiNameLong.str().c_str(),
					      lamMassNbins, lamMassXmin, lamMassXmax) );
	lamMass_phi_names_short.push_back( phiNameShort.str() );
	lamMass_phi_names_long.push_back( phiNameLong.str() );
	lamMass_phi_minima.push_back( lamMass_phi_min );
      }
      lamMassInPhiBins = fs->make<TH1F>("LamMassBiasVsPhi",
					"#Lambda^{0} mass bias vs. #phi of lowest-p_{T} track",
					lamMass_phi_nBins, -M_PI, M_PI);

      double lamMass_pt_binWidth1 = 0.25 / (double) lamMass_pt_nBinSubdiv;//0. < pT < 0.25
      double lamMass_pt_binWidth2 = lamMass_pt_binWidth1;//0.25 < pT < 0.5
      double lamMass_pt_binWidth3 = 0.5 / (double) lamMass_pt_nBinSubdiv;//0.5 < pT < 1.
      double lamMass_pt_binWidth4 = lamMass_pt_binWidth3;//1. < pT < 1.5
      double lamMass_pt_binWidth5 = lamMass_pt_binWidth3;//1.5 < pT < 2.
      double lamMass_pt_binWidth6 = 1.0 / (double) lamMass_pt_nBinSubdiv;//2. < pT < 3.
      double lamMass_pt_min = 0.;
      //cout << "Making pT histos" << endl;
      while( lamMass_pt_min <= 3. ) {
	//cout << "lamMass_pt_min: " << lamMass_pt_min << endl;
	ostringstream ptNameShort;
	ostringstream ptNameLong;
	ptNameShort << "lamMass_pt_" << lamMass_pt_min;
	ptNameLong << "#Lambda^{0} invariant mass, p_{T} bin minimum = "
		   << lamMass_pt_min;
	lamMass_pt.push_back( fs->make<TH1F>(ptNameShort.str().c_str(),
					    ptNameLong.str().c_str(),
					    lamMassNbins, lamMassXmin, lamMassXmax) );
	lamMass_pt_names_short.push_back( ptNameShort.str() );
	lamMass_pt_names_long.push_back( ptNameLong.str() );
	lamMass_pt_minima.push_back( lamMass_pt_min );
	//cout << "Minima size is now " << lamMas
	if( lamMass_pt_min < 0.25
	    && (lamMass_pt_min + lamMass_pt_binWidth1) <= 0.25)  {
	  lamMass_pt_min += lamMass_pt_binWidth1;
	}
	else if( lamMass_pt_min < 0.25
		 && (lamMass_pt_min + lamMass_pt_binWidth1) > 0.25 ) {
	  lamMass_pt_min += lamMass_pt_binWidth2;
	}
	else if( lamMass_pt_min < 0.5
		 && (lamMass_pt_min + lamMass_pt_binWidth2) <= 0.5 ) {
	  lamMass_pt_min += lamMass_pt_binWidth2;
	}
	else if( lamMass_pt_min < 0.5
		 && (lamMass_pt_min + lamMass_pt_binWidth2) > 0.5 ) {
	  lamMass_pt_min += lamMass_pt_binWidth3;
	}
	else if( lamMass_pt_min < 1.
		 && (lamMass_pt_min + lamMass_pt_binWidth3) <= 1. ) {
	  lamMass_pt_min += lamMass_pt_binWidth3;
	}
	else if( lamMass_pt_min < 1.
		 && (lamMass_pt_min + lamMass_pt_binWidth3) > 1. ) {
	  lamMass_pt_min += lamMass_pt_binWidth4;
	}
	else if( lamMass_pt_min < 1.5
		 && (lamMass_pt_min + lamMass_pt_binWidth4) <= 1.5 ) {
	  lamMass_pt_min += lamMass_pt_binWidth4;
	}
	else if( lamMass_pt_min < 1.5
		 && (lamMass_pt_min + lamMass_pt_binWidth4) > 1.5 ) {
	  lamMass_pt_min += lamMass_pt_binWidth5;
	}
	else if( lamMass_pt_min < 2.
		 && (lamMass_pt_min + lamMass_pt_binWidth5) <= 2. ) {
	  lamMass_pt_min += lamMass_pt_binWidth5;
	}
	else if( lamMass_pt_min < 2.
		 && (lamMass_pt_min + lamMass_pt_binWidth5) > 2. ) {
	  lamMass_pt_min += lamMass_pt_binWidth6;
	}
	else if( lamMass_pt_min < 3.
		 && (lamMass_pt_min + lamMass_pt_binWidth6) <= 3. ) {
	  lamMass_pt_min += lamMass_pt_binWidth6;
	}
	else if( lamMass_pt_min < 3.) {
	  lamMass_pt_min = 3.;
	}
	else {
	  lamMass_pt_min = 4.;
	}

      }

      vector<float> minimaForTH1;
      unsigned int ndx = 0;
      for( vector<double>::iterator iMIN = lamMass_pt_minima.begin();
	   iMIN != lamMass_pt_minima.end();
	   iMIN++ ) {
	minimaForTH1.push_back(*iMIN);
	if( ndx == lamMass_pt_minima.size() - 1 ) {
	  //cout << "Pushed back a 15. " << endl;
	  minimaForTH1.push_back( 6. );
	}
	ndx++;
      }
      lamMassInPtBins = fs->make<TH1F>("LamMassBiasVsPt",
				      "#Lambda^{0} mass bias vs. p_{T} of lowest-p_{T} track",
				      lamMass_pt_minima.size(), &minimaForTH1[0]);
      
    }
  }
}

void V0RecoAnalyzer::endJob() {
  using namespace std;

  if( writeHistos && instanceName == string("Kshort") ) {
    ostringstream ksoss;
    ostringstream ksoss_doubgaus;
    ksoss << ksMassBinWidth << "*gausn(0) + [3] + [4]*(x-0.49767)"
	  << " + [5]*(x-0.49767)^2";
    // p0*exp(-0.5*((x-p1)/p2)^2)
    /*ksoss_doubgaus << ksMassBinWidth 
		   << "*[0]*[3]*exp(-0.5*((x-[1])/[2])^2) + "
		   << ksMassBinWidth 
		   << "*[0]*(1 - [3])*exp(-0.5*((x-[1])/[4])^2) + "
		   << "[5] + [6]*(x-0.49767)";*/
    double ksMassBinWidth_DG = ksMassBinWidth / sqrt(2*3.141592654);
    ksoss_doubgaus << ksMassBinWidth_DG 	
		   << "*[0]*[3]*exp(-0.5*((x-[1])/[2])^2)/[2] + "
		   << ksMassBinWidth_DG 
		   << "*[0]*(1 - [3])*exp(-0.5*((x-[1])/[4])^2)/[4] + "
		   << "[5] + [6]*(x-[1]) + [7]*(x-[1])^2";

    TF1 *ksFit_doubGaus = new TF1("ksFit_doubGaus", 
				  ksoss_doubgaus.str().c_str(),
				  ksMassXmin, ksMassXmax);
    ksFit_doubGaus->SetParName( 0, "yield" );
    ksFit_doubGaus->SetParName( 1, "mean" );
    ksFit_doubGaus->SetParName( 2, "sigma1" );
    ksFit_doubGaus->SetParName( 3, "fraction" );
    ksFit_doubGaus->SetParLimits( 3, 0., 1. );
    ksFit_doubGaus->SetParName( 4, "sigma2" );
    ksFit_doubGaus->SetParName( 5, "const" );
    ksFit_doubGaus->SetParName( 6, "slope" );
    ksFit_doubGaus->SetParName( 7, "quadconst" );

    ksFit_doubGaus->SetParameter( 0, 4.4444*ksCandMass->GetMaximum() );
    ksFit_doubGaus->SetParameter( 1, 0.49767 );
    ksFit_doubGaus->SetParameter( 2, 0.0045 );
    ksFit_doubGaus->SetParameter( 3, 0.75 );
    ksFit_doubGaus->SetParameter( 4, 0.011 );
    ksFit_doubGaus->SetParameter( 5, 0.1*ksCandMass->GetMaximum() );
    ksFit_doubGaus->SetParameter( 6, 1. );
    ksFit_doubGaus->SetParameter( 7, -1. );

    TF1 *ksFit = new TF1("ksFit", ksoss.str().c_str(), ksMassXmin, ksMassXmax);
    ksFit->SetParName( 0, "yield" );
    ksFit->SetParName( 1, "mean" );
    ksFit->SetParName( 2, "sigma" );
    ksFit->SetParName( 3, "const" );
    ksFit->SetParName( 4, "slope" );
    ksFit->SetParName( 5, "quadconst" );

    ksFit->SetParameter( 0, 4.4444*ksCandMass->GetMaximum() );
    ksFit->SetParameter( 1, 0.49767 );
    ksFit->SetParameter( 2, 0.005 );
    ksFit->SetParLimits( 2, 0., 0.010 );
    ksFit->SetParameter( 3, 0.1*ksCandMass->GetMaximum() );
    ksFit->SetParameter( 4, 1. );
    ksFit->SetParameter( 5, -1. );

    /*
    TF1 *ksFit_doubGaus = new TF1("ksFitDG", ksoss_doubgaus.str().c_str(),
				  ksMassXmin, ksMassXmax);
    ksFit_doubGaus->SetParName( 0, "yield" );
    ksFit_doubGaus->SetParName( 1, "mean" );
    ksFit_doubGaus->SetParName( 2, "sigma1" );
    ksFit_doubGaus->SetParName( 3, "fraction" );
    ksFit_doubGaus->SetParName( 4, "sigma2" );
    ksFit_doubGaus->SetParName( 5, "const" );
    ksFit_doubGaus->SetParName( 6, "slope" );

    ksFit_doubGaus->SetParameter( 0, 4.4444*ksCandMass->GetMaximum() );
    ksFit_doubGaus->SetParameter( 1, 0.49767 );
    ksFit_doubGaus->SetParameter( 2, 0.005 );
    ksFit_doubGaus->SetParameter( 3, 0.9 );
    ksFit_doubGaus->SetParameter( 4, 0.007 );
    ksFit_doubGaus->SetParameter( 5, 0.1*ksCandMass->GetMaximum() );
    ksFit_doubGaus->SetParameter( 6, 0. );
    */

    ksR->Add( ksRSignal, ksRBg, 1., -0.5 );
    ksZ->Add( ksZSignal, ksZBg, 1., -0.5 );
    ksZvsRBgSubt->Add( ksZvsRFull, ksZvsRBg, 1., -0.5);
    ksEta->Add( ksEtaSignal, ksEtaBg, 1., -0.5 );
    ksPhi->Add( ksPhiSignal, ksPhiBg, 1., -0.5 );
    ksPt->Add( ksPtSignal, ksPtBg, 1., -0.5 );

    ksCandMass->Fit("ksFit_doubGaus", "RLE");

    // Now do fits for mass bias plots
    int ksEtaCount = 0;
    for( vector<TH1F*>::iterator iETA = ksMass_eta.begin();
	 iETA != ksMass_eta.end();
	 iETA++ ) {
      //cout << "---> Fitting " << ksMass_eta_names_short[ksEtaCount] << endl;
      ksFit->SetParameter( 0, 4.4444*(*iETA)->GetMaximum() );
      ksFit->SetParameter( 1, 0.49767 );
      ksFit->SetParameter( 2, 0.005 );
      ksFit->SetParameter( 3, 0.1*(*iETA)->GetMaximum() );
      ksFit->SetParameter( 4, 1. );
      ksFit->SetParameter( 5, -1. );

      int fitStatus = (*iETA)->Fit("ksFit", "RLE");
      if( !fitStatus ) {
	ksMassInEtaBins->SetBinContent( ksEtaCount + 1, ksFit->GetParameter(1) );
	ksMassInEtaBins->SetBinError( ksEtaCount + 1, ksFit->GetParError(1) );
      }
      else {
	ksMassInEtaBins->SetBinContent( ksEtaCount + 1, ksMassConst );
	ksMassInEtaBins->SetBinError( ksEtaCount + 1, 0. );
      }
      ksEtaCount++;
    }

    //cout << "Doing Ks phi, count = " << ksMass_phi.size() << endl;
    int ksPhiCount = 0;
    for( vector<TH1F*>::iterator iPHI = ksMass_phi.begin();
	 iPHI != ksMass_phi.end();
	 iPHI++ ) {
      cout << "---> Fitting " << ksMass_phi_names_short[ksPhiCount] << endl;
      ksFit->SetParameter( 0, 4.4444*(*iPHI)->GetMaximum() );
      ksFit->SetParameter( 1, 0.49767 );
      ksFit->SetParameter( 2, 0.005 );
      ksFit->SetParameter( 3, 0.1*(*iPHI)->GetMaximum() );
      ksFit->SetParameter( 4, 1. );
      ksFit->SetParameter( 5, -1. );

      int fitStatus = (*iPHI)->Fit("ksFit", "RLE");
      if( !fitStatus ) {
	ksMassInPhiBins->SetBinContent( ksPhiCount + 1, ksFit->GetParameter(1) );
	ksMassInPhiBins->SetBinError( ksPhiCount + 1, ksFit->GetParError(1) );
      }
      else {
	ksMassInPhiBins->SetBinContent( ksPhiCount + 1, ksMassConst );
	ksMassInPhiBins->SetBinError( ksPhiCount + 1, 0. );
      }
      ksPhiCount++;
    }

    ksEtaCount = ksPhiCount = 0;
    //    int numEta = ksMass_eta_nBins * 2;
    int numPhi = ksMass_phi_nBins / 2;
    for( vector<TH1F*>::iterator iEP = ksMass_eta_phi.begin();
	 iEP != ksMass_eta_phi.end();
	 iEP++ ) {
      ksFit->SetParameter( 0, 4.4444*(*iEP)->GetMaximum() );
      ksFit->SetParameter( 1, 0.49767 );
      ksFit->SetParameter( 2, 0.005 );
      ksFit->SetParameter( 3, 0.1*(*iEP)->GetMaximum() );
      ksFit->SetParameter( 4, 1. );
      ksFit->SetParameter( 5, -1. );

      int fitStatus = (*iEP)->Fit("ksFit", "RLE");
      if( !fitStatus ) {
	ksMassBiasEtaVsPhi->SetBinContent( ksPhiCount + 1, 
					   ksEtaCount + 1, ksFit->GetParameter(1) );
	ksMassBiasEtaVsPhi->SetBinError( ksPhiCount + 1,
					 ksEtaCount + 1, ksFit->GetParError(1) );
      }
      else {
	ksMassBiasEtaVsPhi->SetBinContent( ksPhiCount + 1,
					ksEtaCount + 1, 0.497648 );
	ksMassBiasEtaVsPhi->SetBinError( ksPhiCount + 1,
					 ksEtaCount + 1, 0. );
      }
      ksPhiCount++;
      if( ksPhiCount == numPhi ) {
	ksEtaCount++;
	ksPhiCount = 0;
      }
    }


    int ksPtCount = 0;
    for( vector<TH1F*>::iterator iPT = ksMass_pt.begin();
	 iPT != ksMass_pt.end();
	 iPT++ ) {
      //cout << "---> Fitting " << ksMass_pt_names_short[ksPtCount] << endl;
      ksFit->SetParameter( 0, 4.4444*(*iPT)->GetMaximum() );
      ksFit->SetParameter( 1, 0.49767 );
      ksFit->SetParameter( 2, 0.005 );
      ksFit->SetParameter( 3, 0.1*(*iPT)->GetMaximum() );
      ksFit->SetParameter( 4, 1. );
      ksFit->SetParameter( 5, -1. );

      int fitStatus = (*iPT)->Fit("ksFit", "RLE");
      if( !fitStatus ) {
	ksMassInPtBins->SetBinContent( ksPtCount + 1, ksFit->GetParameter(1) );
	ksMassInPtBins->SetBinError( ksPtCount + 1, ksFit->GetParError(1) );
      }
      else {
	ksMassInPtBins->SetBinContent( ksPtCount + 1, ksMassConst );
	ksMassInPtBins->SetBinError( ksPtCount + 1, 0. );
      }
      ksPtCount++;
    }
  }

  if( writeHistos && instanceName == string("Lambda") ) {
    ostringstream lamoss;
    lamoss << lamMassBinWidth << "*gausn(0) + [3]*(x - "
	   << piMass + protonMass << ")^(1/2) + [4]*(x - "
	   << piMass + protonMass << ")^(3/2)";
    ostringstream lamfitoss_doubGaus;
    double lamMassBinWidth_DG = lamMassBinWidth/sqrt(2*3.141592654);
    lamfitoss_doubGaus << lamMassBinWidth_DG
		       << "*[0]*[3]*exp(-0.5*((x-[1])/[2])^2)/[2] + "
		       << lamMassBinWidth_DG
		       << "*[0]*(1-[3])*exp(-0.5*((x-[1])/[4])^2)/[4] + "
		       << "[5]*(x - " << piMass + protonMass << ")^(1/2) + [6]*(x-"
		       << piMass + protonMass << ")^(3/2)";
    TF1 *lamFit_doubGaus = new TF1("lamFit_doubGaus", lamfitoss_doubGaus.str().c_str(),
				   piMass+protonMass, lamMassXmax);
    lamFit_doubGaus->SetParName( 0, "yield" );
    lamFit_doubGaus->SetParName( 1, "mean" );
    lamFit_doubGaus->SetParName( 2, "sigma1" );
    lamFit_doubGaus->SetParName( 3, "fraction" );
    lamFit_doubGaus->SetParLimits( 3, 0., 1. );
    lamFit_doubGaus->SetParName( 4, "sigma2" );
    lamFit_doubGaus->SetParName( 5, "sqrt" );
    lamFit_doubGaus->SetParName( 6, "sqrtcube" );
    lamFit_doubGaus->SetParameter( 0, 8.*lamCandMass->GetMaximum() );
    lamFit_doubGaus->SetParameter( 1, 1.1159 );
    lamFit_doubGaus->SetParameter( 2, 0.0016 );
    lamFit_doubGaus->SetParameter( 3, 0.44 );
    lamFit_doubGaus->SetParameter( 4, 0.0037);
    lamFit_doubGaus->SetParameter( 5, 0.001*lamCandMass->GetMaximum()/lamMassBinWidth );
    lamFit_doubGaus->SetParameter( 6, 0.001*lamCandMass->GetMaximum()/lamMassBinWidth );

    TF1 *lamFit = new TF1("lamFit", lamoss.str().c_str(), piMass+protonMass, lamMassXmax);
    lamFit->SetParName( 0, "yield" );
    lamFit->SetParName( 1, "GausMean" );
    lamFit->SetParName( 2, "GausSigma" );
    lamFit->SetParName( 3, "c1" );
    lamFit->SetParName( 4, "c2" );

    lamFit->SetParameter( 0, 2.6*lamCandMass->GetMaximum() );
    lamFit->SetParameter( 1, 1.1156 );
    lamFit->SetParameter( 2, 0.002 );
    lamFit->SetParameter( 3, 0.75*lamCandMass->GetMaximum() );
    lamFit->SetParameter( 4, 1.85*lamCandMass->GetMaximum() );

    lamR->Add( lamRSignal, lamRBg, 1., -0.5 );
    lamZ->Add( lamZSignal, lamZBg, 1., -0.5 );
    lamZvsRBgSubt->Add( lamZvsRFull, lamZvsRBg, 1., -0.5);
    lamEta->Add( lamEtaSignal, lamEtaBg, 1., -0.5 );
    lamPhi->Add( lamPhiSignal, lamPhiBg, 1., -0.5 );
    lamPt->Add( lamPtSignal, lamPtBg, 1., -0.5 );

    lamCandMass->Fit("lamFit_doubGaus", "RLE");

    int lamEtaCount = 0;
    for( vector<TH1F*>::iterator iETA = lamMass_eta.begin();
	 iETA != lamMass_eta.end();
	 iETA++ ) {
      //cout << "---> Fitting " << lamMass_eta_names_short[lamEtaCount] << endl;
      lamFit->SetParameter( 0, 2.6*(*iETA)->GetMaximum() );
      lamFit->SetParameter( 1, 1.1156 );
      lamFit->SetParameter( 2, 0.002 );
      lamFit->SetParameter( 3, 0.75*(*iETA)->GetMaximum() );
      lamFit->SetParameter( 4, 1.85*(*iETA)->GetMaximum() );

      int fitStatus = (*iETA)->Fit("lamFit", "RLE");
      if( !fitStatus ) {
	lamMassInEtaBins->SetBinContent( lamEtaCount + 1, lamFit->GetParameter(1) );
	lamMassInEtaBins->SetBinError( lamEtaCount + 1, lamFit->GetParError(1) );
      }
      else {
	lamMassInEtaBins->SetBinContent( lamEtaCount + 1, lamMassConst );
	lamMassInEtaBins->SetBinError( lamEtaCount + 1, 0. );
      }
      lamEtaCount++;
    }

    int lamPhiCount = 0;
    for( vector<TH1F*>::iterator iPHI = lamMass_phi.begin();
	 iPHI != lamMass_phi.end();
	 iPHI++ ) {
      //cout << "---> Fitting " << lamMass_phi_names_short[lamPhiCount] << endl;
      lamFit->SetParameter( 0, 2.6*(*iPHI)->GetMaximum() );
      lamFit->SetParameter( 1, 1.1156 );
      lamFit->SetParameter( 2, 0.002 );
      lamFit->SetParameter( 3, 0.75*(*iPHI)->GetMaximum() );
      lamFit->SetParameter( 4, 1.85*(*iPHI)->GetMaximum() );

      int fitStatus = (*iPHI)->Fit("lamFit", "RLE");
      if( !fitStatus ) {
	lamMassInPhiBins->SetBinContent( lamPhiCount + 1, lamFit->GetParameter(1) );
	lamMassInPhiBins->SetBinError( lamPhiCount + 1, lamFit->GetParError(1) );
      }
      else {
	lamMassInPhiBins->SetBinContent( lamPhiCount + 1, lamMassConst );
	lamMassInPhiBins->SetBinError( lamPhiCount + 1, 0. );
      }
      lamPhiCount++;
    }

    lamEtaCount = lamPhiCount = 0;

    int lamPtCount = 0;
    for( vector<TH1F*>::iterator iPT = lamMass_pt.begin();
	 iPT != lamMass_pt.end();
	 iPT++ ) {
      //cout << "---> Fitting " << lamMass_pt_names_short[lamPtCount] << endl;
      lamFit->SetParameter( 0, 2.6*(*iPT)->GetMaximum() );
      lamFit->SetParameter( 1, 1.1156 );
      lamFit->SetParameter( 2, 0.002 );
      lamFit->SetParameter( 3, 0.75*(*iPT)->GetMaximum() );
      lamFit->SetParameter( 4, 1.85*(*iPT)->GetMaximum() );

      int fitStatus = (*iPT)->Fit("lamFit", "RLE");
      //cout << "Fit returned " << isGoodFit << endl;
      if( !fitStatus ) {
	lamMassInPtBins->SetBinContent( lamPtCount + 1, lamFit->GetParameter(1) );
	lamMassInPtBins->SetBinError( lamPtCount + 1, lamFit->GetParError(1) );
      }
      else {
	lamMassInPtBins->SetBinContent( lamPtCount + 1, lamMassConst );
	lamMassInPtBins->SetBinError( lamPtCount + 1, 0. );
      }
      lamPtCount++;
    }
  }
}

DEFINE_FWK_MODULE(V0RecoAnalyzer);
