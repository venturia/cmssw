import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.trackSelectionPVEffSequence_cff import *

seqNoSelection = cms.Sequence(seqPhysCollSelectionMC)

seqTrigSelection = cms.Sequence(seqBitSelectionMC)

seqTrackSelection = cms.Sequence(seqTrigSelection + seqVeryGoodTrackSelection)
