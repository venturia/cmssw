import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("LogErrorTestCrossCorr")


process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_noinfo_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")


#--------------------------------------
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestLogErrSequence_cff")
process.load("TrackingPFG.Configuration.seedMultInvestLogErrSequence_cff")
process.load("TrackingPFG.Configuration.simpleTrackLogErrSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")
process.load("TrackingPFG.Configuration.recoLogErrSequence_cff")

#----------------------------------------------------------------------
 
process.pNewTooManyClusters = cms.Path(
    process.seqLogErrNOTTooManyClustersRECOSelection +
    process.seqLogErrNOTTooManySeedsRECOSelection +
    process.seqLogErrTooManyClustersSelection
    )

process.pNewTooManySeeds = cms.Path(
    process.seqLogErrNOTTooManyClustersRECOSelection +
    process.seqLogErrNOTTooManySeedsRECOSelection +
    process.seqLogErrTooManySeedsSelection
    )

process.p0TooManyClustersRECO = cms.Path(
    process.seqLogErrTooManyClustersRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
#    process.seqSeedMultInvestLogErr +
    process.seqClusMultInvestLogErr +
    process.seqSimpleTrackLogErr
    )

process.p0TooManySeedsRECO = cms.Path(
    process.seqLogErrTooManySeedsRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
#    process.seqSeedMultInvestLogErr +
    process.seqClusMultInvestLogErr +
    process.seqSimpleTrackLogErr
    )

process.pTooManyClustersTooManyClustersRECO = cms.Path(
    process.seqLogErrTooManyClustersRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
    process.seqLogErrTooManyClustersSelection +
#    process.seqSeedMultInvestLogErrTooManyClusters +
    process.seqClusMultInvestLogErrTooManyClusters +
    process.seqSimpleTrackLogErrTooManyClusters +
#    process.seqSeedMultInvestLogErrTracking +
    process.seqClusMultInvestLogErrTracking +
    process.seqSimpleTrackLogErrTracking
    )
process.pTooManyClustersTooManySeedsRECO = cms.Path(
    process.seqLogErrTooManySeedsRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
    process.seqLogErrTooManyClustersSelection +
#    process.seqSeedMultInvestLogErrTooManyClusters +
    process.seqClusMultInvestLogErrTooManyClusters +
    process.seqSimpleTrackLogErrTooManyClusters +
#    process.seqSeedMultInvestLogErrTracking +
    process.seqClusMultInvestLogErrTracking +
    process.seqSimpleTrackLogErrTracking
    )


process.pTooManySeedsTooManyCustersRECO = cms.Path(
    process.seqLogErrTooManyClustersRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
    process.seqLogErrTooManySeedsSelection +
#    process.seqSeedMultInvestLogErrTooManySeeds +
    process.seqClusMultInvestLogErrTooManySeeds +
    process.seqSimpleTrackLogErrTooManySeeds +
#    process.seqSeedMultInvestLogErrTracking +
    process.seqClusMultInvestLogErrTracking +
    process.seqSimpleTrackLogErrTracking
    )
process.pTooManySeedsTooManySeedsRECO = cms.Path(
    process.seqLogErrTooManySeedsRECOSelection +
#    process.seqLogErrReco +
    process.seqEventHistoryReco +
    process.seqEventHistory +
    process.seqMultProd + 
    process.seqLogErrTooManySeedsSelection +
#    process.seqSeedMultInvestLogErrTooManySeeds +
    process.seqClusMultInvestLogErrTooManySeeds +
    process.seqSimpleTrackLogErrTooManySeeds +
#    process.seqSeedMultInvestLogErrTracking +
    process.seqClusMultInvestLogErrTracking +
    process.seqSimpleTrackLogErrTracking
    )

#

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('LogErrorTest_crosscorr_PFG.root')
                                   )

#select events which did not have errors in the past and have errors now

process.newerrors = cms.OutputModule("PoolOutputModule",
                                       fileName = cms.untracked.string("newerrors.root"),
                                       outputCommands = cms.untracked.vstring("keep *"),
                                       SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pNew*"))
	)

process.e = cms.EndPath(process.newerrors)
