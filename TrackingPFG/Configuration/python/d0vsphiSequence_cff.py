import FWCore.ParameterSet.Config as cms


from DebugTools.BSSlope.d0phicorranalyzer_cfi import *

d0phicorrCentralTenGeV = d0phicorranalyzer.clone(trackCollection = cms.InputTag("centralTenGeVTracks"))

seqD0PhiCorr = cms.Sequence(d0phicorrCentralTenGeV)
