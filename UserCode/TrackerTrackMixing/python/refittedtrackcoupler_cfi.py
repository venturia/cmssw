import FWCore.ParameterSet.Config as cms

matchedTrackPairs = cms.EDProducer("RefittedTrackCoupler",
                            firstTrackCollection = cms.InputTag("generalTracks"),
                            secondTrackCollection = cms.InputTag("generalTracks"),
                            stripClusterCollection = cms.InputTag("siStripClusters"),
                            pixelClusterCollection = cms.InputTag("siPixelClusters")
                           )

