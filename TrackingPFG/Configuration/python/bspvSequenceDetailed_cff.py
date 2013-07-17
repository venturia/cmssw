import FWCore.ParameterSet.Config as cms

from Validation.RecoVertex.bspvanalyzer_cfi import *

bspvanalyzer.pvCollection = cms.InputTag("goodDisplacedVertices")
bspvanalyzer.bspvHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.2), xMax=cms.untracked.double(0.2),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.2), yMax=cms.untracked.double(0.2),
    nBinZ = cms.untracked.uint32(200), zMin=cms.untracked.double(-50.), zMax=cms.untracked.double(50.),
    nBinZProfile = cms.untracked.uint32(100), zMinProfile=cms.untracked.double(-50.), zMaxProfile=cms.untracked.double(50.)
    )
bspvanalyzer.bspvHistogramMakerPSet.runHistoBXProfile = cms.untracked.bool(False)
#bspvanalyzer.bspvHistogramMakerPSet.runHistoBX2D = cms.untracked.bool(True)

bspvnoslope = bspvanalyzer.clone()
bspvnoslope.bspvHistogramMakerPSet.useSlope = cms.bool(False)

firstonlybspvanalyzer = bspvanalyzer.clone(firstOnly = cms.untracked.bool(True))

onlinebspvanalyzer = bspvanalyzer.clone(bsCollection = cms.InputTag("onlineBeamSpot"))

onlinebspvnoslope = onlinebspvanalyzer.clone()
onlinebspvnoslope.bspvHistogramMakerPSet.useSlope = cms.bool(False)

testbspvanalyzer = bspvanalyzer.clone(bsCollection = cms.InputTag("testBeamSpot"))

testbspvnoslope = testbspvanalyzer.clone()
testbspvnoslope.bspvHistogramMakerPSet.useSlope = cms.bool(False)

bspvpixel = bspvanalyzer.clone(pvCollection = cms.InputTag("pixelVertices"))



seqBSPVAnalyzerDetailed = cms.Sequence(bspvanalyzer + bspvnoslope + firstonlybspvanalyzer
                                       + onlinebspvanalyzer + onlinebspvnoslope
                                       + testbspvanalyzer + testbspvnoslope
                                       + bspvpixel
                                       )
seqBSPVAnalyzerDetailedAOD = cms.Sequence(bspvanalyzer + bspvnoslope + firstonlybspvanalyzer
                                          + onlinebspvanalyzer + onlinebspvnoslope
                                          + testbspvanalyzer + testbspvnoslope
                                          )


