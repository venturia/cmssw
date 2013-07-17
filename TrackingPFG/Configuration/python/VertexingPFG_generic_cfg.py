import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("VertexingPFG")

#prepare options

options = VarParsing.VarParsing()

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
#options.globalTag = "DONOTEXIST::All"
options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")
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

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

if options.isAOD == 1: 
   process.load("TrackingPFG.Configuration.dataPVAnalysisPaths_cff")
else: 
   process.load("TrackingPFG.Configuration.dataPVAnalysisPaths_cff")


# if requested include Paths without HLT selection

if options.noHLT == 1:
   process.pOnlyNoScraping = cms.Path(process.seqHLTSelection +
                                      process.seqProducersMain + process.seqOnlyNoScrapingFilters +
                                      process.seqOnlyNoScrapingAnalysis)


# clone and rename collision analyses sequences


#process.pvgoodDAcolliding.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(True)

#

for label, trigger in zip(options.triggerLabels,options.triggerPaths):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
   getattr(process,"hltSelection"+label).HLTPaths = cms.vstring(trigger)
   
   cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,label)


   setattr(process,"pOnlyNoScraping"+label,cms.Path(getattr(process,"seqHLTSelection"+label) +
                                                    process.seqProducersMain + process.seqOnlyNoScrapingFilters +
                                                    getattr(process,"seqOnlyNoScrapingAnalysis"+label)))
   
#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Vertexing_PFG.root')
                                   )

