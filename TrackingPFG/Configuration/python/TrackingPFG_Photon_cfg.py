import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("TrackingPFGPhoton")

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

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

if options.isAOD == 1: 
   process.load("TrackingPFG.Configuration.dataAnalysisAODPaths_cff")
else: 
   process.load("TrackingPFG.Configuration.dataAnalysisPaths_cff")
   process.load("TrackingPFG.Configuration.dataAuxiliaryAnalysisPaths_cff")

# clone and rename collision analyses sequences

#HLT_Photon20_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon20CleanedL1R")
process.hltSelectionPhoton20CleanedL1R.HLTPaths = cms.vstring("HLT_Photon20_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon20CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon20CleanedL1R")
#process.pvgoodonlynoscrapingPhoton20CleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton20CleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton20CleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon20CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon20CleanedL1R")

process.ptriggerPhoton20CleanedL1R = cms.Path(process.seqHLTSelectionPhoton20CleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton20CleanedL1R)
process.pPVPhoton20CleanedL1R = cms.Path(process.seqHLTSelectionPhoton20CleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton20CleanedL1R)
process.pNoScrapingPhoton20CleanedL1R = cms.Path(process.seqHLTSelectionPhoton20CleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton20CleanedL1R)
process.pOnlyNoScrapingPhoton20CleanedL1R = cms.Path(process.seqHLTSelectionPhoton20CleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton20CleanedL1R)

#HLT_Photon25_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon25CleanedL1R")
process.hltSelectionPhoton25CleanedL1R.HLTPaths = cms.vstring("HLT_Photon25_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon25CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon25CleanedL1R")
#process.pvgoodonlynoscrapingPhoton25CleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton25CleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton25CleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon25CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon25CleanedL1R")

process.ptriggerPhoton25CleanedL1R = cms.Path(process.seqHLTSelectionPhoton25CleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton25CleanedL1R)
process.pPVPhoton25CleanedL1R = cms.Path(process.seqHLTSelectionPhoton25CleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton25CleanedL1R)
process.pNoScrapingPhoton25CleanedL1R = cms.Path(process.seqHLTSelectionPhoton25CleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton25CleanedL1R)
process.pOnlyNoScrapingPhoton25CleanedL1R = cms.Path(process.seqHLTSelectionPhoton25CleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton25CleanedL1R)

#HLT_Photon30_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon30CleanedL1R")
process.hltSelectionPhoton30CleanedL1R.HLTPaths = cms.vstring("HLT_Photon30_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon30CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon30CleanedL1R")
#process.pvgoodonlynoscrapingPhoton30CleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton30CleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton30CleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon30CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon30CleanedL1R")

process.ptriggerPhoton30CleanedL1R = cms.Path(process.seqHLTSelectionPhoton30CleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton30CleanedL1R)
process.pPVPhoton30CleanedL1R = cms.Path(process.seqHLTSelectionPhoton30CleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton30CleanedL1R)
process.pNoScrapingPhoton30CleanedL1R = cms.Path(process.seqHLTSelectionPhoton30CleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton30CleanedL1R)
process.pOnlyNoScrapingPhoton30CleanedL1R = cms.Path(process.seqHLTSelectionPhoton30CleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton30CleanedL1R)

#HLT_Photon50_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon50CleanedL1R")
process.hltSelectionPhoton50CleanedL1R.HLTPaths = cms.vstring("HLT_Photon50_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon50CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon50CleanedL1R")
#process.pvgoodonlynoscrapingPhoton50CleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton50CleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton50CleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon50CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon50CleanedL1R")

process.ptriggerPhoton50CleanedL1R = cms.Path(process.seqHLTSelectionPhoton50CleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton50CleanedL1R)
process.pPVPhoton50CleanedL1R = cms.Path(process.seqHLTSelectionPhoton50CleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton50CleanedL1R)
process.pNoScrapingPhoton50CleanedL1R = cms.Path(process.seqHLTSelectionPhoton50CleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton50CleanedL1R)
process.pOnlyNoScrapingPhoton50CleanedL1R = cms.Path(process.seqHLTSelectionPhoton50CleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton50CleanedL1R)

#HLT_Photon70_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon70CleanedL1R")
process.hltSelectionPhoton70CleanedL1R.HLTPaths = cms.vstring("HLT_Photon70_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon70CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon70CleanedL1R")
#process.pvgoodonlynoscrapingPhoton70CleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton70CleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton70CleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon70CleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon70CleanedL1R")

process.ptriggerPhoton70CleanedL1R = cms.Path(process.seqHLTSelectionPhoton70CleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton70CleanedL1R)
process.pPVPhoton70CleanedL1R = cms.Path(process.seqHLTSelectionPhoton70CleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton70CleanedL1R)
process.pNoScrapingPhoton70CleanedL1R = cms.Path(process.seqHLTSelectionPhoton70CleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton70CleanedL1R)
process.pOnlyNoScrapingPhoton70CleanedL1R = cms.Path(process.seqHLTSelectionPhoton70CleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton70CleanedL1R)


#HLT_Photon35_Isol_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon35IsolCleanedL1R")
process.hltSelectionPhoton35IsolCleanedL1R.HLTPaths = cms.vstring("HLT_Photon35_Isol_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon35IsolCleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon35IsolCleanedL1R")
#process.pvgoodonlynoscrapingPhoton35IsolCleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton35IsolCleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton35IsolCleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon35IsolCleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon35IsolCleanedL1R")

process.ptriggerPhoton35IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton35IsolCleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton35IsolCleanedL1R)
process.pPVPhoton35IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton35IsolCleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton35IsolCleanedL1R)
process.pNoScrapingPhoton35IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton35IsolCleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton35IsolCleanedL1R)
process.pOnlyNoScrapingPhoton35IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton35IsolCleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton35IsolCleanedL1R)

#HLT_Photon40_Isol_Cleaned_L1R

cloneProcessingSnippet(process,process.seqHLTSelection,"Photon40IsolCleanedL1R")
process.hltSelectionPhoton40IsolCleanedL1R.HLTPaths = cms.vstring("HLT_Photon40_Isol_Cleaned_L1R*")

cloneProcessingSnippet(process,process.seqNoScrapingAnalysis,"Photon40IsolCleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyNoScrapingAnalysis,"Photon40IsolCleanedL1R")
#process.pvgoodonlynoscrapingPhoton40IsolCleanedL1R.usePrescaleWeight = cms.bool(True)
#process.pvgoodonlynoscrapingPhoton40IsolCleanedL1R.prescaleWeightProviderPSet.prescaleWeightHltPaths = process.hltSelectionPhoton40IsolCleanedL1R.HLTPaths 

cloneProcessingSnippet(process,process.seqPreScrapingAnalysis,"Photon40IsolCleanedL1R")
cloneProcessingSnippet(process,process.seqOnlyTriggerAnalysis,"Photon40IsolCleanedL1R")

process.ptriggerPhoton40IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton40IsolCleanedL1R + process.seqProducersMain + process.seqTriggerFilters + process.seqOnlyTriggerAnalysisPhoton40IsolCleanedL1R)
process.pPVPhoton40IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton40IsolCleanedL1R + process.seqProducersMain + process.seqPVFilters + process.seqPreScrapingAnalysisPhoton40IsolCleanedL1R)
process.pNoScrapingPhoton40IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton40IsolCleanedL1R + process.seqProducersMain + process.seqNoScrapingFilters + process.seqNoScrapingAnalysisPhoton40IsolCleanedL1R)
process.pOnlyNoScrapingPhoton40IsolCleanedL1R = cms.Path(process.seqHLTSelectionPhoton40IsolCleanedL1R + process.seqProducersMain + process.seqOnlyNoScrapingFilters + process.seqOnlyNoScrapingAnalysisPhoton40IsolCleanedL1R)


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "GR10_E_V5::All"
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_PFG.root')
                                   )

#---------APV induced noisy events

process.outnoisy = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string("apvNoisy.root"),
        outputCommands = cms.untracked.vstring("keep *"),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("plat1","pfhmax1","pfhmax2"))
	)

#-----------------------------------

#process.e = cms.EndPath(process.outnoisy)

