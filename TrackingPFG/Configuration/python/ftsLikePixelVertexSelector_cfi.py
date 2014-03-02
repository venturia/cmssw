import FWCore.ParameterSet.Config as cms

# one PV

ftsLikePixelVertexFilter = cms.EDFilter("VertexSelector",
                                        src = cms.InputTag("pixelVertices"),
                                        cut = cms.string('!isFake & ndof>=2'),
                                        filter = cms.bool(False),   # otherwise it won't filter the events, just produce an empty vertex collection.
)
