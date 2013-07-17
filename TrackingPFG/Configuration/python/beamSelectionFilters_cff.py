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


#BPTX OR and XOR

#HLTLevel1GTSeed used to avoid inconsistency with random triggers
 
#bptxOr = cms.EDFilter("L1Filter",
#                      inputTag = cms.InputTag("gtDigis"),
#                      useAODRecord = cms.bool(False),
#                      useFinalDecision = cms.bool(False),
#                      algorithms = cms.vstring("L1_BptxPlusORMinus")
#                      )


bptxOr = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(False), L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
                               L1SeedsLogicalExpression = cms.string('L1_BptxPlusORMinus'))
seqBPTXOrSelection = cms.Sequence(bptxOr * ~bptxAnd)


#BPTX Plus Only

#bptxPlus = bptxOr.clone(algorithms=cms.vstring("L1_BptxPlus"))
bptxPlus = bptxOr.clone(L1SeedsLogicalExpression=cms.string("L1_BptxPlus"))
#bptxPlus = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('1'))


bptxPlusOnly = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(False), L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
                                     L1SeedsLogicalExpression = cms.string('L1_BptxPlus_NotBptxMinus'))


#BPTX Minus Only

#bptxMinus = bptxOr.clone(algorithms=cms.vstring("L1_BptxMinus"))
bptxMinus = bptxOr.clone(L1SeedsLogicalExpression=cms.string("L1_BptxMinus"))
#bptxMinus = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('2'))


bptxMinusOnly = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(False), L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
                                     L1SeedsLogicalExpression = cms.string('L1_BptxMinus_NotBptxPlus'))

