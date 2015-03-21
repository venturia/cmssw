import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.RecoTrackJets_cff import *

trackjetsTracks = cms.EDFilter("TrackSelector",
                               src = cms.InputTag("generalTracks"),
                               cut = cms.string('pt > 0.3 && quality("highPurity")')
                               )


trackWithVertexRefSelector.nVertices = 99
trackWithVertexRefSelector.zetaVtx = 1.0
trackWithVertexRefSelector.rhoVtx = 0.2
trackWithVertexRefSelector.ptErrorCut = 0.2
trackWithVertexRefSelector.src = cms.InputTag("trackjetsTracks")

ak5TrackJets.UseOnlyVertexTracks = False
ak5TrackJets.UseOnlyOnePV = False
ak5TrackJets.DxyTrVtxMax = 0.2
ak5TrackJets.DzTrVtxMax = 1.0

kt4TrackJets.UseOnlyVertexTracks = False
kt4TrackJets.UseOnlyOnePV = False
kt4TrackJets.DxyTrVtxMax = 0.2
kt4TrackJets.DzTrVtxMax = 1.0

sisCone5TrackJets.UseOnlyVertexTracks = False
sisCone5TrackJets.UseOnlyOnePV = False
sisCone5TrackJets.DxyTrVtxMax = 0.2
sisCone5TrackJets.DzTrVtxMax = 1.0

seqTrackJetsReco = cms.Sequence(trackjetsTracks + recoTrackJets + sisCone5TrackJets)

