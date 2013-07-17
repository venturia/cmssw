import FWCore.ParameterSet.Config as cms

# Event History

froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                              l1ABCCollection=cms.InputTag("scalersRawToDigi")
                              )


# APVPhases

from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1abc_GR09_cfi import *

# event distribution monitoring

from DPGAnalysis.SiStripTools.eventtimedistribution_cfi import *
eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")

eventtimedistribAND = eventtimedistribution.clone()
eventtimedistribNotANDandPlus = eventtimedistribution.clone()
eventtimedistribNotANDandMinus = eventtimedistribution.clone()
eventtimedistribNotANDandOR = eventtimedistribution.clone()
                            
eventtimedistribANDTT = eventtimedistribution.clone()
eventtimedistribNotANDandPlusTT = eventtimedistribution.clone()
eventtimedistribNotANDandMinusTT = eventtimedistribution.clone()
eventtimedistribNotANDandORTT = eventtimedistribution.clone()

# Filters

bptxOr = cms.EDFilter("L1Filter",
                      inputTag = cms.InputTag("gtDigis"),
                      useAODRecord = cms.bool(False),
                      useFinalDecision = cms.bool(False),
                      algorithms = cms.vstring("L1_BptxPlusORMinus")
                      )
bptxPlus = bptxOr.clone(algorithms=cms.vstring("L1_BptxPlus"))
bptxMinus = bptxOr.clone(algorithms=cms.vstring("L1_BptxMinus"))
bptxAnd = bptxOr.clone(algorithms=cms.vstring("L1_ZeroBias_Ext"))  #???

from L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff import *
from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed
es_prefer_l1GtTriggerMaskTechTrig = cms.ESPrefer("L1GtTriggerMaskTechTrigTrivialProducer","l1GtTriggerMaskTechTrig")

#bit 0 selection: BPTX_AND

bptxAndTT = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0'))


# Sequence

seqEventHistoryAll = cms.Sequence(froml1abcHEs + APVPhases + eventtimedistribution )

seqEventHistoryAND = cms.Sequence(bptxAnd + froml1abcHEs + APVPhases + eventtimedistribAND )
seqEventHistoryNotANDandPlus = cms.Sequence(~bptxAnd + bptxPlus + froml1abcHEs + APVPhases + eventtimedistribNotANDandPlus )
seqEventHistoryNotANDandMinus = cms.Sequence(~bptxAnd + bptxMinus + froml1abcHEs + APVPhases + eventtimedistribNotANDandMinus )
seqEventHistoryNotANDandOR = cms.Sequence(~bptxAnd + bptxOr + froml1abcHEs + APVPhases + eventtimedistribNotANDandOR )

seqEventHistoryANDTT = cms.Sequence(bptxAndTT + froml1abcHEs + APVPhases + eventtimedistribANDTT )
seqEventHistoryNotANDandPlusTT = cms.Sequence(~bptxAndTT + bptxPlus + froml1abcHEs + APVPhases + eventtimedistribNotANDandPlusTT )
seqEventHistoryNotANDandMinusTT = cms.Sequence(~bptxAndTT + bptxMinus + froml1abcHEs + APVPhases + eventtimedistribNotANDandMinusTT )
seqEventHistoryNotANDandORTT = cms.Sequence(~bptxAndTT + bptxOr + froml1abcHEs + APVPhases + eventtimedistribNotANDandORTT )

