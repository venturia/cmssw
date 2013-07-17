import FWCore.ParameterSet.Config as cms

validationak5 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("ak5TrackJets"),
                               tracksSource    = cms.InputTag("generalTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )
validationkt4 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("kt4TrackJets"),
                               tracksSource    = cms.InputTag("generalTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )
validationsc5 = cms.EDAnalyzer('TrackJetsValidation',
                               trackjetsSource = cms.InputTag("sisCone5TrackJets"),
                               tracksSource    = cms.InputTag("generalTracks"),
                               verticesSource  = cms.InputTag("offlinePrimaryVertices")
                               )

