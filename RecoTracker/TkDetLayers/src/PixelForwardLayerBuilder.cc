#include "PixelForwardLayerBuilder.h"
#include "PixelForwardLayerPhase1.h"
#include "PixelBladeBuilder.h"

using namespace edm;
using namespace std;

ForwardDetLayer* PixelForwardLayerBuilder::build(const GeometricDet* aPixelForwardLayer,
                                                 const TrackerGeometry* theGeomDetGeometry) {
  vector<const GeometricDet*>  theGeometricPanels = aPixelForwardLayer->components();
  int panelsSize = theGeometricPanels.size();

  /*
  int num = 0;
  for(vector<const GeometricDet*>::const_iterator it= theGeometricPanels.begin();
      it!=theGeometricPanels.end(); it++, ++num) {
    edm::LogInfo("TkDetLayers") << "PanelsSize: " << panelsSize << " , "
                                << "PanelNum: " << num  << " , "
                                << "panel.phi(): " << (*it)->positionBounds().phi()  << " , "
                                << "panel.z():   " << (*it)->positionBounds().z()    << " , "
                                << "panel.y():   " << (*it)->positionBounds().y() << " , "
                                << "panel.x():   " << (*it)->positionBounds().x() << " , "
                                << "panel.r():   " << (*it)->positionBounds().perp() << " , "
                                << "panel.rmax():   " << (*it)->bounds()->rSpan().second << " , "
                                << "comp.size(): " << (*it)->components().size();
  }
  */

  //edm::LogInfo(TkDetLayers) << "pixelFwdLayer.panels().size(): " << panelsSize ;

  vector<const PixelBlade*> theBlades;
  PixelBladeBuilder myBladeBuilder;

  for(int i=0; i< (panelsSize/2); i++) {
    theBlades.push_back( myBladeBuilder.build( theGeometricPanels[i],
					       theGeometricPanels[i+(panelsSize/2)],
					       theGeomDetGeometry ) );
  }

  if ( aPixelForwardLayer->type()==GeometricDet::PixelEndCapPhase1 )
    return new PixelForwardLayerPhase1(theBlades);
  return new PixelForwardLayer(theBlades);
}
