import FWCore.ParameterSet.Config as cms

from FWCore.MessageService.MessageLogger_cfi import MessageLogger

#----------------------------------------------------------------

MessageLogger.cout.placeholder = cms.untracked.bool(False)
MessageLogger.cout.threshold = cms.untracked.string("WARNING")
MessageLogger.cout.default = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
    )
MessageLogger.cout.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(10000)
    )

#MessageLogger.cerr.placeholder = cms.untracked.bool(False)
#MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
#MessageLogger.cerr.default = cms.untracked.PSet(
#    limit = cms.untracked.int32(10000000)
#    )
#MessageLogger.cerr.FwkReport = cms.untracked.PSet(
#    reportEvery = cms.untracked.int32(100000)
#    )

#----Remove too verbose PrimaryVertexProducer

MessageLogger.suppressInfo.append("pixelVerticesAdaptive")
MessageLogger.suppressInfo.append("pixelVerticesAdaptiveNoBS")

#------------------------------------------------------------------


