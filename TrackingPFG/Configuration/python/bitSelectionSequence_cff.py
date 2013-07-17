import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.beamSelectionFilters_andreaBAttempt_cff import *

seqBSC4041Selection = cms.Sequence(bit4041
#                                   + bit36373839
                                   )

# PhysDecl bit

#from HLTrigger.HLTfilters.hltHighLevelDev_cfi import hltHighLevelDev
#physDecl = hltHighLevelDev.clone(HLTPaths = ['HLT_PhysicsDeclared'], HLTPathsPrescales = [1])
#seqPhysDeclBitSelection = cms.Sequence(physDecl)

from HLTrigger.special.hltPhysicsDeclared_cfi import *
hltPhysicsDeclared.L1GtReadoutRecordTag = 'gtDigis'
seqPhysDeclBitSelection = cms.Sequence(hltPhysicsDeclared)



seqPhysCollSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXAndSelection)

seqBitSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXAndSelection
#    + seqBSC4041Selection
    )

seqPhysCollSelectionMC = cms.Sequence(seqPhysDeclBitSelection)

seqBitSelectionMC = cms.Sequence(
#    seqPhysDeclBitSelection +
#    seqBSC4041Selection
    )

seqNonCollidingSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXOrSelection)
seqNonCollidingPlusSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXPlusSelection)
seqNonCollidingMinusSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXMinusSelection)

seqNonCollidingBitSelection = cms.Sequence(
#    seqPhysDeclBitSelection +
    seqBPTXOrSelection + seqBSC4041Selection)

seqBitSelectionNoPhys = cms.Sequence(seqBPTXAndSelection + seqBSC4041Selection)

seqNonCollidingSelectionNoPhys = cms.Sequence(seqBPTXOrSelection)
seqNonCollidingPlusSelectionNoPhys = cms.Sequence(seqBPTXPlusSelection)
seqNonCollidingMinusSelectionNoPhys = cms.Sequence(seqBPTXMinusSelection)


# there is another prescription to use HLTHighLevel instead of HLTHighLevelDev

