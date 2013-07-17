import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.recoConfiguration_cff import *
from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.apvNoiseSequence_cff import *
from TrackingPFG.Configuration.multProdSequence_cff import *
from TrackingPFG.Configuration.nonCollidingSequence_cff import *
#from TrackingPFG.Configuration.collidingSequence_cff import *
#from TrackingPFG.Configuration.preScrapingSequence_cff import *
#from TrackingPFG.Configuration.hltSelectionSequence_cff import *

#---------APV induced noisy events

plat1   = cms.Path(seqBitSelection + seqEventHistoryReco + seqLatencyPlusOne)
pfhmax1 = cms.Path(seqBitSelection + seqEventHistoryReco + seqFrameHeaderMax1)
pfhmax2 = cms.Path(seqBitSelection + seqEventHistoryReco + seqFrameHeaderMax2)


#---------Non colliding BX events

#pnoncollskim = cms.Path(seqNonCollidingSelection + seqNonCollidingSkim +
#                                seqEventHistoryReco + seqEventHistoryNonCollidingSkim )

pnoncollearly = cms.Path(seqNonCollidingSelection +
                         seqEventHistoryReco + seqMultProd + seqRecoNonColliding + 
                         seqEventHistoryNonCollidingEarly + seqNonCollidingEarly)

pnoncoll = cms.Path(seqNonCollidingSelection + seqLargeSiPixelSelection +
                    seqEventHistoryReco + seqMultProd + seqRecoNonColliding + 
                    seqNonColliding + seqEventHistoryNonColliding)

pnoncollplus = cms.Path(seqNonCollidingPlusSelection + seqLargeSiPixelSelection +
                        seqEventHistoryReco +  seqRecoNonColliding + 
                        seqNonCollidingPlus + seqEventHistoryNonCollidingPlus)

pnoncollminus = cms.Path(seqNonCollidingMinusSelection + seqLargeSiPixelSelection +
                         seqEventHistoryReco + seqRecoNonColliding + 
                         seqNonCollidingMinus + seqEventHistoryNonCollidingMinus)

#----Non Colliding BX events with one PV with good quality

pnoncollgoodvtx = cms.Path(seqNonCollidingSelection + seqLargeSiPixelSelection + 
                           seqEventHistoryReco + seqRecoNonColliding + 
                           seqGoodDisplacedPVSelection +
                           seqNonCollidingGoodVtx + seqEventHistoryNonCollidingGoodVtx)

pnoncollplusgoodvtx = cms.Path(seqNonCollidingPlusSelection + seqLargeSiPixelSelection + 
                               seqEventHistoryReco + seqRecoNonColliding + 
                               seqGoodDisplacedPVSelection +
#                               seqNonCollidingPlusGoodVtx +
                               seqEventHistoryNonCollidingPlusGoodVtx)

pnoncollminusgoodvtx = cms.Path(seqNonCollidingMinusSelection + seqLargeSiPixelSelection + 
                                seqEventHistoryReco + seqRecoNonColliding + 
                                seqGoodDisplacedPVSelection +
#                                seqNonCollidingMinusGoodVtx +
                                seqEventHistoryNonCollidingMinusGoodVtx)

