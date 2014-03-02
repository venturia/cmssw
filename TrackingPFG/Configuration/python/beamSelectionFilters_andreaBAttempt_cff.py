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

#

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import *
triggerSelection = triggerResultsFilter.clone(
                                 triggerConditions = cms.vstring(),
                                 hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                 l1tResults = cms.InputTag( "gtDigis" ),
                                 l1tIgnoreMask = cms.bool( True ),
                                 l1techIgnorePrescales  = cms.bool( True)
                                 )

#bit 0 selection: BPTX_AND

#bptxAnd = triggerSelection.clone(triggerConditions = cms.vstring("L1Tech_BPTX_plus_AND_minus"))  this work in 2011 and in 2010 since run 142653
bptxAnd = triggerSelection.clone(triggerConditions = cms.vstring("L1Tech_BPTX_plus_AND_minus OR L1_ZeroBias"))

seqBPTXAndSelection = cms.Sequence(bptxAnd)

#BPTX OR and XOR

#HLTLevel1GTSeed used to avoid inconsistency with random triggers
 

bptxOr = triggerSelection.clone(triggerConditions = cms.vstring("L1Tech_BPTX_plus_OR_minus"))
seqBPTXOrSelection = cms.Sequence(bptxOr * ~bptxAnd)

#BPTX Plus Only

bptxPlusOnly = triggerSelection.clone(triggerConditions = cms.vstring("L1Tech_BPTX_plus AND NOT L1Tech_BPTX_minus"))
seqBPTXPlusSelection = cms.Sequence(bptxPlusOnly)

#BPTX Minus Only

bptxMinusOnly = triggerSelection.clone(triggerConditions = cms.vstring("L1Tech_BPTX_minus AND NOT L1Tech_BPTX_plus"))
seqBPTXMinusSelection = cms.Sequence(bptxMinusOnly)

