import FWCore.ParameterSet.Config as cms

from DPGAnalysis.SiStripTools.sipixelclustermultiplicityprod_cfi import spclustermultprod
from DPGAnalysis.SiStripTools.sistripclustermultiplicityprod_cfi import ssclustermultprod

spclustermultprod.wantedSubDets = cms.VPSet(    
    cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("Pixel")),
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("BPIX"),selection=cms.untracked.vstring("0x1e000000-0x12000000")),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIX"),selection=cms.untracked.vstring("0x1e000000-0x14000000")),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("BPIXL1"),selection=cms.untracked.vstring("0x1e0f0000-0x12010000")),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("BPIXL2"),selection=cms.untracked.vstring("0x1e0f0000-0x12020000")),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("BPIXL3"),selection=cms.untracked.vstring("0x1e0f0000-0x12030000")),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("Lumi"),selection=cms.untracked.vstring("0x1e000000-0x14000000","0x1e0f0000-0x12020000","0x1e0f0000-0x12030000"))
    )


seqMultProdPixelLumi = cms.Sequence(spclustermultprod+ssclustermultprod)

