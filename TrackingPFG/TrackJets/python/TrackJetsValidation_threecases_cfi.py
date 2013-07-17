import FWCore.ParameterSet.Config as cms

trackjetsak5 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("ak5TrackJets"),
                               tracksSource    = cms.InputTag("trackjetsTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )
trackjetskt4 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("kt4TrackJets"),
                               tracksSource    = cms.InputTag("trackjetsTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )
trackjetssc5 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("sisCone5TrackJets"),
                               tracksSource    = cms.InputTag("trackjetsTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )


