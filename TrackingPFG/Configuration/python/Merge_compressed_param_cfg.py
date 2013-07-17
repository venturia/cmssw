import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing


process = cms.Process("merge")

#

# setup 'analysis'  options
paroptions = VarParsing.VarParsing ('analysis')

# setup any defaults you want
#paroptions.outputFile = ''
#paroptions.inputFiles= ''
paroptions.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
paroptions.parseArguments()


process.load("TrackingPFG.Configuration.processOptions_cff")

process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(paroptions.maxEvents) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))

process.load("TrackingPFG.Configuration.poolSource_cff")

process.source.fileNames = cms.untracked.vstring(paroptions.inputFiles)

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string(paroptions.outputFile),
                               outputCommands = cms.untracked.vstring("keep *","drop LumiDetails_lumiProducer_*_*","drop LumiSummary_lumiProducer_*_*")
	)

#-----------------------------------

process.e = cms.EndPath(process.out)

