import FWCore.ParameterSet.Config as cms

# multiplicity monitoring

#strip clusters

from DPGAnalysis.SiStripTools.ssclusmultinvestigator_cfi import *
ssclusmultinvestigator.runHisto = cms.untracked.bool(False)
ssclusmultinvestigator.scaleFactor  = cms.untracked.int32(1)
ssclusmultinvestigator.numberOfBins  = cms.untracked.int32(1000)

ssclusmultinvestnoncoll = ssclusmultinvestigator.clone()
ssclusmultinvestnoncollearly = ssclusmultinvestigator.clone()
ssclusmultinvestprescraping = ssclusmultinvestigator.clone()
ssclusmultinvestonlytrigger = ssclusmultinvestigator.clone()
#ssclusmultinvestpxprob = ssclusmultinvestigator.clone()


from DPGAnalysis.SiStripTools.ssclusmultinvestigatorwithvtx_cfi import *
ssclusmultinvestonlynoscraping = ssclusmultinvestigatorwithvtx.clone(runHisto=cms.untracked.bool(False),scaleFactor=cms.untracked.int32(1),numberOfBins=cms.untracked.int32(1000))
ssclusmultinvestonlynoscraping.vertexCollection = cms.InputTag("goodVertices")
ssclusmultinvestonlynoscraping.digiVtxCorrConfig.scaleFactor = cms.untracked.int32(1)
ssclusmultinvestonlynoscraping.digiVtxCorrConfig.numberOfBins = cms.untracked.int32(200)

ssclusmultinvestonlynoscrapingHLTpixelvtx = ssclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("pixelVerticesDivisiveHLT"),wantInvestHist = cms.bool(False))
ssclusmultinvestonlynoscrapingpixelvtx = ssclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("realPixelVertices"),wantInvestHist = cms.bool(False))
#ssclusmultinvestonlynoscrapingDA = ssclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("goodVerticesDA"))

ssclusmultinvestonlynoscraping.digiVtxCorrConfig.runHisto = cms.untracked.bool(True)

from DPGAnalysis.SiStripTools.ssclusmultlumicorr_cfi import *
ssclusmultlumicorronlynoscraping = ssclusmultlumicorr.clone()
ssclusmultlumicorronlynoscraping.digiLumiCorrConfig.scaleFactor=cms.untracked.int32(1)
ssclusmultlumicorronlynoscraping.digiLumiCorrConfig.numberOfBins=cms.untracked.int32(200)
ssclusmultlumicorronlynoscraping.digiLumiCorrConfig.runHisto = cms.untracked.bool(True)

from DPGAnalysis.SiStripTools.ssclusmultpileupcorr_cfi import *
ssclusmultpileupcorronlytrigger = ssclusmultpileupcorr.clone()
ssclusmultpileupcorronlytrigger.digiPileupCorrConfig.scaleFactor=cms.untracked.int32(1)
ssclusmultpileupcorronlytrigger.digiPileupCorrConfig.numberOfBins=cms.untracked.int32(200)


#pixel clusters

from DPGAnalysis.SiStripTools.spclusmultinvestigator_cfi import *
spclusmultinvestigator.runHisto = cms.untracked.bool(False)
spclusmultinvestigator.scaleFactor  = cms.untracked.int32(10)
spclusmultinvestigator.numberOfBins  = cms.untracked.int32(1000)

spclusmultinvestnoncoll = spclusmultinvestigator.clone()
spclusmultinvestnoncollearly = spclusmultinvestigator.clone()
spclusmultinvestprescraping = spclusmultinvestigator.clone()
spclusmultinvestonlytrigger = spclusmultinvestigator.clone()
#spclusmultinvestpxprob = spclusmultinvestigator.clone()

from DPGAnalysis.SiStripTools.spclusmultinvestigatorwithvtx_cfi import *
spclusmultinvestigatorwithvtx.wantedSubDets = cms.untracked.VPSet(
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"), binMax = cms.int32(200000)),
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXL1"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXL2"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXL3"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("Lumi"), binMax = cms.int32(200000))
    )
spclusmultinvestigatorwithvtx.digiVtxCorrConfig.wantedSubDets = cms.untracked.VPSet(
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"), binMax = cms.int32(200000)),
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXL1"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXL2"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXL3"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("Lumi"), binMax = cms.int32(200000))
    )
spclusmultinvestonlynoscraping = spclusmultinvestigatorwithvtx.clone(runHisto=cms.untracked.bool(False),scaleFactor=cms.untracked.int32(10),numberOfBins=cms.untracked.int32(1000))
spclusmultinvestonlynoscraping.vertexCollection = cms.InputTag("goodVertices")
spclusmultinvestonlynoscraping.digiVtxCorrConfig.scaleFactor = cms.untracked.int32(10)
spclusmultinvestonlynoscraping.digiVtxCorrConfig.numberOfBins = cms.untracked.int32(200)

spclusmultinvestonlynoscrapingHLTpixelvtx = spclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("pixelVerticesDivisiveHLT"),wantInvestHist = cms.bool(False))
spclusmultinvestonlynoscrapingpixelvtx = spclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("realPixelVertices"),wantInvestHist = cms.bool(False))
#spclusmultinvestonlynoscrapingDA = spclusmultinvestonlynoscraping.clone(vertexCollection = cms.InputTag("goodVerticesDA"))

spclusmultinvestonlynoscraping.digiVtxCorrConfig.runHisto = cms.untracked.bool(True)

spclusmultinvestonlynoscrapingPixelLumi = spclusmultinvestonlynoscraping.clone()


from DPGAnalysis.SiStripTools.spclusmultlumicorr_cfi import *
spclusmultlumicorr.digiLumiCorrConfig.wantedSubDets = cms.untracked.VPSet(
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"), binMax = cms.int32(200000)),
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXL1"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXL2"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXL3"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("Lumi"), binMax = cms.int32(200000))
    )
spclusmultlumicorronlynoscraping = spclusmultlumicorr.clone()
spclusmultlumicorronlynoscraping.digiLumiCorrConfig.scaleFactor=cms.untracked.int32(10)
spclusmultlumicorronlynoscraping.digiLumiCorrConfig.numberOfBins=cms.untracked.int32(200)
spclusmultlumicorronlynoscraping.digiLumiCorrConfig.runHisto = cms.untracked.bool(True)

spclusmultlumicorronlynoscrapingPixelLumi = spclusmultlumicorronlynoscraping.clone()

from DPGAnalysis.SiStripTools.spclusmultpileupcorr_cfi import *
spclusmultpileupcorr.digiPileupCorrConfig.wantedSubDets = cms.untracked.VPSet(
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel"), binMax = cms.int32(200000)),
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXL1"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXL2"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXL3"), binMax = cms.int32(100000)),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("Lumi"), binMax = cms.int32(200000))
    )
spclusmultpileupcorronlytrigger = spclusmultpileupcorr.clone()
spclusmultpileupcorronlytrigger.digiPileupCorrConfig.scaleFactor=cms.untracked.int32(10)
spclusmultpileupcorronlytrigger.digiPileupCorrConfig.numberOfBins=cms.untracked.int32(200)

#cluster correlation

from DPGAnalysis.SiStripTools.multiplicitycorr_cfi import *
multiplicitycorr.correlationConfigurations = cms.VPSet(
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclustermultprod"),
             xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(100000), 
             yMultiplicityMap = cms.InputTag("spclustermultprod"),
             yDetSelection = cms.uint32(0), yDetLabel = cms.string("Pixel"), yBins = cms.uint32(1000), yMax=cms.double(20000),
             rBins = cms.uint32(200), scaleFactor =cms.untracked.double(5.),
             runHisto=cms.bool(False),runHistoBXProfile=cms.bool(False),runHistoBX=cms.bool(False),runHisto2D=cms.bool(False)
             )
    )
multcorrnoncoll = multiplicitycorr.clone()
multcorrnoncollearly = multiplicitycorr.clone()
multcorrprescraping = multiplicitycorr.clone()
multcorronlytrigger = multiplicitycorr.clone()
multcorronlynoscraping = multiplicitycorr.clone()
#multcorrpxprob = multiplicitycorr.clone()

multcorronlytrigger.correlationConfigurations = cms.VPSet(
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclustermultprod"),
             xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(1000), xMax=cms.double(100000), 
             yMultiplicityMap = cms.InputTag("spclustermultprod"),
             yDetSelection = cms.uint32(0), yDetLabel = cms.string("Pixel"), yBins = cms.uint32(1000), yMax=cms.double(20000),
             rBins = cms.uint32(200), scaleFactor =cms.untracked.double(5.),
             runHisto=cms.bool(True),runHistoBXProfile=cms.bool(True),runHistoBX=cms.bool(True),runHisto2D=cms.bool(False),
             runHistoProfileBX=cms.untracked.bool(True)
             )
    )


# digitime correlations

from DPGAnalysis.SiStripTools.ssclusmulttimecorrelations_cfi import *
ssclusmulttimecorrelations.runHisto = cms.untracked.bool(False)
ssclusmulttimecorrelations.scaleFactors = cms.untracked.vint32(1)
ssclusmulttimecorrelations.numberOfBins = cms.untracked.int32(1000)
ssclusmulttimecorrelations.wantedSubDets = cms.untracked.VPSet(    
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("TK"),  binMax = cms.int32(9523712/64), phasePartition = cms.untracked.string("All"))
    )




seqClusMultInvest = cms.Sequence(ssclusmultinvestigator + spclusmultinvestigator + multiplicitycorr + ssclusmulttimecorrelations)

seqClusMultInvestNonColl = cms.Sequence(ssclusmultinvestnoncoll + spclusmultinvestnoncoll + multcorrnoncoll)
seqClusMultInvestNonCollEarly = cms.Sequence(ssclusmultinvestnoncollearly + spclusmultinvestnoncollearly + multcorrnoncollearly)
seqClusMultInvestPreScraping = cms.Sequence(ssclusmultinvestprescraping + spclusmultinvestprescraping + multcorrprescraping)
seqClusMultInvestOnlyTrigger = cms.Sequence(ssclusmultinvestonlytrigger + spclusmultinvestonlytrigger + multcorronlytrigger)
seqClusMultInvestOnlyNoScraping = cms.Sequence(ssclusmultinvestonlynoscraping + spclusmultinvestonlynoscraping +
                                               ssclusmultinvestonlynoscrapingHLTpixelvtx + spclusmultinvestonlynoscrapingHLTpixelvtx +
                                               ssclusmultinvestonlynoscrapingpixelvtx + spclusmultinvestonlynoscrapingpixelvtx +
#                                               ssclusmultinvestonlynoscrapingDA + spclusmultinvestonlynoscrapingDA +
                                               ssclusmultlumicorronlynoscraping + spclusmultlumicorronlynoscraping +
                                               multcorronlynoscraping)
seqClusMultInvestOnlyNoScrapingPixelLumi = cms.Sequence(spclusmultinvestonlynoscrapingPixelLumi +
                                                        spclusmultlumicorronlynoscrapingPixelLumi +
                                                        multcorronlynoscraping)
#seqClusMultInvestPxProb = cms.Sequence(ssclusmultinvestpxprob + spclusmultinvestpxprob + multcorrpxprob)

seqMCClusMultInvestOnlyTrigger = cms.Sequence(ssclusmultpileupcorronlytrigger + spclusmultpileupcorronlytrigger)
