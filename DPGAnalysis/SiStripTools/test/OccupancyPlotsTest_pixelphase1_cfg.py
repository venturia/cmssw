import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("OccupancyPlotsTest")

from Configuration.StandardSequences.Eras import eras

process = cms.Process('OccupancyPlotsTest',eras.Run2_2017)

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('fromRAW',
                  "0",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "=1 if from RAW")
options.register ('withTracks',
                  "0",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "=1 if analysis of on-track clusters has to be done")
options.register ('HLTprocess',
                  "HLT",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTProcess")
options.register ('triggerPath',
                  "HLT_*",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "list of HLT paths")
options.register ('trackCollection',
                  "generalTracks",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Track collection to use")
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

options.parseArguments()

#

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    fileMode = cms.untracked.string("FULLMERGE")
    )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.destinations.extend(cms.vstring("detids"))
process.MessageLogger.categories.extend(cms.vstring("GeometricDetBuilding","DuplicateHitFinder","BuildingTrackerDetId",
                                                    "SubDetectorGeometricDetType","BuildingGeomDetUnits","LookingForFirstStrip",
                                                    "BuildingSubDetTypeMap","SubDetTypeMapContent","NumberOfLayers","IsThereTest"))
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string("INFO")
#process.MessageLogger.cout.threshold = cms.untracked.string("WARNING")
#process.MessageLogger.debugModules = cms.untracked.vstring("*")
process.MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
    )
process.MessageLogger.detids = cms.untracked.PSet(
    default = cms.untracked.PSet(
        limit = cms.untracked.int32(0)
        ),
    BuildingTrackerDetId = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    GeometricDetBuilding = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    SubDetectorGeometricDetType = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    BuildingGeomDetUnits = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    LookingForFirstStrip = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    BuildingSubDetTypeMap = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    SubDetTypeMapContent = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    NumberOfLayers = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    IsThereTest = cms.untracked.PSet(
        limit = cms.untracked.int32(100000000)
        ),
    threshold = cms.untracked.string("DEBUG")
    )    
process.MessageLogger.cout.DuplicateHitFinder = cms.untracked.PSet(
    limit = cms.untracked.int32(100000000)
    )
process.MessageLogger.cout.FwkSummary = cms.untracked.PSet(
    limit = cms.untracked.int32(100000000)
    )
process.MessageLogger.cout.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000)
    )

process.MessageLogger.cerr.placeholder = cms.untracked.bool(False)
process.MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100000)
    )

#------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(options.inputFiles),
#                    skipBadFiles = cms.untracked.bool(True),
                    inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                    )

# HLT Selection ------------------------------------------------------------
process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.triggerResultsFilter.triggerConditions = cms.vstring(options.triggerPath)
process.triggerResultsFilter.hltResults = cms.InputTag( "TriggerResults", "", options.HLTprocess )
process.triggerResultsFilter.l1tResults = cms.InputTag( "" )
process.triggerResultsFilter.throw = cms.bool(False)

process.seqHLTSelection = cms.Sequence(process.triggerResultsFilter)
if options.triggerPath=="*":
    process.seqHLTSelection = cms.Sequence()


#--------------------------------------

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")



process.seqRECO = cms.Sequence()

if options.fromRAW == 1:
    process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
    process.load("Configuration.StandardSequences.L1Reco_cff")
    process.siPixelClusters = process.siPixelClustersPreSplitting.clone()
    process.seqRECO = cms.Sequence(process.scalersRawToDigi +
                                   process.siStripDigis + process.siStripZeroSuppression + process.siStripClusters
                                   + process.siPixelDigis + process.siPixelClusters )


#

process.froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                                      l1ABCCollection=cms.InputTag("scalersRawToDigi")
                                      )
process.load("DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1tsDB_cfi")
process.APVPhases.wantHistos = cms.untracked.bool(True)
process.load("DPGAnalysis.SiStripTools.eventtimedistribution_cfi")
process.eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")
process.load("DPGAnalysis.SiStripTools.l1TSDebugger_cfi")

process.seqEventHistoryReco = cms.Sequence(process.froml1abcHEs + process.APVPhases)
process.seqEventHistory = cms.Sequence(process.eventtimedistribution + process.l1TSDebugger)

#from DPGAnalysis.SiStripTools.occupancyplotsselections_cff import *
#from DPGAnalysis.SiStripTools.occupancyplotsselections_simplified_cff import *
from DPGAnalysis.SiStripTools.occupancyplotsselections_pixelphase1_cff import *
from DPGAnalysis.SiStripTools.occupancyplotsselections_pixelphase1_detailed_cff import *

process.ssclusmultprod = cms.EDProducer("SiStripClusterMultiplicityProducer",
                                        clusterdigiCollection = cms.InputTag("siStripClusters"),
                                        wantedSubDets = cms.VPSet(
        cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("TK")),
        cms.PSet(detSelection = cms.uint32(3),detLabel = cms.string("TIB")),
        cms.PSet(detSelection = cms.uint32(4),detLabel = cms.string("TID")),
        cms.PSet(detSelection = cms.uint32(5),detLabel = cms.string("TOB")),
        cms.PSet(detSelection = cms.uint32(6),detLabel = cms.string("TEC"))
        )
                                        )
process.ssclusmultprod.wantedSubDets.extend(OccupancyPlotsStripWantedSubDets)
process.ssclusmultprodontrack=process.ssclusmultprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

process.ssclusoccuprod = cms.EDProducer("SiStripClusterMultiplicityProducer",
                                        clusterdigiCollection = cms.InputTag("siStripClusters"),
                                        withClusterSize = cms.untracked.bool(True),
                                        wantedSubDets = cms.VPSet()
                                        )
process.ssclusoccuprod.wantedSubDets.extend(OccupancyPlotsStripWantedSubDets)
process.ssclusoccuprodontrack=process.ssclusoccuprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

process.spclusmultprod = cms.EDProducer("SiPixelClusterMultiplicityProducer",
                                        clusterdigiCollection = cms.InputTag("siPixelClusters"),
                                        wantedSubDets = cms.VPSet(
        cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"),selection=cms.untracked.vstring("0x1e000000-0x12000000","0x1e000000-0x14000000")),
        cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"),selection=cms.untracked.vstring("0x1e000000-0x12000000")),
        cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXLayer1"),selection=cms.untracked.vstring("0x1ef00000-0x12100000")),
        cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXLayer2"),selection=cms.untracked.vstring("0x1ef00000-0x12200000")),
        cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXLayer3"),selection=cms.untracked.vstring("0x1ef00000-0x12300000")),
        cms.PSet(detSelection = cms.uint32(14),detLabel = cms.string("BPIXLayer4"),selection=cms.untracked.vstring("0x1ef00000-0x12400000")),
        cms.PSet(detSelection = cms.uint32(21),detLabel = cms.string("BPIXLayer1Odd"),selection=cms.untracked.vstring("0x1ef01000-0x12101000")),
        cms.PSet(detSelection = cms.uint32(22),detLabel = cms.string("BPIXLayer1Even"),selection=cms.untracked.vstring("0x1ef01000-0x12100000")),
        cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"),selection=cms.untracked.vstring("0x1e000000-0x14000000"))
        )
                                        )
process.spclusmultprod.wantedSubDets.extend(OccupancyPlotsPixelWantedSubDets)
process.spclusmultprodontrack=process.spclusmultprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

#process.spclusoccuprod = cms.EDProducer("SiPixelClusterMultiplicityProducer",
#                                        clusterdigiCollection = cms.InputTag("siPixelClusters"),
#                                        withClusterSize = cms.untracked.bool(True),
#                                        wantedSubDets = cms.VPSet()
#                                        )
#process.spclusoccuprod.wantedSubDets.extend(OccupancyPlotsPixelWantedSubDets)

process.spclusoccuprod = process.spclusmultprod.clone(withClusterSize = cms.untracked.bool(True))
process.spclusoccuprodontrack=process.spclusoccuprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

process.spdetailedclusmultprod = process.spclusmultprod.clone(wantedSubDets=cms.VPSet())
process.spdetailedclusmultprod.wantedSubDets.extend(OccupancyPlotsBPIXOddEvenWantedSubDets)
process.spdetailedclusmultprod.wantedSubDets.extend(OccupancyPlotsBPIXLaddersWantedSubDets)

process.spdetailedclusmultprodontrack=process.spdetailedclusmultprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

process.spdetailedclusoccuprod = process.spdetailedclusmultprod.clone(withClusterSize = cms.untracked.bool(True))
process.spdetailedclusoccuprodontrack=process.spdetailedclusoccuprod.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))



process.load("DPGAnalysis.SiStripTools.sipixeldigimultiplicityprod_cfi")
process.spdigimultprod.wantedSubDets = process.spclusmultprod.wantedSubDets
process.spdetaileddigimultprod = process.spdigimultprod.clone(wantedSubDets = process.spdetailedclusmultprod.wantedSubDets)

process.seqMultProd = cms.Sequence(process.ssclusmultprod + process.ssclusoccuprod +
                                   process.spclusmultprod + process.spclusoccuprod +
                                   process.spdetailedclusmultprod + process.spdetailedclusoccuprod)

#process.spclusoccuprodxy = process.spclusoccuprod.clone()
#process.spclusoccuprodxy.wantedSubDets = OccupancyPlotsFPIXmDetailedWantedSubDets
#process.spclusoccuprodxy.wantedSubDets.extend(OccupancyPlotsFPIXpDetailedWantedSubDets)
#process.spclusoccuprodxyontrack=process.spclusoccuprodxy.clone(clusterdigiCollection = cms.InputTag("AlignmentTrackSelector"))

#process.seqMultProd = cms.Sequence(process.ssclusmultprod + process.ssclusoccuprod +
#                                   process.spclusmultprod + process.spclusoccuprod +
#                                   process.ssclusmultprodontrack + process.ssclusoccuprodontrack +
#                                   process.spclusmultprodontrack + process.spclusoccuprodontrack +
#                                   process.spclusmultprodxy + process.spclusoccuprodxy +
#                                   process.spclusmultprodxyontrack + process.spclusoccuprodxyontrack 
#                                   )

if options.withTracks == 1:
    process.seqMultProd = cms.Sequence(process.ssclusmultprod + process.ssclusoccuprod +
                                       process.spclusmultprod + process.spclusoccuprod +
                                       process.spdetailedclusmultprod + process.spdetailedclusoccuprod +
                                       process.ssclusmultprodontrack + process.ssclusoccuprodontrack +
                                       process.spclusmultprodontrack + process.spclusoccuprodontrack +
                                       process.spdetailedclusmultprodontrack + process.spdetailedclusoccuprodontrack )

if options.fromRAW == 1:
    process.seqMultProd.insert(0,process.spdigimultprod)
    process.seqMultProd.insert(0,process.spdetaileddigimultprod)

process.load("DPGAnalysis.SiStripTools.ssclusmultinvestigator_cfi")
process.ssclusmultinvestigator.multiplicityMap=cms.InputTag("ssclusmultprod")
process.ssclusmultinvestigator.scaleFactor=cms.untracked.int32(1)
process.load("DPGAnalysis.SiStripTools.spclusmultinvestigator_cfi")
process.spclusmultinvestigator.multiplicityMap=cms.InputTag("spclusmultprod")
process.spclusmultinvestigator.scaleFactor=cms.untracked.int32(10)
process.spclusmultinvestigator.wantedSubDets = cms.untracked.VPSet(    
                               cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"), binMax = cms.int32(400000)),
                               cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"), binMax = cms.int32(200000)),
                               cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"), binMax = cms.int32(200000)),
                               cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXLayer1"), binMax=cms.int32(100000)),
                               cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXLayer2"), binMax=cms.int32(50000)),
                               cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXLayer3"), binMax=cms.int32(50000)),
                               cms.PSet(detSelection = cms.uint32(14),detLabel = cms.string("BPIXLayer4"), binMax=cms.int32(50000)),
                               cms.PSet(detSelection = cms.uint32(21),detLabel = cms.string("BPIXLayer1Odd"), binMax=cms.int32(50000)),
                               cms.PSet(detSelection = cms.uint32(22),detLabel = cms.string("BPIXLayer1Even"), binMax=cms.int32(50000)),
                               cms.PSet(detSelection = cms.uint32(111),detLabel = cms.string("BPIXL1mod1"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(112),detLabel = cms.string("BPIXL1mod2"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(113),detLabel = cms.string("BPIXL1mod3"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(114),detLabel = cms.string("BPIXL1mod4"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(115),detLabel = cms.string("BPIXL1mod5"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(116),detLabel = cms.string("BPIXL1mod6"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(117),detLabel = cms.string("BPIXL1mod7"), binMax=cms.int32(10000)),
                               cms.PSet(detSelection = cms.uint32(118),detLabel = cms.string("BPIXL1mod8"), binMax=cms.int32(10000))
                              )

process.spclusoccuinvestigator = process.spclusmultinvestigator.clone(multiplicityMap = cms.InputTag("spclusoccuprod"),scaleFactor = cms.untracked.int32(1),hitName = cms.untracked.string("pixels"))
process.spdigimultinvestigator = process.spclusmultinvestigator.clone(multiplicityMap = cms.InputTag("spdigimultprod"),scaleFactor = cms.untracked.int32(1),hitName = cms.untracked.string("pixels"))

process.multiplicitycorr = cms.EDAnalyzer('MultiplicityCorrelator',
                            correlationConfigurations = cms.VPSet(    
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclusmultprod"), xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(150000), 
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(11), yDetLabel = cms.string("BPIXLayer1"), yBins = cms.uint32(1000), yMax=cms.double(10000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(20.),
             runHisto=cms.bool(False),runHistoBXProfile=cms.bool(False),runHistoBX=cms.bool(False),runHisto2D=cms.bool(False)),
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclusmultprod"), xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(150000), 
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(14), yDetLabel = cms.string("BPIXLayer4"), yBins = cms.uint32(1000), yMax=cms.double(5000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(40.),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(True)),
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclusmultprod"), xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(150000), 
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(21), yDetLabel = cms.string("BPIXLayer1Odd"), yBins = cms.uint32(1000), yMax=cms.double(5000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(40.),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(True)),
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclusmultprod"), xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(150000), 
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(22), yDetLabel = cms.string("BPIXLayer1Even"), yBins = cms.uint32(1000), yMax=cms.double(5000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(40.),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(True)),
    cms.PSet(xMultiplicityMap = cms.InputTag("spclusmultprod"), xDetSelection = cms.uint32(14), xDetLabel = cms.string("BPIXLayer4"), xBins = cms.uint32(1000), xMax=cms.double(5000),
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(11), yDetLabel = cms.string("BPIXLayer1"), yBins = cms.uint32(1000), yMax=cms.double(10000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(.5),
             runHisto=cms.bool(False),runHistoBXProfile=cms.bool(False),runHistoBX=cms.bool(False),runHisto2D=cms.bool(False)),
    cms.PSet(xMultiplicityMap = cms.InputTag("spclusmultprod"), xDetSelection = cms.uint32(14), xDetLabel = cms.string("BPIXLayer4"), xBins = cms.uint32(1000), xMax=cms.double(5000),
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(21), yDetLabel = cms.string("BPIXLayer1Odd"), yBins = cms.uint32(1000), yMax=cms.double(5000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(1),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(True)),
    cms.PSet(xMultiplicityMap = cms.InputTag("spclusmultprod"), xDetSelection = cms.uint32(14), xDetLabel = cms.string("BPIXLayer4"), xBins = cms.uint32(1000), xMax=cms.double(5000),
             yMultiplicityMap = cms.InputTag("spclusmultprod"), yDetSelection = cms.uint32(22), yDetLabel = cms.string("BPIXLayer1Even"), yBins = cms.uint32(1000), yMax=cms.double(5000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(1),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(True))
    )
                                  )



process.load("DPGAnalysis.SiStripTools.pixeldigiprofiler_cfi")
process.pixeldigiprofiler.selections.extend(cms.VPSet(
        cms.PSet(label=cms.string("BPIXLayer1mod1"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100004")),
        cms.PSet(label=cms.string("BPIXLayer1mod2"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100008")),
        cms.PSet(label=cms.string("BPIXLayer1mod3"),selection=cms.untracked.vstring("0x1ef00ffc-0x1210000c")),
        cms.PSet(label=cms.string("BPIXLayer1mod4"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100010")),
        cms.PSet(label=cms.string("BPIXLayer1mod5"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100014")),
        cms.PSet(label=cms.string("BPIXLayer1mod6"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100018")),
        cms.PSet(label=cms.string("BPIXLayer1mod7"),selection=cms.untracked.vstring("0x1ef00ffc-0x1210001c")),
        cms.PSet(label=cms.string("BPIXLayer1mod8"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100020"))
        )
)


process.load("DPGAnalysis.SiStripTools.occupancyplots_cfi")
process.occupancyplots.file = cms.untracked.FileInPath("SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt")
process.occupancyplots.wantedSubDets = cms.VPSet()
process.occupancyplots.wantedSubDets.extend(OccupancyPlotsPixelWantedSubDets)
process.occupancyplots.wantedSubDets.extend(OccupancyPlotsStripWantedSubDets)
process.occupancyplots.multiplicityMaps = cms.VInputTag(cms.InputTag("spclusmultprod"),cms.InputTag("ssclusmultprod"))
process.occupancyplots.occupancyMaps = cms.VInputTag(cms.InputTag("spclusoccuprod"),cms.InputTag("ssclusoccuprod"))

process.occupancyplotsontrack = process.occupancyplots.clone()
process.occupancyplotsontrack.wantedSubDets = cms.VPSet()
process.occupancyplotsontrack.wantedSubDets.extend(OccupancyPlotsPixelWantedSubDets)
process.occupancyplotsontrack.wantedSubDets.extend(OccupancyPlotsStripWantedSubDets)
process.occupancyplotsontrack.multiplicityMaps = cms.VInputTag(cms.InputTag("spclusmultprodontrack"),cms.InputTag("ssclusmultprodontrack"))
process.occupancyplotsontrack.occupancyMaps = cms.VInputTag(cms.InputTag("spclusoccuprodontrack"),cms.InputTag("ssclusoccuprodontrack"))

process.pixeldigioccupancyplots = process.occupancyplots.clone()
process.pixeldigioccupancyplots.wantedSubDets = process.spdigimultprod.wantedSubDets
process.pixeldigioccupancyplots.multiplicityMaps = cms.VInputTag(cms.InputTag("spdigimultprod"))
process.pixeldigioccupancyplots.occupancyMaps = cms.VInputTag(cms.InputTag("spdigimultprod"))

process.pixeldetailedoccupancyplots = process.occupancyplots.clone()
process.pixeldetailedoccupancyplots.wantedSubDets = process.spdetailedclusoccuprod.wantedSubDets
process.pixeldetailedoccupancyplots.multiplicityMaps = cms.VInputTag(cms.InputTag("spdetailedclusmultprod"))
process.pixeldetailedoccupancyplots.occupancyMaps = cms.VInputTag(cms.InputTag("spdetailedclusoccuprod"))

process.pixeldetaileddigioccupancyplots = process.occupancyplots.clone()
process.pixeldetaileddigioccupancyplots.wantedSubDets = process.spdetaileddigimultprod.wantedSubDets
process.pixeldetaileddigioccupancyplots.multiplicityMaps = cms.VInputTag(cms.InputTag("spdetaileddigimultprod"))
process.pixeldetaileddigioccupancyplots.occupancyMaps = cms.VInputTag(cms.InputTag("spdetaileddigimultprod"))


#process.pixeloccupancyxyplots = process.occupancyplots.clone()
#process.pixeloccupancyxyplots.wantedSubDets = process.spclusoccuprodxy.wantedSubDets
#process.pixeloccupancyxyplots.multiplicityMaps = cms.VInputTag(cms.InputTag("spclusmultprodxy"))
#process.pixeloccupancyxyplots.occupancyMaps = cms.VInputTag(cms.InputTag("spclusoccuprodxy"))

process.pixeldetailedoccupancyplotsontrack = process.occupancyplots.clone()
process.pixeldetailedoccupancyplotsontrack.wantedSubDets = process.spdetailedclusoccuprodontrack.wantedSubDets
process.pixeldetailedoccupancyplotsontrack.multiplicityMaps = cms.VInputTag(cms.InputTag("spdetailedclusmultprodontrack"))
process.pixeldetailedoccupancyplotsontrack.occupancyMaps = cms.VInputTag(cms.InputTag("spdetailedclusoccuprodontrack"))

#process.pixeloccupancyxyplotsontrack = process.pixeloccupancyxyplots.clone()
#process.pixeloccupancyxyplotsontrack.wantedSubDets = process.spclusoccuprodxyontrack.wantedSubDets
#process.pixeloccupancyxyplotsontrack.multiplicityMaps = cms.VInputTag(cms.InputTag("spclusmultprodxyontrack"))
#process.pixeloccupancyxyplotsontrack.occupancyMaps = cms.VInputTag(cms.InputTag("spclusoccuprodxyontrack"))

#process.load("TrackingPFG.Utilities.bxlumianalyzer_cfi")

process.goodVertices = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),  
   filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

process.load("Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi")
process.primaryvertexanalyzer.pvCollection=cms.InputTag("goodVertices")
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto=cms.untracked.bool(False)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHistoProfile=cms.untracked.bool(False)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)

process.load("DPGAnalysis.SiStripTools.trackcount_cfi")
process.trackcount.trackCollection = cms.InputTag(options.trackCollection)
process.load("Validation.RecoVertex.bspvanalyzer_cfi")
process.bspvanalyzer.pvCollection = cms.InputTag("goodVertices")

process.load("DPGAnalysis.SiStripTools.duplicaterechits_cfi")
process.duplicaterechits.trackCollection = cms.InputTag(options.trackCollection)

process.seqAnalyzers = cms.Sequence(
    process.seqEventHistory +
    process.spclusmultinvestigator + process.spclusoccuinvestigator + process.ssclusmultinvestigator +
    process.multiplicitycorr +
    process.occupancyplots +
    process.pixeldetailedoccupancyplots
    )

if options.withTracks == 1:
    process.seqAnalyzers = cms.Sequence(
        process.seqEventHistory +
        #process.bxlumianalyzer + 
        process.primaryvertexanalyzer +
        process.spclusmultinvestigator + process.spclusoccuinvestigator + process.ssclusmultinvestigator +
        process.multiplicitycorr +
        process.occupancyplots +     process.occupancyplotsontrack + 
        process.pixeldetailedoccupancyplots +     process.pixeldetailedoccupancyplotsontrack + 
        process.trackcount + process.bspvanalyzer
        # + process.duplicaterechits
) 

if options.fromRAW == 1:
    process.seqAnalyzers.insert(0,process.spdigimultinvestigator)
    process.seqAnalyzers.insert(0,process.pixeldigiprofiler)
    process.seqAnalyzers.insert(0,process.pixeldigioccupancyplots)
    process.seqAnalyzers.insert(0,process.pixeldetaileddigioccupancyplots)

#process.seqAnalyzers = cms.Sequence(
#    #process.bxlumianalyzer +
##    process.goodVertices + process.primaryvertexanalyzer +
#    process.occupancyplots +     process.occupancyplotsontrack + 
#    process.pixeloccupancyplots + process.pixeloccupancyplotsontrack + 
#    process.pixeloccupancyxyplots + process.pixeloccupancyxyplotsontrack)

#-------------------------------------------------------------------------------------------

process.load("Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi")

process.seqProducers = cms.Sequence(process.seqEventHistoryReco + process.seqMultProd)

if options.withTracks == 1:
    process.seqProducers = cms.Sequence(process.seqEventHistoryReco + 
                                        process.AlignmentTrackSelector + 
                                        process.goodVertices +
                                        process.seqMultProd)

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')


process.siStripQualityESProducer.ListOfRecordToMerge=cms.VPSet(
#    cms.PSet( record = cms.string("SiStripDetVOffRcd"),    tag    = cms.string("") ),
    cms.PSet( record = cms.string("SiStripDetCablingRcd"), tag    = cms.string("") ),
    cms.PSet( record = cms.string("RunInfoRcd"),           tag    = cms.string("") ),
    cms.PSet( record = cms.string("SiStripBadChannelRcd"), tag    = cms.string("") ),
    cms.PSet( record = cms.string("SiStripBadFiberRcd"),   tag    = cms.string("") ),
    cms.PSet( record = cms.string("SiStripBadModuleRcd"),  tag    = cms.string("") )
)

process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('OccupancyPlotsTest_'+options.tag+'.root')
                                   )

cloneProcessingSnippet(process,process.seqAnalyzers,"All")

process.p0 = cms.Path(
    process.seqRECO +
    process.seqProducers +
    process.seqAnalyzersAll +
    process.seqHLTSelection +
    process.seqAnalyzers
)

for label, trigger,negate in zip(options.triggerLabels,options.triggerPaths,options.negateFlags):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
   getattr(process,"triggerResultsFilter"+label).triggerConditions = cms.vstring(trigger)

   if negate == 1:
      tempmodule = getattr(process,"triggerResultsFilter"+label)
      getattr(process,"seqHLTSelection"+label).replace(getattr(process,"triggerResultsFilter"+label),~tempmodule)

   cloneProcessingSnippet(process,process.seqAnalyzers,label)
   
   setattr(process,"ptrigger"+label,cms.Path(process.seqRECO +
                                             process.seqProducers +
                                             getattr(process,"seqHLTSelection"+label) +
                                             getattr(process,"seqAnalyzers"+label)))



print process.dumpPython()
