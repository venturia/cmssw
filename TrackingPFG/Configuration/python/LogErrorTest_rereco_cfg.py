import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("LogErrorTestRereco")

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

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_noinfo_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")

#--------------------------------------
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestLogErrSequence_cff")
process.load("TrackingPFG.Configuration.simpleTrackLogErrSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")
process.load("TrackingPFG.Configuration.recoLogErrSequence_cff")

## offlineBeamSpot from scalers

#from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import *
#process.offlineBeamSpot = onlineBeamSpotProducer.clone()



################################################
##### TLR
################################################

    ## TRACKING:
    ## Skip events with HV off
process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfCosmicClusters=20000
process.secTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 20000
process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters=20000
process.thTripletsA.ClusterCheckPSet.MaxNumberOfPixelClusters = 5000
process.thTripletsB.ClusterCheckPSet.MaxNumberOfPixelClusters = 5000

###### FIXES TRIPLETS FOR LARGE BS DISPLACEMENT ######

### prevent bias in pixel vertex
process.pixelVertices.useBeamConstraint = False

### pixelTracks
#---- new parameters ----
process.pixelTracks.RegionFactoryPSet.RegionPSet.nSigmaZ  = 4.06
process.pixelTracks.RegionFactoryPSet.RegionPSet.originHalfLength = cms.double(40.6)

### 0th step of iterative tracking
#---- new parameters ----
process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ   = cms.double(4.06)  
process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.originHalfLength = 40.6

### 2nd step of iterative tracking
#---- new parameters ----
process.secTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.47)  
process.secTriplets.RegionFactoryPSet.RegionPSet.originHalfLength = 44.7


################################################
 
process.p0 = cms.Path(
                      process.seqLogErrReco +
                      process.seqEventHistoryReco +
                      process.seqEventHistory +
                      process.seqMultProd + 
                      process.seqClusMultInvestLogErr +
                      process.seqSimpleTrackLogErr
                      )

process.pTooManyClusters = cms.Path(
                      process.seqLogErrReco +
                      process.seqEventHistoryReco +
                      process.seqEventHistory +
                      process.seqMultProd + 
                      process.seqLogErrTooManyClustersSelection +
                      process.seqClusMultInvestLogErrTooManyClusters +
                      process.seqSimpleTrackLogErrTooManyClusters +
                      process.seqClusMultInvestLogErrTracking +
                      process.seqSimpleTrackLogErrTracking
                      )

process.pTooManySeeds = cms.Path(
                      process.seqLogErrReco +
                      process.seqEventHistoryReco +
                      process.seqEventHistory +
                      process.seqMultProd + 
                      process.seqLogErrTooManySeedsSelection +
                      process.seqClusMultInvestLogErrTooManySeeds +
                      process.seqSimpleTrackLogErrTooManySeeds +
                      process.seqClusMultInvestLogErrTracking +
                      process.seqSimpleTrackLogErrTracking
                      )

process.pTooManyTriplets = cms.Path(
                      process.seqLogErrReco +
                      process.seqEventHistoryReco +
                      process.seqEventHistory +
                      process.seqMultProd + 
                      process.seqLogErrTooManyTripletsSelection +
                      process.seqClusMultInvestLogErrTooManyTriplets +
                      process.seqSimpleTrackLogErrTooManyTriplets +
                      process.seqClusMultInvestLogErrTracking +
                      process.seqSimpleTrackLogErrTracking
                      )

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('LogErrorTest_rereco_PFG.root')
                                   )

