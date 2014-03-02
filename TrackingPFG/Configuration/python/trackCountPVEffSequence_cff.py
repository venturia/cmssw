import FWCore.ParameterSet.Config as cms


from trackCount.TrackCount.trackcount_cfi import *

trackcount.trackCollection = cms.InputTag("generalTracks")

trackcountCut1 = trackcount.clone()
trackcountCut2 = trackcount.clone()
trackcountCut3 = trackcount.clone()
trackcountCut4 = trackcount.clone()
trackcountCut5 = trackcount.clone()
trackcountCut6 = trackcount.clone()

trackcountTrigSel = trackcount.clone()

trackcountTrigSelCut1 = trackcount.clone()
trackcountTrigSelCut2 = trackcount.clone()
trackcountTrigSelCut3 = trackcount.clone()
trackcountTrigSelCut4 = trackcount.clone()
trackcountTrigSelCut5 = trackcount.clone()
trackcountTrigSelCut6 = trackcount.clone()

trackcountTrackSel = trackcount.clone()

trackcountTrackSelCut1 = trackcount.clone()
trackcountTrackSelCut2 = trackcount.clone()
trackcountTrackSelCut3 = trackcount.clone()
trackcountTrackSelCut4 = trackcount.clone()
trackcountTrackSelCut5 = trackcount.clone()
trackcountTrackSelCut6 = trackcount.clone()

#non collding

trackcountNonColl = trackcount.clone()

trackcountNonCollCut1 = trackcount.clone()
trackcountNonCollCut2 = trackcount.clone()
trackcountNonCollCut3 = trackcount.clone()
trackcountNonCollCut4 = trackcount.clone()
trackcountNonCollCut5 = trackcount.clone()
trackcountNonCollCut6 = trackcount.clone()

trackcountNonCollHpFracCut = trackcount.clone()
trackcountNonCollPxProbCut = trackcount.clone()
trackcountNonCollLogErrCut = trackcount.clone()

trackcountNonCollTrigSel = trackcount.clone()

trackcountNonCollTrigSelCut1 = trackcount.clone()
trackcountNonCollTrigSelCut2 = trackcount.clone()
trackcountNonCollTrigSelCut3 = trackcount.clone()
trackcountNonCollTrigSelCut4 = trackcount.clone()
trackcountNonCollTrigSelCut5 = trackcount.clone()
trackcountNonCollTrigSelCut6 = trackcount.clone()

trackcountNonCollTrigSelHpFracCut = trackcount.clone()
trackcountNonCollTrigSelPxProbCut = trackcount.clone()
trackcountNonCollTrigSelLogErrCut = trackcount.clone()

trackcountNonCollTrigSelHpFracVtxCut = trackcount.clone()
trackcountNonCollTrigSelPxProbVtxCut = trackcount.clone()

trackcountNonCollTrackSel = trackcount.clone()

trackcountNonCollTrackSelCut1 = trackcount.clone()
trackcountNonCollTrackSelCut2 = trackcount.clone()
trackcountNonCollTrackSelCut3 = trackcount.clone()
trackcountNonCollTrackSelCut4 = trackcount.clone()
trackcountNonCollTrackSelCut5 = trackcount.clone()
trackcountNonCollTrackSelCut6 = trackcount.clone()


from TrackingPFG.Configuration.hpSelectionSequence_cff import *

trackcountHp = trackcount.clone(trackCollection = cms.InputTag("highPurityTracks"))

trackcountHpCut1 = trackcountHp.clone()
trackcountHpCut2 = trackcountHp.clone()
trackcountHpCut3 = trackcountHp.clone()
trackcountHpCut4 = trackcountHp.clone()
trackcountHpCut5 = trackcountHp.clone()
trackcountHpCut6 = trackcountHp.clone()

trackcountHpTrigSel = trackcountHp.clone()

trackcountHpTrigSelCut1 = trackcountHp.clone()
trackcountHpTrigSelCut2 = trackcountHp.clone()
trackcountHpTrigSelCut3 = trackcountHp.clone()
trackcountHpTrigSelCut4 = trackcountHp.clone()
trackcountHpTrigSelCut5 = trackcountHp.clone()
trackcountHpTrigSelCut6 = trackcountHp.clone()

trackcountHpTrackSel = trackcountHp.clone()

trackcountHpTrackSelCut1 = trackcountHp.clone()
trackcountHpTrackSelCut2 = trackcountHp.clone()
trackcountHpTrackSelCut3 = trackcountHp.clone()
trackcountHpTrackSelCut4 = trackcountHp.clone()
trackcountHpTrackSelCut5 = trackcountHp.clone()
trackcountHpTrackSelCut6 = trackcountHp.clone()

#non colliding


trackcountHpNonColl = trackcountHp.clone()

trackcountHpNonCollCut1 = trackcountHp.clone()
trackcountHpNonCollCut2 = trackcountHp.clone()
trackcountHpNonCollCut3 = trackcountHp.clone()
trackcountHpNonCollCut4 = trackcountHp.clone()
trackcountHpNonCollCut5 = trackcountHp.clone()
trackcountHpNonCollCut6 = trackcountHp.clone()

trackcountHpNonCollTrigSel = trackcountHp.clone()

trackcountHpNonCollTrigSelCut1 = trackcountHp.clone()
trackcountHpNonCollTrigSelCut2 = trackcountHp.clone()
trackcountHpNonCollTrigSelCut3 = trackcountHp.clone()
trackcountHpNonCollTrigSelCut4 = trackcountHp.clone()
trackcountHpNonCollTrigSelCut5 = trackcountHp.clone()
trackcountHpNonCollTrigSelCut6 = trackcountHp.clone()

trackcountHpNonCollTrackSel = trackcountHp.clone()

trackcountHpNonCollTrackSelCut1 = trackcountHp.clone()
trackcountHpNonCollTrackSelCut2 = trackcountHp.clone()
trackcountHpNonCollTrackSelCut3 = trackcountHp.clone()
trackcountHpNonCollTrackSelCut4 = trackcountHp.clone()
trackcountHpNonCollTrackSelCut5 = trackcountHp.clone()
trackcountHpNonCollTrackSelCut6 = trackcountHp.clone()


seqTrackCountPVEff = cms.Sequence(trackcount + seqHighPurity + trackcountHp)

seqTrackCountPVEffCut1 = cms.Sequence(trackcountCut1 + seqHighPurity + trackcountHpCut1)
seqTrackCountPVEffCut2 = cms.Sequence(trackcountCut2 + seqHighPurity + trackcountHpCut2)
seqTrackCountPVEffCut3 = cms.Sequence(trackcountCut3 + seqHighPurity + trackcountHpCut3)
seqTrackCountPVEffCut4 = cms.Sequence(trackcountCut4 + seqHighPurity + trackcountHpCut4)
seqTrackCountPVEffCut5 = cms.Sequence(trackcountCut5 + seqHighPurity + trackcountHpCut5)
seqTrackCountPVEffCut6 = cms.Sequence(trackcountCut6 + seqHighPurity + trackcountHpCut6)

seqTrackCountPVEffTrigSel = cms.Sequence(trackcountTrigSel + seqHighPurity + trackcountHpTrigSel)

seqTrackCountPVEffTrigSelCut1 = cms.Sequence(trackcountTrigSelCut1 + seqHighPurity + trackcountHpTrigSelCut1)
seqTrackCountPVEffTrigSelCut2 = cms.Sequence(trackcountTrigSelCut2 + seqHighPurity + trackcountHpTrigSelCut2)
seqTrackCountPVEffTrigSelCut3 = cms.Sequence(trackcountTrigSelCut3 + seqHighPurity + trackcountHpTrigSelCut3)
seqTrackCountPVEffTrigSelCut4 = cms.Sequence(trackcountTrigSelCut4 + seqHighPurity + trackcountHpTrigSelCut4)
seqTrackCountPVEffTrigSelCut5 = cms.Sequence(trackcountTrigSelCut5 + seqHighPurity + trackcountHpTrigSelCut5)
seqTrackCountPVEffTrigSelCut6 = cms.Sequence(trackcountTrigSelCut6 + seqHighPurity + trackcountHpTrigSelCut6)

seqTrackCountPVEffTrackSel = cms.Sequence(trackcountTrackSel + seqHighPurity + trackcountHpTrackSel)

seqTrackCountPVEffTrackSelCut1 = cms.Sequence(trackcountTrackSelCut1 + seqHighPurity + trackcountHpTrackSelCut1)
seqTrackCountPVEffTrackSelCut2 = cms.Sequence(trackcountTrackSelCut2 + seqHighPurity + trackcountHpTrackSelCut2)
seqTrackCountPVEffTrackSelCut3 = cms.Sequence(trackcountTrackSelCut3 + seqHighPurity + trackcountHpTrackSelCut3)
seqTrackCountPVEffTrackSelCut4 = cms.Sequence(trackcountTrackSelCut4 + seqHighPurity + trackcountHpTrackSelCut4)
seqTrackCountPVEffTrackSelCut5 = cms.Sequence(trackcountTrackSelCut5 + seqHighPurity + trackcountHpTrackSelCut5)
seqTrackCountPVEffTrackSelCut6 = cms.Sequence(trackcountTrackSelCut6 + seqHighPurity + trackcountHpTrackSelCut6)

# non colliding

seqTrackCountPVEffNonColl = cms.Sequence(trackcountNonColl + seqHighPurity + trackcountHpNonColl)

seqTrackCountPVEffNonCollCut1 = cms.Sequence(trackcountNonCollCut1 + seqHighPurity + trackcountHpNonCollCut1)
seqTrackCountPVEffNonCollCut2 = cms.Sequence(trackcountNonCollCut2 + seqHighPurity + trackcountHpNonCollCut2)
seqTrackCountPVEffNonCollCut3 = cms.Sequence(trackcountNonCollCut3 + seqHighPurity + trackcountHpNonCollCut3)
seqTrackCountPVEffNonCollCut4 = cms.Sequence(trackcountNonCollCut4 + seqHighPurity + trackcountHpNonCollCut4)
seqTrackCountPVEffNonCollCut5 = cms.Sequence(trackcountNonCollCut5 + seqHighPurity + trackcountHpNonCollCut5)
seqTrackCountPVEffNonCollCut6 = cms.Sequence(trackcountNonCollCut6 + seqHighPurity + trackcountHpNonCollCut6)

seqTrackCountPVEffNonCollHpFracCut = cms.Sequence(trackcountNonCollHpFracCut)
seqTrackCountPVEffNonCollPxProbCut = cms.Sequence(trackcountNonCollPxProbCut)
seqTrackCountPVEffNonCollLogErrCut = cms.Sequence(trackcountNonCollLogErrCut)

seqTrackCountPVEffNonCollTrigSel = cms.Sequence(trackcountNonCollTrigSel + seqHighPurity + trackcountHpNonCollTrigSel)

seqTrackCountPVEffNonCollTrigSelCut1 = cms.Sequence(trackcountNonCollTrigSelCut1 + seqHighPurity + trackcountHpNonCollTrigSelCut1)
seqTrackCountPVEffNonCollTrigSelCut2 = cms.Sequence(trackcountNonCollTrigSelCut2 + seqHighPurity + trackcountHpNonCollTrigSelCut2)
seqTrackCountPVEffNonCollTrigSelCut3 = cms.Sequence(trackcountNonCollTrigSelCut3 + seqHighPurity + trackcountHpNonCollTrigSelCut3)
seqTrackCountPVEffNonCollTrigSelCut4 = cms.Sequence(trackcountNonCollTrigSelCut4 + seqHighPurity + trackcountHpNonCollTrigSelCut4)
seqTrackCountPVEffNonCollTrigSelCut5 = cms.Sequence(trackcountNonCollTrigSelCut5 + seqHighPurity + trackcountHpNonCollTrigSelCut5)
seqTrackCountPVEffNonCollTrigSelCut6 = cms.Sequence(trackcountNonCollTrigSelCut6 + seqHighPurity + trackcountHpNonCollTrigSelCut6)

seqTrackCountPVEffNonCollTrigSelHpFracCut = cms.Sequence(trackcountNonCollTrigSelHpFracCut)
seqTrackCountPVEffNonCollTrigSelPxProbCut = cms.Sequence(trackcountNonCollTrigSelPxProbCut)
seqTrackCountPVEffNonCollTrigSelLogErrCut = cms.Sequence(trackcountNonCollTrigSelLogErrCut)

seqTrackCountPVEffNonCollTrigSelHpFracVtxCut = cms.Sequence(trackcountNonCollTrigSelHpFracVtxCut)
seqTrackCountPVEffNonCollTrigSelPxProbVtxCut = cms.Sequence(trackcountNonCollTrigSelPxProbVtxCut)

seqTrackCountPVEffNonCollTrackSel = cms.Sequence(trackcountNonCollTrackSel + seqHighPurity + trackcountHpNonCollTrackSel)

seqTrackCountPVEffNonCollTrackSelCut1 = cms.Sequence(trackcountNonCollTrackSelCut1 + seqHighPurity + trackcountHpNonCollTrackSelCut1)
seqTrackCountPVEffNonCollTrackSelCut2 = cms.Sequence(trackcountNonCollTrackSelCut2 + seqHighPurity + trackcountHpNonCollTrackSelCut2)
seqTrackCountPVEffNonCollTrackSelCut3 = cms.Sequence(trackcountNonCollTrackSelCut3 + seqHighPurity + trackcountHpNonCollTrackSelCut3)
seqTrackCountPVEffNonCollTrackSelCut4 = cms.Sequence(trackcountNonCollTrackSelCut4 + seqHighPurity + trackcountHpNonCollTrackSelCut4)
seqTrackCountPVEffNonCollTrackSelCut5 = cms.Sequence(trackcountNonCollTrackSelCut5 + seqHighPurity + trackcountHpNonCollTrackSelCut5)
seqTrackCountPVEffNonCollTrackSelCut6 = cms.Sequence(trackcountNonCollTrackSelCut6 + seqHighPurity + trackcountHpNonCollTrackSelCut6)

