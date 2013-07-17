import FWCore.ParameterSet.Config as cms

process = cms.Process('DIFF')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('promptReco nevts:-1'),
    name = cms.untracked.string('PyReleaseValidation')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
)
# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:/data/real/900GeV/BSCSkims_ReRecos/BSCskim_123592-fittedBSv2-stdReco-vtxLevel2-all.root'
        #'file:/data/real/900GeV/BSCSkims_ReRecos/bit40-123592-stdReco-GR09_P_V7.root'
        'file:promptReco_RAW2DIGI_L1Reco_RECO_DQM_ALCA.root'
    )
)

# Other statements
process.GlobalTag.globaltag = 'GR09_P_V7::All'

# Output definition
process.FEVT = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.FEVTEventContent.outputCommands,
    fileName = cms.untracked.string('diff-PR.root'),
)
process.output_step = cms.Path(process.FEVT)

process.trackDiff = cms.EDProducer("TrackDiff",
    tracksBefore = cms.InputTag("generalTracks","","EXPRESS"),
    tracksAfter  = cms.InputTag("generalTracks","","RECO"),
    #cut = cms.string(""),
    cut = cms.string("numberOfValidHits>4 && pt>.3"),
    minFraction = cms.double(0.75),
)
process.diff = cms.Path(process.trackDiff)

process.FEVT.outputCommands = [ 'drop *', 'keep *_generalTracks_*_*', 'keep *_siPixelClusters__*', 'keep *_siStripClusters__*', 'keep *_trackDiff_*_*' ]

process.schedule = cms.Schedule(process.diff,process.output_step)



