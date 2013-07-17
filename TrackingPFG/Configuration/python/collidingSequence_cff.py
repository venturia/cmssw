import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.conversionSequence_cff import *
#from TrackingPFG.Configuration.conversionSequence_MC_cff import *
from TrackingPFG.Configuration.simpleTrackSequence_cff import *
from TrackingPFG.Configuration.pvSequence_cff import *
#from TrackingPFG.Configuration.bsSequence_cff import *
from TrackingPFG.Configuration.bspvSequence_cff import *
from TrackingPFG.Configuration.trackJetsSequence_cff import *
from TrackingPFG.Configuration.v0Sequence_cff import *
from TrackingPFG.Configuration.clusMultInvestSequence_cff import *
from TrackingPFG.Configuration.d0vsphiSequence_cff import *

seqColliding = cms.Sequence(seqClusMultInvest + seqSimpleTrackColliding + seqPixelTrackColliding
                            + seqPVAnalyzer + seqBSPVAnalyzer + seqTrackJets
#                            + seqConversion
                            + seqD0PhiCorr
                            + seqV0)

seqNoScrapingAnalysis = cms.Sequence(seqEventHistorySelected +
                                     seqColliding
                                     )

#seqCollidingPxProb = cms.Sequence(seqClusMultInvestPxProb)
