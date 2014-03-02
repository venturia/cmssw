# online beam spot (from scalers)

from TrackingPFG.Configuration.onlineBeamSpotRecoSequence_cff import *

# additional beam spot from DB

testBeamSpot = cms.EDProducer("BeamSpotProducer")

seqBSRecoBSPVDetailed = cms.Sequence(onlineBeamSpot + testBeamSpot)

