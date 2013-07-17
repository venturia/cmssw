import FWCore.ParameterSet.Config as cms

#from TrackingPFG.Configuration.pixelVertexAdaptive_cff import *
from TrackingPFG.Configuration.offlinePrimaryVerticesDA_cfi import *
#from TrackingPFG.Configuration.pixelVertexAdaptiveNoBS_cff import *
from TrackingPFG.Configuration.pixelVertexDivisiveStdCuts_cfi import *
#from TrackingPFG.Configuration.pixelVertexDivisiveNewCuts_cfi import *

seqVertexReco = cms.Sequence(#offlinePrimaryVerticesDA #+
                             #                                  pixelVerticesAdaptive +
                             #                                  pixelVerticesAdaptiveNoBS +
                                                               pixelVerticesDivisiveHLT # +
                             #                                  pixelVerticesDivisiveNewCuts
                             )

seqVertexRecoAOD = cms.Sequence(#offlinePrimaryVerticesDA #+
                                #                                  pixelVerticesAdaptiveNoBS +
                                #                                  pixelVerticesDivisiveStdCuts +
                                #                                  pixelVerticesDivisiveNewCuts
                                )


offlinePrimaryVerticesDAWithBS = offlinePrimaryVerticesDA.clone(useBeamConstraint = cms.bool(True))

seqVertexRecoDetailed = cms.Sequence(offlinePrimaryVerticesDA + offlinePrimaryVerticesDAWithBS )
