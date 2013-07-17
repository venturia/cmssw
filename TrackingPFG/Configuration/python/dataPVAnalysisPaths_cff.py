import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff import *
from Configuration.StandardSequences.GeometryDB_cff import *
from Configuration.StandardSequences.Reconstruction_cff import *

from TrackingPFG.Configuration.pixelVertexRecoSequence_cff import *
from TrackingPFG.Configuration.goodVertexSelector_cfi import *
from TrackingPFG.Configuration.pvSequenceDetailed_cff import *
from TrackingPFG.Configuration.bsSequence_cff import *

from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.hltSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *

# producer sequences

seqProducersMain = cms.Sequence(seqEventHistoryReco +
                                seqVertexRecoDetailed +
                                seqGoodVerticesDetailed
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

seqOnlyNoScrapingAnalysis = cms.Sequence(seqEventHistory + seqPVAnalyzerDetailed + seqBSAnalyzerDetailed)

