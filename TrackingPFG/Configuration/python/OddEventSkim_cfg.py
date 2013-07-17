import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("OddEventSkimNew")

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

options.parseArguments()

#

process.load("TrackingPFG.Configuration.processOptions_cff")
process.load("TrackingPFG.Configuration.MessageLogger_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("TrackingPFG.Configuration.poolSource_cff")
process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

# event selection
process.load("TrackingPFG.Configuration.bitSelectionSequence_cff")
process.load("TrackingPFG.Configuration.hltSelectionSequence_cff")
process.load("TrackingPFG.Configuration.logErrorSelectionSequence_cff")

process.load("TrackingPFG.Utilities.jetfilter_cfi")

process.centraljetfilter = process.jetfilter.clone(maxRapidityCut = cms.double(2.4), nJetMin = cms.uint32(1))

process.load("TrackingPFG.Configuration.hpSelectionSequence_cff")
process.load("TrackingPFG.Configuration.goodVertexSelector_cfi")
process.seqPixelLessReco = cms.Sequence(process.highPurityTracks + process.goodDisplacedVertices)

process.load("TrackingPFG.Utilities.pixellessfilter_cfi")
process.pixellessfilter.trackCollection = cms.InputTag("highPurityTracks")
process.pixellessfilter.vtxCollection = cms.InputTag("goodDisplacedVertices")
process.pixellessfilter.filter=cms.bool(True)
process.pixellessfilter.vtxzMax=cms.double(12)
process.niter4hpfilter = process.pixellessfilter.clone(cuts=cms.vdouble(0.7,0.,0.))
process.niter5hpfilter = process.pixellessfilter.clone(cuts=cms.vdouble(0.,0.7,0.))


# event time history
process.load("TrackingPFG.Configuration.eventHistorySequence_cff")
process.eventtimedistrnotrack = process.eventtimedistribution.clone()
process.eventtimedistrnotrackskim = process.eventtimedistribution.clone()
process.eventtimedistrnotrackwithtwojets = process.eventtimedistribution.clone()
process.eventtimedistrnotrackwithcentraljet = process.eventtimedistribution.clone()
process.eventtimedistrnovertex = process.eventtimedistribution.clone()
process.eventtimedistrnovertexskim = process.eventtimedistribution.clone()
process.eventtimedistrnovertexwithtwojets = process.eventtimedistribution.clone()
process.eventtimedistrnovertexwithcentraljet = process.eventtimedistribution.clone()
process.eventtimedistroffdiag = process.eventtimedistribution.clone()
process.eventtimedistrnostrip = process.eventtimedistribution.clone()
process.eventtimedistrmanystripclus = process.eventtimedistribution.clone()
process.eventtimedistrtoomanystripclus = process.eventtimedistribution.clone()
process.eventtimedistrtoomanyerrors = process.eventtimedistribution.clone()
process.eventtimedistrmanyclus = process.eventtimedistribution.clone()
process.eventtimedistrniter4hp = process.eventtimedistribution.clone()
process.eventtimedistrniter5hp = process.eventtimedistribution.clone()

# cluster multiplicity
process.load("TrackingPFG.Configuration.multProdSequence_cff")
process.load("TrackingPFG.Configuration.clusMultInvestOddEventSkimSequence_cff")

#track count
process.load("TrackingPFG.Configuration.simpleTrackSequence_cff")
process.trackcountoffdiag = process.trackcount.clone()
process.trackcountnostrip = process.trackcount.clone()
process.trackcountnovertex = process.trackcount.clone()
process.trackcountnovertexskim = process.trackcount.clone()
process.trackcountnovertexwithtwojets = process.trackcount.clone()
process.trackcountnovertexwithcentraljet = process.trackcount.clone()
process.trackcountmanystripclus = process.trackcount.clone()
process.trackcounttoomanystripclus = process.trackcount.clone()
process.trackcountmanyclus = process.trackcount.clone()
process.trackcountniter4hp = process.trackcount.clone()
process.trackcountniter5hp = process.trackcount.clone()
process.trackcounthpniter4hp = process.trackcounthp.clone()
process.trackcounthpniter5hp = process.trackcounthp.clone()

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
process.manystripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("( mult2 > 18000+7*mult1)"))
process.toomanystripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2>50000) && ( mult2 > 18000+7*mult1)"))
process.manyclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 > 50000) && (mult1 > 6500)"))
process.nostripclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 <= 1) && (mult1 > 50)"))
process.offdiagonal = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("( mult2 < 7*(mult1-1000))"))
process.someclusters = process.bysipixelvssistripclustmulteventfilter.clone(cut=cms.string("(mult2 > 50) && (mult1 > 20)"))

process.seqManyStripClusters = cms.Sequence(process.manystripclusters)
process.seqTooManyStripClusters = cms.Sequence(process.toomanystripclusters)
process.seqManyClusters = cms.Sequence(process.manyclusters)
process.seqTooManyErrors = cms.Sequence(process.logErrorAnalysisTooManyErrors)
#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag

#process.hltSelection.HLTPaths = cms.vstring("HLT_Jet140U*")
process.hltSelection.HLTPaths = cms.vstring(options.hltPath)

process.p0 = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                      process.seqEventHistoryReco +
                      process.eventtimedistribution
                      )

#process.pniter4hp = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
#                             process.seqEventHistoryReco +
#                             process.seqPixelLessReco +
#                             process.niter4hpfilter +
#                             process.seqMultProd +
#                             process.eventtimedistrniter4hp +
#                             process.trackcountniter4hp +
#                             process.trackcounthpniter4hp +
#                             process.seqClusMultInvestNiter4hp)

#process.pniter5hp = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
#                             process.seqEventHistoryReco +
#                             process.seqPixelLessReco +
#                             process.niter5hpfilter +
#                             process.seqMultProd +
#                             process.eventtimedistrniter5hp +
#                             process.trackcountniter5hp +
#                             process.trackcounthpniter5hp +
#                             process.seqClusMultInvestNiter5hp)

process.pnotrack = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                            process.seqEventHistoryReco +
                            ~process.notrack +
                            ~process.logErrorAnalysisTooManyClusters +
                            process.seqMultProd +
                            process.eventtimedistrnotrack +
                            process.seqClusMultInvestNoTrack)

process.pnotrackskim = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                process.seqEventHistoryReco +
                                ~process.notrack +
                                ~process.logErrorAnalysisTooManyClusters +
                                process.someclusters + 
                                process.seqMultProd +
                                process.eventtimedistrnotrackskim +
                                process.seqClusMultInvestNoTrackSkim)

process.pnotrackwithtwojets = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                       process.seqEventHistoryReco +
                                       ~process.notrack +
                                       ~process.logErrorAnalysisTooManyClusters +
                                       process.jetfilter +
                                       process.seqMultProd +
                                       process.eventtimedistrnotrackwithtwojets +
                                       process.seqClusMultInvestNoTrackWithTwoJets)

process.pnotrackwithcentraljet = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                          process.seqEventHistoryReco +
                                          ~process.notrack +
                                          ~process.logErrorAnalysisTooManyClusters +
                                          process.jetfilter +
                                          process.centraljetfilter +
                                          process.seqMultProd +
                                          process.eventtimedistrnotrackwithcentraljet +
                                          process.seqClusMultInvestNoTrackWithCentralJet)

process.pnovertex = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                             process.seqEventHistoryReco +
                             ~process.novertex +
                             ~process.logErrorAnalysisTooManyClusters +
                             process.seqMultProd +
                             process.eventtimedistrnovertex +
                             process.trackcountnovertex +
                             process.seqClusMultInvestNoVertex)

process.pnovertexskim = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                 process.seqEventHistoryReco +
                                 ~process.novertex +
                                 ~process.logErrorAnalysisTooManyClusters +
                                 process.someclusters + 
                                 process.seqMultProd +
                                 process.eventtimedistrnovertexskim +
                                 process.trackcountnovertexskim +
                                 process.seqClusMultInvestNoVertexSkim)

process.pnovertexwithtwojets = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                        process.seqEventHistoryReco +
                                        ~process.novertex +
                                        ~process.logErrorAnalysisTooManyClusters +
                                        process.jetfilter +
                                        process.seqMultProd +
                                        process.eventtimedistrnovertexwithtwojets +
                                        process.trackcountnovertexwithtwojets +
                                        process.seqClusMultInvestNoVertexWithTwoJets)

process.pnovertexwithcentraljet = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                           process.seqEventHistoryReco +
                                           ~process.novertex +
                                           ~process.logErrorAnalysisTooManyClusters +
                                           process.jetfilter +
                                           process.centraljetfilter +
                                           process.seqMultProd +
                                           process.eventtimedistrnovertexwithcentraljet +
                                           process.trackcountnovertexwithcentraljet +
                                           process.seqClusMultInvestNoVertexWithCentralJet)
                                           
process.pnostrip = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                            process.seqEventHistoryReco +
                            process.nostripclusters +
                            process.seqMultProd +
                            process.eventtimedistrnostrip +
                            process.trackcountnostrip +
                            process.seqClusMultInvestNoStrip)

process.poffdiagonal = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                process.seqEventHistoryReco +
                                process.offdiagonal +
                                process.seqMultProd +
                                process.eventtimedistroffdiag +
                                process.trackcountoffdiag +
                                process.seqClusMultInvestOffDiag)

process.pmanystripclus = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                  process.seqEventHistoryReco +
                                  process.seqManyStripClusters +
                                  process.seqMultProd +
                                  process.eventtimedistrmanystripclus +
                                  process.trackcountmanystripclus +
                                  process.seqClusMultInvestManyStripClus)

process.ptoomanystripclus = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                     process.seqEventHistoryReco +
                                     process.seqTooManyStripClusters +
                                     process.seqMultProd +
                                     process.eventtimedistrtoomanystripclus +
                                     process.trackcounttoomanystripclus +
                                     process.seqClusMultInvestTooManyStripClus)

process.pmanyclus = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                             process.seqEventHistoryReco +
                             process.seqManyClusters +
                             process.seqMultProd +
                             process.eventtimedistrmanyclus +
                             process.trackcountmanyclus +
                             process.seqClusMultInvestManyClus)

process.ptoomanyerrors = cms.Path(process.dcsstatus + process.seqHLTSelection + process.seqBitSelection +
                                  process.seqEventHistoryReco +
                                  process.seqTooManyErrors +
                                  process.seqMultProd +
                                  process.eventtimedistrtoomanyerrors)


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('OddEventSkim.root')
                                   )

process.outoddevent = cms.OutputModule("PoolOutputModule",
                                       fileName = cms.untracked.string("oddevents.root"),
                                       outputCommands = cms.untracked.vstring("keep *"),
                                       SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("poffdiagonal",
                                                                                                    "pnostrip",
                                                                                                    "ptoomanystripclus","pmanystripclus", #"pmanyclus",
                                                                                                    "pnotrackskim","pnovertexskim",
                                                                                                    "pnotrackwithtwojets","pnovertexwithtwojets",
                                                                                                    "pnotrackwithcentraljet","pnovertexwithcentraljet"))
	)

#process.outpxllessevent = cms.OutputModule("PoolOutputModule",
#                                           fileName = cms.untracked.string("pxllessevents.root"),
#                                           outputCommands = cms.untracked.vstring("keep *"),
#                                           SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("pniter4hp","pniter5hp"))
#	)

process.e = cms.EndPath(process.outoddevent)
#process.schedule = cms.Schedule(process.ptoomanystripclus,process.pmanyclus,process.e)

#-----------------------------------


