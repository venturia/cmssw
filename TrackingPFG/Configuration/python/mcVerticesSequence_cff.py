import FWCore.ParameterSet.Config as cms

# seed multiplicity monitoring

from Validation.RecoVertex.mcvsrecoverticesanalyzer_cfi import *
mcvsrecogoodvertices = mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("goodVertices"))
mcvsrecogooddisplacedvertices = mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("goodDisplacedVertices"))
mcvsrecopixelvertices = mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("realPixelVertices"))
mcvsrecoHLTpixelvertices = mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveHLT"))

seqMCVertices = cms.Sequence(mcvsrecogoodvertices + mcvsrecogooddisplacedvertices + mcvsrecopixelvertices + mcvsrecoHLTpixelvertices)
