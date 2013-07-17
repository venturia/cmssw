import FWCore.ParameterSet.Config as cms

# Event History

froml1abcHEs = cms.EDProducer("EventWithHistoryProducerFromL1ABC",
                              l1ABCCollection=cms.InputTag("scalersRawToDigi")
                              )


# APVPhases

#from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts_cfi import *
from DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts2011_cfi import *

# event distribution monitoring

from DPGAnalysis.SiStripTools.eventtimedistribution_cfi import *
eventtimedistribution.historyProduct = cms.InputTag("froml1abcHEs")

eventtimedistribution.startingLSFraction = cms.untracked.uint32(16)
eventtimedistribution.maxLSBeforeRebin = cms.untracked.uint32(200)

eventtimedistranydcs = eventtimedistribution.clone()
eventtimedistrnotrack = eventtimedistribution.clone()
eventtimedistrnotrackskim = eventtimedistribution.clone()
eventtimedistrnotrackwithtwojets = eventtimedistribution.clone()
eventtimedistrnotrackwithcentraljet = eventtimedistribution.clone()
eventtimedistrnovertex = eventtimedistribution.clone()
eventtimedistrnovertexskim = eventtimedistribution.clone()
eventtimedistrnovertexwithtwojets = eventtimedistribution.clone()
eventtimedistrnovertexwithcentraljet = eventtimedistribution.clone()
eventtimedistroffdiag = eventtimedistribution.clone()
eventtimedistrnostrip = eventtimedistribution.clone()
eventtimedistrnoclusters = eventtimedistribution.clone()
eventtimedistrmanystripclus = eventtimedistribution.clone()
eventtimedistrtoomanystripclus = eventtimedistribution.clone()
eventtimedistrtoomanyerrors = eventtimedistribution.clone()
eventtimedistrmanyclus = eventtimedistribution.clone()
eventtimedistrnitertibtidhp = eventtimedistribution.clone()
eventtimedistrnitertobtechp = eventtimedistribution.clone()
eventtimedistrniterpixellesshp = eventtimedistribution.clone()

eventtimedistribution.dbxHistosParams = cms.untracked.VPSet(
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(7)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(6)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(5)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(4)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(3)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(2)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(1))
    )
eventtimedistrmanystripclus.dbxHistosParams = cms.untracked.VPSet(
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(7)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(6)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(5)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(4)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(3)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(2)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(1))
    )
eventtimedistrtoomanystripclus.dbxHistosParams = cms.untracked.VPSet(
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(7)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(6)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(5)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(4)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(3)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(2)),
    cms.PSet(nbins=cms.int32(2000),min=cms.double(-0.5),max=cms.double(3999.5),firstEvent=cms.uint32(0),secondEvent=cms.uint32(1))
    )
                            

# Sequence

seqEventHistoryReco = cms.Sequence(froml1abcHEs + APVPhases)

