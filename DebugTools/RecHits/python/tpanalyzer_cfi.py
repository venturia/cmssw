import FWCore.ParameterSet.Config as cms

tpanalyzer = cms.EDAnalyzer("TPAnalyzer",
                            trackingParticlesCollection = cms.InputTag("mergedtruth","MergedTrackTruth"),
                            wantedSubDets = cms.VPSet(
    cms.PSet(name=cms.string("FPIX"),title=cms.string("FPIX"),selection=cms.vstring("0xfe000000-0x14000000")),
    cms.PSet(name=cms.string("BPIX"),title=cms.string("BPIX"),selection=cms.vstring("0xfe000000-0x12000000")),
    cms.PSet(name=cms.string("Pixel"),title=cms.string("Pixel"),selection=cms.vstring("0xfe000000-0x14000000","0xfe000000-0x12000000"))
    )
                            
                            )

