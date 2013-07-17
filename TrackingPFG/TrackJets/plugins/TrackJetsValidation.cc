// -*- C++ -*-
//
// Package:    TrackJetsValidation
// Class:      TrackJetsValidation
// 
/**\class TrackJetsValidation TrackJetsValidation.cc AnalysisExamples/TrackJetsValidation/src/TrackJetsValidation.cc

 Description: Analyzer to obtain basic histogram to validate the TrackJets creation

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Julien Caudron
//         Created:  Tue Jan 25 18:20:59 CET 2010
// $Id: TrackJetsValidation.cc,v 1.3 2010/10/05 13:48:05 venturia Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1D.h"
#include "TH2D.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/JetReco/interface/TrackJet.h"
#include "DataFormats/JetReco/interface/TrackJetCollection.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

//
// class declaration
//

class TrackJetsValidation : public edm::EDAnalyzer {
   public:
      explicit TrackJetsValidation(const edm::ParameterSet&);
      ~TrackJetsValidation();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
  double DeltaPhi(double v1, double v2);
  double GetDeltaR(double eta1, double eta2, double phi1, double phi2);

      // ----------member data ---------------------------
private:
  edm::InputTag trackjetsSource_;
  edm::InputTag tracksSource_;
  edm::InputTag verticesSource_;
  TH1D *h_vertices_number;
  TH1D *h_vertices_numberofjets;
  TH2D *h_vertices_numbervsnumberused;

  TH1D *h_tracks_number;
  TH1D *h_tracks_eta;
  TH1D *h_tracks_phi;
  TH1D *h_tracks_pt;
  TH1D *h_tracks_normchi2;
  TH1D *h_tracks_pterrorcut;
  TH1D *h_tracks_nvh;
  TH1D *h_tracks_nlh;
  TH1D *h_tracks_log10d0bscor;
  TH1D *h_tracks_log10d0;
  TH1D *h_tracks_log10dz;
  TH1D *h_tracks_injet;
  TH1D *h_tracks_logpt;
  TH2D *h_tracks_injetvslogpt;
  TH2D *h_tracks_log10d0vslogpt;

  TH1D *h_trackjets_number;
  TH1D *h_trackjets_eta;
  TH1D *h_trackjets_phi;
  TH1D *h_trackjets_pt;
  TH1D *h_trackjets_fhc;
  TH1D *h_trackjets_numberofusedvertices;

  TH1D *h_constituents_number;
  TH1D *h_constituents_pt;
  TH1D *h_constituents_dr;
  TH1D *h_constituents_dphi;
  TH1D *h_constituents_deta;
  TH1D *h_constituents_drweighted;
  TH1D *h_constituents_dphiweighted;
  TH1D *h_constituents_detaweighted;
  TH1D *h_constituents_normchi2;
  TH1D *h_constituents_pterrorcut;
  TH1D *h_constituents_nvh;
  TH1D *h_constituents_nlh;
  TH1D *h_constituents_ptoverjetpt;
  TH1D *h_constituents_log10d0;
  TH1D *h_constituents_log10d0bscor;
  TH1D *h_constituents_log10dz;
  TH1D *h_constituents_logpt;
  TH2D *h_constituents_log10d0vslogpt;

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
TrackJetsValidation::TrackJetsValidation(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
  trackjetsSource_   = iConfig.getParameter<edm::InputTag>("trackjetsSource");
  tracksSource_      = iConfig.getParameter<edm::InputTag>("tracksSource");
  verticesSource_    = iConfig.getParameter<edm::InputTag>("verticesSource");
}


TrackJetsValidation::~TrackJetsValidation()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

//------------------------------------------------------------------------------
double TrackJetsValidation::DeltaPhi(double v1, double v2)
{ // Computes the correctly normalized phi difference
  // v1, v2 = phi of object 1 and 2
  double diff = fabs(v2 - v1);
  double corr = 2*acos(-1.) - diff;
  if (diff < acos(-1.)){ return diff;} else { return corr;}

}

//------------------------------------------------------------------------------
double TrackJetsValidation::GetDeltaR(double eta1, double eta2, double phi1, double phi2)
{ // Computes the DeltaR of two objects from their eta and phi values
  return sqrt(((eta1-eta2)*(eta1-eta2))+(DeltaPhi(phi1, phi2)*DeltaPhi(phi1, phi2)));
} 


// ------------ method called to for each event  ------------
void
TrackJetsValidation::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   //iEvent.id().event();
   //iEvent.id().run();
   //iEvent.getLuminosityBlock().id().luminosityBlock(); 

   edm::Handle<reco::TrackJetCollection> trackjets; 
   iEvent.getByLabel(trackjetsSource_, trackjets);
   edm::Handle<reco::TrackCollection> tracks; 
   iEvent.getByLabel(tracksSource_, tracks);
   edm::Handle<reco::VertexCollection> vertices; 
   iEvent.getByLabel(verticesSource_, vertices);

   reco::BeamSpot bSpot;
   edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
   //   iEvent.getByType(recoBeamSpotHandle);
   iEvent.getByLabel("offlineBeamSpot",recoBeamSpotHandle);
   bSpot = *recoBeamSpotHandle;

   h_vertices_number->Fill(vertices->size());
   for(reco::VertexCollection::const_iterator v = vertices->begin(); v != vertices->end(); ++v){
     int noj=0;
     for(reco::TrackJetCollection::const_iterator tj = trackjets->begin(); tj != trackjets->end(); ++tj){
       //not ideal, should use Ref instead
       if (tj->primaryVertex()->position()==v->position()) noj++;
     }
     h_vertices_numberofjets->Fill(noj);
   }

   h_tracks_number->Fill(tracks->size());
   for(reco::TrackCollection::const_iterator t = tracks->begin(); t != tracks->end(); ++t){
     h_tracks_eta->Fill(t->eta());
     h_tracks_phi->Fill(t->phi());
     h_tracks_pt->Fill(t->pt());
     h_tracks_logpt->Fill(log(t->pt()));
     h_tracks_normchi2->Fill(t->chi2()/t->ndof());
     h_tracks_pterrorcut->Fill(std::max(1.,(t->chi2()/t->ndof()))*(t->ptError()/t->pt()));
     h_tracks_nvh->Fill(t->numberOfValidHits());
     h_tracks_nlh->Fill(t->numberOfLostHits());
     double trDZ0 = t->vz() - bSpot.z0();
     math::XYZPoint point(bSpot.x0()+bSpot.dxdz()*trDZ0,bSpot.y0()+bSpot.dydz()*trDZ0, bSpot.z0());
     h_tracks_log10d0bscor->Fill(log10(fabs(-1*t->dxy(point))));
     h_tracks_log10d0->Fill(log10(fabs(-1*t->dxy())));
     h_tracks_log10dz->Fill(log10(fabs(t->dz())));
     int pij=0;
     for(reco::TrackJetCollection::const_iterator tj = trackjets->begin(); tj != trackjets->end(); ++tj){
       for (unsigned int i=0;i<tj->numberOfTracks();++i){
	 //not ideal, should use Ref instead
	 if ( (tj->track(i)->momentum()==t->momentum()) && (tj->track(i)->referencePoint()==t->referencePoint()) ) pij++;
       }
     }
     h_tracks_injet->Fill(pij);
     h_tracks_injetvslogpt->Fill(pij,log(t->pt()));
     h_tracks_log10d0vslogpt->Fill(log10(fabs(-1*t->dxy())),log(t->pt()));

   }

   h_trackjets_number->Fill(trackjets->size());
   std::vector<math::XYZPoint> lov;   
   for(reco::TrackJetCollection::const_iterator tj = trackjets->begin(); tj != trackjets->end(); ++tj){
     h_trackjets_eta->Fill(tj->eta());
     h_trackjets_phi->Fill(tj->phi());
     h_trackjets_pt->Fill(tj->pt());

     bool nuv=true;
     for (unsigned int i=0;i<lov.size();++i){
       //not ideal, should use Ref instead
       if (tj->primaryVertex()->position() == lov[i]) {nuv=false;break;}
     }
     if (nuv){
       lov.push_back(tj->primaryVertex()->position());
     }

     h_constituents_number->Fill(tj->numberOfTracks());
     double hpt=0;
     for (unsigned int i=0;i<tj->numberOfTracks();++i){
       edm::Ptr<reco::Track> t = tj->track(i);
       if (hpt<t->pt())hpt=t->pt();
       h_constituents_pt->Fill(t->pt());
       h_constituents_dr->Fill(GetDeltaR(t->eta(),tj->eta(),t->phi(),tj->phi()));
       h_constituents_dphi->Fill(DeltaPhi(t->phi(),tj->phi()));
       h_constituents_deta->Fill(fabs(tj->eta()-t->eta()));
       h_constituents_drweighted->Fill(GetDeltaR(t->eta(),tj->eta(),t->phi(),tj->phi()),t->pt()/tj->pt());
       h_constituents_dphiweighted->Fill(DeltaPhi(t->phi(),tj->phi()),t->pt()/tj->pt());
       h_constituents_detaweighted->Fill(fabs(tj->eta()-t->eta()),t->pt()/tj->pt());
       h_constituents_normchi2->Fill(t->chi2()/t->ndof());
       h_constituents_pterrorcut->Fill(std::max(1.,(t->chi2()/t->ndof()))*(t->ptError()/t->pt()));
       h_constituents_nvh->Fill(t->numberOfValidHits());
       h_constituents_nlh->Fill(t->numberOfLostHits());
       h_constituents_ptoverjetpt->Fill(t->pt()/tj->pt());
       double trDZ0 = t->vz() - bSpot.z0();
       math::XYZPoint point(bSpot.x0()+bSpot.dxdz()*trDZ0,bSpot.y0()+bSpot.dydz()*trDZ0, bSpot.z0());
       h_constituents_log10d0bscor->Fill(log10(fabs(-1*t->dxy(point))));
       h_constituents_log10d0->Fill(log10(fabs(-1*t->dxy())));
       h_constituents_log10dz->Fill(log10(fabs(t->dz())));
       h_constituents_logpt->Fill(log(t->pt()));
       h_constituents_log10d0vslogpt->Fill(log10(fabs(-1*t->dxy())),log(t->pt()));
     }
     h_trackjets_fhc->Fill(hpt/tj->pt());
   }
   h_trackjets_numberofusedvertices->Fill(lov.size());
   h_vertices_numbervsnumberused->Fill(vertices->size(),lov.size());
}


// ------------ method called once each job just before starting event loop  ------------
void 
TrackJetsValidation::beginJob()
{
  edm::Service<TFileService> fs;

  h_vertices_number = fs->make<TH1D>("vertices_number","vertices_number;Number of vertices;",4,-0.5,3.5);
  h_vertices_numberofjets = fs->make<TH1D>("vertices_numberofjets","vertices_numberofjets;Number of TrackJets per vertex;",30,-0.5,29.5);
  h_vertices_numbervsnumberused = fs->make<TH2D>("vertices_numbervsnumberused","vertices_numbervsnumberused;Number of vertices;Number of vertices used by TrackJets",4,-0.5,3.5,4,-0.5,3.5);

  h_tracks_number = fs->make<TH1D>("tracks_number","tracks_number;Number of tracks;",100,-0.5,99.5);
  h_tracks_eta = fs->make<TH1D>("tracks_eta","tracks_eta;#eta (Tracks);",100,-4,4);
  h_tracks_phi = fs->make<TH1D>("tracks_phi","tracks_phi;#phi (Tracks);",100,-3.2,3.2);
  h_tracks_pt = fs->make<TH1D>("tracks_pt","tracks_pt;p_{T} (Tracks);",100,0,100);
  h_tracks_logpt = fs->make<TH1D>("tracks_logpt","tracks_logpt;log(p_{T}) (Tracks);",100,-4,6);
  h_tracks_normchi2 = fs->make<TH1D>("tracks_normchi2","tracks_normchi2;Normalized #Chi^{2} (Tracks);",100,0,8);
  h_tracks_pterrorcut = fs->make<TH1D>("tracks_pterrorcut","tracks_pterrorcut;max(Normalized #Chi^{2},1) * p_{T}Error/p_{T} (Tracks);",100,0,2);
  h_tracks_nvh = fs->make<TH1D>("tracks_nvh","tracks_nvh;Number Of Valid Hits (Tracks);",40,-0.5,39.5);
  h_tracks_nlh = fs->make<TH1D>("tracks_nlh","tracks_nlh;Number Of Lost Hits (Tracks);",5,-0.5,4.5);
  h_tracks_log10d0 = fs->make<TH1D>("tracks_log10d0","tracks_d0;log_{10}(d0) (Tracks);",100,-7,3);
  h_tracks_log10d0bscor = fs->make<TH1D>("tracks_log10d0bscor","tracks_d0bscor;log_{10}(d0)_{BeamSpot corrected} (Tracks);",100,-7,3);
  h_tracks_log10dz = fs->make<TH1D>("tracks_log10dz","tracks_dz;dz (Tracks);",100,-2,2);
  h_tracks_injet = fs->make<TH1D>("tracks_injet","tracks_injet;Number of TrackJet in which the track appears;",3,-0.5,2.5);
  h_tracks_injetvslogpt = fs->make<TH2D>("tracks_injetvslogpt","tracks_injetvslogpt;Number of TrackJet in which the track appears;log(p_{T})",3,-0.5,2.5,10,-4,6);
  h_tracks_log10d0vslogpt = fs->make<TH2D>("tracks_log10d0vslogpt","tracks_log10d0vslogpt;log_{10}(d0);log(p_{T})",20,-7,3,20,-4,6);

  h_constituents_number = fs->make<TH1D>("constituents_number","constituents_number;Number of constituents;",16,-0.5,15.5);
  h_constituents_pt = fs->make<TH1D>("constituents_pt","constituents_pt;p_{T} (Constituents);",100,0,100);
  h_constituents_logpt = fs->make<TH1D>("constituents_logpt","constituents_logpt;log(p_{T}) (Constituents);",100,-4,6);
  h_constituents_normchi2 = fs->make<TH1D>("constituents_normchi2","constituents_normchi2;Normalized #Chi^{2} (Constituents);",100,0,8);
  h_constituents_pterrorcut = fs->make<TH1D>("constituents_pterrorcut","constituents_pterrorcut;max(Normalized #Chi^{2},1) * p_{T}Error/p_{T} (Constituents);",100,0,2);
  h_constituents_nvh = fs->make<TH1D>("constituents_nvh","constituents_nvh;Number Of Valid Hits (Constituents);",40,-0.5,39.5);
  h_constituents_nlh = fs->make<TH1D>("constituents_nlh","constituents_nlh;Number Of Lost Hits (Constituents);",5,-0.5,4.5);
  h_constituents_log10d0 = fs->make<TH1D>("constituents_log10d0","constituents_log10d0;log_{10}(d0) (Constituents);",100,-7,3);
  h_constituents_log10d0bscor = fs->make<TH1D>("constituents_log10d0bscor","constituents_log10d0bscor;log_{10}(d0)_{BeamSpot corrected} (Constituents);",100,-7,3);
  h_constituents_log10dz = fs->make<TH1D>("constituents_log10dz","constituents_log10dz;log_{10}(dz) (Constituents);",100,-2,2);
  h_constituents_dr = fs->make<TH1D>("constituents_dr","constituents_dr;dr with the TrackJet axis (Constituents);",100,0,0.7);
  h_constituents_deta = fs->make<TH1D>("constituents_deta","constituents_deta;deta with the TrackJet axis (Constituents);",100,0,0.7);
  h_constituents_dphi = fs->make<TH1D>("constituents_dphi","constituents_dphi;dphi the TrackJet axis (Constituents);",100,0,0.7);
  h_constituents_drweighted = fs->make<TH1D>("constituents_drweighted","constituents_drweighted;dr with the TrackJet axis (Constituents), weighted by p_{T}(constituent)/p_{T}(TrackJets);",100,0,0.7);
  h_constituents_detaweighted = fs->make<TH1D>("constituents_detaweighted","constituents_detaweighted;deta with the TrackJet axis (Constituents), weighted by p_{T}(constituent)/p_{T}(TrackJets);",100,0,0.7);
  h_constituents_dphiweighted = fs->make<TH1D>("constituents_dphiweighted","constituents_dphiweighted;dphi the TrackJet axis (Constituents), weighted by p_{T}(constituent)/p_{T}(TrackJets);",100,0,0.7);
  h_constituents_ptoverjetpt = fs->make<TH1D>("constituents_ptoverjetpt","constituents_ptoverjetpt;p_{T} (Constituents) / p_{T} (TrackJet);",100,0,1.1);
  h_constituents_log10d0vslogpt = fs->make<TH2D>("constituents_log10d0vslogpt","constituents_log10d0vslogpt;log_{10}(d0);log(p_{T})",20,-7,3,20,-4,6);

  h_trackjets_number = fs->make<TH1D>("trackjets_number","trackjets_number;Number of trackjets;",100,-0.5,99.5);
  h_trackjets_eta = fs->make<TH1D>("trackjets_eta","trackjets_eta;#eta (Trackjets);",100,-4,4);
  h_trackjets_phi = fs->make<TH1D>("trackjets_phi","trackjets_phi;#phi (Trackjets);",100,-3.2,3.2);
  h_trackjets_pt = fs->make<TH1D>("trackjets_pt","trackjets_pt;p_{T} (Trackjets);",100,0,100);
  h_trackjets_fhc = fs->make<TH1D>("trackjets_fhc","trackjets_fhc;max(p_{T} (constituents)) / p_{T} (Trackjets);",100,0,1.1);
  h_trackjets_numberofusedvertices = fs->make<TH1D>("trackjets_numberofusedvertices","trackjets_numberofusedvertices;Number of Vertices used by Trackjets;",4,-0.5,3.5);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TrackJetsValidation::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackJetsValidation);
