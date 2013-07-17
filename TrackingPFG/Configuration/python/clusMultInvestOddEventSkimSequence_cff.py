import FWCore.ParameterSet.Config as cms

# multiplicity monitoring

from DPGAnalysis.SiStripTools.ssclusmultinvestigator_cfi import *
ssclusmultinvestigator.runHisto = cms.untracked.bool(False)
ssclusmultinvestigator.scaleFactor=cms.untracked.int32(2)

ssclusmultinvestnotrack = ssclusmultinvestigator.clone()
ssclusmultinvestnotrackskim = ssclusmultinvestigator.clone()
ssclusmultinvestnotrackwithtwojets = ssclusmultinvestigator.clone()
ssclusmultinvestnotrackwithcentraljet = ssclusmultinvestigator.clone()
ssclusmultinvestnovertex = ssclusmultinvestigator.clone()
ssclusmultinvestnovertexskim = ssclusmultinvestigator.clone()
ssclusmultinvestnovertexwithtwojets = ssclusmultinvestigator.clone()
ssclusmultinvestnovertexwithcentraljet = ssclusmultinvestigator.clone()
ssclusmultinvestoffdiag = ssclusmultinvestigator.clone()
ssclusmultinvestnostrip = ssclusmultinvestigator.clone()
ssclusmultinvestmanystripclus = ssclusmultinvestigator.clone()
ssclusmultinvesttoomanystripclus = ssclusmultinvestigator.clone()
ssclusmultinvestmanyclus = ssclusmultinvestigator.clone()
ssclusmultinvestniter4hp =  ssclusmultinvestigator.clone()
ssclusmultinvestniter5hp =  ssclusmultinvestigator.clone()


from DPGAnalysis.SiStripTools.spclusmultinvestigator_cfi import *
spclusmultinvestigator.runHisto = cms.untracked.bool(False)
spclusmultinvestigator.scaleFactor=cms.untracked.int32(20)

spclusmultinvestnotrack = spclusmultinvestigator.clone()
spclusmultinvestnotrackskim = spclusmultinvestigator.clone()
spclusmultinvestnotrackwithtwojets = spclusmultinvestigator.clone()
spclusmultinvestnotrackwithcentraljet = spclusmultinvestigator.clone()
spclusmultinvestnovertex = spclusmultinvestigator.clone()
spclusmultinvestnovertexskim = spclusmultinvestigator.clone()
spclusmultinvestnovertexwithtwojets = spclusmultinvestigator.clone()
spclusmultinvestnovertexwithcentraljet = spclusmultinvestigator.clone()
spclusmultinvestoffdiag = spclusmultinvestigator.clone()
spclusmultinvestnostrip = spclusmultinvestigator.clone()
spclusmultinvestmanystripclus = spclusmultinvestigator.clone()
spclusmultinvesttoomanystripclus = spclusmultinvestigator.clone()
spclusmultinvestmanyclus = spclusmultinvestigator.clone()
spclusmultinvestniter4hp =  spclusmultinvestigator.clone()
spclusmultinvestniter5hp =  spclusmultinvestigator.clone()

from DPGAnalysis.SiStripTools.multiplicitycorr_cfi import *
multiplicitycorr.correlationConfigurations = cms.VPSet(
    cms.PSet(xMultiplicityMap = cms.InputTag("ssclustermultprod"),
             xDetSelection = cms.uint32(0), xDetLabel = cms.string("TK"), xBins = cms.uint32(3000), xMax=cms.double(100000), 
             yMultiplicityMap = cms.InputTag("spclustermultprod"),
             yDetSelection = cms.uint32(0), yDetLabel = cms.string("Pixel"), yBins = cms.uint32(1000), yMax=cms.double(30000),
             rBins = cms.uint32(200), scaleFactor = cms.untracked.double(5.),
             runHisto=cms.bool(False),runHistoBXProfile=cms.bool(False),runHistoBX=cms.bool(False),runHisto2D=cms.bool(False)
             )
    )

multcorrnotrack = multiplicitycorr.clone()
multcorrnotrackskim = multiplicitycorr.clone()
multcorrnotrackwithtwojets = multiplicitycorr.clone()
multcorrnotrackwithcentraljet = multiplicitycorr.clone()
multcorrnovertex = multiplicitycorr.clone()
multcorrnovertexskim = multiplicitycorr.clone()
multcorrnovertexwithtwojets = multiplicitycorr.clone()
multcorrnovertexwithcentraljet = multiplicitycorr.clone()
multcorroffdiag = multiplicitycorr.clone()
multcorrnostrip = multiplicitycorr.clone()
multcorrmanystripclus = multiplicitycorr.clone()
multcorrtoomanystripclus = multiplicitycorr.clone()
multcorrmanyclus = multiplicitycorr.clone()
multcorrniter4hp = multiplicitycorr.clone()
multcorrniter5hp = multiplicitycorr.clone()


seqClusMultInvestNoTrack = cms.Sequence(ssclusmultinvestnotrack + spclusmultinvestnotrack + multcorrnotrack)
seqClusMultInvestNoTrackSkim = cms.Sequence(ssclusmultinvestnotrackskim + spclusmultinvestnotrackskim + multcorrnotrackskim)
seqClusMultInvestNoTrackWithTwoJets = cms.Sequence(ssclusmultinvestnotrackwithtwojets + spclusmultinvestnotrackwithtwojets + multcorrnotrackwithtwojets)
seqClusMultInvestNoTrackWithCentralJet = cms.Sequence(ssclusmultinvestnotrackwithcentraljet + spclusmultinvestnotrackwithcentraljet + multcorrnotrackwithcentraljet)

seqClusMultInvestNoVertex = cms.Sequence(ssclusmultinvestnovertex + spclusmultinvestnovertex + multcorrnovertex)
seqClusMultInvestNoVertexSkim = cms.Sequence(ssclusmultinvestnovertexskim + spclusmultinvestnovertexskim + multcorrnovertexskim)
seqClusMultInvestNoVertexWithTwoJets = cms.Sequence(ssclusmultinvestnovertexwithtwojets + spclusmultinvestnovertexwithtwojets + multcorrnovertexwithtwojets)
seqClusMultInvestNoVertexWithCentralJet = cms.Sequence(ssclusmultinvestnovertexwithcentraljet + spclusmultinvestnovertexwithcentraljet + multcorrnovertexwithcentraljet)

seqClusMultInvestOffDiag = cms.Sequence(ssclusmultinvestoffdiag + spclusmultinvestoffdiag + multcorroffdiag)
seqClusMultInvestNoStrip = cms.Sequence(ssclusmultinvestnostrip + spclusmultinvestnostrip + multcorrnostrip)

seqClusMultInvestManyStripClus = cms.Sequence(ssclusmultinvestmanystripclus + spclusmultinvestmanystripclus + multcorrmanystripclus)
seqClusMultInvestTooManyStripClus = cms.Sequence(ssclusmultinvesttoomanystripclus + spclusmultinvesttoomanystripclus + multcorrtoomanystripclus)
seqClusMultInvestManyClus = cms.Sequence(ssclusmultinvestmanyclus + spclusmultinvestmanyclus + multcorrmanyclus)

seqClusMultInvestNiter4hp = cms.Sequence(ssclusmultinvestniter4hp + spclusmultinvestniter4hp + multcorrniter4hp)
seqClusMultInvestNiter5hp = cms.Sequence(ssclusmultinvestniter5hp + spclusmultinvestniter5hp + multcorrniter5hp)
