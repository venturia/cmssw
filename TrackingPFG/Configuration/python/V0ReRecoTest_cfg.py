import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("V0ReRecoTest")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('newAlignment',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if a new alignment sqlite file has to be used")

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)


process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
#process.load("Configuration.StandardSequences.MagneticField_38T_polyFit2D_cff")
#process.ParametrizedMagneticFieldProducer.version = 'PolyFit3D'
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("TrackingPFG.Configuration.v0RecoSequence_cff")
process.load("TrackingPFG.Configuration.v0Sequence_cff")
process.load("TrackingPFG.Configuration.v0TrackSelectionSequence_cff")
process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")

process.load("trackCount.TrackCount.trackcount_cfi")
process.trackcount.trackCollection = cms.InputTag("generalTracks")
process.trackFromV0count = process.trackcount.clone(trackCollection = cms.InputTag("tracksFromV0"))
process.trackFromNewV0count = process.trackcount.clone(trackCollection = cms.InputTag("newTracksFromV0"))
process.trackFromOtobV0count = process.trackcount.clone(trackCollection = cms.InputTag("tracksFromOtobV0"))
process.trackFromNewOtobV0count = process.trackcount.clone(trackCollection = cms.InputTag("newTracksFromOtobV0"))

process.load("TrackingPFG.Configuration.trackComparatorSequence_cff")

process.hltSelection.HLTPaths = cms.vstring("HLT_ZeroBias_*")

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

if options.newAlignment == 1:
    import CalibTracker.Configuration.Common.PoolDBESSource_cfi
    process.trackerBowedSensors = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
            connect = cms.string('sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/PayLoads/craft10BowedSensors/alignments_MP.db'),

                toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerSurfaceDeformationRcd'),
                                                                          tag = cms.string('Deformations')
                                                                          )
                                                        )
                )
    process.prefer_trackerBowedSensors = cms.ESPrefer("PoolDBESSource", "trackerBowedSensors")
    

process.p0 = cms.Path(process.seqHLTSelection + process.seqBitSelection +
                      process.seqV0Reco + process.seqV0Tracks + process.seqV0fromV0Reco +
                      process.seqV0 + process.seqV0fromV0 +
                      process.trackcount +
                      process.trackFromV0count + process.trackFromNewV0count +
                      process.trackFromOtobV0count + process.trackFromNewOtobV0count +
                      process.seqTrackComparator)

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('V0ReRecoTest.root')
                                   )


#-----------------------------------


