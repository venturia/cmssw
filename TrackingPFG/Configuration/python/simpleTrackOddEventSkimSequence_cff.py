import FWCore.ParameterSet.Config as cms


from trackCount.TrackCount.trackcount_cfi import *

trackcount.trackCollection = cms.InputTag("generalTracks")
trackcountoffdiag = trackcount.clone()
trackcountnostrip = trackcount.clone()
trackcountnovertex = trackcount.clone()
trackcountnovertexskim = trackcount.clone()
trackcountnovertexwithtwojets = trackcount.clone()
trackcountnovertexwithcentraljet = trackcount.clone()
trackcountmanystripclus = trackcount.clone()
trackcounttoomanystripclus = trackcount.clone()
trackcountmanyclus = trackcount.clone()
trackcountnitertibtidhp = trackcount.clone()
trackcountnitertobtechp = trackcount.clone()
trackcountniterpixellesshp = trackcount.clone()


trackcounthp = trackcount.clone(trackCollection = cms.InputTag("highPurityTracks"))
trackcounthpnitertibtidhp = trackcounthp.clone()
trackcounthpnitertobtechp = trackcounthp.clone()
trackcounthpniterpixellesshp = trackcounthp.clone()

from TrackingPFG.Utilities.pixellessfilter_cfi import *
pixellessfilter.newIter=cms.bool(True)

pxllessoffdiag = pixellessfilter.clone(vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllesshpoffdiag = pixellessfilter.clone(trackCollection = cms.InputTag("highPurityTracks"),vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllessCentraloffdiag = pxllessoffdiag.clone(vtxzMax=cms.double(12))
pxllesshpCentraloffdiag = pxllesshpoffdiag.clone(vtxzMax=cms.double(12))

pxllessmanystripclus = pxllessoffdiag.clone()
pxllesstoomanystripclus = pxllessoffdiag.clone()
pxllessmanyclus = pxllessoffdiag.clone()

pxllesshpmanystripclus = pxllesshpoffdiag.clone()
pxllesshptoomanystripclus = pxllesshpoffdiag.clone()
pxllesshpmanyclus = pxllesshpoffdiag.clone()

pxllessCentralmanystripclus = pxllessCentraloffdiag.clone()
pxllessCentraltoomanystripclus = pxllessCentraloffdiag.clone()
pxllessCentralmanyclus = pxllessCentraloffdiag.clone()

pxllesshpCentralmanystripclus = pxllesshpCentraloffdiag.clone()
pxllesshpCentraltoomanystripclus = pxllesshpCentraloffdiag.clone()
pxllesshpCentralmanyclus = pxllesshpCentraloffdiag.clone()

seqSimpleTrackNoVertex = cms.Sequence(trackcountnovertex)
seqSimpleTrackNoVertexSkim = cms.Sequence(trackcountnovertexskim)
seqSimpleTrackNoVertexWithTwoJets = cms.Sequence(trackcountnovertexwithtwojets)
seqSimpleTrackNoVertexWithCentralJet = cms.Sequence(trackcountnovertexwithcentraljet)
seqSimpleTrackNoStrip = cms.Sequence(trackcountnostrip)
seqSimpleTrackOffDiag = cms.Sequence(trackcountoffdiag + pxllessoffdiag + pxllesshpoffdiag + pxllessCentraloffdiag + pxllesshpCentraloffdiag)
seqSimpleTrackManyStripClus = cms.Sequence(trackcountmanystripclus + pxllessmanystripclus + pxllesshpmanystripclus + pxllessCentralmanystripclus + pxllesshpCentralmanystripclus)
seqSimpleTrackTooManyStripClus = cms.Sequence(trackcounttoomanystripclus + pxllesstoomanystripclus + pxllesshptoomanystripclus + pxllessCentraltoomanystripclus + pxllesshpCentraltoomanystripclus)
seqSimpleTrackManyClus = cms.Sequence(trackcountmanyclus + pxllessmanyclus + pxllesshpmanyclus + pxllessCentralmanyclus + pxllesshpCentralmanyclus)
seqSimpleTrackNitertibtidhp = cms.Sequence(trackcountnitertibtidhp + trackcounthpnitertibtidhp)
seqSimpleTrackNitertobtechp = cms.Sequence(trackcountnitertobtechp + trackcounthpnitertobtechp)
seqSimpleTrackNiterpixellesshp = cms.Sequence(trackcountniterpixellesshp + trackcounthpniterpixellesshp)
