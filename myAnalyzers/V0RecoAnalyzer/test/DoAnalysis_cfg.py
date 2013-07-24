import FWCore.ParameterSet.Config as cms

process = cms.Process("V0ANALYSIS")

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(10000)
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

#process.GlobalTag.globaltag = 'MC_31X_V3::All'

process.ksAnalyzer = cms.EDAnalyzer('V0RecoAnalyzer',
#    v0Collection = cms.InputTag('generalV0Candidates:Kshort'),
    v0Collection = cms.InputTag('v0CollectionMaker:allVees'),
    pvAvailable = cms.bool(False),
    beamSpotAvailable = cms.bool(False),
    tracksAvailable = cms.bool(False),
    instanceName = cms.string('Kshort'),
    writeTree = cms.bool(True),
    writeHistos = cms.bool(True),
    ksMassXmin = cms.double(0.305),
    ksMassXmax = cms.double(0.795),
    ksMassNbins = cms.int32(70),
    ksMass_eta_nBins = cms.int32(5),
    ksMass_phi_nBins = cms.int32(6),
#    ksMass_pt_nBins  = cms.int32(5),
    ksMass_pt_nBinSubdiv = cms.int32(1),
    lamMassXmin = cms.double(1.07),
    lamMassXmax = cms.double(1.16),
    lamMassNbins = cms.int32(60),
    lamMass_eta_nBins = cms.int32(5),
    lamMass_phi_nBins = cms.int32(6),
#    lamMass_pt_nBins = cms.int32(5),
    lamMass_pt_nBinSubdiv = cms.int32(1)
)

process.lamAnalyzer = cms.EDAnalyzer('V0RecoAnalyzer',
#    v0Collection = cms.InputTag('generalV0Candidates:Lambda'),
    v0Collection = cms.InputTag('v0CollectionMaker:allVees'),
    instanceName = cms.string('Lambda'),
    pvAvailable = cms.bool(False),
    beamSpotAvailable = cms.bool(False),
    tracksAvailable = cms.bool(False),
    writeTree = cms.bool(True),
    writeHistos = cms.bool(True),
    ksMassXmin = cms.double(0.44), 
    ksMassXmax = cms.double(0.56),
    ksMassNbins = cms.int32(60),
    ksMass_eta_nBins = cms.int32(5),
    ksMass_phi_nBins = cms.int32(6),
#    ksMass_pt_nBins  = cms.int32(5),
    ksMass_pt_nBinSubdiv = cms.int32(1),
    lamMassXmin = cms.double(1.08),
    lamMassXmax = cms.double(1.16),
    lamMassNbins = cms.int32(40),
    lamMass_eta_nBins = cms.int32(5),
    lamMass_phi_nBins = cms.int32(6),
#    lamMass_pt_nBins = cms.int32(5),
    lamMass_pt_nBinSubdiv = cms.int32(1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:v0Collection123596_gp_goodpixel_christophe_FEVT.root'
#        'file:v0CollectionSelfContained.root'
#        'file:v0CollectionSelfContained_2.root',
#        'file:v0CollectionSelfContained_3.root',
#        'file:v0CollectionSelfContained_4.root'
    )
)

process.TFileService = cms.Service('TFileService',
    fileName = cms.string('v0analysis.root')
)

process.analysis = cms.Path(process.ksAnalyzer+process.lamAnalyzer)

process.schedule = cms.Schedule(process.analysis)

