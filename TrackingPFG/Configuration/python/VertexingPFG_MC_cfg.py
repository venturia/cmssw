import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("VertexingPFGMC")

#prepare options

options = VarParsing.VarParsing()

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
options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")

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

process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","",options.HLTprocess)

# clone and rename collision analyses sequences

#All Events

process.pOnlyNoScraping = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysis)


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Vertexing_PFG.root')
                                   )

