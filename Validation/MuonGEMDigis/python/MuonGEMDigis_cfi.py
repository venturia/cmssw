import FWCore.ParameterSet.Config as cms

gemDigiValidation = cms.EDAnalyzer('MuonGEMDigis',
	outputFile = cms.string(''),
	stripLabel= cms.InputTag('simMuonGEMDigis'),
	cscPadLabel = cms.InputTag('simMuonGEMCSCPadDigis'),
	cscCopadLabel = cms.InputTag('simMuonGEMCSCPadDigis','Coincidence') ,
	simInputLabel = cms.untracked.string('g4SimHits'),
	minPt = cms.untracked.double(5.),
	maxEta = cms.untracked.double(2.45),
	minEta = cms.untracked.double(1.55), 
	PlotBinInfo = cms.PSet(
			nBinGlobalZR = cms.untracked.vdouble(200,200,200,110,140,210), 
			RangeGlobalZR = cms.untracked.vdouble(564,572,786,794,794,802,130,240,190,330,120,330), 
  ),
	simTrackMatching = cms.PSet(
            verboseSimHit = cms.untracked.int32(0),
            simInputLabel = cms.untracked.string('g4SimHits'),
            # GEM digi matching:
            verboseGEMDigi = cms.untracked.int32(0),
            gemDigiInput = cms.untracked.InputTag("simMuonGEMDigis"),
            gemPadDigiInput = cms.untracked.InputTag("simMuonGEMCSCPadDigis"),
            gemCoPadDigiInput = cms.untracked.InputTag("simMuonGEMCSCPadDigis", "Coincidence"),
            minBXGEM = cms.untracked.int32(-1),
            maxBXGEM = cms.untracked.int32(1),
            matchDeltaStripGEM = cms.untracked.int32(1),
            gemDigiMinEta  = cms.untracked.double(1.55),
            gemDigiMaxEta  = cms.untracked.double(2.18),
            gemDigiMinPt = cms.untracked.double(5.0),
  ),
)
