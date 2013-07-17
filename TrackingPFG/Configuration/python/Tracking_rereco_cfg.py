import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TrackingRereco")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('isMC',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if MC are analyzed")
options.register ('withTLR',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if TLR has to be applied")

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_noinfo_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

#--------------------------------------
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("TrackingPFG.Configuration.recoLogErrSequence_cff")

process.load("TrackingPFG.Configuration.multProdSequence_cff")
#process.load("TrackingPFG.Configuration.clusMultInvestSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestLogErrSequence_cff")

process.load("DPGAnalysis.SiStripTools.ssclusmultinvestigatorwithvtx_cfi")
process.ssclusmultinvestigatorwithvtx.runHisto=cms.untracked.bool(False)
process.ssclusmultinvestigatorwithvtx.scaleFactor=cms.untracked.int32(2)
process.ssclusmultinvestigatorwithvtx.vertexCollection = cms.InputTag("goodDisplacedVertices")
process.ssclusmultinvestigatorwithvtx.digiVtxCorrConfig.scaleFactor = cms.untracked.int32(2)

process.load("DPGAnalysis.SiStripTools.spclusmultinvestigatorwithvtx_cfi")
process.spclusmultinvestigatorwithvtx.runHisto=cms.untracked.bool(False)
process.spclusmultinvestigatorwithvtx.scaleFactor=cms.untracked.int32(10)
process.spclusmultinvestigatorwithvtx.vertexCollection = cms.InputTag("goodDisplacedVertices")
process.spclusmultinvestigatorwithvtx.digiVtxCorrConfig.scaleFactor = cms.untracked.int32(10)

process.load("TrackingPFG.Configuration.simpleTrackLogErrSequence_cff")

#process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
#process.froml1abcHEs.forceNoOffset=cms.untracked.bool(True)
#process.load("DPGAnalysis.SiStripTools.l1abcdebugger_cfi")

process.load("TrackingPFG.Configuration.goodVertexSelector_cfi")
process.goodVerticesRECO = process.goodVertices.clone(src = cms.InputTag("offlinePrimaryVertices","","RECO"))
process.goodDisplacedVerticesRECO = process.goodDisplacedVertices.clone(src = cms.InputTag("offlinePrimaryVertices","","RECO"))
process.load("TrackingPFG.Configuration.pixelVertexDivisiveStdCuts_cfi")
process.load("TrackingPFG.Configuration.pvSequence_cff")
process.pvgoodcollidingRECO = process.pvgoodcolliding.clone(pvCollection=cms.InputTag("goodVerticesRECO"))
process.pixelvertexanalyzerRECO= process.pixelvertexanalyzer.clone(pvCollection=cms.InputTag("pixelVertices","","RECO"))


#process.pickEvents = cms.EDFilter(
#    "PickEvents",
#    RunEventList = cms.untracked.string("listrunev")
#    )


process.load("TrackingPFG.Configuration.hpSelectionSequence_cff")
process.highPurityTracksRECO = process.highPurityTracks.clone(src=cms.InputTag("generalTracks","","RECO"))

#process.load("trackCount.TrackCount.trackcount_cfi")
#process.trackcount.trackCollection = cms.InputTag("generalTracks")
process.trackcountRECO = process.trackcount.clone(trackCollection = cms.InputTag("generalTracks","","RECO"))
#process.trackcounthp = process.trackcount.clone(trackCollection=cms.InputTag("highPurityTracks"))
process.trackcounthpRECO = process.trackcountRECO.clone(trackCollection=cms.InputTag("highPurityTracksRECO"))
process.pixeltrackcountRECO = process.pixeltrackcount.clone(trackCollection=cms.InputTag("pixelTracks","","RECO"))

process.load("TrackingPFG.Utilities.pixellessfilter_cfi")
process.pxllessFilter = process.pixellessfilter.clone(vtxCollection = cms.InputTag("goodDisplacedVertices"),newIter=cms.bool(True))
process.pxllesshpFilter = process.pixellessfilter.clone(vtxCollection = cms.InputTag("goodDisplacedVertices"),
                                                        trackCollection = cms.InputTag("highPurityTracks"),newIter=cms.bool(True))
process.pxllessCentralFilter = process.pxllessFilter.clone(vtxzMax=cms.double(12))
process.pxllesshpCentralFilter = process.pxllesshpFilter.clone(vtxzMax=cms.double(12))
process.pxllessFilterRECO = process.pxllessFilter.clone(trackCollection=cms.InputTag("generalTracks","","RECO"),
                                                        vtxCollection = cms.InputTag("goodDisplacedVerticesRECO"),newIter=cms.bool(False))
process.pxllesshpFilterRECO = process.pxllesshpFilter.clone(vtxCollection = cms.InputTag("goodDisplacedVerticesRECO"),
                                                            trackCollection = cms.InputTag("highPurityTracksRECO"),newIter=cms.bool(False))
process.pxllessCentralFilterRECO = process.pxllessFilterRECO.clone(vtxzMax=cms.double(12))
process.pxllesshpCentralFilterRECO = process.pxllesshpFilterRECO.clone(vtxzMax=cms.double(12))


process.load("tracking.TrackRecoMonitoring.seedmultiplicitymonitor_newtracking_cfi")
#process.load("tracking.TrackRecoMonitoring.seedmultiplicitymonitor_cfi")
#process.seedmultiplicitymonitor.seedCollections = cms.VPSet(
#   cms.PSet(src=cms.InputTag("newSeedFromTriplets")),
#   cms.PSet(src=cms.InputTag("newSeedFromPairs"),maxValue=cms.untracked.double(500000),nBins=cms.untracked.uint32(2000)),
#   cms.PSet(src=cms.InputTag("secTriplets")),
#   cms.PSet(src=cms.InputTag("thTripletsA")),
#   cms.PSet(src=cms.InputTag("thTripletsB")),
#   cms.PSet(src=cms.InputTag("thTriplets"),maxValue=cms.untracked.double(200000)),
#   cms.PSet(src=cms.InputTag("fourthPLSeeds")),
#   cms.PSet(src=cms.InputTag("fifthSeeds"))
#   )
process.seedmultiplicitymonitor.multiplicityCorrelations = cms.VPSet(
    cms.PSet(multiplicityMap = cms.InputTag("ssclustermultprod"),
             detSelection = cms.uint32(0), detLabel = cms.string("TK"), nBins = cms.uint32(1000), nBinsEta = cms.uint32(100), maxValue=cms.double(100000)
             ),
    cms.PSet(multiplicityMap = cms.InputTag("spclustermultprod"),
             detSelection = cms.uint32(0), detLabel = cms.string("Pixel"), nBins = cms.uint32(1000),  nBinsEta = cms.uint32(100), maxValue=cms.double(20000)
             )
    )

process.load("CommonTools.RecoAlgos.recoTrackRefSelector_cfi")
process.initialtrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter0"),ptMin=cms.double(0.))
process.lowpttripletstrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter1"),ptMin=cms.double(0.))
process.pixelpairstrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter2"),ptMin=cms.double(0.))
process.detachedtripletstrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter3"),ptMin=cms.double(0.))
process.mixedtripletstrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter4"),ptMin=cms.double(0.))
process.pixellesstrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter5"),ptMin=cms.double(0.))
process.tobtectrackrefs = process.recoTrackRefSelector.clone(algorithm=cms.vstring("iter6"),ptMin=cms.double(0.))

process.finalseedmultmonitor = process.seedmultiplicitymonitor.clone(
   seedCollections =
   cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks")),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter0"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("initialtrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter1"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("lowpttripletstrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter2"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("pixelpairstrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter3"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("detachedtripletstrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter4"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("mixedtripletstrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter5"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("pixellesstrackrefs"))),
             cms.PSet(src=cms.InputTag("generalTracks"),
                      trackFilter=cms.PSet(suffix=cms.string("iter6"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("tobtectrackrefs")))))


process.finalinitialseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter0"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("initialtrackrefs")))))

process.finallowpttripletsseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter1"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("lowpttripletstrackrefs")))))

process.finalpixelpairsseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter2"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("pixelpairstrackrefs")))))

process.finaldetachedtripletsseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter3"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("detachedtripletstrackrefs")))))

process.finalmixedtripletsseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter4"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("mixedtripletstrackrefs")))))

process.finalpixellessseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter5"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("pixellesstrackrefs")))))

process.finaltobtecseedmultmonitor = process.seedmultiplicitymonitor.clone(seedCollections = cms.VPSet(cms.PSet(src=cms.InputTag("generalTracks"),trackFilter=cms.PSet(suffix=cms.string("iter6"),trkCollection=cms.InputTag("generalTracks"),selRefTrkCollection=cms.InputTag("tobtectrackrefs")))))


process.load("TrackingPFG.Configuration.mcVerticesLogErrSequence_cff")
process.load("Validation.RecoVertex.mcvsrecoverticesanalyzer_cfi")

process.mcvsrecogoodverticesanalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("goodVertices"))
process.mcvsrecogoodverticesanalyzerRECO = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("goodVerticesRECO"))
process.mcvsrecopixelverticesanalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVertices"))
process.mcvsrecopixelverticesanalyzerRECO = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVertices","","RECO"))
process.mcvsrecopixelverticesHLTLikeanalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveHLT"))

process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSequence_cff")

process.seqPTooManyClusters = cms.Sequence(
                      process.seqLogErrTooManyClustersSelection +
                      process.seqLogErrorTooManyClusters 
                      )

process.seqPTooManySeeds = cms.Sequence(
                      process.seqLogErrTooManySeedsSelection +
                      process.seqLogErrorTooManySeeds 
                      )

process.seqPTooManyTriplets = cms.Sequence(
                      process.seqLogErrTooManyTripletsSelection +
                      process.seqLogErrorTooManyTriplets 
                      )

if options.isMC == 1:
   process.seqPTooManyClusters += process.seqMCVerticesLogErrTooManyClusters
   process.seqPTooManySeeds += process.seqMCVerticesLogErrTooManySeeds
   process.seqPTooManyTriplets += process.seqMCVerticesLogErrTooManyTriplets



################################################

#if options.withTLR == 1:
#   process.pixelTracks.OrderedHitsFactoryPSet.GeneratorPSet.SeedComparitorPSet.ComponentName = 'LowPtClusterShapeSeedComparitor'
   
#process.newSeedFromTriplets.SeedComparitorPSet.ComponentName = 'none'
#process.secTriplets.SeedComparitorPSet.ComponentName = 'none'

#process.newSeedFromTriplets.OrderedHitsFactoryPSet.GeneratorPSet.SeedComparitorPSet.ComponentName = 'LowPtClusterShapeSeedComparitor'
#process.secTriplets.OrderedHitsFactoryPSet.GeneratorPSet.SeedComparitorPSet.ComponentName = 'LowPtClusterShapeSeedComparitor'

#new threeholds

#process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=20000
#process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfPixelClusters=20000
#process.secTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=20000
#process.thTripletsA.ClusterCheckPSet.MaxNumberOfPixelClusters = 20000
#process.thTripletsB.ClusterCheckPSet.MaxNumberOfPixelClusters = 20000
#process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfPixelClusters=20000
#process.fifthSeeds.ClusterCheckPSet.MaxNumberOfPixelClusters = 20000

#process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfCosmicClusters=150000
#process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfCosmicClusters=150000
#process.secTriplets.ClusterCheckPSet.MaxNumberOfCosmicClusters=150000
#process.thTripletsA.ClusterCheckPSet.MaxNumberOfCosmicClusters = 150000
#process.thTripletsB.ClusterCheckPSet.MaxNumberOfCosmicClusters =150000
#process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters=150000
#process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters =150000

#process.newTrackCandidateMaker.maxNSeeds = cms.uint32(500000)
#process.stepOneTrackCandidateMaker.maxNSeeds = cms.uint32(500000)
#process.secTrackCandidates.maxNSeeds = cms.uint32(500000)
#process.thTrackCandidates.maxNSeeds = cms.uint32(500000)
#process.fourthTrackCandidates.maxNSeeds = cms.uint32(500000)
#process.fifthTrackCandidates.maxNSeeds = cms.uint32(500000)


#TLR

#if options.isMC == 1:
#   from Configuration.GlobalRuns.reco_TLR_42X import customisePPData
#   process=customisePPData(process)

#####################################################################################

process.seqProducers = cms.Sequence(process.seqLogErrReco
                                    + process.seqMultProd
#                                    + process.seqEventHistoryReco
                                    + process.pixelVerticesDivisiveHLT
                                    + process.goodVertices + process.goodVerticesRECO
                                    + process.goodDisplacedVertices + process.goodDisplacedVerticesRECO
                                    + process.highPurityTracks + process.highPurityTracksRECO
                                    + process.initialtrackrefs
                                    + process.lowpttripletstrackrefs
                                    + process.pixelpairstrackrefs
                                    + process.detachedtripletstrackrefs
                                    + process.mixedtripletstrackrefs
                                    + process.pixellesstrackrefs
                                    + process.tobtectrackrefs
)

process.p0 = cms.Path(
    #    process.pickEvents 
    #    + process.siPixelDigis + process.siStripDigis + process.scalersRawToDigi
    process.seqProducers
    + process.trackcount + process.trackcountRECO
    + process.pxllessFilter + process.pxllessFilterRECO 
    + process.pxllessCentralFilter + process.pxllessCentralFilterRECO 
    + process.trackcounthp + process.trackcounthpRECO
    + process.pxllesshpFilter + process.pxllesshpFilterRECO 
    + process.pxllesshpCentralFilter + process.pxllesshpCentralFilterRECO 
    + process.pixeltrackcount + process.pixeltrackcountRECO
    + process.seedmultiplicitymonitor
    + process.finalseedmultmonitor
    + process.finalinitialseedmultmonitor
    + process.finallowpttripletsseedmultmonitor
    + process.finalpixelpairsseedmultmonitor
    + process.finaldetachedtripletsseedmultmonitor
    + process.finalmixedtripletsseedmultmonitor
    + process.finalpixellessseedmultmonitor
    + process.finaltobtecseedmultmonitor
    + process.multiplicitycorr + process.ssclusmultinvestigatorwithvtx + process.spclusmultinvestigatorwithvtx
    + process.pvgoodcolliding + process.pvgoodcollidingRECO
    + process.pixelvertexanalyzer + process.pixelvertexanalyzerRECO
    + process.pixelvertexHLTLike
    + process.mcvsrecogoodverticesanalyzer + process.mcvsrecogoodverticesanalyzerRECO
    + process.mcvsrecopixelverticesanalyzer + process.mcvsrecopixelverticesanalyzerRECO
    + process.mcvsrecopixelverticesHLTLikeanalyzer 
    + process.mcverticesanalyzer
    )

process.pTooManyClusters = cms.Path(process.seqProducers + process.seqPTooManyClusters +
                                    process.seqClusMultInvestLogErrTooManyClusters + 
                                    process.seqSimpleTrackLogErrTooManyClusters )
process.pTooManyseeds = cms.Path(process.seqProducers + process.seqPTooManySeeds +
                                 process.seqClusMultInvestLogErrTooManySeeds + 
                                 process.seqSimpleTrackLogErrTooManySeeds )
process.pTooManytriplets = cms.Path(process.seqProducers + process.seqPTooManyTriplets +
                                    process.seqClusMultInvestLogErrTooManyTriplets + 
                                    process.seqSimpleTrackLogErrTooManyTriplets )


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

#process.GlobalTag.toGet = cms.VPSet(
#   cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
##            tag = cms.string("SiPixelTemplateDBObject_38T_v3_mc"),
#            tag = cms.string("SiPixelTemplateDBObject38Tv2_mc"),
#            connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PIXEL")
#            )
#   )


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_rereco.root')
#                                   fileName = cms.string('TrackerLocal_rereco.root')
                                   )

#print process.dumpPython()
