import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("HighVertexMultEventSkim")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
#options.globalTag = "DONOTEXIST::All"
options.register ('hltPath',
                  "*",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTPath")

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

# event selection
process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")

# event time history
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")

process.veryGoodVertices = cms.EDFilter("VertexSelector",
                                        src = cms.InputTag("offlinePrimaryVertices"),
                                        cut = cms.string("!isFake && ndof > 6 && abs(z) <= 36 && position.Rho <= 2"),
                                        filter = cms.bool(True)   # otherwise it won't filter the events, just produce an empty vertex collection.
                                )

process.highVertexMultiplicity = cms.EDFilter("VertexCountFilter",
                                              src = cms.InputTag("veryGoodVertices"),
                                              minNumber = cms.uint32(40),
                                              maxNumber = cms.uint32(200000)
                                              )

process.load("Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi")
process.primaryvertexanalyzer.pvCollection = cms.InputTag("veryGoodVertices")
process.primaryvertexanalyzer.vHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
    nBinZ = cms.untracked.uint32(300), zMin=cms.untracked.double(-30.), zMax=cms.untracked.double(30.)
    )
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto=cms.untracked.bool(False)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(False)

process.pvselectedanalyzer = process.primaryvertexanalyzer.clone()

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

#process.hltSelection.HLTPaths = cms.vstring("HLT_Jet140U*")
process.hltSelection.HLTPaths = cms.vstring(options.hltPath)

process.phighvtxmult = cms.Path(process.seqHLTSelection + process.seqBitSelection +
                                process.veryGoodVertices +
                                process.primaryvertexanalyzer +
                                process.highVertexMultiplicity +
                                process.seqEventHistoryReco +
                                process.seqEventHistory +
                                process.pvselectedanalyzer
                                )

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('HighVertexMultEventSkim.root')
                                   )

process.outhighvtxmultevent = cms.OutputModule("PoolOutputModule",
                                       fileName = cms.untracked.string("highvtxmultevents.root"),
                                       outputCommands = cms.untracked.vstring("keep *"),
                                       SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("phighvtxmult"))
	)


process.e = cms.EndPath(process.outhighvtxmultevent)


#-----------------------------------


