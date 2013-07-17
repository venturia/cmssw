import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerTest")

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(),
                            skipBadFiles = cms.untracked.bool(True),
                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                            )

#

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR09_R_35X_V3::All"

#

process.load("TrackingPFG.Configuration.triggerFilterTestSequence_cff")

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('TriggerTest.root')
                                   )

process.pall = cms.Path(process.seqEventHistoryAll)

process.pand = cms.Path(process.seqEventHistoryAND)
process.pplus = cms.Path(process.seqEventHistoryNotANDandPlus)
process.pminus = cms.Path(process.seqEventHistoryNotANDandMinus)
process.pxor = cms.Path(process.seqEventHistoryNotANDandOR)

process.pandtt = cms.Path(process.seqEventHistoryANDTT)
process.pplustt = cms.Path(process.seqEventHistoryNotANDandPlusTT)
process.pminustt = cms.Path(process.seqEventHistoryNotANDandMinusTT)
process.pxortt = cms.Path(process.seqEventHistoryNotANDandORTT)

