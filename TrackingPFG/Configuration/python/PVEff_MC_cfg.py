import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingPFG")

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")


process.load("TrackingPFG.Configuration.mcPVEffAnalysisPaths_cff")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "START3X_V26A::All"


#

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('PVEff_PFG.root')
                                   )

