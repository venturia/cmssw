import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingPFG")

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")


process.load("TrackingPFG.Configuration.dataBeamBkgAnalysisPaths_cff")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR10_P_V5::All"


#

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('BeamBkg_PFG.root')
                                   )

