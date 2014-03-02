import FWCore.ParameterSet.Config as cms

from Validation.RecoVertex.beamspotanalyzer_cfi import *

beamspotanalyzer.bsHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
    nBinZ = cms.untracked.uint32(200), zMin=cms.untracked.double(-20.), zMax=cms.untracked.double(20.),
    nBinSigmaZ = cms.untracked.uint32(200), sigmaZMin=cms.untracked.double(0.), sigmaZMax=cms.untracked.double(15.)
    )

onlinebsanalyzer = beamspotanalyzer.clone(bsCollection = cms.InputTag("onlineBeamSpot"))

testbsanalyzer = beamspotanalyzer.clone(bsCollection = cms.InputTag("testBeamSpot"))

seqBSAnalyzer = cms.Sequence(beamspotanalyzer + onlinebsanalyzer
#                             + testbsanalyzer
                             )


seqBSAnalyzerDetailed = cms.Sequence(beamspotanalyzer)

seqBSAnalyzerBSPVDetailed = cms.Sequence(beamspotanalyzer + onlinebsanalyzer + testbsanalyzer )
