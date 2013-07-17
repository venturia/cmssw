import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.recoConfiguration_cff import *
#from TrackingPFG.Configuration.bitSelectionSequence_MC_cff import *
from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.apvNoiseSequence_cff import *
from TrackingPFG.Configuration.multProdSequence_cff import *
from TrackingPFG.Configuration.nonCollidingSequence_cff import *
#from TrackingPFG.Configuration.collidingSequence_MC_cff import *
from TrackingPFG.Configuration.collidingSequence_cff import *
from TrackingPFG.Configuration.preScrapingSequence_cff import *

#p0 = cms.Path(seqPhysCollSelectionMC +
#                      seqEventHistoryReco +
#                      seqEventHistory +
#                      seqPVSelection +
#                      seqPreScraping + seqNoScrapingSelection +
#                      seqReco +
#                      seqColliding
#                      )

#p0.remove("pixeltrackcount")

