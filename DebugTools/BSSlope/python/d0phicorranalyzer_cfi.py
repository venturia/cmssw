import FWCore.ParameterSet.Config as cms

d0phicorranalyzer = cms.EDAnalyzer('D0PhiCorrAnalyzer',
                                   trackCollection = cms.InputTag('generalTracks'),
                                   bsCollection = cms.InputTag('offlineBeamSpot'),
                                   errorAsWeight = cms.bool(False)
                      )
