import FWCore.ParameterSet.Config as cms

# event selection

from DPGAnalysis.SiStripTools.largesipixelclusterevents_cfi import *

largeSiPixelClusterEvents.absoluteThreshold = cms.untracked.int32(10)
largeSiPixelClusterEvents.moduleThreshold = cms.untracked.int32(1000)

verylargeSiPixelClusterEvents = largeSiPixelClusterEvents.clone()
verylargeSiPixelClusterEvents.absoluteThreshold = cms.untracked.int32(200)

# multiplicity monitoring

from TrackingPFG.Configuration.clusMultInvestSequence_cff import *

# track simple plots

from TrackingPFG.Configuration.simpleTrackSequence_cff import *

# event selection based on pixel activity

seqLargeSiPixelSelection= cms.Sequence(largeSiPixelClusterEvents)
#seqVetoVeryLargeSiPixelSelection= cms.Sequence(~verylargeSiPixelClusterEvents)

# primary vertex monitoring

from TrackingPFG.Configuration.pvSequence_cff import *

seqNonCollidingSkim = cms.Sequence(largeSiPixelClusterEvents)

seqNonCollidingEarly = cms.Sequence(seqClusMultInvestNonCollEarly)

seqNonColliding = cms.Sequence(seqClusMultInvestNonColl + seqPVAnalyzerNonColliding +
                               seqGoodPVAnalyzerNonColliding + seqSimpleTrackNonColliding)

seqNonCollidingPlus  = cms.Sequence(seqPVAnalyzerNonCollidingPlus + seqGoodPVAnalyzerNonCollidingPlus)

seqNonCollidingMinus = cms.Sequence(seqPVAnalyzerNonCollidingMinus + seqGoodPVAnalyzerNonCollidingMinus)

seqNonCollidingGoodVtx = cms.Sequence(seqSimpleTrackNonCollidingGoodVtx)

#seqNonCollidingPlusGoodVtx  = cms.Sequence()

#seqNonCollidingMinusGoodVtx = cms.Sequence()

