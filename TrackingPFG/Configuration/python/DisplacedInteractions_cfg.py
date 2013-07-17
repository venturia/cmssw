import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("DisplacedInteractions")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
#options.globalTag = "DONOTEXIST::All"
options.register ('hltPath',
                  "HLT_JET140U*",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTPath")
options.register ('HLTprocess',
                  "HLT",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "HLTProcess")
options.register ('isMC',
                  0,
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  " = 1 if MC are analyzed")

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

# event selection
process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("DPGAnalysis.Skims.DetStatus_cfi")
process.dcsstatus.DetectorType = cms.vstring("TIBTID","TOB","TECp","TECm","BPIX","FPIX") 


process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")
process.hltSelection.TriggerResultsTag = cms.InputTag("TriggerResults","",options.HLTprocess)

if options.isMC == 1: 
   process.seqBasicSelection = cms.Sequence()
else: 
   process.seqBasicSelection = cms.Sequence(process.dcsstatus + process.seqBitSelection)

# jet selection

process.load("TrackingPFG.Utilities.jetfilter_cfi")
process.centraljetfilter = process.jetfilter.clone(maxRapidityCut = cms.double(2.4), nJetMin = cms.uint32(1))

process.seqWithTwoJets = cms.Sequence(process.jetfilter)
process.seqWithCentralJet = cms.Sequence(process.jetfilter + process.centraljetfilter)


# event time history
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.eventtimedistrwithvertexwithtwojets = process.eventtimedistribution.clone()
process.eventtimedistrwithvertexwithcentraljet = process.eventtimedistribution.clone()
process.eventtimedistrnovertexwithtwojets = process.eventtimedistribution.clone()
process.eventtimedistrnovertexwithcentraljet = process.eventtimedistribution.clone()

# Vertex MC truth

process.load("Validation.RecoVertex.mcverticesanalyzer_cfi")
process.mcverticeswithvertexwithtwojets = process.mcverticesanalyzer.clone()
process.mcverticeswithvertexwithcentraljet = process.mcverticesanalyzer.clone()
process.mcverticesnovertexwithtwojets = process.mcverticesanalyzer.clone()
process.mcverticesnovertexwithcentraljet = process.mcverticesanalyzer.clone()


# event based distributions

if options.isMC == 1:
   process.seqEventStatWithVertexWithTwoJets = cms.Sequence(process.eventtimedistrwithvertexwithtwojets + process.mcverticeswithvertexwithtwojets)
   process.seqEventStatWithVertexWithCentralJet = cms.Sequence(process.eventtimedistrwithvertexwithcentraljet + process.mcverticeswithvertexwithcentraljet)
   process.seqEventStatNoVertexWithTwoJets = cms.Sequence(process.eventtimedistrnovertexwithtwojets + process.mcverticesnovertexwithtwojets)
   process.seqEventStatNoVertexWithCentralJet = cms.Sequence(process.eventtimedistrnovertexwithcentraljet + process.mcverticesnovertexwithcentraljet)
else:
   process.seqEventStatWithVertexWithTwoJets = cms.Sequence(process.eventtimedistrwithvertexwithtwojets)
   process.seqEventStatWithVertexWithCentralJet = cms.Sequence(process.eventtimedistrwithvertexwithcentraljet)
   process.seqEventStatNoVertexWithTwoJets = cms.Sequence(process.eventtimedistrnovertexwithtwojets)
   process.seqEventStatNoVertexWithCentralJet = cms.Sequence(process.eventtimedistrnovertexwithcentraljet)
   
# filters on vertex

process.novertex = cms.EDFilter("VertexSelector",
                                src = cms.InputTag("offlinePrimaryVertices"),
                                cut = cms.string("!isFake && ndof > 4 && abs(z) <= 36 && position.Rho <= 2"),
                                filter = cms.bool(True)   # otherwise it won't filter the events, just produce an empty vertex collection.
                                )
process.withvertex = cms.EDFilter("VertexSelector",
                                  src = cms.InputTag("offlinePrimaryVertices"),
                                  cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                  filter = cms.bool(True)   # otherwise it won't filter the events, just produce an empty vertex collection.
                                  )

process.basicvertices = cms.EDFilter("VertexSelector",
                                     src = cms.InputTag("offlinePrimaryVertices"),
                                     cut = cms.string("!isFake && ndof > 4"),
                                     filter = cms.bool(False)   # otherwise it won't filter the events, just produce an empty vertex collection.
                                     )

# special PV reconstruction only for no vertex paths

process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi")
process.pixellessVertices = process.offlinePrimaryVertices.clone()
process.pixellessVertices.minNdof  = cms.double(4.0)
process.pixellessVertices.TkFilterParameters.minPixelLayersWithHits = cms.int32(0)
process.pixellessVertices.TkClusParameters.TkGapClusParameters.zSeparation = cms.double(0.5)

process.seqSpecialReco = cms.Sequence(process.pixellessVertices)

# vertex  filter sequences

process.seqWithVertex = cms.Sequence(process.withvertex)
process.seqNoVertex = cms.Sequence(~process.novertex + process.seqSpecialReco)
process.seqSideBandsVertex = cms.Sequence(~process.withvertex + process.novertex)

# common reco

process.seqCommonReco = cms.Sequence(process.basicvertices + process.seqEventHistoryReco)

# common sequence

process.seqCommon = cms.Sequence(process.seqBasicSelection + process.seqCommonReco)

# jet spectrum analyzers

process.load("TrackingPFG.Utilities.jetspectrumanalyzer_cfi")
process.jetspectrumwithvertexwithtwojets = process.jetspectrumanalyzer.clone()
process.jetspectrumnovertexwithtwojets = process.jetspectrumanalyzer.clone()

process.jetspectrumwithvertexwithcentraljet = process.jetspectrumanalyzer.clone(maxRapidityCut = cms.double(2.4))
process.jetspectrumnovertexwithcentraljet = process.jetspectrumanalyzer.clone(maxRapidityCut = cms.double(2.4))

# primary vertex analyzers

process.load("Validation.RecoVertex.anotherprimaryvertexanalyzer_cfi")
process.primaryvertexanalyzer.vHistogramMakerPSet.histoParameters = cms.untracked.PSet(
   nBinX = cms.untracked.uint32(2000), xMin=cms.untracked.double(-0.5), xMax=cms.untracked.double(0.5),
   nBinY = cms.untracked.uint32(2000), yMin=cms.untracked.double(-0.5), yMax=cms.untracked.double(0.5),
   nBinZ = cms.untracked.uint32(1500), zMin=cms.untracked.double(-150.), zMax=cms.untracked.double(150.)
   )
process.primaryvertexanalyzer.vHistogramMakerPSet.runHisto=cms.untracked.bool(False)

process.allpvwithvertexwithtwojets = process.primaryvertexanalyzer.clone()
process.firstpvwithvertexwithtwojets = process.primaryvertexanalyzer.clone(firstOnly = cms.untracked.bool(True))
process.goodpvwithvertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"))
process.firstgoodpvwithvertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"),
                                                                               firstOnly = cms.untracked.bool(True))
process.allpvwithvertexwithcentraljet = process.primaryvertexanalyzer.clone()
process.firstpvwithvertexwithcentraljet = process.primaryvertexanalyzer.clone(firstOnly = cms.untracked.bool(True))
process.goodpvwithvertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"))
process.firstgoodpvwithvertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"),
                                                                               firstOnly = cms.untracked.bool(True))
process.allpvnovertexwithtwojets = process.primaryvertexanalyzer.clone()
process.firstpvnovertexwithtwojets = process.primaryvertexanalyzer.clone(firstOnly = cms.untracked.bool(True))
process.goodpvnovertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"))
process.firstgoodpvnovertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"),
                                                                               firstOnly = cms.untracked.bool(True))
process.pxllesspvnovertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("pixellessVertices"))
process.firstpxllesspvnovertexwithtwojets = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("pixellessVertices"),
                                                                               firstOnly = cms.untracked.bool(True))
process.allpvnovertexwithcentraljet = process.primaryvertexanalyzer.clone()
process.firstpvnovertexwithcentraljet = process.primaryvertexanalyzer.clone(firstOnly = cms.untracked.bool(True))
process.goodpvnovertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"))
process.firstgoodpvnovertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("basicvertices"),
                                                                               firstOnly = cms.untracked.bool(True))
process.pxllesspvnovertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("pixellessVertices"))
process.firstpxllesspvnovertexwithcentraljet = process.primaryvertexanalyzer.clone(pvCollection = cms.InputTag("pixellessVertices"),
                                                                               firstOnly = cms.untracked.bool(True))

process.seqPVWithVertexWithTwoJets = cms.Sequence(process.allpvwithvertexwithtwojets +
                                                  process.firstpvwithvertexwithtwojets +
                                                  process.goodpvwithvertexwithtwojets +               
                                                  process.firstgoodpvwithvertexwithtwojets)
process.seqPVWithVertexWithCentralJet = cms.Sequence(process.allpvwithvertexwithcentraljet +
                                                  process.firstpvwithvertexwithcentraljet +
                                                  process.goodpvwithvertexwithcentraljet +               
                                                  process.firstgoodpvwithvertexwithcentraljet)
process.seqPVNoVertexWithTwoJets = cms.Sequence(process.allpvnovertexwithtwojets +
                                                  process.firstpvnovertexwithtwojets +
                                                  process.goodpvnovertexwithtwojets +               
                                                  process.firstgoodpvnovertexwithtwojets +
                                                  process.pxllesspvnovertexwithtwojets +               
                                                  process.firstpxllesspvnovertexwithtwojets)
process.seqPVNoVertexWithCentralJet = cms.Sequence(process.allpvnovertexwithcentraljet +
                                                  process.firstpvnovertexwithcentraljet +
                                                  process.goodpvnovertexwithcentraljet +               
                                                  process.firstgoodpvnovertexwithcentraljet +
                                                  process.pxllesspvnovertexwithcentraljet +               
                                                  process.firstpxllesspvnovertexwithcentraljet)
# analysis paths

process.seqWithVertexWithTwoJetsAnalysis = cms.Sequence(process.seqEventStatWithVertexWithTwoJets + process.jetspectrumwithvertexwithtwojets +
                                                        process.seqPVWithVertexWithTwoJets)
process.seqNoVertexWithTwoJetsAnalysis = cms.Sequence(process.seqEventStatNoVertexWithTwoJets + process.jetspectrumnovertexwithtwojets +
                                                      process.seqPVNoVertexWithTwoJets)
process.seqWithVertexWithCentralJetAnalysis = cms.Sequence(process.seqEventStatWithVertexWithCentralJet + process.jetspectrumwithvertexwithcentraljet +
                                                           process.seqPVWithVertexWithCentralJet)
process.seqNoVertexWithCentralJetAnalysis = cms.Sequence(process.seqEventStatNoVertexWithCentralJet + process.jetspectrumnovertexwithcentraljet +
                                                         process.seqPVNoVertexWithCentralJet)


#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

#----------------------------------------------------------------------------

#process.hltSelection.HLTPaths = cms.vstring("HLT_Jet140U*")
process.hltSelection.HLTPaths = cms.vstring(options.hltPath)

process.pwithvertexwithtwojets = cms.Path(process.seqCommon + process.seqHLTSelection + process.seqWithTwoJets + process.seqWithVertex +
                                          process.seqWithVertexWithTwoJetsAnalysis )
process.pnovertexwithtwojets = cms.Path(process.seqCommon + process.seqHLTSelection + process.seqWithTwoJets + process.seqNoVertex +
                                        process.seqNoVertexWithTwoJetsAnalysis )
process.pwithvertexwithcentraljet = cms.Path(process.seqCommon + process.seqHLTSelection + process.seqWithCentralJet + process.seqWithVertex +
                                             process.seqWithVertexWithCentralJetAnalysis )
process.pnovertexwithcentraljet = cms.Path(process.seqCommon + process.seqHLTSelection + process.seqWithCentralJet + process.seqNoVertex +
                                           process.seqNoVertexWithCentralJetAnalysis )



cloneProcessingSnippet(process,process.seqHLTSelection,"Jet140U")
process.hltSelectionJet140U.HLTPaths = cms.vstring("HLT_Jet140U*")

cloneProcessingSnippet(process,process.seqWithVertexWithTwoJetsAnalysis,"Jet140U")
cloneProcessingSnippet(process,process.seqNoVertexWithTwoJetsAnalysis,"Jet140U")
cloneProcessingSnippet(process,process.seqWithVertexWithCentralJetAnalysis,"Jet140U")
cloneProcessingSnippet(process,process.seqNoVertexWithCentralJetAnalysis,"Jet140U")

process.pwithvertexwithtwojetsJet140U = cms.Path(process.seqCommon + process.seqHLTSelectionJet140U + process.seqWithTwoJets + process.seqWithVertex +
                                          process.seqWithVertexWithTwoJetsAnalysisJet140U )
process.pnovertexwithtwojetsJet140U = cms.Path(process.seqCommon + process.seqHLTSelectionJet140U + process.seqWithTwoJets + process.seqNoVertex +
                                        process.seqNoVertexWithTwoJetsAnalysisJet140U )
process.pwithvertexwithcentraljetJet140U = cms.Path(process.seqCommon + process.seqHLTSelectionJet140U + process.seqWithCentralJet + process.seqWithVertex +
                                             process.seqWithVertexWithCentralJetAnalysisJet140U )
process.pnovertexwithcentraljetJet140U = cms.Path(process.seqCommon + process.seqHLTSelectionJet140U + process.seqWithCentralJet + process.seqNoVertex +
                                           process.seqNoVertexWithCentralJetAnalysisJet140U )

#----------------------------------

cloneProcessingSnippet(process,process.seqHLTSelection,"Jet70U")
process.hltSelectionJet70U.HLTPaths = cms.vstring("HLT_Jet70U*")

cloneProcessingSnippet(process,process.seqWithVertexWithTwoJetsAnalysis,"Jet70U")
cloneProcessingSnippet(process,process.seqNoVertexWithTwoJetsAnalysis,"Jet70U")
cloneProcessingSnippet(process,process.seqWithVertexWithCentralJetAnalysis,"Jet70U")
cloneProcessingSnippet(process,process.seqNoVertexWithCentralJetAnalysis,"Jet70U")

process.pwithvertexwithtwojetsJet70U = cms.Path(process.seqCommon + process.seqHLTSelectionJet70U + process.seqWithTwoJets + process.seqWithVertex +
                                          process.seqWithVertexWithTwoJetsAnalysisJet70U )
process.pnovertexwithtwojetsJet70U = cms.Path(process.seqCommon + process.seqHLTSelectionJet70U + process.seqWithTwoJets + process.seqNoVertex +
                                              process.seqNoVertexWithTwoJetsAnalysisJet70U )
process.pwithvertexwithcentraljetJet70U = cms.Path(process.seqCommon + process.seqHLTSelectionJet70U + process.seqWithCentralJet + process.seqWithVertex +
                                                   process.seqWithVertexWithCentralJetAnalysisJet70U )
process.pnovertexwithcentraljetJet70U = cms.Path(process.seqCommon + process.seqHLTSelectionJet70U + process.seqWithCentralJet + process.seqNoVertex +
                                                 process.seqNoVertexWithCentralJetAnalysisJet70U )

#--------------------------------------
cloneProcessingSnippet(process,process.seqHLTSelection,"Jet50U")
process.hltSelectionJet50U.HLTPaths = cms.vstring("HLT_Jet50U*")

cloneProcessingSnippet(process,process.seqWithVertexWithTwoJetsAnalysis,"Jet50U")
cloneProcessingSnippet(process,process.seqNoVertexWithTwoJetsAnalysis,"Jet50U")
cloneProcessingSnippet(process,process.seqWithVertexWithCentralJetAnalysis,"Jet50U")
cloneProcessingSnippet(process,process.seqNoVertexWithCentralJetAnalysis,"Jet50U")

process.pwithvertexwithtwojetsJet50U = cms.Path(process.seqCommon + process.seqHLTSelectionJet50U + process.seqWithTwoJets + process.seqWithVertex +
                                          process.seqWithVertexWithTwoJetsAnalysisJet50U )
process.pnovertexwithtwojetsJet50U = cms.Path(process.seqCommon + process.seqHLTSelectionJet50U + process.seqWithTwoJets + process.seqNoVertex +
                                        process.seqNoVertexWithTwoJetsAnalysisJet50U )
process.pwithvertexwithcentraljetJet50U = cms.Path(process.seqCommon + process.seqHLTSelectionJet50U + process.seqWithCentralJet + process.seqWithVertex +
                                             process.seqWithVertexWithCentralJetAnalysisJet50U )
process.pnovertexwithcentraljetJet50U = cms.Path(process.seqCommon + process.seqHLTSelectionJet50U + process.seqWithCentralJet + process.seqNoVertex +
                                           process.seqNoVertexWithCentralJetAnalysisJet50U )


#-----------------------------------

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('DisplacedInteractions.root')
                                   )

#----------------------------------
process.novertexevent = cms.OutputModule("PoolOutputModule",
                                         fileName = cms.untracked.string("novertexevents.root"),
                                         outputCommands = cms.untracked.vstring("keep *"),
                                         SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pnovertex*"))
	)

#process.e = cms.EndPath(process.novertexevent)


