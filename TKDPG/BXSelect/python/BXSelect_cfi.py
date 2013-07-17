import FWCore.ParameterSet.Config as cms

bxSelect = cms.EDFilter("BXSelect",
  # vector of BX's to select
  SelectBXs = cms.vuint32(51),
  # window around the BXs to select
  # 1 means only the BX, 2 will select BX-1,BX,BX+1 ; 0 will select nothing
  SelectionWindow = cms.uint32(1)
)
