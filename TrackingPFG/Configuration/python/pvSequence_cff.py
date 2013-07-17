import FWCore.ParameterSet.Config as cms

from Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi import *

pvanalyzertobecloned = primaryvertexanalyzer.clone()
pvanalyzertobecloned.vHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
    nBinZ = cms.untracked.uint32(300), zMin=cms.untracked.double(-30.), zMax=cms.untracked.double(30.)
    )


# good only, no ZS, one with and one without prescale factor

pvgoodcolliding = pvanalyzertobecloned.clone(pvCollection=cms.InputTag("goodVertices"))
pvgoodcolliding.vHistogramMakerPSet.runHistoBXProfile2D=cms.untracked.bool(True)
#pvgoodcolliding.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(True)
pvgoodonlynoscraping = pvgoodcolliding.clone()
pvgoodonlynoscraping.vHistogramMakerPSet.runHisto=cms.untracked.bool(False)
pvgoodonlynoscraping.vHistogramMakerPSet.runHisto2D=cms.untracked.bool(False)

#pvgoodDAcolliding = pvgoodcolliding.clone(pvCollection=cms.InputTag("goodVerticesDA"))

# all vertices, no ZS

primaryvertexanalyzer.vHistogramMakerPSet.histoParameters = cms.untracked.PSet(
    nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
    nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
    nBinZ = cms.untracked.uint32(300), zMin=cms.untracked.double(-50.), zMax=cms.untracked.double(50.)
    )
primaryvertexanalyzer.vHistogramMakerPSet.runHistoProfile=cms.untracked.bool(False)
primaryvertexanalyzer.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)

# ZS

pvfirstonlycolliding = pvanalyzertobecloned.clone(pvCollection=cms.InputTag("goodVertices"),firstOnly=cms.untracked.bool(True))
pvfirstonlycolliding.vHistogramMakerPSet.runHistoProfile=cms.untracked.bool(False)
pvfirstonlycolliding.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)

pvnoncolliding = pvanalyzertobecloned.clone()
pvnoncolliding.vHistogramMakerPSet.runHistoProfile=cms.untracked.bool(False)
pvnoncolliding.vHistogramMakerPSet.runHistoBXProfile=cms.untracked.bool(False)
pvnoncollidingplus = pvnoncolliding.clone()
pvnoncollidingminus = pvnoncolliding.clone()

pvgoodnoncolliding = pvnoncolliding.clone(pvCollection=cms.InputTag("goodDisplacedVertices"))
pvgoodnoncollidingplus = pvgoodnoncolliding.clone()
pvgoodnoncollidingminus = pvgoodnoncolliding.clone()


pixelvertexanalyzer = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVertices"))
#pixelvertexFTSLike = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("ftsLikePixelVertexFilter"))
pixelvertexHLTLike = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveHLT"))
#pixelvertexadaptiveanalyzer = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVerticesAdaptive"))
#pixelvertexadaptiveanalyzer.vHistogramMakerPSet.runHisto=cms.untracked.bool(False)
#pixelvertexadaptivenobsanalyzer = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVerticesAdaptiveNoBS"),runHisto=cms.untracked.bool(False))
#pixelvertexdivisivestdcutsanalyzer = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveStdCuts"),runHisto=cms.untracked.bool(False))
#pixelvertexdivisivenewcutsanalyzer = pvanalyzertobecloned.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveNewCuts"),runHisto=cms.untracked.bool(False))


seqPVAnalyzer = cms.Sequence(pvfirstonlycolliding 
#                             pixelvertexFTSLike #+ 
#                             pixelvertexadaptiveanalyzer #+
#                             pixelvertexadaptivenobsanalyzer +
#                             pixelvertexdivisivestdcutsanalyzer +
#                             pixelvertexdivisivenewcutsanalyzer
                             )
seqPVAnalyzerAOD = cms.Sequence(pvfirstonlycolliding #+
#                             pixelvertexanalyzer +
#                             pixelvertexFTSLike +
#                             pixelvertexadaptiveanalyzer +
#                             pixelvertexadaptivenobsanalyzer +
#                             pixelvertexdivisivestdcutsanalyzer +
#                             pixelvertexdivisivenewcutsanalyzer
                             )
seqPVAnalyzerOnlyNoScraping = cms.Sequence(primaryvertexanalyzer +
                                           pvgoodonlynoscraping +
                                           pvgoodcolliding +
#                                           pvgoodDAcolliding 
                                           pixelvertexanalyzer +
                                           pixelvertexHLTLike
                                           )
seqPVAnalyzerOnlyNoScrapingAOD = cms.Sequence(primaryvertexanalyzer +
                                           pvgoodonlynoscraping +
                                           pvgoodcolliding 
#                                           pvgoodDAcolliding 
                                           )
seqPVAnalyzerOnlyNoScrapingPixelLumi = cms.Sequence(pvgoodcolliding)


seqPVAnalyzerNonColliding = cms.Sequence(pvnoncolliding)


seqPVAnalyzerNonCollidingPlus = cms.Sequence(pvnoncollidingplus)

seqPVAnalyzerNonCollidingMinus = cms.Sequence(pvnoncollidingminus)

seqGoodPVAnalyzerNonColliding = cms.Sequence(pvgoodnoncolliding)


seqGoodPVAnalyzerNonCollidingPlus = cms.Sequence(pvgoodnoncollidingplus)

seqGoodPVAnalyzerNonCollidingMinus = cms.Sequence(pvgoodnoncollidingminus)

