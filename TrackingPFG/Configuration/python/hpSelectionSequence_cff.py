import FWCore.ParameterSet.Config as cms

#from Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi import *
#highPurityTracks = AlignmentTrackSelector.clone()
#highPurityTracks.trackQualities = cms.vstring("highPurity")

highPurityTracks = cms.EDFilter("TrackSelector",
                               src = cms.InputTag("generalTracks"),
                               cut = cms.string('quality("highPurity")')
                               )



seqHighPurity = cms.Sequence(highPurityTracks)

pasTracks = cms.EDFilter("TrackSelector",
                         src = cms.InputTag("generalTracks"),
                         cut = cms.string('quality("highPurity") && pt > 0.5 ')
                         )



seqPASTracks = cms.Sequence(pasTracks)

oneGeVTracks = cms.EDFilter("TrackSelector",
                         src = cms.InputTag("generalTracks"),
                         cut = cms.string('quality("highPurity") && pt > 1.0 ')
                         )

seqOneGeVTracks = cms.Sequence(oneGeVTracks)

centralTenGeVTracks = cms.EDFilter("TrackSelector",
                                   src = cms.InputTag("generalTracks"),
                                   cut = cms.string('quality("highPurity") && pt > 10.0 && abs(eta)<1.0 ')
                                   )

seqCentralTenGeVTracks = cms.Sequence(centralTenGeVTracks)

