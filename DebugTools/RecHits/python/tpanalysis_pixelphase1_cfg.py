import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TPAnalysis")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register('globalTag',
                 "DONOTEXIST::All",
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string,          # string, int, or float
                 "GlobalTag")
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#
process.load("DebugTools.OverlapProblem.processOptions_cff")
process.load("DebugTools.OverlapProblem.MessageLogger_cff")

process.MessageLogger.cout.threshold = cms.untracked.string("WARNING")
#process.MessageLogger.debugModules = cms.untracked.vstring("overlapproblemanalyzer")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            #                    skipBadFiles = cms.untracked.bool(True),
                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                            )

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
#process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.Geometry.GeometryExtendedPhaseIPixelReco_cff")
process.load("Configuration.Geometry.GeometryExtendedPhaseIPixel_cff")
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")


process.load('SLHCUpgradeSimulations.Geometry.fakeConditions_Phase1_R30F12_cff')
process.trackerTopologyConstants.pxb_layerStartBit = cms.uint32(18)  # check if they induce a difference
process.trackerTopologyConstants.pxb_ladderMask = cms.uint32(1023)  # check if they induce a difference

process.load("DebugTools.RecHits.tpanalyzer_cfi")

process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
process.load("IOMC.RandomEngine.IOMC_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.mix.digitizers.pixel.MissCalibrate = False
process.mix.digitizers.pixel.LorentzAngle_DB = False
process.mix.digitizers.pixel.killModules = False
process.mix.digitizers.pixel.useDB = False
process.mix.digitizers.pixel.DeadModules_DB = False
process.mix.digitizers.pixel.NumPixelBarrel = cms.int32(4)
process.mix.digitizers.pixel.NumPixelEndcap = cms.int32(3)
process.mix.digitizers.pixel.ThresholdInElectrons_FPix = cms.double(2000.0)
process.mix.digitizers.pixel.ThresholdInElectrons_BPix = cms.double(2000.0)
process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L1 = cms.double(2000.0)
process.mix.digitizers.pixel.thePixelColEfficiency_BPix4 = cms.double(0.999)
process.mix.digitizers.pixel.thePixelEfficiency_BPix4 = cms.double(0.999)
process.mix.digitizers.pixel.thePixelChipEfficiency_BPix4 = cms.double(0.999)
process.mix.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(False)

process.p0 = cms.Path( process.mix + process.mergedtruth + process.tpanalyzer )

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('TPAnalysis.root')
                                   )

#print process.dumpPython()
