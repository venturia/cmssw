import FWCore.ParameterSet.Config as cms

from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import *
onlineBeamSpot = onlineBeamSpotProducer.clone()
onlineBeamSpot.setSigmaZ = cms.double(-1.)
