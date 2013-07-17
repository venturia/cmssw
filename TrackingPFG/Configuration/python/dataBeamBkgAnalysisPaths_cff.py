import FWCore.ParameterSet.Config as cms



from TrackingPFG.Configuration.eventSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.vertexSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.trackCountPVEffSequence_cff import *

from TrackingPFG.Configuration.eventSelectionNonCollPVEffSequence_cff import *
from TrackingPFG.Configuration.clusMultInvestPVEffSequence_cff import *

from TrackingPFG.Configuration.logErrorSelectionSequence_cff import *

from TrackingPFG.Configuration.eventHistoryPVEffSequence_cff import *



                     
#--------------------------------------------------------------
#non colliding

#no selection

pnoncollnosel = cms.Path(seqNoSelectionNonColl + seqEventHistoryNonColl + seqClusMultInvestPVEffNonColl + seqTrackCountPVEffNonColl)

pnoncollnoselCut5 = cms.Path(seqNoSelectionNonColl + seqPVCut5Selection + seqClusMultInvestPVEffNonCollCut5 + seqTrackCountPVEffNonCollCut5)

pnoncollnoselHpFracCut = cms.Path(seqNoSelectionNonColl + seqHpFracCutSelection + seqClusMultInvestPVEffNonCollHpFracCut + seqTrackCountPVEffNonCollHpFracCut)
pnoncollnoselPxProbCut = cms.Path(seqNoSelectionNonColl + seqPxProbCutSelection + seqClusMultInvestPVEffNonCollPxProbCut + seqTrackCountPVEffNonCollPxProbCut)
pnoncollnoselLogErrTooManyClusterCut = cms.Path(seqNoSelectionNonColl + seqLogErrTooManyClustersSelection + seqClusMultInvestPVEffNonCollLogErrCut + seqTrackCountPVEffNonCollLogErrCut)
pnoncollnoselLogErrTooManySeedsCut = cms.Path(seqNoSelectionNonColl + seqLogErrTooManySeedsSelection + seqClusMultInvestPVEffNonCollLogErrCut + seqTrackCountPVEffNonCollLogErrCut)


# trigger selection paths

pnoncolltrigsel = cms.Path(seqTrigSelectionNonColl + seqEventHistoryNonCollTrigSel + seqClusMultInvestPVEffNonCollTrigSel + seqTrackCountPVEffNonCollTrigSel)

pnoncolltrigselCut5 = cms.Path(seqTrigSelectionNonColl + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelCut5 + seqTrackCountPVEffNonCollTrigSelCut5)

pnoncollnoselTrigSelHpFracCut = cms.Path(seqTrigSelectionNonColl + seqHpFracCutSelection + seqClusMultInvestPVEffNonCollTrigSelHpFracCut + seqTrackCountPVEffNonCollTrigSelHpFracCut)
pnoncollnoselTrigSelPxProbCut = cms.Path(seqTrigSelectionNonColl + seqPxProbCutSelection + seqClusMultInvestPVEffNonCollTrigSelPxProbCut + seqTrackCountPVEffNonCollTrigSelPxProbCut)
pnoncollnoselTrigSelLogErrTooManyClustersCut = cms.Path(seqTrigSelectionNonColl + seqLogErrTooManyClustersSelection + seqClusMultInvestPVEffNonCollTrigSelLogErrCut + seqTrackCountPVEffNonCollTrigSelLogErrCut)
pnoncollnoselTrigSelLogErrTooManySeedsCut = cms.Path(seqTrigSelectionNonColl + seqLogErrTooManySeedsSelection + seqClusMultInvestPVEffNonCollTrigSelLogErrCut + seqTrackCountPVEffNonCollTrigSelLogErrCut)

pnoncollnoselTrigSelHpFracVtxCut = cms.Path(seqTrigSelectionNonColl + seqHpFracCutSelection + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelHpFracVtxCut + seqTrackCountPVEffNonCollTrigSelHpFracVtxCut)
pnoncollnoselTrigSelPxProbVtxCut = cms.Path(seqTrigSelectionNonColl + seqPxProbCutSelection + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelPxProbVtxCut + seqTrackCountPVEffNonCollTrigSelPxProbVtxCut)

