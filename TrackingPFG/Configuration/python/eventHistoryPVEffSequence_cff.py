import FWCore.ParameterSet.Config as cms

# Event History

froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                              l1ABCCollection=cms.InputTag("scalersRawToDigi")
                              )


# APVPhases

from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts_cfi import *

# event distribution monitoring

from DPGAnalysis.SiStripTools.eventtimedistribution_cfi import *
eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")

eventtimedistribnoncoll = eventtimedistribution.clone()
eventtimedistribnoncollTrigSel = eventtimedistribution.clone()
eventtimedistribnoncollTrackSel = eventtimedistribution.clone()

# Sequence

seqEventHistoryNonColl = cms.Sequence(froml1abcHEs + APVPhases + eventtimedistribnoncoll )
seqEventHistoryNonCollTrigSel = cms.Sequence(froml1abcHEs + APVPhases + eventtimedistribnoncollTrigSel )
seqEventHistoryNonCollTrackSel = cms.Sequence(froml1abcHEs + APVPhases + eventtimedistribnoncollTrackSel )

