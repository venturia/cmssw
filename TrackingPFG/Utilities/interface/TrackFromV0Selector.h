#ifndef Utilities_TrackFromV0Selector_h
#define Utilities_TrackFromV0Selector_h
/* \class TrackFromV0Selector
 *
 * \author Andrea Venturi, INFN
 *  from RecoTrackSelector
 *
 */
#include <vector>
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "FWCore/Utilities/interface/InputTag.h"

namespace edm {
  class ParameterSet;
  class Event;
  class EventSetup;
  template <class T> class Handle;
}

class TrackFromV0Selector {
 public:
  typedef reco::TrackCollection collection;
  typedef std::vector<const reco::Track *> container;
  typedef container::const_iterator const_iterator;
  
  /// Constructors
  TrackFromV0Selector();
  TrackFromV0Selector ( const edm::ParameterSet & cfg );
  const_iterator begin() const { return selected_.begin(); }
  const_iterator end() const { return selected_.end(); }
    
    
  void select( const edm::Handle<collection>& c, const edm::Event & event, const edm::EventSetup&);
  size_t size() const;
      
 protected:
      std::vector<edm::InputTag> v0collections_;
      double massmin_;
      double massmax_;
      container selected_;

};

#endif
