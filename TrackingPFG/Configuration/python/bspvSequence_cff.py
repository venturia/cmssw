import FWCore.ParameterSet.Config as cms

from Validation.RecoVertex.bspvanalyzer_cfi import *

bspvanalyzer.pvCollection = cms.InputTag("oneGoodVertexFilter")
bspvanalyzer.bspvHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.2), xMax=cms.untracked.double(0.2),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.2), yMax=cms.untracked.double(0.2),
    nBinZ = cms.untracked.uint32(200), zMin=cms.untracked.double(-30.), zMax=cms.untracked.double(30.),
    nBinZProfile = cms.untracked.uint32(60), zMinProfile=cms.untracked.double(-30.), zMaxProfile=cms.untracked.double(30.)
    )
bspvanalyzer.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)
#bspvanalyzer.bspvHistogramMakerPSet.runHistoBX2D = cms.untracked.bool(True)

bspvnoslope = bspvanalyzer.clone()
bspvnoslope.bspvHistogramMakerPSet.useSlope = cms.bool(False)
bspvnoslope.bspvHistogramMakerPSet.runHistoProfile = cms.untracked.bool(False)
bspvnoslope.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)

firstonlybspvanalyzer = bspvanalyzer.clone(firstOnly = cms.untracked.bool(True))
firstonlybspvanalyzer.bspvHistogramMakerPSet.runHistoProfile = cms.untracked.bool(False)
firstonlybspvanalyzer.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)
#firstonlybspvanalyzer.bspvHistogramMakerPSet.runHistoBX2D = cms.untracked.bool(False)

bspvallgood = bspvanalyzer.clone(pvCollection = cms.InputTag("goodDisplacedVertices"))
bspvallgood.bspvHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.2), xMax=cms.untracked.double(0.2),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.2), yMax=cms.untracked.double(0.2),
    nBinZ = cms.untracked.uint32(200), zMin=cms.untracked.double(-50.), zMax=cms.untracked.double(50.),
    nBinZProfile = cms.untracked.uint32(100), zMinProfile=cms.untracked.double(-50.), zMaxProfile=cms.untracked.double(50.)
    )
bspvallgood.bspvHistogramMakerPSet.runHistoProfile = cms.untracked.bool(False)
bspvallgood.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)

bspvpixel = bspvanalyzer.clone(pvCollection = cms.InputTag("pixelVertices"))
bspvpixel.bspvHistogramMakerPSet.runHistoProfile = cms.untracked.bool(False)
bspvpixel.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)

onlinebspvanalyzer = bspvanalyzer.clone(bsCollection = cms.InputTag("onlineBeamSpot"))
onlinebspvanalyzer.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)
#onlinebspvanalyzer.bspvHistogramMakerPSet.runHistoBX2D = cms.untracked.bool(False)

testbspvanalyzer = bspvanalyzer.clone(bsCollection = cms.InputTag("testBeamSpot"))
testbspvanalyzer.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)
#testbspvanalyzer.bspvHistogramMakerPSet.runHistoBX2D = cms.untracked.bool(False)

seqBSPVAnalyzer = cms.Sequence(bspvanalyzer + bspvnoslope + firstonlybspvanalyzer + onlinebspvanalyzer
#                               + testbspvanalyzer
                               + bspvpixel
                               )
seqBSPVAnalyzerAOD = cms.Sequence(bspvanalyzer + bspvnoslope + firstonlybspvanalyzer + onlinebspvanalyzer
#                               + testbspvanalyzer
                               )

seqBSPVAnalyzerOnlyNoScraping = cms.Sequence(bspvallgood)

