import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.pvSequence_cff import *
from TrackingPFG.Configuration.simpleTrackSequence_cff import *
from TrackingPFG.Configuration.clusMultInvestSequence_cff import *
from TrackingPFG.Configuration.bsSequence_cff import *
from TrackingPFG.Configuration.bspvSequence_cff import *

seqOnlyNoScrapingAnalysis = cms.Sequence(
#    seqClusMultInvestOnlyNoScraping +
    seqSimpleTrackOnlyNoScraping +
    seqBSAnalyzer +
    seqBSPVAnalyzerOnlyNoScraping +
    seqPVAnalyzerOnlyNoScrapingAOD)
