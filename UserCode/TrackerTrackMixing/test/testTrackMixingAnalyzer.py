import FWCore.ParameterSet.Config as cms

process = cms.Process('AN')

process.load('FWCore/MessageService/MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/g/gpetrucc/scratch0/tracking-perf/tobonly/CMSSW_3_3_4/src/Mix/DMDataOnData_TkOnly.root')
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/g/gpetrucc/scratch0/tracking-perf/tobonly/CMSSW_3_3_4/src/Mix/DMDataOnData_TkOnly_MinBias.root')
)

process.ana = cms.EDFilter("TrackMixingAnalyzer",
    tracksSignal = cms.InputTag("generalTracks",  "","RECO1"),
    pixelsSignal = cms.InputTag("siPixelClusters","","RECO1"),
    stripsSignal = cms.InputTag("siStripClusters","","RECO1"),
    mixData      = cms.InputTag("mixData",        "","RECO2"),
    tracksMix    = cms.InputTag("generalTracks",  "","RECO2"),
    pixelsMix    = cms.InputTag("siPixelClusters","","RECO2"),
    stripsMix    = cms.InputTag("siStripClusters","","RECO2"),
    pileupEvents = cms.uint32(1),
    #cut = cms.string("numberOfValidHits() > 5"),
    cut = cms.string(""),
    minSharedHitFraction = cms.double(.75),
    debug = cms.untracked.bool(True),
)

process.path = cms.Path(
    process.ana
)
