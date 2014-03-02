import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TrackingRereco")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
options.register ('isMC',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if MC are analyzed")
options.register ('withTLR',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if TLR has to be applied")

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_noinfo_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

#--------------------------------------
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("TrackingPFG.Configuration.recoPixelOnlySequence_cff")

process.load("TrackingPFG.Configuration.simpleTrackLogErrSequence_cff")
process.pixeltrackcountRECO = process.pixeltrackcount.clone(trackCollection=cms.InputTag("pixelTracks","","RECO"))

process.load("TrackingPFG.Configuration.pixelVertexDivisiveStdCuts_cfi")
process.load("TrackingPFG.Configuration.pvSequence_cff")
process.pixelvertexanalyzerRECO= process.pixelvertexanalyzer.clone(pvCollection=cms.InputTag("pixelVertices","","RECO"))
process.hltpixelvertex3DbbPhianalyzer= process.pixelvertexanalyzer.clone(pvCollection=cms.InputTag("hltPixelVertices3DbbPhi"))

process.load("Validation.RecoVertex.mcvsrecoverticesanalyzer_cfi")

process.mcvsrecopixelverticesanalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVertices"))
process.mcvsrecopixelverticesanalyzerRECO = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVertices","","RECO"))
process.mcvsrecopixelverticesHLTLikeanalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("pixelVerticesDivisiveHLT"))
process.mcvsrecohltpixelvertices3DbbPhianalyzer = process.mcvsrecoverticesanalyzer.clone(pvCollection = cms.InputTag("hltPixelVertices3DbbPhi"))


process.seqProducers = cms.Sequence(process.seqPixelOnlyTrackReReco
                                    + process.pixelVerticesDivisiveHLT
)

if options.withTLR == 1:
   process.pixelTracks.OrderedHitsFactoryPSet.GeneratorPSet.SeedComparitorPSet.ComponentName = 'none'


process.p0 = cms.Path(
    #    process.pickEvents 
    #    + process.siPixelDigis + process.siStripDigis + process.scalersRawToDigi
    process.seqProducers
    + process.pixeltrackcount + process.pixeltrackcountRECO
    + process.pixelvertexanalyzer + process.pixelvertexanalyzerRECO
    + process.pixelvertexHLTLike
    + process.hltpixelvertex3DbbPhianalyzer
    + process.mcvsrecopixelverticesanalyzer + process.mcvsrecopixelverticesanalyzerRECO
    + process.mcvsrecopixelverticesHLTLikeanalyzer 
    + process.mcvsrecohltpixelvertices3DbbPhianalyzer 
    )


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

#process.GlobalTag.toGet = cms.VPSet(
#   cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
##            tag = cms.string("SiPixelTemplateDBObject_38T_v3_mc"),
#            tag = cms.string("SiPixelTemplateDBObject38Tv2_mc"),
#            connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PIXEL")
#            )
#   )


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('Tracking_rereco_pixelonly.root')
#                                   fileName = cms.string('TrackerLocal_rereco.root')
                                   )

#print process.dumpPython()
