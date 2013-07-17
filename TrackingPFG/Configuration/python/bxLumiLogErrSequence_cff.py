import FWCore.ParameterSet.Config as cms

# seed multiplicity monitoring

from TrackingPFG.Utilities.bxlumianalyzer_cfi import *

bxlumianyerror = bxlumianalyzer.clone()
bxlumitracking = bxlumianalyzer.clone()
bxlumitoomanyclusters = bxlumianalyzer.clone()
bxlumitoomanyseeds = bxlumianalyzer.clone()
bxlumitoomanytriplets = bxlumianalyzer.clone()

# changes only fox bxlumianalyzer
bxlumianalyzer.runHisto = cms.bool(True)
#bxlumianalyzer.maxLSBeforeRebin = cms.uint32(800)
#

seqBXLumiLogErr = cms.Sequence(bxlumianalyzer)
seqBXLumiLogErrAnyError = cms.Sequence(bxlumianyerror)
seqBXLumiLogErrTracking = cms.Sequence(bxlumitracking)
seqBXLumiLogErrTooManyClusters = cms.Sequence(bxlumitoomanyclusters)
seqBXLumiLogErrTooManySeeds = cms.Sequence(bxlumitoomanyseeds)
seqBXLumiLogErrTooManyTriplets = cms.Sequence(bxlumitoomanytriplets)
