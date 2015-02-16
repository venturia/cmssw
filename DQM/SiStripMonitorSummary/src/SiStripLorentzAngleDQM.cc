#include "DQM/SiStripMonitorSummary/interface/SiStripLorentzAngleDQM.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "TCanvas.h"

// -----
SiStripLorentzAngleDQM::SiStripLorentzAngleDQM(const edm::EventSetup & eSetup,
					       edm::ParameterSet const& hPSet,
					       edm::ParameterSet const& fPSet):
  SiStripBaseCondObjDQM(eSetup, hPSet, fPSet),
  last_id_processed_(0)									       
{

  // Build the Histo_TkMap:
  if(HistoMaps_On_ ) Tk_HM_ = new TkHistoMap("SiStrip/Histo_Map","LA_TkMap",0.);

}
// -----



// -----
SiStripLorentzAngleDQM::~SiStripLorentzAngleDQM(){}
// -----


// -----
void SiStripLorentzAngleDQM::getActiveDetIds(const edm::EventSetup & eSetup){
  
  getConditionObject(eSetup);

  std::map<uint32_t,float>::const_iterator LAMapIter_;
  std::map<uint32_t,float> LAMap_ = lorentzangleHandle_->getLorentzAngles();

  for( LAMapIter_ = LAMap_.begin();
       LAMapIter_!= LAMap_.end(); LAMapIter_++){

    activeDetIds.push_back((*LAMapIter_).first);
  }

}

// -----
void SiStripLorentzAngleDQM::saveSummaryMEs(){
  for (std::map<uint32_t, ModMEs>::iterator iter=SummaryMEsMap_.begin(); iter!=SummaryMEsMap_.end(); iter++){

    ModMEs selME;
    selME = iter->second;

    if(SummaryOnStringLevel_On_){
      if (fPSet_.getParameter<bool>("OutputSummaryProfileAtLayerLevelAsImage")){
	savePNG(selME.SummaryOfProfileDistr);
      }
      if (fPSet_.getParameter<bool>("OutputCumulativeSummaryAtLayerLevelAsImage")){
	savePNG(selME.SummaryOfCumulDistr);
      }
    }
    else{
      if(hPSet_.getParameter<bool>("FillSummaryProfileAtLayerLevel") && fPSet_.getParameter<bool>("OutputSummaryProfileAtLayerLevelAsImage")){
	savePNG(selME.SummaryOfProfileDistr);
      }
      if(hPSet_.getParameter<bool>("FillCumulativeSummaryAtLayerLevel") && fPSet_.getParameter<bool>("OutputCumulativeSummaryAtLayerLevelAsImage")){
	savePNG(selME.SummaryOfCumulDistr);
      }
    }
  }
}
// -----



// -----
void SiStripLorentzAngleDQM::fillMEsForLayer( /*std::map<uint32_t, ModMEs> selMEsMap_,*/ uint32_t selDetId_, const TrackerTopology* tTopo){
  int subDetId_ = ((selDetId_>>25)&0x7);
  if( subDetId_<3 ||subDetId_>6 ){ 
    edm::LogError("SiStripLorentzAngle")
      << "[SiStripLorentzAngle::fillMEsForLayer] WRONG INPUT : no such subdetector type : "
      << subDetId_ << " and detId " << selDetId_ << " therefore no filling!" 
      << std::endl;
  }    
  else if (SummaryOnLayerLevel_On_) {    
     if(getLayerNameAndId(last_id_processed_, tTopo)==getLayerNameAndId(selDetId_, tTopo)){return;}
   } 
  else if (SummaryOnStringLevel_On_) {
    if(getStringNameAndId(last_id_processed_, tTopo)==getStringNameAndId(selDetId_, tTopo)){return;}
  } 
  last_id_processed_ = selDetId_;

  SiStripHistoId hidmanager;

      
  std::string hSummaryOfProfile_description;
  hSummaryOfProfile_description  = hPSet_.getParameter<std::string>("SummaryOfProfile_description");

  std::string hSummary_name; 

  if( subDetId_<3 || subDetId_>6 ){ 
    edm::LogError("SiStripLorentzAngleDQM")
      << "[SiStripLorentzAngleDQM::fillMEsForLayer] WRONG INPUT : no such subdetector type : "
      << subDetId_ << " no folder set!" 
      << std::endl;
    return;
  }

  uint32_t selSubDetId_ =  ((selDetId_>>25)&0x7);
  SiStripSubStructure substructure_;
  
  std::vector<uint32_t> sameLayerDetIds_;
  sameLayerDetIds_.clear();

  if (SummaryOnStringLevel_On_) {  //FILLING FOR STRING LEVEL

    hSummary_name = hidmanager.createHistoLayer(hSummaryOfProfile_description, "layer", getStringNameAndId(selDetId_,tTopo).first, "") ;
    std::map<uint32_t, ModMEs>::iterator selMEsMapIter_ = SummaryMEsMap_.find(getStringNameAndId(selDetId_,tTopo).second);
    
    ModMEs selME_;
    if ( selMEsMapIter_ != SummaryMEsMap_.end())
      selME_ =selMEsMapIter_->second;

    getSummaryMEs(selME_,selDetId_,tTopo);
  
    // -----   					   
    sameLayerDetIds_.clear();
   
    if(selSubDetId_==3){  //  TIB
      if(tTopo->tibIsInternalString(selDetId_)){
	substructure_.getTIBDetectors(activeDetIds, sameLayerDetIds_, tTopo->tibLayer(selDetId_),0,1,tTopo->tibString(selDetId_));
      }
      if(tTopo->tibIsExternalString(selDetId_)){
	substructure_.getTIBDetectors(activeDetIds, sameLayerDetIds_, tTopo->tibLayer(selDetId_),0,2,tTopo->tibString(selDetId_));
      } 
    }
    else if(selSubDetId_==4){  // TID
      substructure_.getTIDDetectors(activeDetIds, sameLayerDetIds_, 0,0,0,0);
    }
    else if(selSubDetId_==5){  // TOB
      substructure_.getTOBDetectors(activeDetIds, sameLayerDetIds_, tTopo->tobLayer(selDetId_),0,tTopo->tobRod(selDetId_));
    }
    else if(selSubDetId_==6){  // TEC
      substructure_.getTECDetectors(activeDetIds, sameLayerDetIds_, 0,0,0,0,0,0);
    }
 
    // -----

    for(unsigned int i=0;i< sameLayerDetIds_.size(); i++){
	selME_.SummaryOfProfileDistr->Fill(i+1,lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));

	// Fill the Histo_TkMap+TkMap with the LA:
        if(HistoMaps_On_ ) Tk_HM_->fill(sameLayerDetIds_[i], lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));

	  std::cout<<sameLayerDetIds_[i]<<"\t"<<lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i])<<std::endl;

	if(fPSet_.getParameter<bool>("TkMap_On") || hPSet_.getParameter<bool>("TkMap_On")){
	  fillTkMap(sameLayerDetIds_[i], lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));
	}
	
    } 
    
    std::string hSummaryOfCumul_description;
    hSummaryOfCumul_description  = hPSet_.getParameter<std::string>("SummaryOfCumul_description");
    
    std::string hSummaryOfCumul_name; 
    
    if( subDetId_<3 || subDetId_>6 ){ 
      edm::LogError("SiStripLorentzAngleDQM")
	<< "[SiStripLorentzAngleDQM::fillMEsForLayer] WRONG INPUT : no such subdetector type : "
	<< subDetId_ << " no folder set!" 
	<< std::endl;
      return;
    }
    
    hSummaryOfCumul_name = hidmanager.createHistoLayer(hSummaryOfCumul_description, "layer", getStringNameAndId(selDetId_,tTopo).first, "") ;
    
    for(unsigned int i=0;i< sameLayerDetIds_.size(); i++){
	selME_.SummaryOfCumulDistr->Fill(lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));
    } 
  } //FILLING FOR STRING LEVEL
  
  
  else { //FILLING FOR LAYER LEVEL

    std::map<uint32_t, ModMEs>::iterator selMEsMapIter_ = SummaryMEsMap_.find(getLayerNameAndId(selDetId_,tTopo).second);
    
    ModMEs selME_;
    if ( selMEsMapIter_ != SummaryMEsMap_.end())
      selME_ =selMEsMapIter_->second;
    
    getSummaryMEs(selME_,selDetId_,tTopo);
    
    if(hPSet_.getParameter<bool>("FillSummaryProfileAtLayerLevel")){

      hSummary_name = hidmanager.createHistoLayer(hSummaryOfProfile_description, "layer", getLayerNameAndId(selDetId_,tTopo).first, "") ;    
    
      // -----   					   
      sameLayerDetIds_.clear();

      sameLayerDetIds_=GetSameLayerDetId(activeDetIds,selDetId_,tTopo);     

      for(unsigned int i=0;i< sameLayerDetIds_.size(); i++){
	  selME_.SummaryOfProfileDistr->Fill(i+1,lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));

	  // Fill the Histo_TkMap with LA:
	  if(HistoMaps_On_ ) Tk_HM_->fill(sameLayerDetIds_[i], lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));

	if(fPSet_.getParameter<bool>("TkMap_On") || hPSet_.getParameter<bool>("TkMap_On")){
	  fillTkMap(sameLayerDetIds_[i], lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));

	}

      } 
    }//if Fill ...

    if(hPSet_.getParameter<bool>("FillCumulativeSummaryAtLayerLevel")){

      std::string hSummaryOfCumul_description;
      hSummaryOfCumul_description  = hPSet_.getParameter<std::string>("SummaryOfCumul_description");
    
      std::string hSummaryOfCumul_name; 
    
      if( subDetId_<3 || subDetId_>6 ){ 
	edm::LogError("SiStripLorentzAngleDQM")
	  << "[SiStripLorentzAngleDQM::fillMEsForLayer] WRONG INPUT : no such subdetector type : "
	  << subDetId_ << " no folder set!" 
	  << std::endl;
	return;
      }
    
      hSummaryOfCumul_name = hidmanager.createHistoLayer(hSummaryOfCumul_description, "layer", getLayerNameAndId(selDetId_,tTopo).first, "") ;
    
      for(unsigned int i=0;i< sameLayerDetIds_.size(); i++){
	  selME_.SummaryOfCumulDistr->Fill(lorentzangleHandle_->getLorentzAngle(sameLayerDetIds_[i]));
      }
    }//if Fill ... 
  } //FILLING FOR LAYER LEVEL
  
}  
// -----
 
