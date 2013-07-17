import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff import *
from Configuration.StandardSequences.GeometryDB_cff import *
from Configuration.StandardSequences.Reconstruction_cff import *
#from Configuration.StandardSequences.Reconstruction_cff import siPixelRecHits
#from Configuration.StandardSequences.Reconstruction_cff import recopixelvertexing
#from Configuration.StandardSequences.Reconstruction_cff import ckftracks
#from Configuration.StandardSequences.Reconstruction_cff import vertexreco
#from Configuration.StandardSequences.Reconstruction_cff import logErrorHarvester

## offlineBeamSpot from scalers
#
#from RecoVertex.BeamSpotProducer.BeamSpotOnline_cfi import *
#offlineBeamSpot = onlineBeamSpotProducer.clone()

# tracker local reco

seqTrackerLocalReReco = cms.Sequence(trackerlocalreco)

# track reco

seqTrackReReco = cms.Sequence(siPixelRecHits + siStripMatchedRecHits +
#                              offlineBeamSpot +
                              recopixelvertexing + ckftracks+vertexreco)

# log error harverster

seqLogErrHarvester = cms.Sequence(logErrorHarvester)

# global

seqLogErrReco = cms.Sequence(seqTrackReReco + seqLogErrHarvester)
