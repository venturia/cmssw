#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms

process = cms.Process("Geometry")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("SimTracker.TrackerMaterialAnalysis.double10GeVMuons_cfi")

# gaussian Vertex Smearing
process.load("IOMC.EventVertexGenerators.VtxSmearedGauss_cfi")

# detector simulation (Geant4-based) with tracking material accounting 
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_40T_cff")
process.load("SimTracker.TrackerMaterialAnalysis.trackingMaterialProducer_cff")
process.trackingMaterialProducer.UseMagneticField = True

# message logger
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkJob = cms.untracked.PSet(    # but FwkJob category - those unlimitted

            limit = cms.untracked.int32(-1)
        )
    ),
    categories = cms.untracked.vstring('FwkJob'),
    destinations = cms.untracked.vstring('cout')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        'drop *',                                                       # drop all objects
        'keep MaterialAccountingTracks_trackingMaterialProducer_*_*'),  # but the material accounting informations
    fileName = cms.untracked.string('file:material.root')
)

process.path = cms.Path(process.generator + process.VtxSmeared + process.trackingMaterialProducer)
process.outpath = cms.EndPath(process.out)
