import FWCore.ParameterSet.Config as cms

overlapproblemtsosanalyzer = cms.EDAnalyzer("OverlapProblemTSOSAnalyzer",
                                            trajTrackAssoCollection = cms.InputTag("refittedTracks"),
                                            onlyValidRecHit = cms.bool(True)
                                            )

