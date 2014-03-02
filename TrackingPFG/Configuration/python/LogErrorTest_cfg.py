import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TrackingPFG")

options = VarParsing.VarParsing("analysis")

options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")
options.register ('isMC',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if MC are analyzed")

options.parseArguments()



process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

#--------------------------------------
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestLogErrSequence_cff")
process.load("TrackingPFG.Configuration.simpleTrackLogErrSequence_cff")
process.load("TrackingPFG.Configuration.mcVerticesLogErrSequence_cff")
process.load("TrackingPFG.Configuration.bxLumiLogErrSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSequence_cff")

process.seqProducers = cms.Sequence(process.seqEventHistoryReco + process.seqMultProd)
process.seqProducersAOD = cms.Sequence(process.seqEventHistoryReco)


process.seqP0 = cms.Sequence(
                             process.seqLogError +
                             process.seqBXLumiLogErr
                             )

process.seqPAnyError = cms.Sequence(
                                   process.seqLogErrAnyErrorSelection +
                                   process.seqEventHistoryLogErrAnyError +
                                   process.seqLogErrorAnyError +
                                   process.seqBXLumiLogErrAnyError
                                   
                                   )


process.seqPCosmicRegional = cms.Sequence(
                      process.seqLogErrCosmicRegionalSelection +
                      process.seqEventHistoryLogErrCosmicRegional
                      )

process.seqPTooManyClusters = cms.Sequence(
                      process.seqLogErrTooManyClustersSelection +
                      process.seqEventHistoryLogErrTooManyClusters +
                      process.seqLogErrorTooManyClusters +
                      process.seqBXLumiLogErrTooManyClusters +
                      process.seqEventHistoryLogErrTracking +
                      process.seqLogErrorTracking +
                      process.seqBXLumiLogErrTracking
                      )

process.seqPTooManySeeds = cms.Sequence(
                      process.seqLogErrTooManySeedsSelection +
                      process.seqEventHistoryLogErrTooManySeeds +
                      process.seqLogErrorTooManySeeds +
                      process.seqBXLumiLogErrTooManySeeds +
                      process.seqEventHistoryLogErrTracking +
                      process.seqLogErrorTracking +
                      process.seqBXLumiLogErrTracking 
                      )

process.seqPTooManyTriplets = cms.Sequence(
                      process.seqLogErrTooManyTripletsSelection +
                      process.seqEventHistoryLogErrTooManyTriplets +
                      process.seqLogErrorTooManyTriplets +
                      process.seqBXLumiLogErrTooManyTriplets +
                      process.seqEventHistoryLogErrTracking +
                      process.seqLogErrorTracking +
                      process.seqBXLumiLogErrTracking 
                      )

if options.isMC == 1:
   process.seqP0 += process.seqMCVerticesLogErr
   process.seqPAnyError += process.seqMCVerticesLogErrAnyError
   process.seqPTooManyClusters += process.seqMCVerticesLogErrTooManyClusters
   process.seqPTooManyClusters += process.seqMCVerticesLogErrTracking
   process.seqPTooManySeeds += process.seqMCVerticesLogErrTooManySeeds
   process.seqPTooManySeeds += process.seqMCVerticesLogErrTracking
   process.seqPTooManyTriplets += process.seqMCVerticesLogErrTooManyTriplets
   process.seqPTooManyTriplets += process.seqMCVerticesLogErrTracking

if options.isAOD == 0:
   process.p0 = cms.Path(process.seqProducers + process.seqP0 +
                         process.seqClusMultInvestLogErr )
   process.pAnyError = cms.Path(process.seqProducers + process.seqPAnyError +
                                process.seqClusMultInvestLogErrAnyError + process.seqSimpleTrackLogErrAnyError)
   process.pCosmicRegional =cms.Path(process.seqProducers + process.seqPCosmicRegional)
   process.pTooManyClusters = cms.Path(process.seqProducers + process.seqPTooManyClusters +
                                       process.seqClusMultInvestLogErrTooManyClusters + process.seqClusMultInvestLogErrTracking +
                                       process.seqSimpleTrackLogErrTooManyClusters + process.seqSimpleTrackLogErrTracking)
   process.pTooManyseeds = cms.Path(process.seqProducers + process.seqPTooManySeeds +
                                    process.seqClusMultInvestLogErrTooManySeeds + process.seqClusMultInvestLogErrTracking +
                                    process.seqSimpleTrackLogErrTooManySeeds + process.seqSimpleTrackLogErrTracking)
   process.pTooManytriplets = cms.Path(process.seqProducers + process.seqPTooManyTriplets +
                                    process.seqClusMultInvestLogErrTooManyTriplets + process.seqClusMultInvestLogErrTracking +
                                    process.seqSimpleTrackLogErrTooManyTriplets + process.seqSimpleTrackLogErrTracking)
else:
   process.p0 = cms.Path(process.seqProducersAOD + process.seqP0)
   process.pAnyError = cms.Path(process.seqProducersAOD + process.seqPAnyError + process.seqSimpleTrackLogErrAnyErrorAOD)
   process.pCosmicRegional =cms.Path(process.seqProducersAOD + process.seqPCosmicRegional)
   process.pTooManyClusters = cms.Path(process.seqProducersAOD + process.seqPTooManyClusters +
                                       process.seqSimpleTrackLogErrTooManyClustersAOD + process.seqSimpleTrackLogErrTrackingAOD)
   process.pTooManyseeds = cms.Path(process.seqProducersAOD + process.seqPTooManySeeds +
                                    process.seqSimpleTrackLogErrTooManySeedsAOD + process.seqSimpleTrackLogErrTrackingAOD)
   process.pTooManytriplets = cms.Path(process.seqProducersAOD + process.seqPTooManyTriplets +
                                    process.seqSimpleTrackLogErrTooManyTripletsAOD + process.seqSimpleTrackLogErrTrackingAOD)



#----GlobalTag ------------------------

#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "GR10_E_V5::All"

#

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('LogErrorTest_PFG.root')
                                   )

process.outlogerrevent = cms.OutputModule("PoolOutputModule",
                                          fileName = cms.untracked.string("logerrevents.root"),
                                          outputCommands = cms.untracked.vstring("keep *"),
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring( "pTooManyClusters")))
process.e = cms.EndPath(process.outlogerrevent)
