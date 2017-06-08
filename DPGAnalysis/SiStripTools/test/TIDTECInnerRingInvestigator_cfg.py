import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("TIDTECInnerRingInvestigator")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('fromRAW',
                  "0",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "=1 if from RAW")
options.register ('HLTprocess',
                  "HLT",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTProcess")
options.register ('triggerPaths',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "list of HLT paths")
options.register ('triggerLabels',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "list of labels")
options.register ('negateFlags',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "list of flags to negate HLT selection")

options.parseArguments()

#

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    fileMode = cms.untracked.string("FULLMERGE")
    )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string("INFO")
process.MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cout.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000)
    )

process.MessageLogger.cerr.placeholder = cms.untracked.bool(False)
process.MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100000)
    )


#------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(options.inputFiles),
#                    skipBadFiles = cms.untracked.bool(True),
                    inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                    )

# HLT Selection ------------------------------------------------------------
process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", options.HLTprocess )
process.triggerResultsFilter.l1tResults = cms.InputTag( "" )
process.triggerResultsFilter.throw = cms.bool(False)

process.seqHLTSelection = cms.Sequence(process.triggerResultsFilter)

#--------------------------------------
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.seqRECO = cms.Sequence()

if options.fromRAW == 1:
    process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
    process.load("Configuration.StandardSequences.L1Reco_cff")
    process.siPixelClusters = process.siPixelClustersPreSplitting.clone()
    process.seqRECO = cms.Sequence(process.scalersRawToDigi +
                                   process.siStripDigis + process.siStripZeroSuppression + process.siStripClusters
                                   + process.siPixelDigis + process.siPixelClusters )


#

process.froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                                      l1ABCCollection=cms.InputTag("scalersRawToDigi")
                                      )
process.load("DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1tsDB_cfi")
process.load("DPGAnalysis.SiStripTools.eventtimedistribution_cfi")

process.seqEventHistoryReco = cms.Sequence(process.froml1abcHEs + process.APVPhases)
process.seqEventHistory = cms.Sequence(process.eventtimedistribution)

process.eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")



process.load("DPGAnalysis.SiStripTools.sistripclustermultiplicityprod_cfi")

#process.ssclustermultprod.withClusterSize=cms.untracked.bool(True)

process.ssclustermultprod.wantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(101),detLabel = cms.string("TIDring1"),selection=cms.untracked.vstring("0x1e000600-0x18000200")),
    cms.PSet(detSelection = cms.uint32(102),detLabel = cms.string("TIDring2"),selection=cms.untracked.vstring("0x1e000600-0x18000400")),
    cms.PSet(detSelection = cms.uint32(201),detLabel = cms.string("TECring1"),selection=cms.untracked.vstring("0x1e0000e0-0x1c000020")),
    cms.PSet(detSelection = cms.uint32(202),detLabel = cms.string("TECring2"),selection=cms.untracked.vstring("0x1e0000e0-0x1c000040"))
)

process.seqMultProd = cms.Sequence(process.ssclustermultprod)


process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterToDigiProducer_cfi")


process.seqProducers = cms.Sequence(process.seqEventHistoryReco + process.seqMultProd + process.siStripClustersToDigis)

#from HLTrigger.HLTfilters.triggerResultsFilter_cfi import *
#process.hltSelection = triggerResultsFilter.clone(
#                                          triggerConditions = cms.vstring("HLT_ZeroBias_*"),
#                                          hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
#                                          l1tResults = cms.InputTag( "" ),
#                                          throw = cms.bool(False)
#                                          )


process.load("DPGAnalysis.SiStripTools.ssclusmultinvestigator_cfi")
process.ssclusmultinvestigator.runHisto = cms.untracked.bool(True)
process.ssclusmultinvestigator.scaleFactor=cms.untracked.int32(1)
process.ssclusmultinvestigator.wantedSubDets = cms.untracked.VPSet(    
    cms.PSet(detSelection = cms.uint32(101),detLabel = cms.string("TIDring1"), binMax = cms.int32(1000)),
    cms.PSet(detSelection = cms.uint32(102),detLabel = cms.string("TIDring2"), binMax = cms.int32(1000)),
    cms.PSet(detSelection = cms.uint32(201),detLabel = cms.string("TECring1"), binMax = cms.int32(1000)),
    cms.PSet(detSelection = cms.uint32(202),detLabel = cms.string("TECring2"), binMax = cms.int32(1000))
    )

process.load("DPGAnalysis.SiStripTools.clusterbigeventsdebugger_cfi")
process.clusterbigeventsdebugger.selections = cms.VPSet(
cms.PSet(detSelection = cms.uint32(101),label = cms.string("TIDring1"),selection=cms.untracked.vstring("0x1e000600-0x18000200")),
cms.PSet(detSelection = cms.uint32(102),label = cms.string("TIDring2"),selection=cms.untracked.vstring("0x1e000600-0x18000400")),
cms.PSet(detSelection = cms.uint32(201),label = cms.string("TECring1"),selection=cms.untracked.vstring("0x1e0000e0-0x1c000020")),
cms.PSet(detSelection = cms.uint32(202),label = cms.string("TECring2"),selection=cms.untracked.vstring("0x1e0000e0-0x1c000040"))
)

process.load("DPGAnalysis.SiStripTools.digibigeventsdebugger_cfi")
process.digibigeventsdebugger.selections = process.clusterbigeventsdebugger.selections
process.digibigeventsdebugger.collection = cms.InputTag("siStripClustersToDigis","ZeroSuppressed")
#process.digibigeventsdebugger.foldedStrips = cms.untracked.bool(True)

process.seqClusMultInvest = cms.Sequence(process.ssclusmultinvestigator + process.clusterbigeventsdebugger + process.digibigeventsdebugger ) 

process.seqAnalyzers = cms.Sequence(process.seqEventHistory + process.seqClusMultInvest)

process.p0 = cms.Path(
    process.seqRECO + 
    process.seqProducers +
    process.seqAnalyzers)

for label, trigger,negate in zip(options.triggerLabels,options.triggerPaths,options.negateFlags):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
   getattr(process,"triggerResultsFilter"+label).triggerConditions = cms.vstring(trigger)

   if negate == 1:
      tempmodule = getattr(process,"triggerResultsFilter"+label)
      getattr(process,"seqHLTSelection"+label).replace(getattr(process,"triggerResultsFilter"+label),~tempmodule)

   cloneProcessingSnippet(process,process.seqAnalyzers,label)
   
   setattr(process,"ptrigger"+label,cms.Path(process.seqRECO +
                                             process.seqProducers +
                                             getattr(process,"seqHLTSelection"+label) +
                                             getattr(process,"seqAnalyzers"+label)))

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('TIDTECInnerRingInvestigator_'+options.tag+'.root')
                                   )

#print process.dumpPython()
