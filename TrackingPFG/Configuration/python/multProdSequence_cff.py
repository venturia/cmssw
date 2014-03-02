import FWCore.ParameterSet.Config as cms

from DPGAnalysis.SiStripTools.sipixelclustermultiplicityprod_cfi import spclustermultprod
from DPGAnalysis.SiStripTools.sistripclustermultiplicityprod_cfi import ssclustermultprod


seqMultProd = cms.Sequence(spclustermultprod+ssclustermultprod)

