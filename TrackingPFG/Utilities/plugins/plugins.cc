/** \class reco::TrackFromV0Selector
 *
 * \author Andrea Venturi, INFN
 *
 */
#include "FWCore/Framework/interface/MakerMacros.h"
#include "TrackingPFG/Utilities/interface/TrackFromV0Selector.h"
#include "CommonTools/UtilAlgos/interface/ObjectSelector.h"

namespace reco {
  typedef ObjectSelector<TrackFromV0Selector> TrackFromV0Selector;
  DEFINE_FWK_MODULE(TrackFromV0Selector);
}
