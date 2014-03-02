import FWCore.ParameterSet.Config as cms

# multiplicity monitoring

from DPGAnalysis.SiStripTools.ssclusmultinvestigator_cfi import *
ssclusmultinvestigator.runHisto = cms.untracked.bool(False)
ssclusmultinvestigator.scaleFactor=cms.untracked.int32(1)
ssclusmultinvestanyerror = ssclusmultinvestigator.clone()
ssclusmultinvesttracking = ssclusmultinvestigator.clone()
ssclusmultinvesttoomanyclusters = ssclusmultinvestigator.clone()
ssclusmultinvesttoomanyseeds = ssclusmultinvestigator.clone()
ssclusmultinvesttoomanytriplets = ssclusmultinvestigator.clone()

from DPGAnalysis.SiStripTools.spclusmultinvestigator_cfi import *
spclusmultinvestigator.runHisto = cms.untracked.bool(False)
spclusmultinvestigator.scaleFactor=cms.untracked.int32(3)
spclusmultinvestanyerror = spclusmultinvestigator.clone()
spclusmultinvesttracking = spclusmultinvestigator.clone()
spclusmultinvesttoomanyclusters = spclusmultinvestigator.clone()
spclusmultinvesttoomanyseeds = spclusmultinvestigator.clone()
spclusmultinvesttoomanytriplets = spclusmultinvestigator.clone()

from DPGAnalysis.SiStripTools.multiplicitycorr_cfi import *
multiplicitycorr.correlationConfigurations = cms.VPSet(
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclustermultprod"),
             xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(3000), xMax=cms.double(200000), 
             yMultiplicityMap = cms.InputTag("spclustermultprod"),
             yDetSelection = cms.uint32(0), yDetLabel = cms.string("Pixel"), yBins = cms.uint32(1000), yMax=cms.double(60000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(5.),
             runHisto=cms.bool(False),runHistoBXProfile=cms.bool(False),runHistoBX=cms.bool(False),runHisto2D=cms.bool(False)
             )
    )

multcorranyerror = multiplicitycorr.clone()
multcorrtracking = multiplicitycorr.clone()
multcorrtoomanyclusters = multiplicitycorr.clone()
multcorrtoomanyseeds = multiplicitycorr.clone()
multcorrtoomanytriplets = multiplicitycorr.clone()

seqClusMultInvestLogErr = cms.Sequence(spclusmultinvestigator + ssclusmultinvestigator + multiplicitycorr) 
seqClusMultInvestLogErrAnyError = cms.Sequence(spclusmultinvestanyerror + ssclusmultinvestanyerror + multcorranyerror) 
seqClusMultInvestLogErrTracking = cms.Sequence(spclusmultinvesttracking + ssclusmultinvesttracking + multcorrtracking) 
seqClusMultInvestLogErrTooManyClusters = cms.Sequence(spclusmultinvesttoomanyclusters + ssclusmultinvesttoomanyclusters + multcorrtoomanyclusters) 
seqClusMultInvestLogErrTooManySeeds = cms.Sequence(spclusmultinvesttoomanyseeds + ssclusmultinvesttoomanyseeds + multcorrtoomanyseeds) 
seqClusMultInvestLogErrTooManyTriplets = cms.Sequence(spclusmultinvesttoomanytriplets + ssclusmultinvesttoomanytriplets + multcorrtoomanytriplets) 
