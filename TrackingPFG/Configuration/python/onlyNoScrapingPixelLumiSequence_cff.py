import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.pvSequence_cff import *
from TrackingPFG.Configuration.simpleTrackSequence_cff import *
from TrackingPFG.Configuration.clusMultInvestPixelLumiSequence_cff import *
from TrackingPFG.Configuration.bsSequence_cff import *
from TrackingPFG.Configuration.bspvSequence_cff import *

seqOnlyNoScrapingPixelLumiAnalysis = cms.Sequence(seqEventHistory +
                                                  seqClusMultInvestOnlyNoScrapingPixelLumi +
                                                  seqPVAnalyzerOnlyNoScrapingPixelLumi)

