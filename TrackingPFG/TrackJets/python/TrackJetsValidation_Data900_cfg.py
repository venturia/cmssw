import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
        '/store/data/BeamCommissioning09/MinimumBias/RECO/Dec19thReReco_341_v1/0002/EE2D8EDE-0DED-DE11-853C-0026189437F8.root')
                            #                        ,eventsToProcess = cms.untracked.VEventRange('run:min-run:max')
                            )

# lumisection selection
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('123596:1-123596:69')

#to avoid crash due to mixing between incompatible runs
process.source.inputCommands = cms.untracked.vstring("keep *", "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT",
                                                     "drop edmErrorSummaryEntrys_logErrorHarvester__RECO")

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff") ### real data
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'GR09_R_34X_V2::All'

####################################
# events skimming

# bit40andhalobeamveto bit0 vertexcondition

process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
from HLTrigger.HLTfilters.hltLevel1GTSeed_cfi import hltLevel1GTSeed
process.bit40 = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('40 AND NOT (36 OR 37 OR 38 OR 39)'))
process.bptxAnd = hltLevel1GTSeed.clone(L1TechTriggerSeeding = cms.bool(True), L1SeedsLogicalExpression = cms.string('0'))

process.oneGoodVertexFilter = cms.EDFilter("VertexSelector",
                                           src = cms.InputTag("offlinePrimaryVertices"),
                                           cut = cms.string("!isFake && tracksSize > 3 && abs(z) <= 15 && position.Rho <= 2"),
                                           filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
                                           )

process.noScraping= cms.EDFilter("FilterOutScraping",
                                 applyfilter = cms.untracked.bool(True),
                                 debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
                                 numtrack = cms.untracked.uint32(10),
                                 thresh = cms.untracked.double(0.2)
                                 )

#####################################
# trackjets

process.load("RecoJets.Configuration.RecoTrackJets_cff")

process.trackWithVertexRefSelector.nVertices = 99
process.trackWithVertexRefSelector.zetaVtx = 1.0
process.trackWithVertexRefSelector.rhoVtx = 0.3
process.trackWithVertexRefSelector.ptErrorCut = 0.2

process.ak5TrackJets.UseOnlyVertexTracks = False
process.ak5TrackJets.UseOnlyOnePV = False
process.ak5TrackJets.DxyTrVtxMax = 0.1
process.ak5TrackJets.DzTrVtxMax = 0.5

process.kt4TrackJets.UseOnlyVertexTracks = False
process.kt4TrackJets.UseOnlyOnePV = False
process.kt4TrackJets.DxyTrVtxMax = 0.1
process.kt4TrackJets.DzTrVtxMax = 0.5

process.sisCone5TrackJets.UseOnlyVertexTracks = False
process.sisCone5TrackJets.UseOnlyOnePV = False
process.sisCone5TrackJets.DxyTrVtxMax = 0.1
process.sisCone5TrackJets.DzTrVtxMax = 0.5

#########################################
# analyzers

process.validationak5 = cms.EDAnalyzer('TrackJetsValidation',
                                        trackjetsSource = cms.InputTag("ak5TrackJets"),
                                        tracksSource    = cms.InputTag("generalTracks"),
                                        verticesSource  = cms.InputTag("offlinePrimaryVertices")
                                        )
process.validationkt4 = cms.EDAnalyzer('TrackJetsValidation',
                                        trackjetsSource = cms.InputTag("kt4TrackJets"),
                                        tracksSource    = cms.InputTag("generalTracks"),
                                        verticesSource  = cms.InputTag("offlinePrimaryVertices")
                                        )
process.validationsc5 = cms.EDAnalyzer('TrackJetsValidation',
                                        trackjetsSource = cms.InputTag("sisCone5TrackJets"),
                                        tracksSource    = cms.InputTag("generalTracks"),
                                        verticesSource  = cms.InputTag("offlinePrimaryVertices")
                                        )


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("out.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

process.p0 = cms.Path(process.bit40 * process.bptxAnd * process.oneGoodVertexFilter * process.noScraping * process.recoTrackJets*process.sisCone5TrackJets*process.validationak5*process.validationkt4*process.validationsc5)

