import FWCore.ParameterSet.Config as cms


from TrackingPFG.Configuration.bsRecoSequence_cff import *
from TrackingPFG.Configuration.goodVertexSelector_cfi import *
from TrackingPFG.Configuration.pvSequenceDetailed_cff import *
from TrackingPFG.Configuration.bsSequence_cff import *
from TrackingPFG.Configuration.bspvSequenceDetailed_cff import *

from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.hltSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *

# producer sequences

seqProducersMain = cms.Sequence(seqEventHistoryReco +
                                seqBSRecoBSPVDetailed +
                                seqGoodVerticesBSPVDetailed
                                )

# filter sequences: data


seqOnlyNoScrapingFilters = cms.Sequence(seqBitSelection+
                                    seqNoScrapingSelection
                                    )
# filter sequences: MC


seqOnlyNoScrapingFiltersMC = cms.Sequence(seqBitSelectionMC+
                                    seqNoScrapingSelection
                                    )

# analysis sequences: 

seqOnlyNoScrapingAnalysis = cms.Sequence(seqEventHistory + seqPVAnalyzerBSPVDetailedAOD + seqBSAnalyzerBSPVDetailed + seqBSPVAnalyzerDetailedAOD )

