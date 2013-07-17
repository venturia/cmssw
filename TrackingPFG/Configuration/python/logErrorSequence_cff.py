import FWCore.ParameterSet.Config as cms


from TrackingPFG.Utilities.logerroranalyzer_cfi import *



logerroranyerror = logerroranalyzer.clone()
logerrortracking = logerroranalyzer.clone()
logerrortoomanyclusters = logerroranalyzer.clone()
logerrortoomanyseeds = logerroranalyzer.clone()
logerrortoomanytriplets = logerroranalyzer.clone()

seqLogError = cms.Sequence(logerroranalyzer)
seqLogErrorAnyError = cms.Sequence(logerroranyerror)
seqLogErrorTracking = cms.Sequence(logerrortracking)
seqLogErrorTooManyClusters = cms.Sequence(logerrortoomanyclusters)
seqLogErrorTooManySeeds = cms.Sequence(logerrortoomanyseeds)
seqLogErrorTooManyTriplets = cms.Sequence(logerrortoomanytriplets)
