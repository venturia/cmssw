import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("CollidingBXTestComplete")

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

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    fileMode = cms.untracked.string("FULLMERGE")
    )

process.load("FWCore.MessageService.MessageLogger_cfi")

#----------------------------------------------------------------

process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string("DEBUG")
process.MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cout.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000)
    )

process.MessageLogger.debugModules = cms.untracked.vstring("bptxAnd","bptxAndTT")
#process.MessageLogger.debugModules = cms.untracked.vstring("*")


process.MessageLogger.cerr.placeholder = cms.untracked.bool(False)
process.MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100000)
    )

#----Remove too verbose PrimaryVertexProducer

process.MessageLogger.suppressInfo.append("pixelVerticesAdaptive")
process.MessageLogger.suppressInfo.append("pixelVerticesAdaptiveNoBS")

#----Remove too verbose BeamSpotOnlineProducer

process.MessageLogger.suppressInfo.append("testBeamSpot")
process.MessageLogger.suppressInfo.append("onlineBeamSpot")
#------------------------------------------------------------------


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring("file:/afs/cern.ch/cms/tracking/output/odd_events.root"),
#                    skipBadFiles = cms.untracked.bool(True),
                    inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                    )


from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
process.es_prefer_l1GtTriggerMaskTechTrig = cms.ESPrefer("L1GtTriggerMaskTechTrigTrivialProducer","l1GtTriggerMaskTechTrig")

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff")
process.es_prefer_l1GtTriggerMaskAlgoTrig = cms.ESPrefer("L1GtTriggerMaskAlgoTrigTrivialProducer","l1GtTriggerMaskAlgoTrig")

#bit 0 selection: BPTX_AND

process.bptxAndTT = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0'))

process.bptxAnd = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(False), L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
                                        L1SeedsLogicalExpression = cms.string('L1_BptxPlus AND L1_BptxMinus'))


# BPTX OR

 
process.bptxOr = cms.EDFilter("L1Filter",
                      inputTag = cms.InputTag("gtDigis"),
                      useAODRecord = cms.bool(False),
                      useFinalDecision = cms.bool(False),
                      algorithms = cms.vstring("L1_BptxPlusORMinus")
                      )


process.bptxPlus = process.bptxOr.clone(algorithms=cms.vstring("L1_BptxPlus"))

process.bptxMinus = process.bptxOr.clone(algorithms=cms.vstring("L1_BptxMinus"))

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_R_38X_V13A::All"

process.pnoand = cms.Path(process.bptxPlus * process.bptxMinus * ~process.bptxAnd)

process.pnoandTT = cms.Path(process.bptxPlus * process.bptxMinus * ~process.bptxAndTT)

process.pand = cms.Path(process.bptxPlus * process.bptxMinus * process.bptxAnd)

process.outodd = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string("odd_events.root"),
        outputCommands = cms.untracked.vstring("keep *"),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pnoand"))
	)


#-----------------------------------

#process.e = cms.EndPath(process.outodd)

