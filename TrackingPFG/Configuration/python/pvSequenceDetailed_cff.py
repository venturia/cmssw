import FWCore.ParameterSet.Config as cms

from Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi import *

primaryvertexanalyzer.vHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
    nBinZ = cms.untracked.uint32(500), zMin=cms.untracked.double(-50.), zMax=cms.untracked.double(50.)
    )

pvanalyzer = primaryvertexanalyzer.clone()
pvanalyzerWithBS = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("offlinePrimaryVerticesWithBS"),
                                               bsConstrained = cms.bool(True))
pvanalyzerDA = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("offlinePrimaryVerticesDA"))
pvanalyzerDAWithBS = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("offlinePrimaryVerticesDAWithBS"),
                                                 bsConstrained = cms.bool(True))

pvgood = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("goodDisplacedVertices"))
pvgoodWithBS = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("goodDisplacedVerticesWithBS"),
                                           bsConstrained = cms.bool(True))
pvgoodDA = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("goodDisplacedVerticesDA"))
pvgoodDAWithBS = primaryvertexanalyzer.clone(pvCollection=cms.InputTag("goodDisplacedVerticesDAWithBS"),
                                             bsConstrained = cms.bool(True))

seqPVAnalyzerDetailed = cms.Sequence(pvanalyzer + pvanalyzerWithBS + pvanalyzerDA + pvanalyzerDAWithBS +
                                     pvgood + pvgoodWithBS + pvgoodDA + pvgoodDAWithBS )


pvgoodbspv = pvgood.clone()
pvgoodbspv.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)
pvgoodfirstonly = pvgoodbspv.clone(firstOnly = cms.untracked.bool(True))
pixelvertexanalyzer = pvgoodbspv.clone(pvCollection = cms.InputTag("pixelVertices"))

seqPVAnalyzerBSPVDetailed = cms.Sequence(pvgoodbspv + pvgoodfirstonly + pixelvertexanalyzer)

seqPVAnalyzerBSPVDetailedAOD = cms.Sequence(pvgoodbspv + pvgoodfirstonly)


