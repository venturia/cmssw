import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("V0Tracks")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)


process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("TrackingPFG.Configuration.v0RecoSequence_cff")
process.load("TrackingPFG.Configuration.v0Sequence_cff")
process.load("TrackingPFG.Configuration.v0TrackSelectionSequence_cff")

process.tracksFromOtobV0.v0Collections = cms.VInputTag(cms.InputTag("generalV0Candidates:Kshort"))
process.tracksFromOtobV0.maxMass = cms.double(0.4826)
process.tracksFromOtobV0.minMass = cms.double(0.5126)

process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")

process.load("trackCount.TrackCount.trackcount_cfi")
process.trackcount.trackCollection = cms.InputTag("generalTracks")
process.trackFromOtobV0count = process.trackcount.clone(trackCollection = cms.InputTag("tracksFromOtobV0"))


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

process.hltSelection.HLTPaths = cms.vstring("HLT_ZeroBias_*")

process.p0 = cms.Path(process.seqHLTSelection + process.seqBitSelection +
                      process.v0generalreco +
                      process.tracksFromOtobV0 +
                      process.v0generalanalysis +
                      process.trackcount +
                      process.trackFromOtobV0count )

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('V0Tracks.root')
                                   )


#-----------------------------------


