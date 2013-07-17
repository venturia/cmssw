import FWCore.ParameterSet.Config as cms

bxlumianalyzer = cms.EDAnalyzer("BXLumiAnalyzer",
                                lumiCollection = cms.InputTag("lumiProducer"),
                                maxLSBeforeRebin = cms.uint32(100),
                                runHisto = cms.bool(False)
                           )

