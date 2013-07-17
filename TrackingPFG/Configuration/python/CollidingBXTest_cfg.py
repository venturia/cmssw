import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("CollidingBXTest")

#prepare options

options = VarParsing.VarParsing()

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

process.pnoand = cms.Path(process.bptxPlus * process.bptxMinus * ~process.bptxAnd)


process.outodd = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string("odd_events.root"),
        outputCommands = cms.untracked.vstring("keep *"),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pnoand"))
	)


#-----------------------------------

process.e = cms.EndPath(process.outodd)

