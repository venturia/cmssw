import FWCore.ParameterSet.Config as cms

#from myAnalyzers.V0RecoAnalyzer.runV0Analysis_cff import *

#extracted from the file above

from UserCode.TrackerTrackMixing.refittedtrackcoupler_cfi import *
matchedTrackPairs.secondTrackCollection = cms.InputTag("tracksFromV0")
matchedNewTrackPairs = matchedTrackPairs.clone(secondTrackCollection = cms.InputTag("newTracksFromV0"))
matchedV0TrackPairs = matchedTrackPairs.clone(firstTrackCollection = cms.InputTag("tracksFromV0"),
                                              secondTrackCollection = cms.InputTag("newTracksFromV0"))
matchedOtobV0TrackPairs = matchedTrackPairs.clone(firstTrackCollection = cms.InputTag("tracksFromOtobV0"),
                                                  secondTrackCollection = cms.InputTag("newTracksFromOtobV0"))



from TrackingPFG.Utilities.trackcomparator_cfi import *

newtrackcomparator = trackcomparator.clone(trackPairCollection = cms.InputTag("matchedNewTrackPairs"))
v0trackcomparator = trackcomparator.clone(trackPairCollection = cms.InputTag("matchedV0TrackPairs"))
otobv0trackcomparator = trackcomparator.clone(trackPairCollection = cms.InputTag("matchedOtobV0TrackPairs"))

seqTrackComparator = cms.Sequence(matchedTrackPairs * trackcomparator +
                                  matchedNewTrackPairs * newtrackcomparator +
                                  matchedV0TrackPairs * v0trackcomparator +
                                  matchedOtobV0TrackPairs * otobv0trackcomparator
                                  )
