import FWCore.ParameterSet.Config as cms


gemHitsValidation = cms.EDAnalyzer('MuonGEMHits',
    outputFile = cms.string(''),
    verbose = cms.untracked.int32(0),
    simInputLabel = cms.untracked.string('g4SimHits'),
    simTrackMatching = cms.PSet( 
       gemMinPt = cms.untracked.double(4.5),
       gemMinEta = cms.untracked.double(1.45),
       gemMaxEta = cms.untracked.double(2.5)
    ),
    PlotBinInfo = cms.PSet(
			# st1, st2_short, st2_long of xbin, st1,st2_short,st2_long of ybin
			nBinGlobalZR = cms.untracked.vdouble(200,200,200,110,140,210), 
			# st1 xmin, xmax, st2_short xmin, xmax, st2_long xmin, xmax, st1 ymin, ymax...
			RangeGlobalZR = cms.untracked.vdouble(564,572,786,794,794,802,130,240,190,330,120,330), 
    )

)

