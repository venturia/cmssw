import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.trackSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
from TrackingPFG.Configuration.pxProbSelectionSequence_cff import *


seqNoSelection = cms.Sequence(seqPhysCollSelection)

seqTrigSelection = cms.Sequence(seqBitSelection)

seqTrackSelection = cms.Sequence(seqTrigSelection + seqVeryGoodTrackSelection)

noScraping.thresh = cms.untracked.double(0.25)
seqHpFracCutSelection = cms.Sequence(seqNoScrapingSelection)

seqPxProbCutSelection = cms.Sequence(seqPxProbFilter)
