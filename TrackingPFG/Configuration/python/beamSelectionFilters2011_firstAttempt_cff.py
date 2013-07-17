import FWCore.ParameterSet.Config as cms

from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed
#hltLevel1GTSeed.L1NrBxInEvent = 1 # check the impact on BSC veto!!

# unmask masked bits

from L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff import *
es_prefer_l1GtTriggerMaskTechTrig = cms.ESPrefer("L1GtTriggerMaskTechTrigTrivialProducer","l1GtTriggerMaskTechTrig")

from L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff import *
es_prefer_l1GtTriggerMaskAlgoTrig = cms.ESPrefer("L1GtTriggerMaskAlgoTrigTrivialProducer","l1GtTriggerMaskAlgoTrig")

# bit 40+41 no BH  selection

bit4041 = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('(40 OR 41)'))

bit36373839 = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)'))


#bit 0 selection: BPTX_AND

bptxAnd = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0'))

#bptxAnd = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(False), L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
#                                L1SeedsLogicalExpression = cms.string('L1_BptxPlus AND L1_BptxMinus'))

seqBPTXAndSelection = cms.Sequence(bptxAnd)

#BPTX OR and XOR

#HLTLevel1GTSeed used to avoid inconsistency with random triggers
 

bptxOr = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('3'))

seqBPTXOrSelection = cms.Sequence(bptxOr * ~bptxAnd)

#BPTX Plus Only

bptxPlus = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('1'))
seqBPTXPlusSelection = cms.Sequence(bptxPlus + ~bptxAnd)

#BPTX Minus Only

bptxMinus = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('2'))
seqBPTXMinusSelection = cms.Sequence(bptxMinus + ~bptxAnd)
