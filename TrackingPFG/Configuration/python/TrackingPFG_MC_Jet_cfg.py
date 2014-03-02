import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("TrackingPFGMCJet")

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
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

process.load("TrackingPFG.Configuration.dataAnalysisPaths_cff")

process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","",options.HLTprocess)

# clone and rename collision analyses sequences

#All Events

process.ptrigger = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysis)
process.pPV = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysis)
process.pNoScraping = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysis)
process.pOnlyNoScraping = cms.Path(process.seqHLTSelection + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysis)
#DiJetAve140U

cloneProcessingSnippet(process,process.seqHLTSelection,"DiJetAve140U")
process.hltSelectionDiJetAve140U.HLTPaths = cms.vstring("HLT_DiJetAve140U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"DiJetAve140U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"DiJetAve140U")
#process.pvgoodonlynoscrapingDiJetAve140U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingDiJetAve140U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionDiJetAve140U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"DiJetAve140U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"DiJetAve140U")

process.ptriggerDiJetAve140U = cms.Path(process.seqHLTSelectionDiJetAve140U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisDiJetAve140U)
process.pPVDiJetAve140U = cms.Path(process.seqHLTSelectionDiJetAve140U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisDiJetAve140U)
process.pNoScrapingDiJetAve140U = cms.Path(process.seqHLTSelectionDiJetAve140U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisDiJetAve140U)
process.pOnlyNoScrapingDiJetAve140U = cms.Path(process.seqHLTSelectionDiJetAve140U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisDiJetAve140U)


#Jet140U

cloneProcessingSnippet(process,process.seqHLTSelection,"Jet140U")
process.hltSelectionJet140U.HLTPaths = cms.vstring("HLT_Jet140U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Jet140U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Jet140U")
#process.pvgoodonlynoscrapingJet140U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingJet140U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionJet140U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Jet140U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Jet140U")

process.ptriggerJet140U = cms.Path(process.seqHLTSelectionJet140U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisJet140U)
process.pPVJet140U = cms.Path(process.seqHLTSelectionJet140U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisJet140U)
process.pNoScrapingJet140U = cms.Path(process.seqHLTSelectionJet140U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisJet140U)
process.pOnlyNoScrapingJet140U = cms.Path(process.seqHLTSelectionJet140U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisJet140U)

#DiJetAve70U

cloneProcessingSnippet(process,process.seqHLTSelection,"DiJetAve70U")
process.hltSelectionDiJetAve70U.HLTPaths = cms.vstring("HLT_DiJetAve70U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"DiJetAve70U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"DiJetAve70U")
#process.pvgoodonlynoscrapingDiJetAve70U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingDiJetAve70U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionDiJetAve70U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"DiJetAve70U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"DiJetAve70U")

process.ptriggerDiJetAve70U = cms.Path(process.seqHLTSelectionDiJetAve70U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisDiJetAve70U)
process.pPVDiJetAve70U = cms.Path(process.seqHLTSelectionDiJetAve70U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisDiJetAve70U)
process.pNoScrapingDiJetAve70U = cms.Path(process.seqHLTSelectionDiJetAve70U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisDiJetAve70U)
process.pOnlyNoScrapingDiJetAve70U = cms.Path(process.seqHLTSelectionDiJetAve70U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisDiJetAve70U)


#Jet70U

cloneProcessingSnippet(process,process.seqHLTSelection,"Jet70U")
process.hltSelectionJet70U.HLTPaths = cms.vstring("HLT_Jet70U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Jet70U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Jet70U")
#process.pvgoodonlynoscrapingJet70U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingJet70U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionJet70U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Jet70U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Jet70U")

process.ptriggerJet70U = cms.Path(process.seqHLTSelectionJet70U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisJet70U)
process.pPVJet70U = cms.Path(process.seqHLTSelectionJet70U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisJet70U)
process.pNoScrapingJet70U = cms.Path(process.seqHLTSelectionJet70U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisJet70U)
process.pOnlyNoScrapingJet70U = cms.Path(process.seqHLTSelectionJet70U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisJet70U)

#Jet50U

cloneProcessingSnippet(process,process.seqHLTSelection,"Jet50U")
process.hltSelectionJet50U.HLTPaths = cms.vstring("HLT_Jet50U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Jet50U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Jet50U")
#process.pvgoodonlynoscrapingJet50U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingJet50U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionJet50U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Jet50U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Jet50U")

process.ptriggerJet50U = cms.Path(process.seqHLTSelectionJet50U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisJet50U)
process.pPVJet50U = cms.Path(process.seqHLTSelectionJet50U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisJet50U)
process.pNoScrapingJet50U = cms.Path(process.seqHLTSelectionJet50U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisJet50U)
process.pOnlyNoScrapingJet50U = cms.Path(process.seqHLTSelectionJet50U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisJet50U)

#Jet30U

cloneProcessingSnippet(process,process.seqHLTSelection,"Jet30U")
process.hltSelectionJet30U.HLTPaths = cms.vstring("HLT_Jet30U*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Jet30U")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Jet30U")
#process.pvgoodonlynoscrapingJet30U.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingJet30U.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionJet30U.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Jet30U")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Jet30U")

process.ptriggerJet30U = cms.Path(process.seqHLTSelectionJet30U + process.seqProducersMain + process.seqTriggerFiltersMC + process.seqOnlyTriggerAnalysisJet30U)
process.pPVJet30U = cms.Path(process.seqHLTSelectionJet30U + process.seqProducersMain + process.seqPVFiltersMC + process.seqPreScrapingAnalysisJet30U)
process.pNoScrapingJet30U = cms.Path(process.seqHLTSelectionJet30U + process.seqProducersMain + process.seqNoScrapingFiltersMC + process.seqNoScrapingAnalysisJet30U)
process.pOnlyNoScrapingJet30U = cms.Path(process.seqHLTSelectionJet30U + process.seqProducersMain + process.seqOnlyNoScrapingFiltersMC + process.seqOnlyNoScrapingAnalysisJet30U)

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "GR10_E_V5::All"
process.GlobalTag.globaltag = options.globalTag

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_PFG.root')
                                   )

