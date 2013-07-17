import FWCore.ParameterSet.Config as cms

trackcomparator = cms.EDAnalyzer("TrackComparator",
                            trackPairCollection = cms.InputTag("matchedTrackPairs")
                           )

