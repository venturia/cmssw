import FWCore.ParameterSet.Config as cms

tracksFromV0 = cms.EDFilter("TrackFromV0Selector",
                            src = cms.InputTag("generalTracks"),
                            v0Collections = cms.VInputTag(cms.InputTag("generalV0Candidates:Kshort"),cms.InputTag("generalV0Candidates:Lambda")),
                            maxMass = cms.double(-1.),
                            minMass = cms.double(1.)
                           )

