import FWCore.ParameterSet.Config as cms

# seed multiplicity monitoring

from Validation.RecoVertex.mcverticesanalyzer_cfi import *
mcverticesanyerror = mcverticesanalyzer.clone()
mcverticestracking = mcverticesanalyzer.clone()
mcverticestoomanyclusters = mcverticesanalyzer.clone()
mcverticestoomanyseeds = mcverticesanalyzer.clone()
mcverticestoomanytriplets = mcverticesanalyzer.clone()

seqMCVerticesLogErr = cms.Sequence(mcverticesanalyzer)
seqMCVerticesLogErrAnyError = cms.Sequence(mcverticesanyerror)
seqMCVerticesLogErrTracking = cms.Sequence(mcverticestracking)
seqMCVerticesLogErrTooManyClusters = cms.Sequence(mcverticestoomanyclusters)
seqMCVerticesLogErrTooManySeeds = cms.Sequence(mcverticestoomanyseeds)
seqMCVerticesLogErrTooManyTriplets = cms.Sequence(mcverticestoomanytriplets)
