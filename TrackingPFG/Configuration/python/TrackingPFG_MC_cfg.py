import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("TrackingPFGMC")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('HLTprocess',
                  "HLT",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTProcess")
options.register ('L1Collection',
                  "gtDigis",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "L1DigiCollection")
options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")
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

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

if options.isAOD == 1:
   process.load("TrackingPFG.Configuration.dataAnalysisAODPaths_cff")
else: 
   process.load("TrackingPFG.Configuration.dataAnalysisPaths_cff")

#process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","",options.HLTprocess)
process.hltSelection.hltResults = cms.InputTag("TriggerResults","",options.HLTprocess)
process.hltSelection.l1tResults = cms.InputTag(options.L1Collection)

# clone and rename collision analyses sequences

#All Events

process.ptrigger = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqTriggerFiltersMC +
                            process.seqOnlyTriggerAnalysis + process.seqOnlyTriggerAnalysisMC)
process.pPV = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysis)
process.pNoScraping = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysis)
process.pOnlyNoScraping = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysis)


for label, trigger,negate in zip(options.triggerLabels,options.triggerPaths,options.negateFlags):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
#   getattr(process,"hltSelection"+label).HLTPaths = cms.vstring(trigger)
   getattr(process,"hltSelection"+label).triggerConditions = cms.vstring(trigger)

   if negate == 1:
      tempmodule = getattr(process,"hltSelection"+label)
      getattr(process,"seqHLTSelection"+label).replace(getattr(process,"hltSelection"+label),~tempmodule)

   cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,label)
   cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysisMC,label)
   cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,label)
   cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,label)

   setattr(process,"ptrigger"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                             process.seqProducersMain + process.seqTriggerFiltersMC +
                                             getattr(process,"seqOnlyTriggerAnalysis"+label) +
                                             getattr(process,"seqOnlyTriggerAnalysisMC"+label)
                                             ))
   setattr(process,"pPV"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                        process.seqProducersMain + process.seqPVFiltersMC +
                                        getattr(process,"seqPreScrapingAnalysis"+label)))
   setattr(process,"pNoScraping"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                                process.seqProducersMain + process.seqNoScrapingFiltersMC +
                                                getattr(process,"seqNoScrapingAnalysis"+label)))
   setattr(process,"pOnlyNoScraping"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                                    process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC +
                                                    getattr(process,"seqOnlyNoScrapingAnalysis"+label)))
   
#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_PFG.root')
                                   )

print process.dumpPython()
