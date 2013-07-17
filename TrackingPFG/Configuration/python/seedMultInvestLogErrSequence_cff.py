import FWCore.ParameterSet.Config as cms

# seed multiplicity monitoring

from tracking.TrackRecoMonitoring.seedmultiplicitymonitor_cfi import *
seedmultmonitortracking = seedmultiplicitymonitor.clone()
seedmultmonitortoomanyclusters = seedmultiplicitymonitor.clone()
seedmultmonitortoomanyseeds = seedmultiplicitymonitor.clone()
seedmultmonitortoomanytriplets = seedmultiplicitymonitor.clone()

seqSeedMultInvestLogErr = cms.Sequence(seedmultiplicitymonitor)
seqSeedMultInvestLogErrTracking = cms.Sequence(seedmultmonitortracking)
seqSeedMultInvestLogErrTooManyClusters = cms.Sequence(seedmultmonitortoomanyclusters)
seqSeedMultInvestLogErrTooManySeeds = cms.Sequence(seedmultmonitortoomanyseeds)
seqSeedMultInvestLogErrTooManyTriplets = cms.Sequence(seedmultmonitortoomanytriplets)
