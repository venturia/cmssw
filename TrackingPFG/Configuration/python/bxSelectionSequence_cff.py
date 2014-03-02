import FWCore.ParameterSet.Config as cms


bxselection = cms.EDFilter("BXSelect",
  # vector of BX's to select
  SelectBXs = cms.vuint32(45,105,184,263,342,449,528,607,686,813,892,999,1078,1157,1236,1343,1422,1501,1580,1707,1786,1893,1972,2051,2130,2237,2316,2395,2474,2589,2668,2775,2854,2933,3012,3119,3198,3277,3356),
  # window around the BXs to select
  # 1 means only the BX, 2 will select BX-1,BX,BX+1 ; 0 will select nothing
  SelectionWindow = cms.uint32(1)
)
