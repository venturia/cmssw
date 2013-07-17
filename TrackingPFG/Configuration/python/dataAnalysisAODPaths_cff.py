import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.recoConfiguration_cff import *
from TrackingPFG.Configuration.ssqhistorySequence_cff import *
from TrackingPFG.Configuration.bitSelectionSequence_cff import *
from TrackingPFG.Configuration.vertexTracksSelectionSequence_cff import *
#from TrackingPFG.Configuration.eventHistorySequence_cff import *
from TrackingPFG.Configuration.multProdSequence_cff import *
from TrackingPFG.Configuration.nonCollidingSequence_cff import *
from TrackingPFG.Configuration.collidingSequenceAOD_cff import *
from TrackingPFG.Configuration.preScrapingSequenceAOD_cff import *
from TrackingPFG.Configuration.onlyNoScrapingSequenceAOD_cff import *
from TrackingPFG.Configuration.onlyTriggerSequenceAOD_cff import *
from TrackingPFG.Configuration.hltSelectionSequence_cff import *

localV0Candidates.innerHitPosCut = -1

#conversionntuplizer.outfile = "ntuple_conversion_test_data.root"    # output file for conversion ntuples

# producer sequences

seqProducersMain = cms.Sequence(seqEventHistoryReco +
                                seqSSQHistory +
#                                seqMultProd +
                                seqRecoAOD
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
# filter sequences: MC

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

