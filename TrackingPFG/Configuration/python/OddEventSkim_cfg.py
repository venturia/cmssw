import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet

process = cms.Process("OddEventSkimNew")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register ('globalTag',
                  "DONOTEXIST::All",
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "GlobalTag")
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

# bad components monitoring

process.load("DPGAnalysis.SiStripTools.sistripqualityhistory_cfi")
process.ssqhistory.eventProcess = cms.bool(True)
#process.ssqhistory.startingLSFraction = cms.untracked.uint32(4)
#process.ssqhistory.maxLSBeforeRebin = cms.untracked.uint32(100)
process.ssqhistory.startingLSFraction = cms.untracked.uint32(16)
process.ssqhistory.maxLSBeforeRebin = cms.untracked.uint32(200)
process.ssqhistory.granularityMode = cms.untracked.uint32(1)
process.ssqhistory.monitoredSiStripQuality = cms.VPSet(
    cms.PSet( name = cms.string("HVDCS"), ssqLabel = cms.string("HVDCS"))
   )


import CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi
process.ssqhvdcs = CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi.siStripQualityESProducer.clone()
process.ssqhvdcs.appendToDataLabel = cms.string("HVDCS")
process.ssqhvdcs.ListOfRecordToMerge=cms.VPSet(
 cms.PSet(record=cms.string('SiStripDetVOffRcd'),tag=cms.string(''))
)


# event time history
process.load("TrackingPFG.Configuration.eventHistoryOddEventSkimSequence_cff")

# cluster multiplicity
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestOddEventSkimSequence_cff")

#track count
process.load("TrackingPFG.Configuration.simpleTrackOddEventSkimSequence_cff")

# Filters ---------------------------------------------------------------------------------------------------

process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")

#process.seqBitSelection = cms.Sequence()

#process.load("TrackingPFG.Utilities.jetfilter_cfi")

process.jetfilter = cms.EDFilter("SimpleJetFilter",
                                                  jetCollection = cms.InputTag("ak5CaloJets"),
                                                  jetIDMap = cms.InputTag("ak5JetID"),
                                                  ptCut = cms.double(30.),
                                                  maxRapidityCut = cms.double(999.0),
                                                  nJetMin = cms.uint32(2)
                                                  )

process.centraljetfilter = process.jetfilter.clone(maxRapidityCut = cms.double(2.4), nJetMin = cms.uint32(1))

process.load("TrackingPFG.Configuration.hpSelectionSequence_cff")
process.load("TrackingPFG.Configuration.goodVertexSelector_cfi")
process.seqPixelLessReco = cms.Sequence(process.highPurityTracks + process.goodDisplacedVertices)

process.load("TrackingPFG.Utilities.pixellessfilter_cfi")
process.pixellessfilter.trackCollection = cms.InputTag("highPurityTracks")
process.pixellessfilter.vtxCollection = cms.InputTag("goodDisplacedVertices")
process.pixellessfilter.newIter=cms.bool(True)
process.pixellessfilter.filter=cms.bool(True)
process.pixellessfilter.vtxzMax=cms.double(12)
process.nitertibtidhpfilter = process.pixellessfilter.clone(cuts=cms.vdouble(0.8,0.,0.))
process.nitertobtechpfilter = process.pixellessfilter.clone(cuts=cms.vdouble(0.,1.0,0.))
process.niterpixellesshpfilter = process.pixellessfilter.clone(cuts=cms.vdouble(0.,0.,1.0))

process.notrack = cms.EDFilter("TrackSelector",
                               src = cms.InputTag("generalTracks"),
                               cut = cms.string(""),
                               filter = cms.bool(True)
                               )

process.novertex = cms.EDFilter("VertexSelector",
                                src = cms.InputTag("offlinePrimaryVertices"),
                                cut = cms.string("!isFake && ndof > 4 && abs(z) <= 36 && position.Rho <= 2"),
                                filter = cms.bool(True)   # otherwise it won't filter the events, just produce an empty vertex collection.
                                )

process.load("DPGAnalysis.Skims.DetStatus_cfi")
process.dcsstatus.DetectorType = cms.vstring("TIBTID","TOB","TECp","TECm","BPIX","FPIX") 

process.load("DPGAnalysis.SiStripTools.bysipixelvssistripclustmulteventfilter_cfi")
process.manystripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("( mult2 > 20000+7*mult1)"))
process.toomanystripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2>50000) && ( mult2 > 20000+7*mult1)"))
process.manyclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 > 50000) && (mult1 > 6500)"))
process.nostripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 <= 1) && (mult1 > 50)"))
process.noclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 <= 1) && (mult1 <= 1)"))
process.offdiagonal = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("( mult2 < 7*(mult1-1000))"))
process.someclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 > 700) && (mult1 > 100)"))

# Global Event Selection Sequence ------------------------------------------------------------------------------------------
process.seqGlobalEventSelAnyDCS = cms.Sequence(process.seqBitSelection)
process.seqGlobalEventSelection = cms.Sequence(process.dcsstatus +  process.seqBitSelection)
#process.seqGlobalEventSelection = cms.Sequence()
# Selection Sequences -------------------------------------------------------------------------------------------------------

process.seqNoTrack = cms.Sequence(~process.notrack +~process.logErrorAnalysisTooManyClusters)
process.seqNoTrackSkim = cms.Sequence(~process.notrack +~process.logErrorAnalysisTooManyClusters + process.someclusters)
process.seqNoTrackWithTwoJets = cms.Sequence(~process.notrack +~process.logErrorAnalysisTooManyClusters + process.jetfilter)
process.seqNoTrackWithCentralJet = cms.Sequence(~process.notrack +~process.logErrorAnalysisTooManyClusters + process.jetfilter + process.centraljetfilter)
process.seqNoVertex = cms.Sequence(~process.novertex + ~process.logErrorAnalysisTooManyClusters)
process.seqNoVertexSkim = cms.Sequence(~process.novertex + ~process.logErrorAnalysisTooManyClusters + process.someclusters)
process.seqNoVertexWithTwoJets = cms.Sequence(~process.novertex + ~process.logErrorAnalysisTooManyClusters + process.jetfilter)
process.seqNoVertexWithCentralJet = cms.Sequence(~process.novertex + ~process.logErrorAnalysisTooManyClusters + process.jetfilter + process.centraljetfilter)
process.seqNoStrip = cms.Sequence(process.nostripclusters)
process.seqNoClusters = cms.Sequence(process.noclusters)
process.seqOffDiagonal = cms.Sequence(process.offdiagonal)
process.seqManyStripClusters = cms.Sequence(process.manystripclusters)
process.seqTooManyStripClusters = cms.Sequence(process.toomanystripclusters)
process.seqManyClusters = cms.Sequence(process.manyclusters)
process.seqTooManyErrors = cms.Sequence(process.logErrorAnalysisTooManyErrors)
process.seqNitertibtidhp = cms.Sequence(process.seqPixelLessReco + process.nitertibtidhpfilter)
process.seqNitertobtechp = cms.Sequence(process.seqPixelLessReco + process.nitertobtechpfilter)
process.seqNiterpixellesshp = cms.Sequence(process.seqPixelLessReco + process.niterpixellesshpfilter)

# Analysis Sequences ---------------------------------------------------------------------------------------------------

process.seqP0Analysis = cms.Sequence(process.eventtimedistribution + process.seqClusMultInvest)
process.seqAnyDCSAnalysis = cms.Sequence(process.eventtimedistranydcs + process.ssqhistory)
process.seqNoTrackAnalysis = cms.Sequence(process.eventtimedistrnotrack + process.seqClusMultInvestNoTrack)
process.seqNoTrackSkimAnalysis = cms.Sequence(process.eventtimedistrnotrackskim + process.seqClusMultInvestNoTrackSkim)
process.seqNoTrackWithTwoJetsAnalysis = cms.Sequence(process.eventtimedistrnotrackwithtwojets + process.seqClusMultInvestNoTrackWithTwoJets)
process.seqNoTrackWithCentralJetAnalysis = cms.Sequence(process.eventtimedistrnotrackwithcentraljet + process.seqClusMultInvestNoTrackWithCentralJet)
process.seqNoVertexAnalysis = cms.Sequence(process.eventtimedistrnovertex + process.seqSimpleTrackNoVertex + process.seqClusMultInvestNoVertex)
process.seqNoVertexSkimAnalysis = cms.Sequence(process.eventtimedistrnovertexskim + process.seqSimpleTrackNoVertexSkim + process.seqClusMultInvestNoVertexSkim)
process.seqNoVertexWithTwoJetsAnalysis = cms.Sequence(process.eventtimedistrnovertexwithtwojets + process.seqSimpleTrackNoVertexWithTwoJets + process.seqClusMultInvestNoVertexWithTwoJets)
process.seqNoVertexWithCentralJetAnalysis = cms.Sequence(process.eventtimedistrnovertexwithcentraljet + process.seqSimpleTrackNoVertexWithCentralJet + process.seqClusMultInvestNoVertexWithCentralJet)
process.seqNoStripAnalysis = cms.Sequence(process.eventtimedistrnostrip + process.seqSimpleTrackNoStrip + process.seqClusMultInvestNoStrip)
process.seqNoClustersAnalysis = cms.Sequence(process.eventtimedistrnoclusters )
process.seqOffDiagonalAnalysis = cms.Sequence(process.eventtimedistroffdiag + process.seqSimpleTrackOffDiag + process.seqClusMultInvestOffDiag)
process.seqManyStripClustersAnalysis = cms.Sequence(process.eventtimedistrmanystripclus + process.seqSimpleTrackManyStripClus + process.seqClusMultInvestManyStripClus)
process.seqTooManyStripClustersAnalysis = cms.Sequence(process.eventtimedistrtoomanystripclus + process.seqSimpleTrackTooManyStripClus + process.seqClusMultInvestTooManyStripClus)
process.seqManyClustersAnalysis = cms.Sequence(process.eventtimedistrmanyclus + process.seqSimpleTrackManyClus + process.seqClusMultInvestManyClus)
process.seqTooManyErrorsAnalysis = cms.Sequence(process.eventtimedistrtoomanyerrors)
process.seqNitertibtidhpAnalysis = cms.Sequence(process.eventtimedistrnitertibtidhp + process.seqSimpleTrackNitertibtidhp + process.seqClusMultInvestNitertibtidhp)
process.seqNitertobtechpAnalysis = cms.Sequence(process.eventtimedistrnitertobtechp + process.seqSimpleTrackNitertobtechp + process.seqClusMultInvestNitertobtechp)
process.seqNiterpixellesshpAnalysis = cms.Sequence(process.eventtimedistrniterpixellesshp + process.seqSimpleTrackNiterpixellesshp + process.seqClusMultInvestNiterpixellesshp)

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

# Generic paths ------------------------------------------------------------------------

if options.noHLT == 1:
   process.p0 = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                         process.seqEventHistoryReco +
                         process.seqMultProd +
                         process.seqP0Analysis)

   process.panydcs = cms.Path(process.seqGlobalEventSelAnyDCS + process.seqHLTSelection +
                         process.seqEventHistoryReco +
                         process.seqAnyDCSAnalysis)

   process.pnitertibtidhp = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection + 
                                     process.seqEventHistoryReco +
                                     process.seqMultProd +
                                     process.seqNitertibtidhp +     
                                     process.seqNitertibtidhpAnalysis)

   process.pnitertobtechp = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection + 
                                     process.seqEventHistoryReco +
                                     process.seqMultProd +
                                     process.seqNitertobtechp +     
                                     process.seqNitertobtechpAnalysis)

   process.pniterpixellesshp = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection + 
                                     process.seqEventHistoryReco +
                                     process.seqMultProd +
                                     process.seqNiterpixellesshp +     
                                     process.seqNiterpixellesshpAnalysis)

   process.pnotrack = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                               process.seqEventHistoryReco +
                               process.seqMultProd +
                               process.seqNoTrack +
                               process.seqNoTrackAnalysis)

   process.pnotrackskim = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                   process.seqEventHistoryReco +
                                   process.seqMultProd +
                                   process.seqNoTrackSkim +
                                   process.seqNoTrackSkimAnalysis)

   process.pnotrackwithtwojets = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                          process.seqEventHistoryReco +
                                          process.seqMultProd +
                                          process.seqNoTrackWithTwoJets +
                                          process.seqNoTrackWithTwoJetsAnalysis)

   process.pnotrackwithcentraljet = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                             process.seqEventHistoryReco +
                                             process.seqMultProd +
                                             process.seqNoTrackWithCentralJet +
                                             process.seqNoTrackWithCentralJetAnalysis)
   
   process.pnovertex = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                process.seqEventHistoryReco +
                                process.seqMultProd +
                                process.seqNoVertex +
                                process.seqNoVertexAnalysis)

   process.pnovertexskim = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                    process.seqEventHistoryReco +
                                    process.seqMultProd +
                                    process.seqNoVertexSkim +
                                    process.seqNoVertexSkimAnalysis)

   process.pnovertexwithtwojets = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                           process.seqEventHistoryReco +
                                           process.seqMultProd +
                                           process.seqNoVertexWithTwoJets +
                                           process.seqNoVertexWithTwoJetsAnalysis)

   process.pnovertexwithcentraljet = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                              process.seqEventHistoryReco +
                                              process.seqMultProd +
                                              process.seqNoVertexWithCentralJet +
                                              process.seqNoVertexWithCentralJetAnalysis)
                                           
   process.pnostrip = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                               process.seqEventHistoryReco +
                               process.seqMultProd +
                               process.seqNoStrip +
                               process.seqNoStripAnalysis)

   process.pnoclusters = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                  process.seqEventHistoryReco +
                                  process.seqNoClusters +
                                  process.seqNoClustersAnalysis)

   process.poffdiagonal = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                   process.seqEventHistoryReco +
                                   process.seqMultProd +
                                   process.seqOffDiagonal +
                                   process.seqPixelLessReco +
                                   process.seqOffDiagonalAnalysis)

   process.pmanystripclus = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                     process.seqEventHistoryReco +
                                     process.seqMultProd +
                                     process.seqManyStripClusters +
                                     process.seqPixelLessReco +
                                     process.seqManyStripClustersAnalysis)

   process.ptoomanystripclus = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                        process.seqEventHistoryReco +
                                        process.seqMultProd +
                                        process.seqTooManyStripClusters +
                                        process.seqPixelLessReco +
                                        process.seqTooManyStripClustersAnalysis)

   process.pmanyclus = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                process.seqEventHistoryReco +
                                process.seqMultProd +
                                process.seqManyClusters +
                                process.seqPixelLessReco +
                                process.seqManyClustersAnalysis)
   
   process.ptoomanyerrors = cms.Path(process.seqGlobalEventSelection + process.seqHLTSelection +
                                     process.seqEventHistoryReco +
                                     process.seqTooManyErrors +
                                     process.seqTooManyErrorsAnalysis)
   
# Cloned paths for each trigger ---------------------------------------------------------------------------
for label, trigger,negate in zip(options.triggerLabels,options.triggerPaths,options.negateFlags):
   cloneProcessingSnippet(process,process.seqHLTSelection,label)
   getattr(process,"hltSelection"+label).triggerConditions = cms.vstring(trigger)

   if negate == 1:
      tempmodule = getattr(process,"hltSelection"+label)
      getattr(process,"seqHLTSelection"+label).replace(getattr(process,"hltSelection"+label),~tempmodule)

   cloneProcessingSnippet(process,process.seqP0Analysis,label)
   cloneProcessingSnippet(process,process.seqAnyDCSAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoTrackAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoTrackSkimAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoTrackWithTwoJetsAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoTrackWithCentralJetAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoVertexAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoVertexSkimAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoVertexWithTwoJetsAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoVertexWithCentralJetAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoStripAnalysis,label)
   cloneProcessingSnippet(process,process.seqNoClustersAnalysis,label)
   cloneProcessingSnippet(process,process.seqOffDiagonalAnalysis,label)
   cloneProcessingSnippet(process,process.seqManyStripClustersAnalysis,label)
   cloneProcessingSnippet(process,process.seqTooManyStripClustersAnalysis,label)
   cloneProcessingSnippet(process,process.seqManyClustersAnalysis,label)
   cloneProcessingSnippet(process,process.seqTooManyErrorsAnalysis,label)
   cloneProcessingSnippet(process,process.seqNitertibtidhpAnalysis,label)
   cloneProcessingSnippet(process,process.seqNitertobtechpAnalysis,label)
   cloneProcessingSnippet(process,process.seqNiterpixellesshpAnalysis,label)

   setattr(process,"p0"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                       process.seqEventHistoryReco + 
                                       getattr(process,"seqP0Analysis"+label)))
   setattr(process,"panydcs"+label,cms.Path(process.seqGlobalEventSelAnyDCS + getattr(process,"seqHLTSelection"+label) +
                                       process.seqEventHistoryReco + 
                                       getattr(process,"seqAnyDCSAnalysis"+label)))
   setattr(process,"pnitertibtidhp"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqMultProd + process.seqNitertibtidhp + 
                                             getattr(process,"seqNitertibtidhpAnalysis"+label)))
   setattr(process,"pnitertobtechp"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqMultProd + process.seqNitertobtechp + 
                                             getattr(process,"seqNitertobtechpAnalysis"+label)))
   setattr(process,"pniterpixellesshp"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqMultProd + process.seqNiterpixellesshp + 
                                             getattr(process,"seqNiterpixellesshpAnalysis"+label)))
   setattr(process,"pnotrack"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqMultProd + process.seqNoTrack + 
                                             getattr(process,"seqNoTrackAnalysis"+label)))
   setattr(process,"pnotrackskim"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                 process.seqEventHistoryReco + process.seqMultProd + process.seqNoTrackSkim + 
                                                 getattr(process,"seqNoTrackSkimAnalysis"+label)))
   setattr(process,"pnotrackwithtwojets"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                        process.seqEventHistoryReco + process.seqMultProd + process.seqNoTrackWithTwoJets + 
                                                        getattr(process,"seqNoTrackWithTwoJetsAnalysis"+label)))
   setattr(process,"pnotrackwithcentraljet"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                           process.seqEventHistoryReco + process.seqMultProd + process.seqNoTrackWithCentralJet + 
                                                           getattr(process,"seqNoTrackWithCentralJetAnalysis"+label)))
   setattr(process,"pnovertex"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                              process.seqEventHistoryReco + process.seqMultProd + process.seqNoVertex + 
                                              getattr(process,"seqNoVertexAnalysis"+label)))
   setattr(process,"pnovertexskim"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                  process.seqEventHistoryReco + process.seqMultProd + process.seqNoVertexSkim + 
                                                  getattr(process,"seqNoVertexSkimAnalysis"+label)))
   setattr(process,"pnovertexwithtwojets"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                         process.seqEventHistoryReco + process.seqMultProd + process.seqNoVertexWithTwoJets + 
                                                         getattr(process,"seqNoVertexWithTwoJetsAnalysis"+label)))
   setattr(process,"pnovertexwithcentraljet"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                            process.seqEventHistoryReco + process.seqMultProd + process.seqNoVertexWithCentralJet + 
                                                            getattr(process,"seqNoVertexWithCentralJetAnalysis"+label)))
   setattr(process,"pnostrip"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqMultProd + process.seqNoStrip + 
                                             getattr(process,"seqNoStripAnalysis"+label)))
   setattr(process,"pnoclusters"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                             process.seqEventHistoryReco + process.seqNoClusters + 
                                             getattr(process,"seqNoClustersAnalysis"+label)))
   setattr(process,"poffdiagonal"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                 process.seqEventHistoryReco + process.seqMultProd  + process.seqOffDiagonal +
                                                 process.seqPixelLessReco +
                                                 getattr(process,"seqOffDiagonalAnalysis"+label)))
   setattr(process,"pmanystripclus"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                   process.seqEventHistoryReco + process.seqMultProd + process.seqManyStripClusters + 
                                                   process.seqPixelLessReco +
                                                   getattr(process,"seqManyStripClustersAnalysis"+label)))
   setattr(process,"ptoomanystripclus"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                      process.seqEventHistoryReco + process.seqMultProd + process.seqTooManyStripClusters +
                                                      process.seqPixelLessReco +
                                                      getattr(process,"seqTooManyStripClustersAnalysis"+label)))
   setattr(process,"pmanyclus"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                              process.seqEventHistoryReco + process.seqMultProd + process.seqManyClusters + process.seqPixelLessReco +
                                              getattr(process,"seqManyClustersAnalysis"+label)))
   setattr(process,"ptoomanyerrors"+label,cms.Path(process.seqGlobalEventSelection + getattr(process,"seqHLTSelection"+label) +
                                                   process.seqEventHistoryReco + process.seqMultProd + process.seqTooManyErrors + 
                                                   getattr(process,"seqTooManyErrorsAnalysis"+label)))
   

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('OddEventSkim.root')
                                   )

process.outoddevent = cms.OutputModule("PoolOutputModule",
                                       fileName = cms.untracked.string("oddevents.root"),
                                       outputCommands = cms.untracked.vstring("keep *"),
                                       SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring( #"poffdiagonal",
                                                                                                    "pnostrip","pnoclusters",
                                                                                                    "ptoomanystripclus","pmanystripclus", #"pmanyclus",
                                                                                                    "pnotrackskim","pnovertexskim",
                                                                                                    "pnotrackwithtwojets","pnovertexwithtwojets",
                                                                                                    "pnotrackwithcentraljet","pnovertexwithcentraljet"
#                                                                                                    "pnitertibtidhp","pnitertobtechp","pniterpixellesshp"
                                                                                                    ))
	)

process.e = cms.EndPath(process.outoddevent)

process.schedule = cms.Schedule()

if options.noHLT == 1:
    process.schedule.append(process.p0)
    process.schedule.append(process.panydcs)
    process.schedule.append(process.pnitertibtidhp)
    process.schedule.append(process.pnitertobtechp)
    process.schedule.append(process.pniterpixellesshp)
    process.schedule.append(process.pnotrack)
    process.schedule.append(process.pnotrackskim)
    process.schedule.append(process.pnotrackwithtwojets)
    process.schedule.append(process.pnotrackwithcentraljet)
    process.schedule.append(process.pnovertex)
    process.schedule.append(process.pnovertexskim)
    process.schedule.append(process.pnovertexwithtwojets)
    process.schedule.append(process.pnovertexwithcentraljet)
    process.schedule.append(process.pnostrip)
    process.schedule.append(process.pnoclusters)
    process.schedule.append(process.poffdiagonal)
    process.schedule.append(process.pmanystripclus)
    process.schedule.append(process.ptoomanystripclus)
    process.schedule.append(process.pmanyclus)
    process.schedule.append(process.ptoomanyerrors)
    
for label in options.triggerLabels:
    process.schedule.append(getattr(process,"p0"+label))
    process.schedule.append(getattr(process,"panydcs"+label))
    process.schedule.append(getattr(process,"pnitertibtidhp"+label))
    process.schedule.append(getattr(process,"pnitertobtechp"+label))
    process.schedule.append(getattr(process,"pniterpixellesshp"+label))
    process.schedule.append(getattr(process,"pnotrack"+label))
    process.schedule.append(getattr(process,"pnotrackskim"+label))
    process.schedule.append(getattr(process,"pnotrackwithtwojets"+label))
    process.schedule.append(getattr(process,"pnotrackwithcentraljet"+label))
    process.schedule.append(getattr(process,"pnovertex"+label))
    process.schedule.append(getattr(process,"pnovertexskim"+label))
    process.schedule.append(getattr(process,"pnovertexwithtwojets"+label))
    process.schedule.append(getattr(process,"pnovertexwithcentraljet"+label))
    process.schedule.append(getattr(process,"pnostrip"+label))
    process.schedule.append(getattr(process,"pnoclusters"+label))
    process.schedule.append(getattr(process,"poffdiagonal"+label))
    process.schedule.append(getattr(process,"pmanystripclus"+label))
    process.schedule.append(getattr(process,"ptoomanystripclus"+label))
    process.schedule.append(getattr(process,"pmanyclus"+label))
    process.schedule.append(getattr(process,"ptoomanyerrors"+label))


process.schedule.append(process.e)

#-----------------------------------


