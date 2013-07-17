import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.trackSelectionPVEffSequence_cff import *

from TrackingPFG.Configuration.multProdSequence_cff import *


#----------------Bkg event selection (to be understood why the import below does not work)
#from TrackingPFG.Configuration.nonCollidingSequence_cff import seqNonCollidingSkim

from DPGAnalysis.SiStripTools.largesipixelclusterevents_cfi import *

largeSiPixelClusterEvents.absoluteThreshold = cms.untracked.int32(10)
largeSiPixelClusterEvents.moduleThreshold = cms.untracked.int32(1000)

seqNonCollidingSkim = cms.Sequence(largeSiPixelClusterEvents)

seqNoSelectionNonColl = cms.Sequence(seqNonCollidingSelection + seqMultProd + seqNonCollidingSkim)

seqTrigSelectionNonColl = cms.Sequence(seqNonCollidingBitSelection + seqMultProd + seqNonCollidingSkim)

seqTrackSelectionNonColl = cms.Sequence(seqTrigSelectionNonColl + seqVeryGoodTrackSelection + seqMultProd + seqNonCollidingSkim)
