import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff import *
from Configuration.StandardSequences.GeometryDB_cff import *
from Configuration.StandardSequences.Reconstruction_cff import *


# TrackerOnlyConversionFinder

#trackerOnlyConversions.AllowTrackBC = cms.bool(False)
#trackerOnlyConversions.AllowRightBC = cms.bool(True)
#trackerOnlyConversions.MinApproach = cms.double(-.25)
#trackerOnlyConversions.rCut = cms.double(2.0)
#trackerOnlyConversions.vtxChi2 = cms.double(0.)

# online beam spot (from scalers)

from TrackingPFG.Configuration.onlineBeamSpotRecoSequence_cff import *

# additional beam spot from DB

testBeamSpot = cms.EDProducer("BeamSpotProducer")

# pixel vertices

from TrackingPFG.Configuration.pixelVertexRecoSequence_cff import *

# TrackJets

from TrackingPFG.Configuration.trackJetsRecoSequence_cff import *

# High purity Tracks

from TrackingPFG.Configuration.hpSelectionSequence_cff import *

# FTSlike pixel vertex

#from TrackingPFG.Configuration.ftsLikePixelVertexSelector_cfi import *

# good Vertices

from TrackingPFG.Configuration.goodVertexSelector_cfi import *

# V0s

from TrackingPFG.Configuration.v0RecoSequence_cff import *

seqReco = cms.Sequence(
#    trackerOnlyConversionSequence +
    onlineBeamSpot +
#    testBeamSpot +
    seqVertexReco +
    seqTrackJetsReco + seqHighPurity + seqPASTracks + seqOneGeVTracks + seqCentralTenGeVTracks +
#    ftsLikePixelVertexFilter +
    seqGoodVertices + 
    seqV0Reco)

seqRecoAOD = cms.Sequence(
#    trackerOnlyConversionSequence +
    onlineBeamSpot +
#    testBeamSpot +
    seqVertexRecoAOD +
    seqTrackJetsReco + seqHighPurity + seqPASTracks + seqOneGeVTracks + seqCentralTenGeVTracks + 
    seqGoodVerticesAOD + 
    seqV0Reco)

seqRecoPixelLumi = cms.Sequence(seqGoodVerticesPixelLumi)

seqRecoNonColliding = cms.Sequence(goodDisplacedVertices)
