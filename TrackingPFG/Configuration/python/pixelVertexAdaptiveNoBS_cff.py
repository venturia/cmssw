import FWCore.ParameterSet.Config as cms

from RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi import *
pixelVerticesAdaptiveNoBS = pixelVertices.clone(useBeamConstraint = cms.bool(False))



