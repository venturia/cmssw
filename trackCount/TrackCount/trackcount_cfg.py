import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.categories.append("TrackLoop")
process.MessageLogger.categories.append("HitLoop")
process.MessageLogger.categories.append("Multiplicity")
process.MessageLogger.infos.placeholder = cms.untracked.bool(False)
process.MessageLogger.infos.threshold = cms.untracked.string("INFO")
process.MessageLogger.infos.default = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
    )
process.MessageLogger.infos.TrackLoop = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
    )
process.MessageLogger.infos.HitLoop = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
    )
process.MessageLogger.infos.Multiplicity = cms.untracked.PSet(
    limit = cms.untracked.int32(1000000)
    )
process.MessageLogger.infos.FwkJob = cms.untracked.PSet(
    limit = cms.untracked.int32(1000000)
    )
process.MessageLogger.cerr.threshold = cms.untracked.string("WARNING")
process.MessageLogger.cerr.Multiplicity = cms.untracked.PSet(
    limit = cms.untracked.int32(0)
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring(
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/1629B803-C56F-DD11-9EF0-001617C3B6C6.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/26B5662F-C76F-DD11-A635-000423D6C8E6.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/3C7BC9FC-C96F-DD11-A716-000423D6BA18.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/4CE80B78-C66F-DD11-A86D-000423D6B444.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/525F6200-C56F-DD11-B11B-001617E30F58.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/58968223-C76F-DD11-83E4-001617C3B76E.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/5EFCB3DC-C56F-DD11-8F8C-000423D98804.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/628A5378-C66F-DD11-AA9C-000423D6CA72.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/88A14B08-C56F-DD11-A01B-000423D6B48C.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/B69BE5DB-C56F-DD11-B01C-000423D9863C.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/C6C32CC1-C56F-DD11-BA17-000423D9870C.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/E2060EBD-C56F-DD11-927D-000423D94700.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/EA6C677C-C66F-DD11-BFBD-000423D6CA6E.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/F06CA1BA-C56F-DD11-9D7E-000423D6B358.root',
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/058/289/F425072D-C76F-DD11-9BC2-000423D9939C.root'
   
    )
                            )

process.demo = cms.EDAnalyzer('TrackCount',
                              trackCollection = cms.InputTag('ctfWithMaterialTracksP5'),
                              orbitNbin = cms.untracked.int32(900)
                              )

process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('prova.root')
                                   )

process.p = cms.Path(process.demo)
