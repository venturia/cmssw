import FWCore.ParameterSet.Config as cms

from DPGAnalysis.SiStripTools.filters.LatencyPlusOneEvents_cfi import latencyPlusOne
latencyPlusOne.commonConfiguration = cms.untracked.PSet(historyProduct = cms.untracked.InputTag("froml1abcHEs"))
latencyPlusOne.filterConfigurations = cms.untracked.VPSet(
    cms.PSet(
    apvModes          = cms.untracked.vint32(47), # select Latency + 1 only in peak mode
    dbxRangeLtcyAware = cms.untracked.vint32(1,1)
    )
    )


from DPGAnalysis.SiStripTools.filters.FrameHeaderEvents_cfi import frameHeaderEvents
frameHeaderEvents.commonConfiguration.historyProduct = cms.untracked.InputTag("froml1abcHEs")
frameHeaderMax1 = frameHeaderEvents.clone()
frameHeaderMax1.filterConfigurations = cms.untracked.VPSet(
    cms.PSet(
    apvModes                   = cms.untracked.vint32(37),
    dbxInCycleRangeLtcyAware = cms.untracked.vint32(300,302)  # deco parameters to be checked !!
    ),
    cms.PSet(
    apvModes                   = cms.untracked.vint32(47),
    dbxInCycleRangeLtcyAware = cms.untracked.vint32(298,300)
    )
    )

frameHeaderMax2 = frameHeaderEvents.clone()
frameHeaderMax2.filterConfigurations = cms.untracked.VPSet(
    cms.PSet(
    apvModes                   = cms.untracked.vint32(37),
    dbxInCycleRangeLtcyAware = cms.untracked.vint32(305,306)  # deco parameters to be checked
    ),
    cms.PSet(
    apvModes                   = cms.untracked.vint32(47),
    dbxInCycleRangeLtcyAware = cms.untracked.vint32(303,304)
    )
    )



#define max1 and max2 both for peak and deco

seqLatencyPlusOne = cms.Sequence(latencyPlusOne)
seqFrameHeaderMax1 = cms.Sequence(frameHeaderMax1)
seqFrameHeaderMax2 = cms.Sequence(frameHeaderMax2)

