import FWCore.ParameterSet.Config as cms

process = cms.Process('OCC')

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR09_R_34X_V2::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('file:/data/gpetrucc/DataMixer/DMPreReco_TkOnly.root'))
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('file:/data/gpetrucc/DataMixer/DMPreProcess_MC.root'))
process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/CE62D4D8-85ED-DE11-8BD2-000423D9853C.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/A0FB9B2E-85ED-DE11-8A8D-001D09F290CE.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/9A2F0DDF-85ED-DE11-B5D1-001D09F290CE.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/820C7C8C-86ED-DE11-83D4-001D09F295FB.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/685C77F0-87ED-DE11-A4A5-000423D60FF6.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/4CFCC894-86ED-DE11-B3F4-001D09F2447F.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/3EA206BD-B5ED-DE11-B481-000423D6C8E6.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/3CCCE28D-86ED-DE11-A583-000423D986C4.root',
        '/store/relval/CMSSW_3_4_1/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V14-v1/0004/2CF90F4D-87ED-DE11-A3AF-003048D375AA.root',
    )
)
 

# Other statements

process.occupancy = cms.EDProducer("TrackerOccupancyAnalyzer",
    tracks = cms.InputTag("generalTracks"),
    strips = cms.InputTag("siStripClusters"),
    pixels = cms.InputTag("siPixelClusters"),
)
process.ana = cms.Path(process.occupancy)

# Output definition
process.FEVT = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *', 'keep recoTracks_generalTracks_*_*', 'keep *_occupancy_*_*' ),
    fileName = cms.untracked.string('occupancy_TTbar.root'),
)
process.output_step = cms.Path(process.FEVT)


