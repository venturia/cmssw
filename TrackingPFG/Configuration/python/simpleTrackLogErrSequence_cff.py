import FWCore.ParameterSet.Config as cms


from trackCount.TrackCount.trackcount_cfi import *

trackcount.trackCollection = cms.InputTag("generalTracks")
trackcountanyerror = trackcount.clone()
trackcounttracking = trackcount.clone()
trackcounttoomanyclusters = trackcount.clone()
trackcounttoomanyseeds = trackcount.clone()
trackcounttoomanytriplets = trackcount.clone()

from TrackingPFG.Configuration.hpSelectionSequence_cff import *

trackcounthp = trackcount.clone(trackCollection = cms.InputTag("highPurityTracks"))
trackcounthpanyerror = trackcounthp.clone()
trackcounthptracking = trackcounthp.clone()
trackcounthptoomanyclusters = trackcounthp.clone()
trackcounthptoomanyseeds = trackcounthp.clone()
trackcounthptoomanytriplets = trackcounthp.clone()

pixeltrackcount = trackcount.clone(trackCollection = cms.InputTag("pixelTracks"))
pixeltrackcountanyerror = pixeltrackcount.clone()
pixeltrackcounttracking = pixeltrackcount.clone()
pixeltrackcounttoomanyclusters = pixeltrackcount.clone()
pixeltrackcounttoomanyseeds = pixeltrackcount.clone()
pixeltrackcounttoomanytriplets = pixeltrackcount.clone()

seqSimpleTrackLogErr = cms.Sequence(trackcount + pixeltrackcount + seqHighPurity + trackcounthp)
seqSimpleTrackLogErrAnyError = cms.Sequence(trackcountanyerror + pixeltrackcountanyerror + seqHighPurity + trackcounthpanyerror)
seqSimpleTrackLogErrTracking = cms.Sequence(trackcounttracking + pixeltrackcounttracking + seqHighPurity + trackcounthptracking)
seqSimpleTrackLogErrTooManyClusters = cms.Sequence(trackcounttoomanyclusters + pixeltrackcounttoomanyclusters + seqHighPurity + trackcounthptoomanyclusters)
seqSimpleTrackLogErrTooManySeeds = cms.Sequence(trackcounttoomanyseeds + pixeltrackcounttoomanyseeds + seqHighPurity + trackcounthptoomanyseeds)
seqSimpleTrackLogErrTooManyTriplets = cms.Sequence(trackcounttoomanytriplets + pixeltrackcounttoomanytriplets + seqHighPurity + trackcounthptoomanytriplets)

seqSimpleTrackLogErrAOD = cms.Sequence(trackcount + seqHighPurity + trackcounthp)
seqSimpleTrackLogErrAnyErrorAOD = cms.Sequence(trackcountanyerror + seqHighPurity + trackcounthpanyerror)
seqSimpleTrackLogErrTrackingAOD = cms.Sequence(trackcounttracking + seqHighPurity + trackcounthptracking)
seqSimpleTrackLogErrTooManyClustersAOD = cms.Sequence(trackcounttoomanyclusters + seqHighPurity + trackcounthptoomanyclusters)
seqSimpleTrackLogErrTooManySeedsAOD = cms.Sequence(trackcounttoomanyseeds + seqHighPurity + trackcounthptoomanyseeds)
seqSimpleTrackLogErrTooManyTripletsAOD = cms.Sequence(trackcounttoomanytriplets + seqHighPurity + trackcounthptoomanytriplets)

