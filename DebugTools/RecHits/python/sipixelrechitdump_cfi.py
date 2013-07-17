import FWCore.ParameterSet.Config as cms

sipixelrechitdump = cms.EDAnalyzer('SiPixelRecHitsDump',
                                   siPixelRHCollection = cms.InputTag('siPixelRecHits')
                      )
