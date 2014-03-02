import FWCore.ParameterSet.Config as cms

pixelVerticesDivisiveNewCuts = cms.EDProducer("PixelVertexProducer",
    WtAverage = cms.bool(True),
    ZOffset = cms.double(5.0),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Verbosity = cms.int32(0),
    UseError = cms.bool(True),
    TrackCollection = cms.InputTag("pixelTracks"),
    ZSeparation = cms.double(1.),    #ZSeparation = cms.double(0.05),
    NTrkMin = cms.int32(2),
    Method2 = cms.bool(True),
    Finder = cms.string('DivisiveVertexFinder'),
    PtMin = cms.double(0.5)    #PtMin = cms.double(1.0)
)

