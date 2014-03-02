import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("D0PhiCorrAnalyzer")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('isAOD',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if AOD are analyzed")
options.register ('noHLT',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if paths with no HLT selection are needed")
options.register ('triggerPaths',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "list of HLT paths")
options.register ('triggerLabels',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "list of labels")
options.register ('negateFlags',
                  "",
                  VarParsing.VarParsing.multiplicity.list, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "list of flags to negate HLT selection")
options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")

options.parseArguments()

#
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    fileMode = cms.untracked.string("FULLMERGE")
    )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string("INFO")
process.MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cout.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000)
    )

process.MessageLogger.cerr.placeholder = cms.untracked.bool(False)
process.MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
process.MessageLogger.cerr.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100000)
    )

#----Remove too verbose PrimaryVertexProducer

process.MessageLogger.suppressInfo.append("pixelVerticesAdaptive")
process.MessageLogger.suppressInfo.append("pixelVerticesAdaptiveNoBS")

#----Remove too verbose BeamSpotOnlineProducer

process.MessageLogger.suppressInfo.append("testBeamSpot")
process.MessageLogger.suppressInfo.append("onlineBeamSpot")
process.MessageLogger.suppressWarning.append("testBeamSpot")
process.MessageLogger.suppressWarning.append("onlineBeamSpot")

#----Remove too verbose TrackRefitter

process.MessageLogger.suppressInfo.append("newTracksFromV0")
process.MessageLogger.suppressInfo.append("newTracksFromOtobV0")


#------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(options.inputFiles),
#                    skipBadFiles = cms.untracked.bool(True),
                    inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                    )
#------------------------------------------------------------------------------------------------------
process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")
#---------------------------------------------------------------------------

process.centralTracks = cms.EDFilter("TrackSelector",
                                    src = cms.InputTag("generalTracks"),
                                    cut = cms.string('quality("highPurity") && abs(eta) < 1.0 ')
                                    )

process.posTracks = cms.EDFilter("TrackSelector",
                                    src = cms.InputTag("centralTracks"),
                                    cut = cms.string('charge > 0. ')
                                    )

process.negTracks = cms.EDFilter("TrackSelector",
                                    src = cms.InputTag("centralTracks"),
                                    cut = cms.string('charge < 0. ')
                                    )

process.oneGeVTracks = cms.EDFilter("TrackSelector",
                                    src = cms.InputTag("centralTracks"),
                                    cut = cms.string('quality("highPurity") && pt > 1.0 ')
                                    )

process.posOneGeVTracks = process.posTracks.clone(src = cms.InputTag("oneGeVTracks"))
process.negOneGeVTracks = process.negTracks.clone(src = cms.InputTag("oneGeVTracks"))


process.tenGeVTracks = cms.EDFilter("TrackSelector",
                                    src = cms.InputTag("centralTracks"),
                                    cut = cms.string('quality("highPurity") && pt > 10.0 ')
                                    )

process.posTenGeVTracks = process.posTracks.clone(src = cms.InputTag("tenGeVTracks"))
process.negTenGeVTracks = process.negTracks.clone(src = cms.InputTag("tenGeVTracks"))


process.oneGeVPixelTracks = cms.EDFilter("TrackSelector",
                                         src = cms.InputTag("pixelTracks"),
                                         cut = cms.string('abs(eta) < 1.0 && pt > 1.0 ')
                                         )
process.fiveGeVPixelTracks = cms.EDFilter("TrackSelector",
                                          src = cms.InputTag("pixelTracks"),
                                          cut = cms.string('abs(eta) < 1.0 && pt > 5.0 ')
                                          )


process.load("DebugTools.BSSlope.d0phicorranalyzer_cfi")
process.d0phicorranalyzer.trackCollection = cms.InputTag("centralTracks")
process.d0phicorrweighted = process.d0phicorranalyzer.clone(errorAsWeight = cms.bool(True))

process.d0phicorrpos = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("posTracks"))
process.d0phicorrposweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("posTracks"))
process.d0phicorrneg = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("negTracks"))
process.d0phicorrnegweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("negTracks"))

process.d0phicorrOneGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("oneGeVTracks"))
process.d0phicorrOneGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("oneGeVTracks"))
process.d0phicorrposOneGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("posOneGeVTracks"))
process.d0phicorrposOneGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("posOneGeVTracks"))
process.d0phicorrnegOneGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("negOneGeVTracks"))
process.d0phicorrnegOneGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("negOneGeVTracks"))

process.d0phicorrTenGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("tenGeVTracks"))
process.d0phicorrTenGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("tenGeVTracks"))
process.d0phicorrposTenGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("posTenGeVTracks"))
process.d0phicorrposTenGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("posTenGeVTracks"))
process.d0phicorrnegTenGeV = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("negTenGeVTracks"))
process.d0phicorrnegTenGeVweighted = process.d0phicorrweighted.clone(trackCollection = cms.InputTag("negTenGeVTracks"))

process.d0phicorrFiveGeVPixel = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("fiveGeVPixelTracks"))
process.d0phicorrOneGeVPixel = process.d0phicorranalyzer.clone(trackCollection = cms.InputTag("oneGeVPixelTracks"))

process.seqTrackFilters = cms.Sequence(process.centralTracks + process.posTracks + process.negTracks +
                                       process.oneGeVTracks + process.posOneGeVTracks + process.negOneGeVTracks +
                                       process.tenGeVTracks + process.posTenGeVTracks + process.negTenGeVTracks 
                                       )

if options.isAOD == 0:
    process.seqPixelTrackFilters = cms.Sequence(process.oneGeVPixelTracks + process.fiveGeVPixelTracks)
else:
    process.seqPixelTrackFilters = cms.Sequence()
    
process.seqP0Analysis = cms.Sequence(process.d0phicorranalyzer + process.d0phicorrweighted +
                                     process.d0phicorrpos + process.d0phicorrposweighted +
                                     process.d0phicorrneg + process.d0phicorrnegweighted +
                                     process.d0phicorrOneGeV + process.d0phicorrOneGeVweighted +
                                     process.d0phicorrposOneGeV + process.d0phicorrposOneGeVweighted +
                                     process.d0phicorrnegOneGeV + process.d0phicorrnegOneGeVweighted +
                                     process.d0phicorrTenGeV + process.d0phicorrTenGeVweighted +
                                     process.d0phicorrposTenGeV + process.d0phicorrposTenGeVweighted +
                                     process.d0phicorrnegTenGeV + process.d0phicorrnegTenGeVweighted
                                     )

if options.isAOD == 0:
    process.seqP0Analysis.extend(process.d0phicorrOneGeVPixel + process.d0phicorrFiveGeVPixel)

if options.noHLT == 1:
    process.p0 = cms.Path(process.seqBitSelection + process.seqTrackFilters + process.seqPixelTrackFilters +
                          process.seqP0Analysis)
    
for label,trigger,negate in zip(options.triggerLabels,options.triggerPaths,options.negateFlags):
    cloneProcessingSnippet(process,process.seqHLTSelection,label)
    getattr(process,"hltSelection"+label).triggerConditions = cms.vstring(trigger)
    
    if negate == 1:
        tempmodule = getattr(process,"hltSelection"+label)
        getattr(process,"seqHLTSelection"+label).replace(getattr(process,"hltSelection"+label),~tempmodule)
        
    cloneProcessingSnippet(process,process.seqP0Analysis,label)

    setattr(process,"p0"+label,cms.Path(process.seqBitSelection + getattr(process,"seqHLTSelection"+label) +
                                        process.seqTrackFilters + process.seqPixelTrackFilters +
                                        getattr(process,"seqP0Analysis"+label)))


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('d0phicorranalyzer.root')
                                   )

