import FWCore.ParameterSet.Config as cms

pixeldigiprofiler = cms.EDAnalyzer('PixelDigiProfiler',
                                          collection = cms.InputTag("siPixelDigis"),
                                          selections = cms.VPSet(
    cms.PSet(label=cms.string("BPIXLayer1"),selection=cms.untracked.vstring("0x1ef00000-0x12100000")),
    cms.PSet(label=cms.string("BPIXLayer2"),selection=cms.untracked.vstring("0x1ef00000-0x12200000")),
    cms.PSet(label=cms.string("BPIXLayer3"),selection=cms.untracked.vstring("0x1ef00000-0x12300000")),
    cms.PSet(label=cms.string("BPIXLayer4"),selection=cms.untracked.vstring("0x1ef00000-0x12400000"))
    )

)
