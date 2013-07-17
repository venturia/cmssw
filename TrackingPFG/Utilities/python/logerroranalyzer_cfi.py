import FWCore.ParameterSet.Config as cms

logerroranalyzer = cms.EDAnalyzer("LogErrorAnalyzer",
                            logErrCollection = cms.InputTag("logErrorHarvester")
                           )

