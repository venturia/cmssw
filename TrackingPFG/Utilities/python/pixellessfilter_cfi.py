import FWCore.ParameterSet.Config as cms

pixellessfilter = cms.EDFilter("PixelLessFilter",
                               trackCollection = cms.InputTag("generalTracks"),
                               vtxCollection = cms.InputTag("offlinePrimaryVertices"),
                               vtxzMax = cms.double(1000),
                               filter = cms.bool(False),
                               newIter = cms.bool(False),
                               cuts = cms.vdouble(0.0,0.0,0.)
                               )
