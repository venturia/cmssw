import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.recoConfiguration_cff import *
from TrackingPFG.Configuration.ssqhistorySequence_cff import *
from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
#from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.multProdSequence_cff import *
from TrackingPFG.Configuration.nonCollidingSequence_cff import *  # is it needed??
from TrackingPFG.Configuration.collidingSequence_cff import *
from TrackingPFG.Configuration.preScrapingSequence_cff import *
from TrackingPFG.Configuration.onlyNoScrapingSequence_cff import *
from TrackingPFG.Configuration.onlyTriggerSequence_cff import *
from TrackingPFG.Configuration.hltSelectionSequence_cff import *

#conversionntuplizer.outfile = "ntuple_conversion_test_data.root"    # output file for conversion ntuples

# producer sequences

seqProducersMain = cms.Sequence(seqEventHistoryReco +
                                seqSSQHistory +
                                seqMultProd +
                                seqReco
                                )

# filter sequences: data

seqTriggerFilters = cms.Sequence(seqBitSelection)

seqPVFilters = cms.Sequence(seqBitSelection+
                            seqPVSelection
                            )

seqNoScrapingFilters = cms.Sequence(seqBitSelection+
                                    seqPVSelection+
                                    seqNoScrapingSelection
                                    )

seqOnlyNoScrapingFilters = cms.Sequence(seqBitSelection+
                                    seqNoScrapingSelection
                                    )
# filter sequences: data

seqTriggerFiltersMC = cms.Sequence(seqBitSelectionMC)

seqPVFiltersMC = cms.Sequence(seqBitSelectionMC+
                            seqPVSelection
                            )

seqNoScrapingFiltersMC = cms.Sequence(seqBitSelectionMC+
                                    seqPVSelection+
                                    seqNoScrapingSelection
                                    )

seqOnlyNoScrapingFiltersMC = cms.Sequence(seqBitSelectionMC+
                                    seqNoScrapingSelection
                                    )

# analysis sequences: MOVED!

#seqNoScrapingAnalysis = cms.Sequence(seqEventHistorySelected +
#                                     seqColliding
#                                     )

