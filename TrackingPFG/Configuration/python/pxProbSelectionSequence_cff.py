import FWCore.ParameterSet.Config as cms

pxprobfilter = cms.EDFilter("FilterScrapingPixelProbability",
                            apply_filter                 = cms.untracked.bool( True  ),
                            select_collision             = cms.untracked.bool( True ),
                            select_pkam                  = cms.untracked.bool( False ),
                            select_other                 = cms.untracked.bool( False ),
                            low_probability              = cms.untracked.double( 0.0 ),
                            low_probability_fraction_cut = cms.untracked.double( 0.4 )
                            )

seqPxProbFilter = cms.Sequence(pxprobfilter)

