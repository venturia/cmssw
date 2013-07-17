import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.simpleTrackSequence_cff import *
#from TrackingPFG.Configuration.clusMultInvestSequence_cff import *

seqOnlyTriggerAnalysis = cms.Sequence(seqEventHistory +
#                                      seqClusMultInvestOnlyTrigger +
                                      seqSimpleTrackOnlyTrigger)

from TrackingPFG.Configuration.mcVerticesSequence_cff import *

seqOnlyTriggerAnalysisMC = cms.Sequence(seqMCVertices)
