import FWCore.ParameterSet.Config as cms



from TrackingPFG.Configuration.eventSelectionPVEffSequence_MC_cff import *
from TrackingPFG.Configuration.vertexSelectionPVEffSequence_cff import *
from TrackingPFG.Configuration.trackCountPVEffSequence_cff import *

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
                     
