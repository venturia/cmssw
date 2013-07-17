import FWCore.ParameterSet.Config as cms

# one PV

oneGoodVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("goodVertices"),
#   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 15 && position.Rho <= 2"),  # old cut
#   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 24 && position.Rho <= 2"),  
   cut = cms.string("!isFake"),  # the cut is applied to the "goodVertices" collection
   filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)
seqPVSelection = cms.Sequence(oneGoodVertexFilter)

# against scraping events: high purity tracks

noScraping= cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.2)  # to be updated
)
seqNoScrapingSelection = cms.Sequence(noScraping)

# Pixel probability selection

#from TrackingPFG.Configuration.pxProbSelectionSequence_cff import *
#seqPxProbCutSelection = cms.Sequence(seqPxProbFilter)

# one good displaced PV

goodDisplacedVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("goodDisplacedVertices"),
   cut = cms.string("!isFake" ), # the cut is applied to the "goodDisplacedVertices" collection
   filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)
seqGoodDisplacedPVSelection = cms.Sequence(goodDisplacedVertexFilter)

