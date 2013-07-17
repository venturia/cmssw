import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.simpleTrackSequence_cff import *
from TrackingPFG.Configuration.clusMultInvestSequence_cff import *

seqPreScrapingAnalysis = cms.Sequence(seqClusMultInvestPreScraping + seqSimpleTrackPreScraping)
