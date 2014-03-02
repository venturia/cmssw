import FWCore.ParameterSet.Config as cms

logErrorAnalysisTooManyClusters = cms.EDFilter("LogErrorEventFilter",
                                               src = cms.InputTag("logErrorHarvester"),
                                               maxErrorFractionInLumi = cms.double(1.0), # if more than 20% of the events in this lumi have errors, the lumi will be excluded from the run summary (not relevant for skimming)
                                               maxErrorFractionInRun  = cms.double(1.0), # if more than 20% of the events in this run (excluding bad lumis)) have errors, the run will be excluded (not relevant for skimming)
                                               maxSavedEventsPerLumiAndError = cms.uint32(100000), # save events with errors but each error can get no no more than 10 events per lumi 
                                               #                                        categoriesToIgnore = cms.vstring("HLTConfigProvider","FastCloningDisabled")
                                               categoriesToWatch = cms.vstring("TooManyClusters"),
                                               modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds")
                                       
                                       )

logErrorAnalysisTooManyTriplets =logErrorAnalysisTooManyClusters.clone(categoriesToWatch = cms.vstring("TooManyTriplets",
                                                                                                       "TooManyPairs",
                                                                                                       "PixelTripletHLTGenerator"))

logErrorAnalysisTooManySeeds =logErrorAnalysisTooManyClusters.clone(categoriesToWatch = cms.vstring("TooManySeeds"))

logErrorAnalysisCosmicRegional =logErrorAnalysisTooManyClusters.clone(categoriesToWatch = cms.vstring("CosmicRegionalSeedGenerator"))

logErrorAnalysisTooManyErrors =logErrorAnalysisTooManyClusters.clone(categoriesToWatch = cms.vstring("TooManyErrors"))

logErrorAnalysisAnyError = logErrorAnalysisTooManyClusters.clone(categoriesToWatch = cms.vstring(),modulesToIgnore = cms.vstring())

seqLogErrTooManyClustersSelection = cms.Sequence(logErrorAnalysisTooManyClusters)
seqLogErrTooManyTripletsSelection = cms.Sequence(logErrorAnalysisTooManyTriplets)
seqLogErrTooManySeedsSelection = cms.Sequence(logErrorAnalysisTooManySeeds)
seqLogErrCosmicRegionalSelection = cms.Sequence(logErrorAnalysisCosmicRegional)
seqLogErrAnyErrorSelection = cms.Sequence(logErrorAnalysisAnyError)

# selection on official (RECO) collection

#logErrorAnalysisTooManyClustersRECO = logErrorAnalysisTooManyClusters.clone(src=cms.InputTag("logErrorHarvester","","reRECO"))
#logErrorAnalysisTooManySeedsRECO = logErrorAnalysisTooManySeeds.clone(src=cms.InputTag("logErrorHarvester","","reRECO"))
#logErrorAnalysisTooManyTripletsRECO = logErrorAnalysisTooManyTriplets.clone(src=cms.InputTag("logErrorHarvester","","reRECO"))
logErrorAnalysisTooManyClustersRECO = logErrorAnalysisTooManyClusters.clone(src=cms.InputTag("logErrorHarvester","","RECO"))
logErrorAnalysisTooManySeedsRECO = logErrorAnalysisTooManySeeds.clone(src=cms.InputTag("logErrorHarvester","","RECO"))
logErrorAnalysisTooManyTripletsRECO = logErrorAnalysisTooManyTriplets.clone(src=cms.InputTag("logErrorHarvester","","RECO"))

seqLogErrTooManyClustersRECOSelection = cms.Sequence(logErrorAnalysisTooManyClustersRECO)
seqLogErrTooManySeedsRECOSelection = cms.Sequence(logErrorAnalysisTooManySeedsRECO)
seqLogErrTooManyTripletsRECOSelection = cms.Sequence(logErrorAnalysisTooManyTripletsRECO)

seqLogErrNOTTooManyClustersRECOSelection = cms.Sequence(~logErrorAnalysisTooManyClustersRECO)
seqLogErrNOTTooManySeedsRECOSelection = cms.Sequence(~logErrorAnalysisTooManySeedsRECO)
seqLogErrNOTTooManyTripletsRECOSelection = cms.Sequence(~logErrorAnalysisTooManyTripletsRECO)

