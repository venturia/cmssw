import FWCore.ParameterSet.Config as cms

conversionntuplizer = cms.EDAnalyzer('ConversionNtuplizer',
                              outfile = cms.string('ntuple_conversion_test_data.root'),
                              kinevtx = cms.bool(True),
                              redovtx = cms.bool(True),
                              hitassoc = cms.bool(False),
                              minPhoPtForEffic = cms.double(0.3),#when hardcoded it was 2.5
                              maxPhoEtaForEffic = cms.double(2.5),
                              maxPhoZForEffic = cms.double(200.),
                              maxPhoRForEffic = cms.double(100.),
                              minPhoPtForPurity = cms.double(0.3),#when hardcoded it was 0.5
                              maxPhoEtaForPurity = cms.double(2.5),
                              maxPhoZForPurity = cms.double(200.),
                              maxPhoRForPurity = cms.double(100.),
                              simulation = cms.bool(False),
                              #simulation = cms.bool(True),
                              prints = cms.bool(False)
)
