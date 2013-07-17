/* \class TrackFromV0Selector
 *
 * \author Andrea Venturi, INFN
 *  from RecoTrackSelector
 *
 */
#include <vector>
#include "DataFormats/Candidate/interface/VertexCompositeCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TrackingPFG/Utilities/interface/TrackFromV0Selector.h"

TrackFromV0Selector::TrackFromV0Selector() {}
TrackFromV0Selector::TrackFromV0Selector ( const edm::ParameterSet & cfg ) :
  v0collections_(cfg.getParameter<std::vector<edm::InputTag> >("v0Collections")),
  massmin_(cfg.getParameter<double>("minMass")),
  massmax_(cfg.getParameter<double>("maxMass"))
{}
    
    
void TrackFromV0Selector::select( const edm::Handle<collection>& c, const edm::Event & event, const edm::EventSetup&) {
  selected_.clear();
  // loop on V0 collections
  for( std::vector<edm::InputTag>::const_iterator v0coll = v0collections_.begin(); v0coll != v0collections_.end(); ++v0coll) {
    edm::Handle<reco::VertexCompositeCandidateCollection> v0s;
    event.getByLabel(*v0coll,v0s);
    //loop on V0s
    for(reco::VertexCompositeCandidateCollection::const_iterator v0= v0s->begin();v0!= v0s->end(); ++v0) {
      if((v0->mass() > massmin_ && v0->mass() < massmax_) || (massmin_ > massmax_)) {
	//loop on V0 daughters
	for(unsigned int icand=0;icand<v0->numberOfDaughters();++icand) {
	  const reco::Candidate* cand = v0->daughter(icand);
	  if(cand->charge()!=0) {
	    const reco::RecoChargedCandidate* chcand = dynamic_cast<const reco::RecoChargedCandidate*>(cand);
	    if(chcand) {
	      bool isnew = true;
	      for(container::const_iterator trk = selected_.begin();trk!= selected_.end(); ++trk) {
		if(chcand->track().get() == *trk) {isnew = false; break;}
	      }
	      if(isnew) selected_.push_back(chcand->track().get());
	    }
	  }
	}
      }
    }
  }
}
size_t TrackFromV0Selector::size() const { return selected_.size(); }

