import FWCore.ParameterSet.Config as cms

process = cms.Process('L1TEMULATION')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Repacked_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("/store/relval/CMSSW_7_0_0_pre8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START70_V1-v1/00000/262AA156-744A-E311-9829-002618943945.root")
    )


process.output = cms.OutputModule(
    "PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    outputCommands = cms.untracked.vstring('keep *',
#                                           'drop FEDRawDataCollection_rawDataRepacker_*_*',
#                                           'drop FEDRawDataCollection_virginRawDataRepacker_*_*'),
    outputCommands = cms.untracked.vstring('drop *',
                                           'keep *_*_*_L1TEMULATION'),    
    fileName = cms.untracked.string('SimL1Emulator_Stage1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
                                           )
process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG')
process.GlobalTag.globaltag = cms.string('POSTLS162_V2::All')
#for HI Data
#process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V27A::All', '')

process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_cff')

## changes to L1 algorithms begin here, the list is exhaustive.
## commented values should be the default
## see L1Trigger/L1TCalorimeter/python/l1tCaloStage1Digis_cfi.py for more info
#process.l1tCaloStage1Digis.FirmwareVersion = cms.uint32(2) # 1=HI algos, 2=PP algos
#process.l1tCaloStage1Digis.egRelativeJetIsolationCut = cms.double(0.5)
#process.l1tCaloStage1Digis.tauRelativeJetIsolationCut = cms.double(1.)
#process.l1tCaloStage1Digis.regionETCutForHT = cms.uint32(7)
#process.l1tCaloStage1Digis.regionETCutForMET = cms.uint32(0)
#process.l1tCaloStage1Digis.minGctEtaForSums = cms.int32(4)
#process.l1tCaloStage1Digis.maxGctEtaForSums = cms.int32(17)

process.p1 = cms.Path(
    process.SimL1Emulator_Stage1
    )

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.p1, process.output_step
    )

# Spit out filter efficiency at the end.
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
