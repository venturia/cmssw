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

  TH1F* m_htibtidratio;
  TH1F* m_htobtecratio;
  TH1F* m_hpxllessratio;
  
  TH2F* m_htibtidvstobtecratio;
  TH2F* m_htibtidvspxllessratio;
  TH2F* m_htobtecvspxllessratio;

  TProfile* m_htibtidratiovsz;
  TProfile* m_htobtecratiovsz;
  TProfile* m_hpxllessratiovsz;

  TH2F* m_htibtidratiovsz2D;
  TH2F* m_htobtecratiovsz2D;
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

  m_htibtidratio = tfserv->make<TH1F>("htibtidratio","atan(tibtid/(withpixel))",100,0.,3.1416/2.);
  m_htibtidratio->GetXaxis()->SetTitle("atan(ratio)");   m_htibtidratio->GetYaxis()->SetTitle("Events"); 
  m_htobtecratio = tfserv->make<TH1F>("htobtecratio","atan(tobtec/(withpixel))",100,0.,3.1416/2.);
  m_htobtecratio->GetXaxis()->SetTitle("atan(ratio)");   m_htobtecratio->GetYaxis()->SetTitle("Events"); 
  m_hpxllessratio = tfserv->make<TH1F>("hpxllessratio","atan(pxlless/(withpixel))",100,0.,3.1416/2.);
  m_hpxllessratio->GetXaxis()->SetTitle("atan(ratio)");   m_hpxllessratio->GetYaxis()->SetTitle("Events"); 

  m_htibtidvstobtecratio = tfserv->make<TH2F>("htibtidvstobtecratio","atan(tibtid/(withpixel)) vs atan(tobtec/(withpixel)) ",100,0.,3.1416/2.,100,0.,3.1416/2.);
  m_htibtidvstobtecratio->GetXaxis()->SetTitle("tobtec");   m_htibtidvstobtecratio->GetYaxis()->SetTitle("tibtid"); 

  m_htibtidvspxllessratio = 
    tfserv->make<TH2F>("htibtidvspxllessratio","atan(tibtid/(withpixel)) vs atan(pxlless/(withpixel)) ",100,0.,3.1416/2.,100,0.,3.1416/2.);
  m_htibtidvspxllessratio->GetXaxis()->SetTitle("pxlless");   m_htibtidvspxllessratio->GetYaxis()->SetTitle("tibtid"); 

  m_htobtecvspxllessratio = 
    tfserv->make<TH2F>("htobtecvspxllessratio","atan(tobtec/(withpixel)) vs atan(pxlless/(withpixel)) ",100,0.,3.1416/2.,100,0.,3.1416/2.);
  m_htobtecvspxllessratio->GetXaxis()->SetTitle("pxlless");   m_htobtecvspxllessratio->GetYaxis()->SetTitle("tobtec"); 

  m_htibtidratiovsz = tfserv->make<TProfile>("htibtidratiovsz","atan(tibtid/(withpixel)) vs main vertex z",100,-30.,30.);
  m_htibtidratiovsz->GetXaxis()->SetTitle("z [cm]");   m_htibtidratiovsz->GetYaxis()->SetTitle("tibtid"); 

  m_htobtecratiovsz = tfserv->make<TProfile>("htobtecratiovsz","atan(tobtec/(withpixel)) vs main vertex z",100,-30.,30.);
  m_htobtecratiovsz->GetXaxis()->SetTitle("z [cm]");   m_htobtecratiovsz->GetYaxis()->SetTitle("tobtec"); 

  m_hpxllessratiovsz = tfserv->make<TProfile>("hpxllessratiovsz","atan(pxlless/(withpixel)) vs main vertex z",100,-30.,30.);
  m_hpxllessratiovsz->GetXaxis()->SetTitle("z [cm]");   m_hpxllessratiovsz->GetYaxis()->SetTitle("pxlless"); 
  
  m_htibtidratiovsz2D = tfserv->make<TH2F>("htibtidratiovsz2D","atan(tibtid/(withpixel)) vs main vertex z",60,-30.,30.,25,0.,3.1416/2.);
  m_htibtidratiovsz2D->GetXaxis()->SetTitle("z [cm]");   m_htibtidratiovsz2D->GetYaxis()->SetTitle("tibtid"); 

  m_htobtecratiovsz2D = tfserv->make<TH2F>("htobtecratiovsz2D","atan(tobtec/(withpixel)) vs main vertex z",60,-30.,30.,25,0.,3.1416/2.);
  m_htobtecratiovsz2D->GetXaxis()->SetTitle("z [cm]");   m_htobtecratiovsz2D->GetYaxis()->SetTitle("tobtec"); 

  m_hpxllessratiovsz2D = tfserv->make<TH2F>("hpxllessratiovsz2D","atan(pxlless/(withpixel)) vs main vertex z",60,-30.,30.,25,0.,3.1416/2.);
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
  
  double ntibtid = 0;
  double ntobtec = 0;
  double nwithpixel = 0;
  double npxlless = 0;

  for(reco::TrackCollection::const_iterator trk=trks->begin();trk!=trks->end();++trk) {

    if(m_newiter) {
      if(trk->algo()==4 || trk->algo()==5 || trk->algo()==6) ++nwithpixel;
      if(trk->algo()==9) ++ntibtid;
      if(trk->algo()==10) ++ntobtec;
      if(trk->hitPattern().numberOfValidPixelHits() == 0) ++npxlless;
    }
    else {
      if(trk->algo()==4 || trk->algo()==5) ++nwithpixel;
      if(trk->algo()==8) ++ntibtid;
      if(trk->algo()==9) ++ntobtec;
      if(trk->hitPattern().numberOfValidPixelHits() == 0) ++npxlless;
    }
  }
  
  double rtibtid = atan2(ntibtid,nwithpixel);
  double rtobtec = atan2(ntobtec,nwithpixel);
  double rpxlless = atan2(npxlless,nwithpixel);

  if(m_filter) selected = rtibtid> m_cuts[0] && rtobtec > m_cuts[1] && rpxlless > m_cuts[2];

  // z coordinate of the first vertex

  Handle<reco::VertexCollection> vertices;
  iEvent.getByLabel(m_vtxCollection,vertices);

  bool goodvtx = false;
  if(vertices->size() && !((*vertices)[0].isFake()) ) {

    double vtxz = (*vertices)[0].z();

    if(abs(vtxz) < m_vtxzcut) {

      goodvtx = true;

      m_htibtidratio->Fill(rtibtid);
      m_htobtecratio->Fill(rtobtec);
      m_hpxllessratio->Fill(rpxlless);
      
      m_htibtidvstobtecratio->Fill(rtobtec,rtibtid);
      m_htibtidvspxllessratio->Fill(rpxlless,rtibtid);
      m_htobtecvspxllessratio->Fill(rpxlless,rtobtec);
      
      m_htibtidratiovsz->Fill(vtxz,rtibtid);
      m_htobtecratiovsz->Fill(vtxz,rtobtec);
      m_hpxllessratiovsz->Fill(vtxz,rpxlless);
      
      m_htibtidratiovsz2D->Fill(vtxz,rtibtid);
      m_htobtecratiovsz2D->Fill(vtxz,rtobtec);
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
