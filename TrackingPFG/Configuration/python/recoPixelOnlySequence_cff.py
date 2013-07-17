import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff import *
from Configuration.StandardSequences.GeometryDB_cff import *
from Configuration.StandardSequences.Reconstruction_cff import *
#from RecoPixelVertexing.Configuration.RecoPixelVertexing_cff import *

hltPixelVertices3DbbPhi = pixelVertices.clone()
hltPixelVertices3DbbPhi.TkFilterParameters.minPt = cms.double(0.5)
hltPixelVertices3DbbPhi.minNdof  = cms.double(0.0)

from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *
#
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *  # from RecoVertex.Configuration.RecoVertex
#
#from RecoTracker.Configuration.RecoTracker_cff import *
#from RecoTracker.IterativeTracking.InitialStep_cff import *
#from TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer_cfi import *

#
from RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff import * # this is needed by siPixelRecHits

from RecoPixelVertexing.PixelLowPtUtilities.ClusterShapeHitFilterESProducer_cfi import * # this is what we are discussing about
#
#from Configuration.StandardSequences.Reconstruction_cff import siPixelRecHits
#from Configuration.StandardSequences.Reconstruction_cff import recopixelvertexing
#from Configuration.StandardSequences.Reconstruction_cff import ckftracks
#from Configuration.StandardSequences.Reconstruction_cff import vertexreco
#from Configuration.StandardSequences.Reconstruction_cff import logErrorHarvester

## offlineBeamSpot from scalers
#
#from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import *
#offlineBeamSpot = onlineBeamSpotProducer.clone()

# track reco

#pixelTracks.OrderedHitsFactoryPSet.GeneratorPSet.SeedComparitorPSet.ComponentName = 'none'

seqPixelOnlyTrackReReco = cms.Sequence(siPixelRecHits +  recopixelvertexing + hltPixelVertices3DbbPhi)


