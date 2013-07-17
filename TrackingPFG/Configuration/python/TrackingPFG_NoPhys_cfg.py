import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingPFG")

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(),
                            skipBadFiles = cms.untracked.bool(True),
                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                            )

#---Reco configuration

process.load("TrackingPFG.Configuration.recoConfiguration_cff")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR09_R_35X_V3::All"


#

process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.vertexTracksSelectionSequence_cff")
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.load("TrackingPFG.Configuration.apvNoiseSequence_cff")
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.nonCollidingSequence_cff")
process.load("TrackingPFG.Configuration.collidingSequence_cff")
process.load("TrackingPFG.Configuration.preScrapingSequence_cff")

process.conversionntuplizer.outfile = "ntuple_conversion_test_data.root"    # output file for conversion ntuples

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_PFG.root')
                                   )

# monitor events before scraping event selection?
# reconstruct pixel vertices with divisive vertexing and compare
# event distribution monitoring for retriggering: Done
# skim beam gas candidate
# skim APV noise candidate: Done? check deco parameters
# global tag


process.p0 = cms.Path(process.seqBitSelectionNoPhys +
                      process.seqEventHistory +
                      process.seqPVSelection +
                      process.seqPreScraping + process.seqNoScrapingSelection +
                      process.seqReco +
                      process.seqColliding
                      )

#---------APV induced noisy events

process.plat1   = cms.Path(process.seqBitSelectionNoPhys + process.seqEventHistory + process.seqLatencyPlusOne)
process.pfhmax1 = cms.Path(process.seqBitSelectionNoPhys + process.seqEventHistory + process.seqFrameHeaderMax1)
process.pfhmax2 = cms.Path(process.seqBitSelectionNoPhys + process.seqEventHistory + process.seqFrameHeaderMax2)


process.outnoisy = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string("apvNoisy.root"),
        outputCommands = cms.untracked.vstring("keep *"),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("plat1","pfhmax1","pfhmax2"))
	)

#---------Non colliding BX events

process.pnoncollskim = cms.Path(process.seqNonCollidingSelectionNoPhys + process.seqNonCollidingSkim +
                                process.seqEventHistoryNonCollidingSkim )

process.pnoncoll = cms.Path(process.seqNonCollidingSelectionNoPhys +
                            process.seqEventHistoryNonCollidingEarly +
                            process.seqMultProd +
                            process.seqNonColliding + process.seqEventHistoryNonColliding)

process.pnoncollplus = cms.Path(process.seqNonCollidingPlusSelectionNoPhys +
                                process.seqNonCollidingPlus + process.seqEventHistoryNonCollidingPlus)

process.pnoncollminus = cms.Path(process.seqNonCollidingMinusSelectionNoPhys +
                                 process.seqNonCollidingMinus + process.seqEventHistoryNonCollidingMinus)

#----Non Colliding BX events with one PV with good quality

process.pnoncollgoodvtx = cms.Path(process.seqNonCollidingSelectionNoPhys + process.seqGoodDisplacedPVSelection +
                                   process.seqNonCollidingGoodVtx + process.seqEventHistoryNonCollidingGoodVtx)

process.pnoncollplusgoodvtx = cms.Path(process.seqNonCollidingPlusSelectionNoPhys + process.seqGoodDisplacedPVSelection +
                                       process.seqNonCollidingPlusGoodVtx + process.seqEventHistoryNonCollidingPlusGoodVtx)

process.pnoncollminusgoodvtx = cms.Path(process.seqNonCollidingMinusSelectionNoPhys + process.seqGoodDisplacedPVSelection +
                                        process.seqNonCollidingMinusGoodVtx + process.seqEventHistoryNonCollidingMinusGoodVtx)

process.outbeamgas = cms.OutputModule("PoolOutputModule",
	fileName = cms.untracked.string("beamgas.root"),
        outputCommands = cms.untracked.vstring("keep *"),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pnoncollskim"))
	)


#-----------------------------------

#process.e = cms.EndPath(process.outnoisy+process.outbeamgas)
#process.e = cms.EndPath(process.outbeamgas)

