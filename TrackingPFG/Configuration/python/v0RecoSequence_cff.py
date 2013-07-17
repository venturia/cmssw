import FWCore.ParameterSet.Config as cms

#from myAnalyzers.V0RecoAnalyzer.runV0Analysis_cff import *

#extracted from the file above

from myProducers.V0CandProducer.v0CandProducer_cfi import *
from RecoVertex.V0Producer.generalV0Candidates_cfi import *

generalV0PATCands = produceV0PATCands.clone(kShortCollection = cms.InputTag('generalV0Candidates:Kshort'),
                                            lambdaCollection = cms.InputTag('generalV0Candidates:Lambda'))

v0reco = cms.Sequence(localV0Candidates*produceV0PATCands)
v0generalreco = cms.Sequence(generalV0PATCands)

#local V0 removed because of too much CPU time: 2011/11/15
#seqV0Reco = cms.Sequence(v0reco+v0generalreco)
seqV0Reco = cms.Sequence(v0generalreco)

fromV0V0Candidates = localV0Candidates.clone(trackRecoAlgorithm = cms.InputTag('tracksFromV0'))
fromV0V0PATCands = produceV0PATCands.clone(kShortCollection = cms.InputTag('fromV0V0Candidates:Kshort'),
                                            lambdaCollection = cms.InputTag('fromV0V0Candidates:Lambda'))

fromNewV0V0Candidates = localV0Candidates.clone(trackRecoAlgorithm = cms.InputTag('newTracksFromV0'))
fromNewV0V0PATCands = produceV0PATCands.clone(kShortCollection = cms.InputTag('fromNewV0V0Candidates:Kshort'),
                                            lambdaCollection = cms.InputTag('fromNewV0V0Candidates:Lambda'))

fromOtobV0V0Candidates = generalV0Candidates.clone(trackRecoAlgorithm = cms.InputTag('tracksFromOtobV0'))
fromOtobV0V0PATCands = produceV0PATCands.clone(kShortCollection = cms.InputTag('fromOtobV0V0Candidates:Kshort'),
                                            lambdaCollection = cms.InputTag('fromOtobV0V0Candidates:Lambda'))

fromNewOtobV0V0Candidates = generalV0Candidates.clone(trackRecoAlgorithm = cms.InputTag('newTracksFromOtobV0'))
fromNewOtobV0V0PATCands = produceV0PATCands.clone(kShortCollection = cms.InputTag('fromNewOtobV0V0Candidates:Kshort'),
                                            lambdaCollection = cms.InputTag('fromNewOtobV0V0Candidates:Lambda'))

v0fromv0reco = cms.Sequence(fromV0V0Candidates*fromV0V0PATCands)
v0fromnewv0reco = cms.Sequence(fromNewV0V0Candidates*fromNewV0V0PATCands)
v0fromotobv0reco = cms.Sequence(fromOtobV0V0Candidates*fromOtobV0V0PATCands)
v0fromnewotobv0reco = cms.Sequence(fromNewOtobV0V0Candidates*fromNewOtobV0V0PATCands)

seqV0fromV0Reco = cms.Sequence(v0fromv0reco + v0fromnewv0reco + v0fromotobv0reco + v0fromnewotobv0reco )
