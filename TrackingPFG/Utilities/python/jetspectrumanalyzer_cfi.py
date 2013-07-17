import FWCore.ParameterSet.Config as cms

jetspectrumanalyzer = cms.EDAnalyzer("JetSpectrumAnalyzer",
                                     jetCollection = cms.InputTag("ak5CaloJets"),
                                     jetIDMap = cms.InputTag("ak5JetID"),
                                     maxRapidityCut = cms.double(999.0)
                         )

