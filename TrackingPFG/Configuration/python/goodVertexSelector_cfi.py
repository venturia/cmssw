import FWCore.ParameterSet.Config as cms

# one PV

goodVertices = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
#   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 15 && position.Rho <= 2"),  # old cut
#   cut = cms.string("!isFake && ndof >= 5 && abs(z) <= 24 && position.Rho <= 2"),  
   cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),  
   filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

goodVerticesDA = goodVertices.clone(src=cms.InputTag("offlinePrimaryVerticesDA"))


goodDisplacedVertices = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && ndof > 4 && position.Rho <= 2" ),
   filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

realPixelVertices = cms.EDFilter("VertexSelector",
   src = cms.InputTag("pixelVertices"),
   cut = cms.string("!isFake" ),
   filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

goodDisplacedVerticesWithBS = goodDisplacedVertices.clone(src = cms.InputTag("offlinePrimaryVerticesWithBS"),
                                                          cut = cms.string("!isFake && ndof > 7 && position.Rho <= 2" ))
goodDisplacedVerticesDA = goodDisplacedVertices.clone(src = cms.InputTag("offlinePrimaryVerticesDA"))
goodDisplacedVerticesDAWithBS = goodDisplacedVertices.clone(src = cms.InputTag("offlinePrimaryVerticesDAWithBS"),
                                                            cut = cms.string("!isFake && ndof > 7 && position.Rho <= 2" ))

seqGoodVertices = cms.Sequence(goodVertices + goodDisplacedVertices + realPixelVertices
#                               + goodVerticesDA
                               )
seqGoodVerticesAOD = cms.Sequence(goodVertices + goodDisplacedVertices
#                               + goodVerticesDA
                               )
seqGoodVerticesPixelLumi = cms.Sequence(goodVertices + goodDisplacedVertices)

seqGoodVerticesDetailed = cms.Sequence(goodDisplacedVertices + goodDisplacedVerticesDA + goodDisplacedVerticesWithBS + goodDisplacedVerticesDAWithBS)

seqGoodVerticesBSPVDetailed = cms.Sequence(goodDisplacedVertices)

