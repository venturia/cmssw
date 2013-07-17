import FWCore.ParameterSet.Config as cms

#from myAnalyzers.V0RecoAnalyzer.runV0Analysis_cff import *

#extracted from the file above

from myAnalyzers.V0RecoAnalyzer.v0RecoAnalyzer_cfi import *

analyzeGeneralKshort = analyzeKshort.clone(v0Collection = cms.InputTag('generalV0PATCands:allVees'))
analyzeGeneralLambda = analyzeLambda.clone(v0Collection = cms.InputTag('generalV0PATCands:allVees'))


v0analysis = cms.Sequence(analyzeKshort*analyzeLambda)
v0generalanalysis = cms.Sequence(analyzeGeneralKshort*analyzeGeneralLambda)

#local V0 removed because of too much CPU time: 2011/11/15
#seqV0 = cms.Sequence(v0analysis+v0generalanalysis)
seqV0 = cms.Sequence(v0generalanalysis)

analyzeFromV0Kshort = analyzeKshort.clone(v0Collection = cms.InputTag('fromV0V0PATCands:allVees'))
analyzeFromV0Lambda = analyzeLambda.clone(v0Collection = cms.InputTag('fromV0V0PATCands:allVees'))

v0fromv0analysis = cms.Sequence(analyzeFromV0Kshort*analyzeFromV0Lambda)

analyzeFromNewV0Kshort = analyzeKshort.clone(v0Collection = cms.InputTag('fromNewV0V0PATCands:allVees'))
analyzeFromNewV0Lambda = analyzeLambda.clone(v0Collection = cms.InputTag('fromNewV0V0PATCands:allVees'))

v0fromnewv0analysis = cms.Sequence(analyzeFromNewV0Kshort*analyzeFromNewV0Lambda)

analyzeFromOtobV0Kshort = analyzeKshort.clone(v0Collection = cms.InputTag('fromOtobV0V0PATCands:allVees'))
analyzeFromOtobV0Lambda = analyzeLambda.clone(v0Collection = cms.InputTag('fromOtobV0V0PATCands:allVees'))

v0fromotobv0analysis = cms.Sequence(analyzeFromOtobV0Kshort*analyzeFromOtobV0Lambda)

analyzeFromNewOtobV0Kshort = analyzeKshort.clone(v0Collection = cms.InputTag('fromNewOtobV0V0PATCands:allVees'))
analyzeFromNewOtobV0Lambda = analyzeLambda.clone(v0Collection = cms.InputTag('fromNewOtobV0V0PATCands:allVees'))

v0fromnewotobv0analysis = cms.Sequence(analyzeFromNewOtobV0Kshort*analyzeFromNewOtobV0Lambda)

seqV0fromV0 = cms.Sequence(v0fromv0analysis+ v0fromnewv0analysis + v0fromotobv0analysis+ v0fromnewotobv0analysis)
