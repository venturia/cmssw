#include "MeasurementTrackerImpl.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/CommonDetUnit/interface/GeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/GluedGeomDet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include "DataFormats/DetId/interface/DetIdCollection.h"

#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiStripCluster/interface/SiStripClusterCollection.h"
#include "DataFormats/Common/interface/ContainerMask.h"

#include "TrackingTools/MeasurementDet/interface/MeasurementDetException.h"

#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "RecoLocalTracker/Records/interface/TrackerCPERecord.h"
#include "RecoLocalTracker/SiStripRecHitConverter/interface/SiStripRecHitMatcher.h"
#include "RecoLocalTracker/SiStripRecHitConverter/interface/StripCPE.h"  

#include "RecoTracker/TkDetLayers/interface/GeometricSearchTracker.h"
#include "RecoTracker/Record/interface/TrackerRecoGeometryRecord.h"
#include "TkStripMeasurementDet.h"
#include "TkPixelMeasurementDet.h"
#include "TkGluedMeasurementDet.h"

#include "CondFormats/SiStripObjects/interface/SiStripNoises.h"
#include "CondFormats/DataRecord/interface/SiStripNoisesRcd.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Services/interface/UpdaterService.h"

#include <iostream>
#include <typeinfo>
#include <map>
#include <algorithm>


//

using namespace std;

namespace {

  struct CmpTKD {
    bool operator()(MeasurementDet const* rh, MeasurementDet const * lh) {
      return rh->fastGeomDet().geographicalId().rawId() < lh->fastGeomDet().geographicalId().rawId();
    }
    bool operator()(MeasurementDet const & rh, MeasurementDet const &  lh) {
      return rh.fastGeomDet().geographicalId().rawId() < lh.fastGeomDet().geographicalId().rawId();
    }
  };

  template<typename TKD>
  void sortTKD( std::vector<TKD*> & det) {
    std::sort(det.begin(),det.end(),CmpTKD());
  }
  template<typename TKD>
  void sortTKD( std::vector<TKD> & det) {
    std::sort(det.begin(),det.end(),CmpTKD());
  }

}


MeasurementTrackerImpl::MeasurementTrackerImpl(const edm::ParameterSet&              conf,
				       const PixelClusterParameterEstimator* pixelCPE,
				       const StripClusterParameterEstimator* stripCPE,
				       const SiStripRecHitMatcher*  hitMatcher,
				       const TrackerGeometry*  trackerGeom,
				       const GeometricSearchTracker* geometricSearchTracker,
                                       const SiStripQuality *stripQuality,
                                       int   stripQualityFlags,
                                       int   stripQualityDebugFlags,
                                       const SiPixelQuality *pixelQuality,
                                       const SiPixelFedCabling *pixelCabling,
                                       int   pixelQualityFlags,
                                       int   pixelQualityDebugFlags,
				       bool isRegional) :
  MeasurementTracker(trackerGeom,geometricSearchTracker),
  pset_(conf),
  name_(conf.getParameter<std::string>("ComponentName")),
  theStDets(hitMatcher,stripCPE,isRegional),
  thePixelCPE(pixelCPE),
  theInactivePixelDetectorLabels(conf.getParameter<std::vector<edm::InputTag> >("inactivePixelDetectorLabels")),
  theInactiveStripDetectorLabels(conf.getParameter<std::vector<edm::InputTag> >("inactiveStripDetectorLabels"))
{
  this->initialize();
  this->initializeStripStatus(stripQuality, stripQualityFlags, stripQualityDebugFlags);
  this->initializePixelStatus(pixelQuality, pixelCabling, pixelQualityFlags, pixelQualityDebugFlags);
  //the measurement tracking is set to skip clusters, the other option is set from outside
  selfUpdateSkipClusters_=conf.exists("skipClusters");
  if (selfUpdateSkipClusters_)
    {
      edm::InputTag skip=conf.getParameter<edm::InputTag>("skipClusters");
      if (skip==edm::InputTag("")) selfUpdateSkipClusters_=false;
    }


  LogDebug("MeasurementTracker")<<"skipping clusters: "<<selfUpdateSkipClusters_;
}

MeasurementTrackerImpl::~MeasurementTrackerImpl()
{
  for(vector<TkPixelMeasurementDet*>::const_iterator it=thePixelDets.begin(); it!=thePixelDets.end(); ++it){
    delete *it;
  }
  
}


void MeasurementTrackerImpl::initialize()
{  
  if(theTrackerGeom->detsPXB().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsPXB().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsPXB()); else addStripDets( theTrackerGeom->detsPXB());} else addPixelDets( theTrackerGeom->detsPXB());
  if(theTrackerGeom->detsPXF().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsPXF().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsPXF()); else addStripDets( theTrackerGeom->detsPXF());} else addPixelDets( theTrackerGeom->detsPXF());
  if(theTrackerGeom->detsTIB().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsTIB().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsTIB()); else addStripDets( theTrackerGeom->detsTIB());} else addStripDets( theTrackerGeom->detsTIB());
  if(theTrackerGeom->detsTID().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsTID().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsTID()); else addStripDets( theTrackerGeom->detsTID());} else addStripDets( theTrackerGeom->detsTID());
  if(theTrackerGeom->detsTOB().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsTOB().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsTOB()); else addStripDets( theTrackerGeom->detsTOB());} else addStripDets( theTrackerGeom->detsTOB());
  if(theTrackerGeom->detsTEC().size()!=0) 
    {if(GeomDetEnumerators::isTrackerPixel(theTrackerGeom->geomDetSubDetector(theTrackerGeom->detsTEC().front()->geographicalId().subdetId()))) 
      addPixelDets( theTrackerGeom->detsTEC()); else addStripDets( theTrackerGeom->detsTEC());} else addStripDets( theTrackerGeom->detsTEC());

  // fist all stripdets
  sortTKD(theStripDets);
  theStDets.init(theStripDets);
  for (unsigned int i=0; i!=theStripDets.size(); ++i)
    theDetMap[theStDets.id(i)] = &theStripDets[i];
  
  // now the glued dets
  sortTKD(theGluedDets);
  for (unsigned int i=0; i!=theGluedDets.size(); ++i)
    initGluedDet(theGluedDets[i]);

  sortTKD(thePixelDets);


}


void MeasurementTrackerImpl::addPixelDets( const TrackingGeometry::DetContainer& dets)
{
  for (TrackerGeometry::DetContainer::const_iterator gd=dets.begin();
       gd != dets.end(); gd++) {
    addPixelDet(*gd, thePixelCPE);
  }  
}

void MeasurementTrackerImpl::addStripDets( const TrackingGeometry::DetContainer& dets)
{
  for (TrackerGeometry::DetContainer::const_iterator gd=dets.begin();
       gd != dets.end(); gd++) {

    const GeomDetUnit* gdu = dynamic_cast<const GeomDetUnit*>(*gd);

    //    StripSubdetector stripId( (**gd).geographicalId());
    //     bool isDetUnit( gdu != 0);
    //     cout << "StripSubdetector glued? " << stripId.glued() 
    // 	 << " is DetUnit? " << isDetUnit << endl;

    if (gdu != 0) {
      addStripDet(*gd);
    }
    else {
      const GluedGeomDet* gluedDet = dynamic_cast<const GluedGeomDet*>(*gd);
      if (gluedDet == 0) {
	throw MeasurementDetException("MeasurementTracker ERROR: GeomDet neither DetUnit nor GluedDet");
      }
      addGluedDet(gluedDet);
    }  
  }
}

void MeasurementTrackerImpl::addStripDet( const GeomDet* gd)
{
  try {
    theStripDets.push_back(TkStripMeasurementDet( gd, theStDets));
  }
  catch(MeasurementDetException& err){
    edm::LogError("MeasurementDet") << "Oops, got a MeasurementDetException: " << err.what() ;
  }
}

void MeasurementTrackerImpl::addPixelDet( const GeomDet* gd,
				      const PixelClusterParameterEstimator* cpe)
{
  TkPixelMeasurementDet* det = new TkPixelMeasurementDet( gd, cpe);
  thePixelDets.push_back(det);
  det->setClusterToSkip(&thePixelsToSkip);
  theDetMap[gd->geographicalId()] = det;
}

void MeasurementTrackerImpl::addGluedDet( const GluedGeomDet* gd)
{
  theGluedDets.push_back(TkGluedMeasurementDet( gd, theStDets.matcher(), theStDets.stripCPE()));
}

void MeasurementTrackerImpl::initGluedDet( TkGluedMeasurementDet & det)
{
  const GluedGeomDet& gd = det.specificGeomDet();
  const MeasurementDet* monoDet = findDet( gd.monoDet()->geographicalId());
  const MeasurementDet* stereoDet = findDet( gd.stereoDet()->geographicalId());
  if (monoDet == 0 || stereoDet == 0) {
    edm::LogError("MeasurementDet") << "MeasurementTracker ERROR: GluedDet components not found as MeasurementDets ";
    throw MeasurementDetException("MeasurementTracker ERROR: GluedDet components not found as MeasurementDets");
  }
  det.init(monoDet,stereoDet);
  theDetMap[gd.geographicalId()] = &det;
}


void MeasurementTrackerImpl::update( const edm::Event& event) const
{
  updatePixels(event);
  updateStrips(event);
  
  /*
  for (std::vector<TkStripMeasurementDet>::const_iterator i=theStripDets.begin();
       i!=theStripDets.end(); i++) {
    if( (*i).isEmpty()){
      std::cout << "stripDet id, #hits: " 
		<<  (*i).geomDet().geographicalId().rawId() << " , "
		<< 0 << std::endl;
    }else{
      std::cout << "stripDet id, #hits: " 
		<<  (*i).geomDet().geographicalId().rawId() << " , "
		<< (*i).size() << " " << (*i).detSet().size() std::endl;
    }
  }
  */
}
void MeasurementTrackerImpl::setClusterToSkip(const edm::InputTag & cluster, const edm::Event& event) const
{
  //method called by user of the measurement tracker to tell what needs to be skiped from the event.
  //there it is incompatible with a configuration in which the measurement tracker already knows what to skip
  // i.e selfUpdateSkipClusters_=True

  LogDebug("MeasurementTracker")<<"setClusterToSkip";
  if (selfUpdateSkipClusters_)
    edm::LogError("MeasurementTracker")<<"this mode of operation is not supported, either the measurement tracker is set to skip clusters, or is being told to skip clusters. not both";

  edm::Handle<edm::ContainerMask<edmNew::DetSetVector<SiPixelCluster> > > pixelClusterMask;
  event.getByLabel(cluster,pixelClusterMask);


  thePixelsToSkip.resize(pixelClusterMask->size());
  pixelClusterMask->copyMaskTo(thePixelsToSkip);
    
  edm::Handle<edm::ContainerMask<edmNew::DetSetVector<SiStripCluster> > > stripClusterMask;
  event.getByLabel(cluster,stripClusterMask);

  theStDets.theStripsToSkip.resize(stripClusterMask->size());
  stripClusterMask->copyMaskTo(theStDets.theStripsToSkip);
  
}

void MeasurementTrackerImpl::unsetClusterToSkip() const {
  //method called by user of the measurement tracker to tell what needs to be skiped from the event.
  //there it is incompatible with a configuration in which the measurement tracker already knows what to skip
  // i.e selfUpdateSkipClusters_=True
  
  LogDebug("MeasurementTracker")<<"unsetClusterToSkip";
  if (selfUpdateSkipClusters_)
    edm::LogError("MeasurementTracker")<<"this mode of operation is not supported, either the measurement tracker is set to skip clusters, or is being told to skip clusters. not both";

  thePixelsToSkip.clear();
  theStDets.theStripsToSkip.clear();
}

void MeasurementTrackerImpl::updatePixels( const edm::Event& event) const
{
  // avoid to update twice from the same event
  if (!edm::Service<UpdaterService>()->checkOnce("MeasurementTrackerImpl::updatePixels::"+name_)) return;

  typedef edmNew::DetSet<SiPixelCluster> PixelDetSet;

  bool switchOffPixelsIfEmpty = (!pset_.existsAs<bool>("switchOffPixelsIfEmpty")) ||
                                (pset_.getParameter<bool>("switchOffPixelsIfEmpty"));

  std::vector<uint32_t> rawInactiveDetIds; 
  if (!theInactivePixelDetectorLabels.empty()) {
    edm::Handle<DetIdCollection> detIds;
    for (std::vector<edm::InputTag>::const_iterator itt = theInactivePixelDetectorLabels.begin(), edt = theInactivePixelDetectorLabels.end(); 
            itt != edt; ++itt) {
      if (event.getByLabel(*itt, detIds)){
        rawInactiveDetIds.insert(rawInactiveDetIds.end(), detIds->begin(), detIds->end());
      }else{
        static bool iFailedAlready=false;
        if (!iFailedAlready){
          edm::LogError("MissingProduct")<<"I fail to get the list of inactive pixel modules, because of 4.2/4.4 event content change.";
          iFailedAlready=true;
        }
      }
    }
    if (!rawInactiveDetIds.empty()) std::sort(rawInactiveDetIds.begin(), rawInactiveDetIds.end());
  }
  // Pixel Clusters
  std::string pixelClusterProducer = pset_.getParameter<std::string>("pixelClusterProducer");
  if( pixelClusterProducer.empty() ) { //clusters have not been produced
    for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
    i!=thePixelDets.end(); i++) {
      if (switchOffPixelsIfEmpty) {
        (**i).setActiveThisEvent(false);
      }else{
        (**i).setEmpty();
      }
    }
  }else{  

    edm::Handle<edmNew::DetSetVector<SiPixelCluster> > pixelClusters;
    event.getByLabel(pixelClusterProducer, pixelClusters);
    const  edmNew::DetSetVector<SiPixelCluster>* pixelCollection = pixelClusters.product();
   
    if (switchOffPixelsIfEmpty && pixelCollection->empty()) {
        for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
             i!=thePixelDets.end(); i++) {
              (**i).setActiveThisEvent(false);
        }
    } else { 

       //std::cout <<"updatePixels "<<pixelCollection->dataSize()<<std::endl;
       thePixelsToSkip.resize(pixelCollection->dataSize());
       std::fill(thePixelsToSkip.begin(),thePixelsToSkip.end(),false);
       
       if(selfUpdateSkipClusters_) {
          edm::Handle<edm::ContainerMask<edmNew::DetSetVector<SiPixelCluster> > > pixelClusterMask;
         //and get the collection of pixel ref to skip
         event.getByLabel(pset_.getParameter<edm::InputTag>("skipClusters"),pixelClusterMask);
         LogDebug("MeasurementTracker")<<"getting pxl refs to skip";
         if (pixelClusterMask.failedToGet())edm::LogError("MeasurementTracker")<<"not getting the pixel clusters to skip";
	 if (pixelClusterMask->refProd().id()!=pixelClusters.id()){
	   edm::LogError("ProductIdMismatch")<<"The pixel masking does not point to the proper collection of clusters: "<<pixelClusterMask->refProd().id()<<"!="<<pixelClusters.id();
	 }
	 pixelClusterMask->copyMaskTo(thePixelsToSkip);
       }
          
       for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
       i!=thePixelDets.end(); i++) {

	 // foreach det get cluster range
	 unsigned int id = (**i).geomDet().geographicalId().rawId();
	 if (!rawInactiveDetIds.empty() && std::binary_search(rawInactiveDetIds.begin(), rawInactiveDetIds.end(), id)) {
	   (**i).setActiveThisEvent(false); continue;
	 }
	 //FIXME
	 //fill the set with what needs to be skipped
	 edmNew::DetSetVector<SiPixelCluster>::const_iterator it = pixelCollection->find( id );
	 if ( it != pixelCollection->end() ){            
           // push cluster range in det
           (**i).update( *it, pixelClusters, id );
	 } else{
           (**i).setEmpty();
	 }
       }
    }
  }
}

void MeasurementTrackerImpl::getInactiveStrips(const edm::Event& event,
					       std::vector<uint32_t> & rawInactiveDetIds) const {
  if (!theInactiveStripDetectorLabels.empty()) {
    edm::Handle<DetIdCollection> detIds;
    for (std::vector<edm::InputTag>::const_iterator itt = theInactiveStripDetectorLabels.begin(), edt = theInactiveStripDetectorLabels.end(); 
	 itt != edt; ++itt) {
      event.getByLabel(*itt, detIds);
      rawInactiveDetIds.insert(rawInactiveDetIds.end(), detIds->begin(), detIds->end());
    }
    if (!rawInactiveDetIds.empty()) std::sort(rawInactiveDetIds.begin(), rawInactiveDetIds.end());
  }
}

void MeasurementTrackerImpl::updateStrips( const edm::Event& event) const
{
  // avoid to update twice from the same event
  if (!edm::Service<UpdaterService>()->checkOnce("MeasurementTrackerImpl::updateStrips::"+name_)) return;

  typedef edmNew::DetSet<SiStripCluster>   StripDetSet;

  std::vector<uint32_t> rawInactiveDetIds;
  getInactiveStrips(event,rawInactiveDetIds);

  // Strip Clusters
  std::string stripClusterProducer = pset_.getParameter<std::string>("stripClusterProducer");
  //first clear all of them
  theStDets.setEmpty();


  if( !stripClusterProducer.compare("") )  return;  //clusters have not been produced

  const int endDet = theStDets.id_.size();
 

  // mark as inactive if in rawInactiveDetIds
  int i=0;
  unsigned int idp=0;
  for ( auto id : rawInactiveDetIds) {
    if (id==idp) continue; // skip multiple id
    idp=id;
    i=theStDets.find(id,i);
    assert(i!=endDet && id == theStDets.id(i));
    theStDets.setActiveThisEvent(i,false);
  }

  //=========  actually load cluster =============
  if(!theStDets.isRegional()){
    edm::Handle<edmNew::DetSetVector<SiStripCluster> > clusterHandle;
    event.getByLabel(stripClusterProducer, clusterHandle);
    const edmNew::DetSetVector<SiStripCluster>* clusterCollection = clusterHandle.product();
    
    
    if (selfUpdateSkipClusters_){
      edm::Handle<edm::ContainerMask<edmNew::DetSetVector<SiStripCluster> > > stripClusterMask;
      //and get the collection of pixel ref to skip
      LogDebug("MeasurementTracker")<<"getting strp refs to skip";
      event.getByLabel(pset_.getParameter<edm::InputTag>("skipClusters"),stripClusterMask);
      if (stripClusterMask.failedToGet())  edm::LogError("MeasurementTracker")<<"not getting the strip clusters to skip";
      if (stripClusterMask->refProd().id()!=clusterHandle.id()){
	edm::LogError("ProductIdMismatch")<<"The strip masking does not point to the proper collection of clusters: "<<stripClusterMask->refProd().id()<<"!="<<clusterHandle.id();
      }
      stripClusterMask->copyMaskTo(theStDets.theStripsToSkip);
    }
    
    theStDets.handle_ = clusterHandle;
    int i=0;
    edmNew::DetSetVector<SiStripCluster>::const_iterator it = (*clusterCollection).begin();
    edmNew::DetSetVector<SiStripCluster>::const_iterator endColl = (*clusterCollection).end();
    // cluster and det and in order (both) and unique so let's use set intersection
    for (;it!=endColl; ++it) {
      StripDetSet detSet = *it;
      unsigned int id = detSet.id();
      while ( id != theStDets.id(i)) { // eventually change to lower_bound
	++i;
	if (endDet==i) throw "we have a problem!!!!";
      }
      
      // push cluster range in det
      if ( theStDets.isActive(i) )
	theStDets.update(i,detSet);
    }

  }else{   // regional
    
    //then set the not-empty ones only
    edm::Handle<edm::RefGetter<SiStripCluster> > refClusterHandle;
    event.getByLabel(stripClusterProducer, refClusterHandle);
    
    std::string lazyGetter = pset_.getParameter<std::string>("stripLazyGetterProducer");
    edm::Handle<edm::LazyGetter<SiStripCluster> > lazyClusterHandle;
    event.getByLabel(lazyGetter,lazyClusterHandle);
    
    if(selfUpdateSkipClusters_){
      edm::Handle<edm::ContainerMask<edmNew::DetSetVector<SiStripCluster> > > stripClusterMask;
      LogDebug("MeasurementTracker")<<"getting reg strp refs to skip";
      event.getByLabel(pset_.getParameter<edm::InputTag>("skipClusters"),stripClusterMask);
      if (stripClusterMask.failedToGet())edm::LogError("MeasurementTracker")<<"not getting the strip clusters to skip";
      if (stripClusterMask->refProd().id()!=lazyClusterHandle.id()){
	edm::LogError("ProductIdMismatch")<<"The strip masking does not point to the proper collection of clusters: "<<stripClusterMask->refProd().id()<<"!="<<lazyClusterHandle.id();
      }       
      stripClusterMask->copyMaskTo(theStDets.theStripsToSkip);
    }
    
    theStDets.regionalHandle_ =  lazyClusterHandle;
    
    uint32_t tmpId=0;
    vector<SiStripCluster>::const_iterator beginIterator;
    edm::RefGetter<SiStripCluster>::const_iterator iregion = refClusterHandle->begin();
    for(;iregion!=refClusterHandle->end();++iregion) {
      const edm::RegionIndex<SiStripCluster>& region = *iregion;
      vector<SiStripCluster>::const_iterator icluster = region.begin();
      const vector<SiStripCluster>::const_iterator endIterator = region.end();
      tmpId = icluster->geographicalId();
      beginIterator = icluster;
      
      //std::cout << "== tmpId ad inizio loop dentro region: " << tmpId << std::endl;
      
      for (;icluster!=endIterator;icluster++) {
	//std::cout << "===== cluster id,pos " 
	//  << icluster->geographicalId() << " , " << icluster->barycenter()
	//  << std::endl;
	//std::cout << "=====making ref in recHits() " << std::endl;
	if( icluster->geographicalId() != tmpId){ 
	  //std::cout << "geo!=tmpId" << std::endl;
	  
	  //cannot we avoid to update the det with detId of itself??  (sure we can!, done!)
	  theStDets.update(concreteDetUpdatable(tmpId)->index(),beginIterator,icluster);
	  
	  tmpId = icluster->geographicalId();
	  beginIterator = icluster;
	  if( icluster == (endIterator-1)){
	    theStDets.update(concreteDetUpdatable(tmpId)->index(),icluster,endIterator);
	  }   
	}else if( icluster == (endIterator-1)){	   
	  theStDets.update(concreteDetUpdatable(tmpId)->index(),beginIterator,endIterator);	 
	}
      }//end loop cluster in one ragion
    }
  }//end of block for updating with regional clusters 
}


TkStripMeasurementDet * MeasurementTrackerImpl::concreteDetUpdatable(DetId id) const {
#ifdef EDM_DEBUG //or similar
  const TkStripMeasurementDet* theConcreteDet = 
    dynamic_cast<const TkStripMeasurementDet*>(findDet(id));
  if(theConcreteDet == 0)
    throw MeasurementDetException("failed casting to TkStripMeasurementDet*");	    
#endif
  // will trigger ondemand unpacking
  return const_cast<TkStripMeasurementDet*>(static_cast<const TkStripMeasurementDet*>(idToDet(id)));
}


void MeasurementTrackerImpl::initializeStripStatus(const SiStripQuality *quality, int qualityFlags, int qualityDebugFlags) {
  edm::ParameterSet cutPset = pset_.getParameter<edm::ParameterSet>("badStripCuts");
   theStDets.initializeStripStatus(quality, qualityFlags, qualityDebugFlags, cutPset);
}

void MeasurementTrackerImpl::initializePixelStatus(const SiPixelQuality *quality, const SiPixelFedCabling *pixelCabling, int qualityFlags, int qualityDebugFlags) {
  if ((quality != 0) && (qualityFlags != 0))  {
    edm::LogInfo("MeasurementTracker") << "qualityFlags = " << qualityFlags;
    unsigned int on = 0, tot = 0, badrocs = 0; 
    for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
	 i!=thePixelDets.end(); i++) {
      uint32_t detid = ((**i).geomDet().geographicalId()).rawId();
      if (qualityFlags & BadModules) {
          bool isOn = quality->IsModuleUsable(detid);
          (*i)->setActive(isOn);
          tot++; on += (unsigned int) isOn;
          if (qualityDebugFlags & BadModules) {
	    edm::LogInfo("MeasurementTracker")<< "MeasurementTrackerImpl::initializePixelStatus : detid " << detid << " is " << (isOn ?  "on" : "off");
          }
       } else {
          (*i)->setActive(true);
       }
       if ((qualityFlags & BadROCs) && (quality->getBadRocs(detid) != 0)) {
          std::vector<LocalPoint> badROCs = quality->getBadRocPositions(detid, *theTrackerGeom, pixelCabling);
          badrocs += badROCs.size();
          (*i)->setBadRocPositions(badROCs);
       } else {
          (*i)->clearBadRocPositions();  
       }
    }
    if (qualityDebugFlags & BadModules) {
        edm::LogInfo("MeasurementTracker PixelModuleStatus") << 
            " Total modules: " << tot << ", active " << on <<", inactive " << (tot - on);
    }
    if (qualityDebugFlags & BadROCs) {
        edm::LogInfo("MeasurementTracker PixelROCStatus") << " Total of bad ROCs: " << badrocs ;
    }
  } else {
    for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
	 i!=thePixelDets.end(); i++) {
      (*i)->setActive(true);          // module ON
    }
  }
}

