import FWCore.ParameterSet.Config as cms



# Dummy

#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
#hltSelection = hltHighLevel.clone(HLTPaths = cms.vstring("*"), throw = cms.bool(False))

# New filter which is able to select on L1 algos too

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import *
hltSelection = triggerResultsFilter.clone(
                                          triggerConditions = cms.vstring("HLT_*"),
                                          hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                          l1tResults = cms.InputTag( "" ),
                                          throw = cms.bool(False)
                                          )


#

seqHLTSelection = cms.Sequence(hltSelection)



## Minimum Bias
#
#hltMinimumBiasSelection = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_L1_BscMinBiasOR_BptxPlusORMinus","HLT_L1Tech_BSC_minBias_OR"), throw = cms.bool(False))
#seqHLTMinBiasSelection = cms.Sequence(hltMinimumBiasSelection)
#
## Jet6U
#
#hltJet6USelection = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_L1Jet6U"))
#seqHLTJet6USelection = cms.Sequence(hltJet6USelection)
#
## SingleEG2
#
#hltSingleEG2Selection = hltHighLevel.clone(HLTPaths = cms.vstring("HLT_L1SingleEG2"))
#seqHLTSingleEG2Selection = cms.Sequence(hltSingleEG2Selection)



