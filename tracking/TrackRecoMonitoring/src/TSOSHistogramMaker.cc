#include "tracking/TrackRecoMonitoring/interface/TSOSHistogramMaker.h"
#include <iostream>
#include "TH1F.h"
#include "TH2F.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"

TSOSHistogramMaker::TSOSHistogramMaker(): m_detsels(), m_selnames(), m_seltitles(), m_histocluslenangle(), m_tsosy(), m_ttrhy(), m_tsosdy() {}

TSOSHistogramMaker::TSOSHistogramMaker(const edm::ParameterSet& iConfig): 
  m_detsels(), m_selnames(), m_seltitles(), m_histocluslenangle(), m_tsosy(), m_ttrhy(), m_tsosdy() 
{
  
  edm::Service<TFileService> tfserv;

  std::vector<edm::ParameterSet> wantedsubds(iConfig.getParameter<std::vector<edm::ParameterSet> >("wantedSubDets"));
					     
  std::cout << "selections found: " << wantedsubds.size() << std::endl;

  for(std::vector<edm::ParameterSet>::iterator ps=wantedsubds.begin();ps!=wantedsubds.end();++ps) {
    m_selnames.push_back(ps->getParameter<std::string>("name"));
    m_seltitles.push_back(ps->getParameter<std::string>("title"));
    m_detsels.push_back(DetIdSelector(ps->getParameter<std::vector<std::string> >("selection")));

    std::string name = "tsosy_" + ps->getParameter<std::string>("name");
    std::string title = "TSOS y " + ps->getParameter<std::string>("title");
    m_tsosy.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),200,-20.,20.));
    name = "tsosprojx_" + ps->getParameter<std::string>("name");
    title = "TSOS x projection " + ps->getParameter<std::string>("title");
    m_tsosprojx.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),400,-2.,2.));
    name = "tsosprojy_" + ps->getParameter<std::string>("name");
    title = "TSOS y projection " + ps->getParameter<std::string>("title");
    m_tsosprojy.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),400,-2.,2.));
    name = "ttrhy_" + ps->getParameter<std::string>("name");
    title = "TT RecHit y " + ps->getParameter<std::string>("title");
    m_ttrhy.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),200,-20.,20.));
    name = "tsosdy_" + ps->getParameter<std::string>("name");
    title = "TSOS-TTRH y " + ps->getParameter<std::string>("title");
    m_tsosdy.push_back(tfserv->make<TH1F>(name.c_str(),title.c_str(),200,-20.,20.));
    name = "cluslenangle_" + ps->getParameter<std::string>("name");
    title = "Cluster Length vs Track Angle " + ps->getParameter<std::string>("title");
    m_histocluslenangle.push_back(tfserv->make<TH2F>(name.c_str(),title.c_str(),200,-1.,1.,40,-0.5,39.5));
		       
  }
}

void TSOSHistogramMaker::fill(const TrajectoryStateOnSurface& tsos, TransientTrackingRecHit::ConstRecHitPointer hit) const {
  
  if(hit==0 || !hit->isValid()) return;
  
  for(unsigned int i=0; i<m_detsels.size() ; ++i) {
    
    if(m_detsels[i].isSelected(hit->geographicalId())) {
      
      m_tsosy[i]->Fill(tsos.localPosition().y());
      m_ttrhy[i]->Fill(hit->localPosition().y());
      m_tsosdy[i]->Fill(tsos.localPosition().y()-hit->localPosition().y());

      if(tsos.localDirection().z() != 0) {
	m_tsosprojx[i]->Fill(tsos.localDirection().x()/tsos.localDirection().z());
	m_tsosprojy[i]->Fill(tsos.localDirection().y()/tsos.localDirection().z());
      }

    }
    
  }
  
  
}



