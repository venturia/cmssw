import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingPFG")

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring(),
#                            skipBadFiles = cms.untracked.bool(True),
#                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
#                            )

process.load("TrackingPFG.Configuration.mcFastSimAnalysisPaths_cff")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "START3X_V26::All"
#process.GlobalTag.globaltag = "START3X_V26A::All"
#process.GlobalTag.globaltag = "START36_V4::All"


#

process.conversionntuplizer.outfile = "ntuple_conversion_test_data.root"    # output file for conversion ntuples

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_PFG.root')
                                   )

