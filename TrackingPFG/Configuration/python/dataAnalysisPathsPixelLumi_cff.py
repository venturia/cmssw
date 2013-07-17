import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.recoConfiguration_cff import *
from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
#from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.multProdPixelLumiSequence_cff import *
from TrackingPFG.Configuration.onlyNoScrapingPixelLumiSequence_cff import *
from TrackingPFG.Configuration.hltSelectionSequence_cff import *

#conversionntuplizer.outfile = "ntuple_conversion_test_data.root"    # output file for conversion ntuples

# producer sequences

seqProducersMain = cms.Sequence(seqEventHistoryReco +
                                seqMultProdPixelLumi +
                                seqRecoPixelLumi
                                )

# filter sequences: data

seqOnlyNoScrapingFilters = cms.Sequence(seqBitSelection+
                                    seqNoScrapingSelection
                                    )
# filter sequences: data

seqOnlyNoScrapingFiltersMC = cms.Sequence(seqBitSelectionMC+
                                    seqNoScrapingSelection
                                    )

# analysis sequences: MOVED!

#seqNoScrapingAnalysis = cms.Sequence(seqEventHistorySelected +
#                                     seqColliding
#                                     )

