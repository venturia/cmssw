import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("BXLumiAnalyzerTest")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('isMC',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if MC are analyzed")

options.parseArguments()

#

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    fileMode = cms.untracked.string("FULLMERGE")
    )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string("INFO")
process.MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
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

#----Remove too verbose PrimaryVertexProducer

process.MessageLogger.suppressInfo.append("pixelVerticesAdaptive")
process.MessageLogger.suppressInfo.append("pixelVerticesAdaptiveNoBS")

#----Remove too verbose BeamSpotOnlineProducer

process.MessageLogger.suppressInfo.append("testBeamSpot")
process.MessageLogger.suppressInfo.append("onlineBeamSpot")
process.MessageLogger.suppressWarning.append("testBeamSpot")
process.MessageLogger.suppressWarning.append("onlineBeamSpot")

#----Remove too verbose TrackRefitter

process.MessageLogger.suppressInfo.append("newTracksFromV0")
process.MessageLogger.suppressInfo.append("newTracksFromOtobV0")

#------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

#--------------------------------------

process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.hltHighLevel.HLTPaths = cms.vstring("HLT_ZeroBias*")
process.hltHighLevel.throw = cms.bool(False)

process.goodVertices = cms.EDFilter("VertexSelector",
                                    src = cms.InputTag("offlinePrimaryVertices"),
                                    #   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 15 && position.Rho <= 2"),  # old cut
                                    #   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 24 && position.Rho <= 2"),  
                                    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),  
                                    filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
                                    )



process.load("Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi")
process.primaryvertexanalyzer.pvCollection=cms.InputTag("goodVertices")
process.primaryvertexanalyzer.vHistogramMakerPSet.maxLSBeforeRebin = cms.uint32(800)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto=cms.untracked.bool(True)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHistoProfile=cms.untracked.bool(True)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(True)

process.load("TrackingPFG.Utilities.bxlumianalyzer_cfi")
process.bxlumianalyzer.runHisto = cms.bool(True)
process.bxlumianalyzer.maxLSBeforeRebin = cms.uint32(800)

process.p0 = cms.Path(
    process.hltHighLevel +
    process.goodVertices +
    process.bxlumianalyzer +
    process.primaryvertexanalyzer
    )

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('BXLumiAnalyzerTest.root')
                                   )

#print process.dumpPython()
