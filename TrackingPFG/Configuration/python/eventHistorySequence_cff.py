import FWCore.ParameterSet.Config as cms

# Event History

froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                              l1ABCCollection=cms.InputTag("scalersRawToDigi")
                              )


# APVPhases

#from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts_cfi import *
from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts2011_cfi import *

# event distribution monitoring

from DPGAnalysis.SiStripTools.eventtimedistribution_cfi import *
eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")

eventtimedistribselected = eventtimedistribution.clone()

eventtimedistribnoncollidingearly = eventtimedistribution.clone()
eventtimedistribnoncollidingskim = eventtimedistribution.clone()

eventtimedistribnoncolliding = eventtimedistribution.clone()
eventtimedistribnoncollidingplus = eventtimedistribution.clone()
eventtimedistribnoncollidingminus = eventtimedistribution.clone()
                            
eventtimedistribnoncollidinggoodvtx = eventtimedistribution.clone()
eventtimedistribnoncollidingplusgoodvtx = eventtimedistribution.clone()
eventtimedistribnoncollidingminusgoodvtx = eventtimedistribution.clone()
                            
eventtimedistriblogerranyerror = eventtimedistribution.clone()
eventtimedistriblogerrtoomanyclusters = eventtimedistribution.clone()
eventtimedistriblogerrtoomanyseeds = eventtimedistribution.clone()
eventtimedistriblogerrtoomanytriplets = eventtimedistribution.clone()
eventtimedistriblogerrtracking = eventtimedistribution.clone()
eventtimedistriblogerrcosmicregional = eventtimedistribution.clone()

                            

# Sequence

seqEventHistoryReco = cms.Sequence(froml1abcHEs + APVPhases)
seqEventHistory = cms.Sequence(eventtimedistribution )
seqEventHistorySelected = cms.Sequence(eventtimedistribselected )
seqEventHistoryNonCollidingSkim = cms.Sequence(eventtimedistribnoncollidingskim )
seqEventHistoryNonCollidingEarly = cms.Sequence(eventtimedistribnoncollidingearly )
seqEventHistoryNonColliding = cms.Sequence(eventtimedistribnoncolliding )
seqEventHistoryNonCollidingPlus = cms.Sequence(eventtimedistribnoncollidingplus )
seqEventHistoryNonCollidingMinus = cms.Sequence(eventtimedistribnoncollidingminus )
seqEventHistoryNonCollidingGoodVtx = cms.Sequence(eventtimedistribnoncollidinggoodvtx )
seqEventHistoryNonCollidingPlusGoodVtx = cms.Sequence(eventtimedistribnoncollidingplusgoodvtx )
seqEventHistoryNonCollidingMinusGoodVtx = cms.Sequence(eventtimedistribnoncollidingminusgoodvtx )

seqEventHistoryLogErrAnyError = cms.Sequence(eventtimedistriblogerranyerror )
seqEventHistoryLogErrTooManyClusters = cms.Sequence(eventtimedistriblogerrtoomanyclusters )
seqEventHistoryLogErrTooManySeeds = cms.Sequence(eventtimedistriblogerrtoomanyseeds )
seqEventHistoryLogErrTooManyTriplets = cms.Sequence(eventtimedistriblogerrtoomanytriplets )
seqEventHistoryLogErrTracking = cms.Sequence(eventtimedistriblogerrtracking )
seqEventHistoryLogErrCosmicRegional = cms.Sequence(eventtimedistriblogerrcosmicregional )

