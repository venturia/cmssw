import FWCore.ParameterSet.Config as cms

from TrackingPFG.Utilities.trackfromv0selector_cfi import *

tracksFromV0.v0Collections = cms.VInputTag(cms.InputTag("localV0Candidates:Kshort"),cms.InputTag("localV0Candidates:Lambda"))

tracksFromOtobV0 = tracksFromV0.clone(v0Collections = cms.VInputTag(cms.InputTag("generalV0Candidates:Kshort"),cms.InputTag("generalV0Candidates:Lambda")))

from RecoTracker.TrackProducer.TrackRefitter_cfi import *

newTracksFromV0 = TrackRefitter.clone(src = cms.InputTag("tracksFromV0"))
newTracksFromOtobV0 = TrackRefitter.clone(src = cms.InputTag("tracksFromOtobV0"))


seqV0Tracks = cms.Sequence(tracksFromV0 * newTracksFromV0 + tracksFromOtobV0 * newTracksFromOtobV0 )

