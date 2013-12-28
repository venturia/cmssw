/* \class TrackFromV0Selector
 *
 * \author Andrea Venturi, INFN
 *  from RecoTrackSelector
 *
 */
#include <vector>
#include "FWCore/Framework/interface/ConsumesCollector.h"
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
TrackFromV0Selector::TrackFromV0Selector ( const edm::ParameterSet & cfg, edm::ConsumesCollector&& iC ) :
  v0collectionTokens_(),
  massmin_(cfg.getParameter<double>("minMass")),
  massmax_(cfg.getParameter<double>("maxMass"))
{
  std::vector<edm::InputTag> v0collections = cfg.getParameter<std::vector<edm::InputTag> >("voCollections");
  for(std::vector<edm::InputTag>::const_iterator v0coll = v0collections.begin(); v0coll != v0collections.end(); ++v0coll) {
    v0collectionTokens_.push_back(iC.consumes<reco::VertexCompositeCandidateCollection>(*v0coll));
  }

}
    
    
void TrackFromV0Selector::select( const edm::Handle<collection>& c, const edm::Event & event, const edm::EventSetup&) {
  selected_.clear();
  // loop on V0 collections
  for( std::vector<edm::EDGetTokenT<reco::VertexCompositeCandidateCollection> >::const_iterator v0colltoken = v0collectionTokens_.begin(); 
       v0colltoken != v0collectionTokens_.end(); ++v0colltoken) {
    edm::Handle<reco::VertexCompositeCandidateCollection> v0s;
    event.getByToken(*v0colltoken,v0s);
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

