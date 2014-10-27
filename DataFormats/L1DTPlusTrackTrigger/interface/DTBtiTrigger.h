/*! \class DTBtiTrigger
 *  \author Ignazio Lazzizzera
 *  \author Sara Vanini
 *  \brief used to store BTI information within DT TP seed creation
 *  \date 2009, Feb 2
 */

#ifndef L1_DTTTI_BTI_h
#define L1_DTTTI_BTI_h

#include <vector>

#include "L1Trigger/DTBti/interface/DTBtiTrigData.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"

/// Class implementation
class DTBtiTrigger : public DTBtiTrigData
{
  public:
    /// Constructors
    DTBtiTrigger();
    DTBtiTrigger( const DTBtiTrigData& bti );
    DTBtiTrigger( const DTBtiTrigData& bti,
                  Global3DPoint position,
                  Global3DVector direction );

    /// Destructor
    ~DTBtiTrigger(){}

    /// Position and direction
    void setCMSPosition( const GlobalPoint pos )   { _position = pos; }
    void setCMSDirection( const GlobalVector dir ) { _direction = dir; }
    Global3DPoint  cmsPosition()  const { return _position; }
    Global3DVector cmsDirection() const { return _direction; }
    std::string sprint() const;

  private :
    int _wheel;
    int _station;
    int _sector;
    int _superLayer;
    Global3DPoint  _position;
    Global3DVector _direction;
};

typedef std::vector< DTBtiTrigger > BtiTrigsCollection;

#endif

