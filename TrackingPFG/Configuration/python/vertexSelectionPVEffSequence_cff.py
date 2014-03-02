import FWCore.ParameterSet.Config as cms

# one PV

vertexFilter = cms.EDFilter("VertexSelector",
                            src = cms.InputTag("offlinePrimaryVertices"),
                            cut = cms.string("!isFake && ndof > 0 && abs(z) <= 15 && position.Rho <= 2"),
                            filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
                            )

vertexFilterCut1 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 0 && abs(z) <= 15 && position.Rho <= 2"))
vertexFilterCut2 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 1 && abs(z) <= 15 && position.Rho <= 2"))
vertexFilterCut3 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 2 && abs(z) <= 15 && position.Rho <= 2"))
vertexFilterCut4 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 3 && abs(z) <= 15 && position.Rho <= 2"))
vertexFilterCut5 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"))
vertexFilterCut6 = vertexFilter.clone(cut = cms.string("!isFake && ndof > 5 && abs(z) <= 15 && position.Rho <= 2"))

seqPVCut1Selection = cms.Sequence(vertexFilterCut1)
seqPVCut2Selection = cms.Sequence(vertexFilterCut2)
seqPVCut3Selection = cms.Sequence(vertexFilterCut3)
seqPVCut4Selection = cms.Sequence(vertexFilterCut4)
seqPVCut5Selection = cms.Sequence(vertexFilterCut5)
seqPVCut6Selection = cms.Sequence(vertexFilterCut6)
