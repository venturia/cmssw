// -*- C++ -*-
//
// Package:    Utilities
// Class:      PixelLessFilter
// 
/**\class PixelLessFilter PixelLessFilter.cc TrackingPFG/Utilities/PixelLessFilter.cc

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
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"

//
// class declaration
//

class PixelLessFilter : public edm::EDFilter {
   public:
      explicit PixelLessFilter(const edm::ParameterSet&);
      ~PixelLessFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------

  edm::InputTag m_trackCollection;
  edm::InputTag m_vtxCollection;
  const double m_vtxzcut;
  const bool m_filter;
  const bool m_newiter;
  const std::vector<double> m_cuts;

  TH1F* m_hiter4ratio;
  TH1F* m_hiter5ratio;
  TH1F* m_hpxllessratio;
  
  TH2F* m_hiter4vs5ratio;
  TH2F* m_hiter4vspxllessratio;
  TH2F* m_hiter5vspxllessratio;

  TProfile* m_hiter4ratiovsz;
  TProfile* m_hiter5ratiovsz;
  TProfile* m_hpxllessratiovsz;

  TH2F* m_hiter4ratiovsz2D;
  TH2F* m_hiter5ratiovsz2D;
  TH2F* m_hpxllessratiovsz2D;

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
PixelLessFilter::PixelLessFilter(const edm::ParameterSet& iConfig):
  m_trackCollection(iConfig.getParameter<edm::InputTag>("trackCollection")),
  m_vtxCollection(iConfig.getParameter<edm::InputTag>("vtxCollection")),
  m_vtxzcut(iConfig.getParameter<double>("vtxzMax")),
  m_filter(iConfig.getParameter<bool>("filter")),
  m_newiter(iConfig.getParameter<bool>("newIter")),
  m_cuts(iConfig.getParameter<std::vector<double> >("cuts"))
{
   //now do what ever initialization is needed

  edm::Service<TFileService> tfserv;

  m_hiter4ratio = tfserv->make<TH1F>("hiter4ratio","atan(iter4/(iter0+1))",100,0.,3.14159/2.);
  m_hiter4ratio->GetXaxis()->SetTitle("atan(ratio)");   m_hiter4ratio->GetYaxis()->SetTitle("Events"); 
  m_hiter5ratio = tfserv->make<TH1F>("hiter5ratio","atan(iter5/(iter0+1))",100,0.,3.14159/2.);
  m_hiter5ratio->GetXaxis()->SetTitle("atan(ratio)");   m_hiter5ratio->GetYaxis()->SetTitle("Events"); 
  m_hpxllessratio = tfserv->make<TH1F>("hpxllessratio","atan(pxlless/(iter0+1))",100,0.,3.14159/2.);
  m_hpxllessratio->GetXaxis()->SetTitle("atan(ratio)");   m_hpxllessratio->GetYaxis()->SetTitle("Events"); 

  m_hiter4vs5ratio = tfserv->make<TH2F>("hiter4vs5ratio","atan(iter4/(iter0+1)) vs atan(iter5/(iter0+1)) ",100,0.,3.14159/2.,100,0.,3.14159/2.);
  m_hiter4vs5ratio->GetXaxis()->SetTitle("iter5");   m_hiter4vs5ratio->GetYaxis()->SetTitle("iter4"); 

  m_hiter4vspxllessratio = 
    tfserv->make<TH2F>("hiter4vspxllessratio","atan(iter4/(iter0+1)) vs atan(pxlless/(iter0+1)) ",100,0.,3.14159/2.,100,0.,3.14159/2.);
  m_hiter4vspxllessratio->GetXaxis()->SetTitle("pxlless");   m_hiter4vspxllessratio->GetYaxis()->SetTitle("iter4"); 

  m_hiter5vspxllessratio = 
    tfserv->make<TH2F>("hiter5vspxllessratio","atan(iter5/(iter0+1)) vs atan(pxlless/(iter0+1)) ",100,0.,3.14159/2.,100,0.,3.14159/2.);
  m_hiter5vspxllessratio->GetXaxis()->SetTitle("pxlless");   m_hiter5vspxllessratio->GetYaxis()->SetTitle("iter5"); 

  m_hiter4ratiovsz = tfserv->make<TProfile>("hiter4ratiovsz","atan(iter4/(iter0+1)) vs main vertex z",100,-30.,30.);
  m_hiter4ratiovsz->GetXaxis()->SetTitle("z [cm]");   m_hiter4ratiovsz->GetYaxis()->SetTitle("iter4"); 

  m_hiter5ratiovsz = tfserv->make<TProfile>("hiter5ratiovsz","atan(iter5/(iter0+1)) vs main vertex z",100,-30.,30.);
  m_hiter5ratiovsz->GetXaxis()->SetTitle("z [cm]");   m_hiter5ratiovsz->GetYaxis()->SetTitle("iter5"); 

  m_hpxllessratiovsz = tfserv->make<TProfile>("hpxllessratiovsz","atan(pxlless/(iter0+1)) vs main vertex z",100,-30.,30.);
  m_hpxllessratiovsz->GetXaxis()->SetTitle("z [cm]");   m_hpxllessratiovsz->GetYaxis()->SetTitle("pxlless"); 
  
  m_hiter4ratiovsz2D = tfserv->make<TH2F>("hiter4ratiovsz2D","atan(iter4/(iter0+1)) vs main vertex z",60,-30.,30.,25,0.,3.14159/2.);
  m_hiter4ratiovsz2D->GetXaxis()->SetTitle("z [cm]");   m_hiter4ratiovsz2D->GetYaxis()->SetTitle("iter4"); 

  m_hiter5ratiovsz2D = tfserv->make<TH2F>("hiter5ratiovsz2D","atan(iter5/(iter0+1)) vs main vertex z",60,-30.,30.,25,0.,3.14159/2.);
  m_hiter5ratiovsz2D->GetXaxis()->SetTitle("z [cm]");   m_hiter5ratiovsz2D->GetYaxis()->SetTitle("iter5"); 

  m_hpxllessratiovsz2D = tfserv->make<TH2F>("hpxllessratiovsz2D","atan(pxlless/(iter0+1)) vs main vertex z",60,-30.,30.,25,0.,3.14159/2.);
  m_hpxllessratiovsz2D->GetXaxis()->SetTitle("z [cm]");   m_hpxllessratiovsz2D->GetYaxis()->SetTitle("pxlless"); 
  

}

PixelLessFilter::~PixelLessFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
PixelLessFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  bool selected = true;
  
  Handle<reco::TrackCollection> trks;
  iEvent.getByLabel(m_trackCollection,trks);
  
  double niter4 = 0;
  double niter5 = 0;
  double niter01 = 0;
  double npxlless = 0;

  for(reco::TrackCollection::const_iterator trk=trks->begin();trk!=trks->end();++trk) {

    if(m_newiter) {
      if(trk->algo()==4 || trk->algo()==5 || trk->algo()==6) ++niter01;
      if(trk->algo()==9) ++niter4;
      if(trk->algo()==10) ++niter5;
      if(trk->hitPattern().numberOfValidPixelHits() == 0) ++npxlless;
    }
    else {
      if(trk->algo()==4 || trk->algo()==5) ++niter01;
      if(trk->algo()==8) ++niter4;
      if(trk->algo()==9) ++niter5;
      if(trk->hitPattern().numberOfValidPixelHits() == 0) ++npxlless;
    }
  }
  
  double riter4 = atan2(niter4,niter01);
  double riter5 = atan2(niter5,niter01);
  double rpxlless = atan2(npxlless,niter01);

  if(m_filter) selected = riter4> m_cuts[0] && riter5 > m_cuts[1] && rpxlless > m_cuts[2];

  // z coordinate of the first vertex

  Handle<reco::VertexCollection> vertices;
  iEvent.getByLabel(m_vtxCollection,vertices);

  bool goodvtx = false;
  if(vertices->size() && !((*vertices)[0].isFake()) ) {

    double vtxz = (*vertices)[0].z();

    if(abs(vtxz) < m_vtxzcut) {

      goodvtx = true;

      m_hiter4ratio->Fill(riter4);
      m_hiter5ratio->Fill(riter5);
      m_hpxllessratio->Fill(rpxlless);
      
      m_hiter4vs5ratio->Fill(riter5,riter4);
      m_hiter4vspxllessratio->Fill(rpxlless,riter4);
      m_hiter5vspxllessratio->Fill(rpxlless,riter5);
      
      m_hiter4ratiovsz->Fill(vtxz,riter4);
      m_hiter5ratiovsz->Fill(vtxz,riter5);
      m_hpxllessratiovsz->Fill(vtxz,rpxlless);
      
      m_hiter4ratiovsz2D->Fill(vtxz,riter4);
      m_hiter5ratiovsz2D->Fill(vtxz,riter5);
      m_hpxllessratiovsz2D->Fill(vtxz,rpxlless);
      
    }
  }
  
  if(m_filter) selected = selected && goodvtx;


  return selected;
}

// ------------ method called once each job just before starting event loop  ------------
void 
PixelLessFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PixelLessFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(PixelLessFilter);
