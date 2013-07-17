import FWCore.ParameterSet.Config as cms

#from Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi import *
#highPurityTracks = AlignmentTrackSelector.clone()
#highPurityTracks.trackQualities = cms.vstring("highPurity")

veryGoodTrack = cms.EDFilter("RecoTrackSelector",
                             src = cms.InputTag("generalTracks"),
                             ptMin = cms.double(.500),
                             minRapidity = cms.double(-3.),
                             maxRapidity = cms.double(3.),
                             tip = cms.double(.01),
                             lip = cms.double(0.5),
                             minHit = cms.int32(0),
                             min3DHit = cms.int32(0),
                             maxChi2 = cms.double(999999.),
                             quality = cms.vstring("highPurity"),
                             algorithm = cms.vstring(),
                             beamSpot = cms.InputTag("offlineBeamSpot"),
                             filter = cms.bool(True)
                             )



seqVeryGoodTrackSelection = cms.Sequence(veryGoodTrack)
