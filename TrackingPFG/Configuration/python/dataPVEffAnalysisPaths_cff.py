import FWCore.ParameterSet.Config as cms



from TrackingPFG.Configuration.eventSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.vertexSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.trackCountPVEffSequence_cff import *

from TrackingPFG.Configuration.eventSelectionNonCollPVEffSequence_cff import *
from TrackingPFG.Configuration.clusMultInvestPVEffSequence_cff import *

from TrackingPFG.Configuration.logErrorSelectionSequence_cff import *

from TrackingPFG.Configuration.eventHistoryPVEffSequence_cff import *



# no selection paths

pnosel = cms.Path(seqNoSelection + seqTrackCountPVEff)

pnoselCut1 = cms.Path(seqNoSelection + seqPVCut1Selection + seqTrackCountPVEffCut1)
pnoselCut2 = cms.Path(seqNoSelection + seqPVCut2Selection + seqTrackCountPVEffCut2)
pnoselCut3 = cms.Path(seqNoSelection + seqPVCut3Selection + seqTrackCountPVEffCut3)
pnoselCut4 = cms.Path(seqNoSelection + seqPVCut4Selection + seqTrackCountPVEffCut4)
pnoselCut5 = cms.Path(seqNoSelection + seqPVCut5Selection + seqTrackCountPVEffCut5)
pnoselCut6 = cms.Path(seqNoSelection + seqPVCut6Selection + seqTrackCountPVEffCut6)

# trigger selection paths

ptrigsel = cms.Path(seqTrigSelection + seqTrackCountPVEffTrigSel)

ptrigselCut1 = cms.Path(seqTrigSelection + seqPVCut1Selection + seqTrackCountPVEffTrigSelCut1)
ptrigselCut2 = cms.Path(seqTrigSelection + seqPVCut2Selection + seqTrackCountPVEffTrigSelCut2)
ptrigselCut3 = cms.Path(seqTrigSelection + seqPVCut3Selection + seqTrackCountPVEffTrigSelCut3)
ptrigselCut4 = cms.Path(seqTrigSelection + seqPVCut4Selection + seqTrackCountPVEffTrigSelCut4)
ptrigselCut5 = cms.Path(seqTrigSelection + seqPVCut5Selection + seqTrackCountPVEffTrigSelCut5)
ptrigselCut6 = cms.Path(seqTrigSelection + seqPVCut6Selection + seqTrackCountPVEffTrigSelCut6)

# track selection paths

ptracksel = cms.Path(seqTrackSelection + seqTrackCountPVEffTrackSel)
                     
ptrackselCut1 = cms.Path(seqTrackSelection + seqPVCut1Selection + seqTrackCountPVEffTrackSelCut1)
ptrackselCut2 = cms.Path(seqTrackSelection + seqPVCut2Selection + seqTrackCountPVEffTrackSelCut2)
ptrackselCut3 = cms.Path(seqTrackSelection + seqPVCut3Selection + seqTrackCountPVEffTrackSelCut3)
ptrackselCut4 = cms.Path(seqTrackSelection + seqPVCut4Selection + seqTrackCountPVEffTrackSelCut4)
ptrackselCut5 = cms.Path(seqTrackSelection + seqPVCut5Selection + seqTrackCountPVEffTrackSelCut5)
ptrackselCut6 = cms.Path(seqTrackSelection + seqPVCut6Selection + seqTrackCountPVEffTrackSelCut6)
                     
#--------------------------------------------------------------
#non colliding

#no selection

pnoncollnosel = cms.Path(seqNoSelectionNonColl + seqEventHistoryNonColl + seqClusMultInvestPVEffNonColl + seqTrackCountPVEffNonColl)

pnoncollnoselCut1 = cms.Path(seqNoSelectionNonColl + seqPVCut1Selection + seqClusMultInvestPVEffNonCollCut1 + seqTrackCountPVEffNonCollCut1)
pnoncollnoselCut2 = cms.Path(seqNoSelectionNonColl + seqPVCut2Selection + seqClusMultInvestPVEffNonCollCut2 + seqTrackCountPVEffNonCollCut2)
pnoncollnoselCut3 = cms.Path(seqNoSelectionNonColl + seqPVCut3Selection + seqClusMultInvestPVEffNonCollCut3 + seqTrackCountPVEffNonCollCut3)
pnoncollnoselCut4 = cms.Path(seqNoSelectionNonColl + seqPVCut4Selection + seqClusMultInvestPVEffNonCollCut4 + seqTrackCountPVEffNonCollCut4)
pnoncollnoselCut5 = cms.Path(seqNoSelectionNonColl + seqPVCut5Selection + seqClusMultInvestPVEffNonCollCut5 + seqTrackCountPVEffNonCollCut5)
pnoncollnoselCut6 = cms.Path(seqNoSelectionNonColl + seqPVCut6Selection + seqClusMultInvestPVEffNonCollCut6 + seqTrackCountPVEffNonCollCut6)

pnoncollnoselHpFracCut = cms.Path(seqNoSelectionNonColl + seqHpFracCutSelection + seqClusMultInvestPVEffNonCollHpFracCut + seqTrackCountPVEffNonCollHpFracCut)
pnoncollnoselPxProbCut = cms.Path(seqNoSelectionNonColl + seqPxProbCutSelection + seqClusMultInvestPVEffNonCollPxProbCut + seqTrackCountPVEffNonCollPxProbCut)
pnoncollnoselLogErrTooManyClustersCut = cms.Path(seqNoSelectionNonColl + seqLogErrTooManyClustersSelection + seqClusMultInvestPVEffNonCollLogErrCut + seqTrackCountPVEffNonCollLogErrCut)
pnoncollnoselLogErrTooManySeedsCut = cms.Path(seqNoSelectionNonColl + seqLogErrTooManySeedsSelection + seqClusMultInvestPVEffNonCollLogErrCut + seqTrackCountPVEffNonCollLogErrCut)


# trigger selection paths

pnoncolltrigsel = cms.Path(seqTrigSelectionNonColl + seqEventHistoryNonCollTrigSel + seqClusMultInvestPVEffNonCollTrigSel + seqTrackCountPVEffNonCollTrigSel)

pnoncolltrigselCut1 = cms.Path(seqTrigSelectionNonColl + seqPVCut1Selection + seqClusMultInvestPVEffNonCollTrigSelCut1 + seqTrackCountPVEffNonCollTrigSelCut1)
pnoncolltrigselCut2 = cms.Path(seqTrigSelectionNonColl + seqPVCut2Selection + seqClusMultInvestPVEffNonCollTrigSelCut2 + seqTrackCountPVEffNonCollTrigSelCut2)
pnoncolltrigselCut3 = cms.Path(seqTrigSelectionNonColl + seqPVCut3Selection + seqClusMultInvestPVEffNonCollTrigSelCut3 + seqTrackCountPVEffNonCollTrigSelCut3)
pnoncolltrigselCut4 = cms.Path(seqTrigSelectionNonColl + seqPVCut4Selection + seqClusMultInvestPVEffNonCollTrigSelCut4 + seqTrackCountPVEffNonCollTrigSelCut4)
pnoncolltrigselCut5 = cms.Path(seqTrigSelectionNonColl + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelCut5 + seqTrackCountPVEffNonCollTrigSelCut5)
pnoncolltrigselCut6 = cms.Path(seqTrigSelectionNonColl + seqPVCut6Selection + seqClusMultInvestPVEffNonCollTrigSelCut6 + seqTrackCountPVEffNonCollTrigSelCut6)

pnoncollnoselTrigSelHpFracCut = cms.Path(seqTrigSelectionNonColl + seqHpFracCutSelection + seqClusMultInvestPVEffNonCollTrigSelHpFracCut + seqTrackCountPVEffNonCollTrigSelHpFracCut)
pnoncollnoselTrigSelPxProbCut = cms.Path(seqTrigSelectionNonColl + seqPxProbCutSelection + seqClusMultInvestPVEffNonCollTrigSelPxProbCut + seqTrackCountPVEffNonCollTrigSelPxProbCut)
pnoncollnoselTrigSelLogErrTooManyClustersCut = cms.Path(seqTrigSelectionNonColl + seqLogErrTooManyClustersSelection + seqClusMultInvestPVEffNonCollTrigSelLogErrCut + seqTrackCountPVEffNonCollTrigSelLogErrCut)
pnoncollnoselTrigSelLogErrTooManySeedsCut = cms.Path(seqTrigSelectionNonColl + seqLogErrTooManySeedsSelection + seqClusMultInvestPVEffNonCollTrigSelLogErrCut + seqTrackCountPVEffNonCollTrigSelLogErrCut)

pnoncollnoselTrigSelHpFracVtxCut = cms.Path(seqTrigSelectionNonColl + seqHpFracCutSelection + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelHpFracVtxCut + seqTrackCountPVEffNonCollTrigSelHpFracVtxCut)
pnoncollnoselTrigSelPxProbVtxCut = cms.Path(seqTrigSelectionNonColl + seqPxProbCutSelection + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrigSelPxProbVtxCut + seqTrackCountPVEffNonCollTrigSelPxProbVtxCut)

# track selection paths

pnoncolltracksel = cms.Path(seqTrackSelectionNonColl + seqEventHistoryNonCollTrackSel + seqClusMultInvestPVEffNonCollTrackSel + seqTrackCountPVEffNonCollTrackSel)
                     
pnoncolltrackselCut1 = cms.Path(seqTrackSelectionNonColl + seqPVCut1Selection + seqClusMultInvestPVEffNonCollTrackSelCut1 + seqTrackCountPVEffNonCollTrackSelCut1)
pnoncolltrackselCut2 = cms.Path(seqTrackSelectionNonColl + seqPVCut2Selection + seqClusMultInvestPVEffNonCollTrackSelCut2 + seqTrackCountPVEffNonCollTrackSelCut2)
pnoncolltrackselCut3 = cms.Path(seqTrackSelectionNonColl + seqPVCut3Selection + seqClusMultInvestPVEffNonCollTrackSelCut3 + seqTrackCountPVEffNonCollTrackSelCut3)
pnoncolltrackselCut4 = cms.Path(seqTrackSelectionNonColl + seqPVCut4Selection + seqClusMultInvestPVEffNonCollTrackSelCut4 + seqTrackCountPVEffNonCollTrackSelCut4)
pnoncolltrackselCut5 = cms.Path(seqTrackSelectionNonColl + seqPVCut5Selection + seqClusMultInvestPVEffNonCollTrackSelCut5 + seqTrackCountPVEffNonCollTrackSelCut5)
pnoncolltrackselCut6 = cms.Path(seqTrackSelectionNonColl + seqPVCut6Selection + seqClusMultInvestPVEffNonCollTrackSelCut6 + seqTrackCountPVEffNonCollTrackSelCut6)
