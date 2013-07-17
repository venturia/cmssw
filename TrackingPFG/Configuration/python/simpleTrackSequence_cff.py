import FWCore.ParameterSet.Config as cms


from trackCount.TrackCount.trackcount_cfi import *

trackcount.trackCollection = cms.InputTag("generalTracks")
trackcountPreScraping = trackcount.clone()
trackcountOnlyNoScraping = trackcount.clone()
trackcountOnlyTrigger = trackcount.clone()
trackcountNonColliding = trackcount.clone()
trackcountNonCollidingGoodVtx = trackcount.clone()


trackcounthp = trackcount.clone(trackCollection = cms.InputTag("highPurityTracks"))
trackcounthpOnlyNoScraping = trackcounthp.clone()
trackcounthpOnlyTrigger = trackcounthp.clone()
trackcountpas = trackcount.clone(trackCollection = cms.InputTag("pasTracks"))
trackcountonegev = trackcount.clone(trackCollection = cms.InputTag("oneGeVTracks"))
pixeltrackcount = trackcount.clone(trackCollection = cms.InputTag("pixelTracks"))

from TrackingPFG.Utilities.pixellessfilter_cfi import *
pixellessfilter.newIter=cms.bool(True)

pxllessOnlyNoScrapingFilter = pixellessfilter.clone(vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllesshpOnlyNoScrapingFilter = pixellessfilter.clone(trackCollection = cms.InputTag("highPurityTracks"),vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllessCentralOnlyNoScrapingFilter = pxllessOnlyNoScrapingFilter.clone(vtxzMax=cms.double(12))
pxllesshpCentralOnlyNoScrapingFilter = pxllesshpOnlyNoScrapingFilter.clone(vtxzMax=cms.double(12))

pxllessFilter = pixellessfilter.clone(vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllesshpFilter = pixellessfilter.clone(trackCollection = cms.InputTag("highPurityTracks"),vtxCollection = cms.InputTag("goodDisplacedVertices"))
pxllessCentralFilter = pxllessFilter.clone(vtxzMax=cms.double(12))
pxllesshpCentralFilter = pxllesshpFilter.clone(vtxzMax=cms.double(12))

seqPixelTrackColliding = cms.Sequence(pixeltrackcount)
seqSimpleTrackColliding = cms.Sequence(trackcount + trackcounthp + trackcountpas+ trackcountonegev
                                            + pxllessFilter + pxllesshpFilter
                                            + pxllessCentralFilter + pxllesshpCentralFilter
                                       )
seqSimpleTrackPreScraping = cms.Sequence(trackcountPreScraping)
seqSimpleTrackOnlyNoScraping = cms.Sequence(trackcountOnlyNoScraping + trackcounthpOnlyNoScraping
                                            + pxllessOnlyNoScrapingFilter + pxllesshpOnlyNoScrapingFilter
                                            + pxllessCentralOnlyNoScrapingFilter + pxllesshpCentralOnlyNoScrapingFilter)
seqSimpleTrackOnlyTrigger = cms.Sequence(trackcountOnlyTrigger + trackcounthpOnlyTrigger)
seqSimpleTrackNonColliding = cms.Sequence(trackcountNonColliding)
seqSimpleTrackNonCollidingGoodVtx = cms.Sequence(trackcountNonCollidingGoodVtx)
