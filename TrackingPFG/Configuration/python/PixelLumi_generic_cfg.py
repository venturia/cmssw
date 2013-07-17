import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("PixelLumi")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")
options.register ('rerunLumiProducer',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if lumiProducer to be rerun")
options.register ('noHLT',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if paths with no HLT selection are needed")
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
options.register ('leadingBXOnlyFlags',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if bxselection filter has to be applied")

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.load("TrackingPFG.Configuration.dataAnalysisPathsPixelLumi_cff")

process.load("TrackingPFG.Configuration.bxSelectionSequence_cff")

if options.rerunLumiProducer == 1:
   process.seqProducersMain += process.lumiProducer


#if options.leadingBXOnly == 1:
#   process.seqHLTSelection += process.bxselection

# debug options

#process.trackcountOnlyNoScraping.runHisto = cms.untracked.bool(True)
#process.trackcounthpOnlyNoScraping.runHisto = cms.untracked.bool(True)

#process.spclusmultinvestonlynoscraping.runHisto = cms.untracked.bool(True)
#process.ssclusmultinvestonlynoscraping.runHisto = cms.untracked.bool(True)

# add ru histos in cluster mult plots

#process.ssclusmultinvestonlytrigger.runHisto = cms.untracked.bool(True)
#process.spclusmultinvestonlytrigger.runHisto = cms.untracked.bool(True)
#process.ssclusmulttimecorrelations.runHisto = cms.untracked.bool(True)

# if requested include Paths without HLT selection

if options.noHLT == 1:
   process.pOnlyNoScraping = cms.Path(process.seqHLTSelection +
                                      process.seqProducersMain + process.seqOnlyNoScrapingFilters +
                                      process.seqOnlyNoScrapingPixelLumiAnalysis)


# clone and rename collision analyses sequences


#process.pvgoodDAcolliding.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(True)

#

for label, trigger,negate,leadingbxonly in zip(options.triggerLabels,options.triggerPaths,options.negateFlags,options.leadingBXOnlyFlags):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
   getattr(process,"hltSelection"+label).triggerConditions = cms.vstring(trigger)

   if negate == 1:
      tempmodule = getattr(process,"hltSelection"+label)
      getattr(process,"seqHLTSelection"+label).replace(getattr(process,"hltSelection"+label),~tempmodule)

   if leadingbxonly == 1:   
      getattr(process,"seqHLTSelection"+label).insert(0,process.bxselection)
   
   cloneProcessingSnippet(process,process.seqOnlyNoScrapingPixelLumiAnalysis,label)
#process.pvgoodonlynoscrapingDiJetAve140U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingDiJetAve140U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionDiJetAve140U.HLTPaths 

   setattr(process,"pOnlyNoScraping"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                                    process.seqProducersMain + process.seqOnlyNoScrapingFilters +
                                                    getattr(process,"seqOnlyNoScrapingPixelLumiAnalysis"+label)))
   
#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('PixelLumi.root')
                                   )

#print process.dumpPython()
