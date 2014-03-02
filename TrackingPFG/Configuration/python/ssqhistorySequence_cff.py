import FWCore.ParameterSet.Config as cms

from DPGAnalysis.SiStripTools.sistripqualityhistory_cff import *

ssqhistory.maxLSBeforeRebin = cms.untracked.uint32(100)
ssqhistory.startingLSFraction = cms.untracked.uint32(1)
ssqhistorystrips = ssqhistory.clone(granularityMode = cms.untracked.uint32(3))

seqSSQHistory = cms.Sequence(ssqhistory + ssqhistorystrips)

