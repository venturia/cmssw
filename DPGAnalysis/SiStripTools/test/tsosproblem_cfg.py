import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("TSOSProblem")

#prepare options

options = VarParsing.VarParsing("analysis")

options.register('globalTag',
                 "DONOTEXIST",
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.string,          # string, int, or float
                 "GlobalTag")
#options.globalTag = "DONOTEXIST::All"

options.parseArguments()

#
process.load("DPGAnalysis.SiStripTools.processOptions_cff")
process.load("DPGAnalysis.SiStripTools.MessageLogger_cff")

#process.MessageLogger.cout.threshold = cms.untracked.string("DEBUG")
#process.MessageLogger.debugModules = cms.untracked.vstring("overlapproblemanalyzer")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            #                    skipBadFiles = cms.untracked.bool(True),
                            inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")
                            )

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")


process.load("DPGAnalysis.SiStripTools.tkAlTrackRefitSequence_cff")
process.refittedTracks.src = cms.InputTag("generalTracks")

process.load("DPGAnalysis.SiStripTools.overlapproblemtsosanalyzer_cfi")

process.overlapproblemtsosanalyzer.tsosHMConf.wanted2DHistos=cms.untracked.bool(True)
process.overlapproblemtsosanalyzer.tsosHMConf.wantedSubDets = cms.VPSet(
    cms.PSet(detSelection=cms.uint32(1100),detLabel=cms.string("TIBL1"),selection=cms.untracked.vstring("0x1e01c000-0x16004000")),     # TIB L1
    cms.PSet(detSelection=cms.uint32(1200),detLabel=cms.string("TIBL2"),selection=cms.untracked.vstring("0x1e01c000-0x16008000")),     # TIB L2 
    cms.PSet(detSelection=cms.uint32(1300),detLabel=cms.string("TIBL3"),selection=cms.untracked.vstring("0x1e01c000-0x1600c000")),     # TIB L3
    cms.PSet(detSelection=cms.uint32(1400),detLabel=cms.string("TIBL4"),selection=cms.untracked.vstring("0x1e01c000-0x16010000")),     # TIB L4
    cms.PSet(detSelection=cms.uint32(3100),detLabel=cms.string("TOBL1"),selection=cms.untracked.vstring("0x1e01c000-0x1a004000")),     # TOB L1
    cms.PSet(detSelection=cms.uint32(3200),detLabel=cms.string("TOBL2"),selection=cms.untracked.vstring("0x1e01c000-0x1a008000")),     # TOB L2
    cms.PSet(detSelection=cms.uint32(3300),detLabel=cms.string("TOBL3"),selection=cms.untracked.vstring("0x1e01c000-0x1a00c000")),     # TOB L3
    cms.PSet(detSelection=cms.uint32(3400),detLabel=cms.string("TOBL4"),selection=cms.untracked.vstring("0x1e01c000-0x1a010000")),     # TOB L4
    cms.PSet(detSelection=cms.uint32(3500),detLabel=cms.string("TOBL5"),selection=cms.untracked.vstring("0x1e01c000-0x1a014000")),     # TOB L5
    cms.PSet(detSelection=cms.uint32(3600),detLabel=cms.string("TOBL6"),selection=cms.untracked.vstring("0x1e01c000-0x1a018000")),     # TOB L6

     cms.PSet(detSelection=cms.uint32(2110),detLabel=cms.string("TIDmD1R1"),selection=cms.untracked.vstring("0x1e007e00-0x18002a00")),     # TID- D1 R1 
     cms.PSet(detSelection=cms.uint32(2120),detLabel=cms.string("TIDmD2R1"),selection=cms.untracked.vstring("0x1e007e00-0x18003200")),     # TID- D2 R1 
     cms.PSet(detSelection=cms.uint32(2130),detLabel=cms.string("TIDmD3R1"),selection=cms.untracked.vstring("0x1e007e00-0x18003a00")),     # TID- D3 R1 
     cms.PSet(detSelection=cms.uint32(2140),detLabel=cms.string("TIDpD1R1"),selection=cms.untracked.vstring("0x1e007e00-0x18004a00")),     # TID+ D1 R1 
     cms.PSet(detSelection=cms.uint32(2150),detLabel=cms.string("TIDpD2R1"),selection=cms.untracked.vstring("0x1e007e00-0x18005200")),     # TID+ D2 R1 
     cms.PSet(detSelection=cms.uint32(2160),detLabel=cms.string("TIDpD3R1"),selection=cms.untracked.vstring("0x1e007e00-0x18005a00")),     # TID+ D3 R1 

     cms.PSet(detSelection=cms.uint32(2210),detLabel=cms.string("TIDmD1R2"),selection=cms.untracked.vstring("0x1e007e00-0x18002c00")),     # TID- D1 R2 
     cms.PSet(detSelection=cms.uint32(2220),detLabel=cms.string("TIDmD2R2"),selection=cms.untracked.vstring("0x1e007e00-0x18003400")),     # TID- D2 R2 
     cms.PSet(detSelection=cms.uint32(2230),detLabel=cms.string("TIDmD3R2"),selection=cms.untracked.vstring("0x1e007e00-0x18003c00")),     # TID- D3 R2 
     cms.PSet(detSelection=cms.uint32(2240),detLabel=cms.string("TIDpD1R2"),selection=cms.untracked.vstring("0x1e007e00-0x18004c00")),     # TID+ D1 R2 
     cms.PSet(detSelection=cms.uint32(2250),detLabel=cms.string("TIDpD2R2"),selection=cms.untracked.vstring("0x1e007e00-0x18005400")),     # TID+ D2 R2 
     cms.PSet(detSelection=cms.uint32(2260),detLabel=cms.string("TIDpD3R2"),selection=cms.untracked.vstring("0x1e007e00-0x18005c00")),     # TID+ D3 R2 

     cms.PSet(detSelection=cms.uint32(2310),detLabel=cms.string("TIDmD1R3"),selection=cms.untracked.vstring("0x1e007e00-0x18002e00")),     # TID- D1 R3 
     cms.PSet(detSelection=cms.uint32(2320),detLabel=cms.string("TIDmD2R3"),selection=cms.untracked.vstring("0x1e007e00-0x18003600")),     # TID- D2 R3 
     cms.PSet(detSelection=cms.uint32(2330),detLabel=cms.string("TIDmD3R3"),selection=cms.untracked.vstring("0x1e007e00-0x18003e00")),     # TID- D3 R3 
     cms.PSet(detSelection=cms.uint32(2340),detLabel=cms.string("TIDpD1R3"),selection=cms.untracked.vstring("0x1e007e00-0x18004e00")),     # TID+ D1 R3 
     cms.PSet(detSelection=cms.uint32(2350),detLabel=cms.string("TIDpD2R3"),selection=cms.untracked.vstring("0x1e007e00-0x18005600")),     # TID+ D2 R3 
     cms.PSet(detSelection=cms.uint32(2360),detLabel=cms.string("TIDpD3R3"),selection=cms.untracked.vstring("0x1e007e00-0x18005e00")),     # TID+ D3 R3 

    cms.PSet(detSelection=cms.uint32(4110),detLabel=cms.string("TECmD1R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044020")),    # TEC- D1 R1 
    cms.PSet(detSelection=cms.uint32(4120),detLabel=cms.string("TECmD2R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048020")),    # TEC- D2 R1 
    cms.PSet(detSelection=cms.uint32(4130),detLabel=cms.string("TECmD3R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c020")),    # TEC- D3 R1 

    cms.PSet(detSelection=cms.uint32(4210),detLabel=cms.string("TECmD1R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044040")),    # TEC- D1 R2 
    cms.PSet(detSelection=cms.uint32(4220),detLabel=cms.string("TECmD2R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048040")),    # TEC- D2 R2 
    cms.PSet(detSelection=cms.uint32(4230),detLabel=cms.string("TECmD3R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c040")),    # TEC- D3 R2 
    cms.PSet(detSelection=cms.uint32(4240),detLabel=cms.string("TECmD4R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050040")),    # TEC- D4 R2 
    cms.PSet(detSelection=cms.uint32(4250),detLabel=cms.string("TECmD5R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054040")),    # TEC- D5 R2 
    cms.PSet(detSelection=cms.uint32(4260),detLabel=cms.string("TECmD6R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058040")),    # TEC- D6 R2 

    cms.PSet(detSelection=cms.uint32(4310),detLabel=cms.string("TECmD1R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044060")),    # TEC- D1 R3 
    cms.PSet(detSelection=cms.uint32(4320),detLabel=cms.string("TECmD2R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048060")),    # TEC- D2 R3 
    cms.PSet(detSelection=cms.uint32(4330),detLabel=cms.string("TECmD3R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c060")),    # TEC- D3 R3 
    cms.PSet(detSelection=cms.uint32(4340),detLabel=cms.string("TECmD4R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050060")),    # TEC- D4 R3 
    cms.PSet(detSelection=cms.uint32(4350),detLabel=cms.string("TECmD5R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054060")),    # TEC- D5 R3 
    cms.PSet(detSelection=cms.uint32(4360),detLabel=cms.string("TECmD6R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058060")),    # TEC- D6 R3 
    cms.PSet(detSelection=cms.uint32(4370),detLabel=cms.string("TECmD7R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c060")),    # TEC- D7 R3 
    cms.PSet(detSelection=cms.uint32(4380),detLabel=cms.string("TECmD8R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060060")),    # TEC- D8 R3 

    cms.PSet(detSelection=cms.uint32(4410),detLabel=cms.string("TECmD1R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044080")),    # TEC- D1 R4 
    cms.PSet(detSelection=cms.uint32(4420),detLabel=cms.string("TECmD2R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048080")),    # TEC- D2 R4 
    cms.PSet(detSelection=cms.uint32(4430),detLabel=cms.string("TECmD3R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c080")),    # TEC- D3 R4 
    cms.PSet(detSelection=cms.uint32(4440),detLabel=cms.string("TECmD4R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050080")),    # TEC- D4 R4 
    cms.PSet(detSelection=cms.uint32(4450),detLabel=cms.string("TECmD5R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054080")),    # TEC- D5 R4 
    cms.PSet(detSelection=cms.uint32(4460),detLabel=cms.string("TECmD6R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058080")),    # TEC- D6 R4 
    cms.PSet(detSelection=cms.uint32(4470),detLabel=cms.string("TECmD7R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c080")),    # TEC- D7 R4 
    cms.PSet(detSelection=cms.uint32(4480),detLabel=cms.string("TECmD8R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060080")),    # TEC- D8 R4 
    cms.PSet(detSelection=cms.uint32(4490),detLabel=cms.string("TECmD9R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c064080")),    # TEC- D9 R4 
    
    cms.PSet(detSelection=cms.uint32(4510),detLabel=cms.string("TECmD1R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440a0")),    # TEC- D1 R5 
    cms.PSet(detSelection=cms.uint32(4520),detLabel=cms.string("TECmD2R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480a0")),    # TEC- D2 R5 
    cms.PSet(detSelection=cms.uint32(4530),detLabel=cms.string("TECmD3R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0a0")),    # TEC- D3 R5 
    cms.PSet(detSelection=cms.uint32(4540),detLabel=cms.string("TECmD4R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500a0")),    # TEC- D4 R5 
    cms.PSet(detSelection=cms.uint32(4550),detLabel=cms.string("TECmD5R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540a0")),    # TEC- D5 R5 
    cms.PSet(detSelection=cms.uint32(4560),detLabel=cms.string("TECmD6R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580a0")),    # TEC- D6 R5 
    cms.PSet(detSelection=cms.uint32(4570),detLabel=cms.string("TECmD7R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0a0")),    # TEC- D7 R5 
    cms.PSet(detSelection=cms.uint32(4580),detLabel=cms.string("TECmD8R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600a0")),    # TEC- D8 R5 
    cms.PSet(detSelection=cms.uint32(4590),detLabel=cms.string("TECmD9R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640a0")),    # TEC- D9 R5 

    cms.PSet(detSelection=cms.uint32(4610),detLabel=cms.string("TECmD1R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440c0")),    # TEC- D1 R6 
    cms.PSet(detSelection=cms.uint32(4620),detLabel=cms.string("TECmD2R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480c0")),    # TEC- D2 R6 
    cms.PSet(detSelection=cms.uint32(4630),detLabel=cms.string("TECmD3R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0c0")),    # TEC- D3 R6 
    cms.PSet(detSelection=cms.uint32(4640),detLabel=cms.string("TECmD4R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500c0")),    # TEC- D4 R6 
    cms.PSet(detSelection=cms.uint32(4650),detLabel=cms.string("TECmD5R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540c0")),    # TEC- D5 R6 
    cms.PSet(detSelection=cms.uint32(4660),detLabel=cms.string("TECmD6R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580c0")),    # TEC- D6 R6 
    cms.PSet(detSelection=cms.uint32(4670),detLabel=cms.string("TECmD7R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0c0")),    # TEC- D7 R6 
    cms.PSet(detSelection=cms.uint32(4680),detLabel=cms.string("TECmD8R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600c0")),    # TEC- D8 R6 
    cms.PSet(detSelection=cms.uint32(4690),detLabel=cms.string("TECmD9R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640c0")),    # TEC- D9 R6 

    cms.PSet(detSelection=cms.uint32(4710),detLabel=cms.string("TECmD1R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440e0")),    # TEC- D1 R7 
    cms.PSet(detSelection=cms.uint32(4720),detLabel=cms.string("TECmD2R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480e0")),    # TEC- D2 R7 
    cms.PSet(detSelection=cms.uint32(4730),detLabel=cms.string("TECmD3R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0e0")),    # TEC- D3 R7 
    cms.PSet(detSelection=cms.uint32(4740),detLabel=cms.string("TECmD4R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500e0")),    # TEC- D4 R7 
    cms.PSet(detSelection=cms.uint32(4750),detLabel=cms.string("TECmD5R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540e0")),    # TEC- D5 R7 
    cms.PSet(detSelection=cms.uint32(4760),detLabel=cms.string("TECmD6R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580e0")),    # TEC- D6 R7 
    cms.PSet(detSelection=cms.uint32(4770),detLabel=cms.string("TECmD7R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0e0")),    # TEC- D7 R7 
    cms.PSet(detSelection=cms.uint32(4780),detLabel=cms.string("TECmD8R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600e0")),    # TEC- D8 R7 
    cms.PSet(detSelection=cms.uint32(4790),detLabel=cms.string("TECmD9R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640e0")),    # TEC- D9 R7 

    cms.PSet(detSelection=cms.uint32(5110),detLabel=cms.string("TECpD1R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084020")),    # TEC+ D1 R1 
    cms.PSet(detSelection=cms.uint32(5120),detLabel=cms.string("TECpD2R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088020")),    # TEC+ D2 R1 
    cms.PSet(detSelection=cms.uint32(5130),detLabel=cms.string("TECpD3R1"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c020")),    # TEC+ D3 R1 

    cms.PSet(detSelection=cms.uint32(5210),detLabel=cms.string("TECpD1R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084040")),    # TEC+ D1 R2 
    cms.PSet(detSelection=cms.uint32(5220),detLabel=cms.string("TECpD2R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088040")),    # TEC+ D2 R2 
    cms.PSet(detSelection=cms.uint32(5230),detLabel=cms.string("TECpD3R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c040")),    # TEC+ D3 R2 
    cms.PSet(detSelection=cms.uint32(5240),detLabel=cms.string("TECpD4R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090040")),    # TEC+ D4 R2 
    cms.PSet(detSelection=cms.uint32(5250),detLabel=cms.string("TECpD5R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094040")),    # TEC+ D5 R2 
    cms.PSet(detSelection=cms.uint32(5260),detLabel=cms.string("TECpD6R2"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098040")),    # TEC+ D6 R2 

    cms.PSet(detSelection=cms.uint32(5310),detLabel=cms.string("TECpD1R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084060")),    # TEC+ D1 R3 
    cms.PSet(detSelection=cms.uint32(5320),detLabel=cms.string("TECpD2R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088060")),    # TEC+ D2 R3 
    cms.PSet(detSelection=cms.uint32(5330),detLabel=cms.string("TECpD3R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c060")),    # TEC+ D3 R3 
    cms.PSet(detSelection=cms.uint32(5340),detLabel=cms.string("TECpD4R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090060")),    # TEC+ D4 R3 
    cms.PSet(detSelection=cms.uint32(5350),detLabel=cms.string("TECpD5R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094060")),    # TEC+ D5 R3 
    cms.PSet(detSelection=cms.uint32(5360),detLabel=cms.string("TECpD6R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098060")),    # TEC+ D6 R3 
    cms.PSet(detSelection=cms.uint32(5370),detLabel=cms.string("TECpD7R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c060")),    # TEC+ D7 R3 
    cms.PSet(detSelection=cms.uint32(5380),detLabel=cms.string("TECpD8R3"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0060")),    # TEC+ D8 R3 

    cms.PSet(detSelection=cms.uint32(5410),detLabel=cms.string("TECpD1R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084080")),    # TEC+ D1 R4 
    cms.PSet(detSelection=cms.uint32(5420),detLabel=cms.string("TECpD2R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088080")),    # TEC+ D2 R4 
    cms.PSet(detSelection=cms.uint32(5430),detLabel=cms.string("TECpD3R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c080")),    # TEC+ D3 R4 
    cms.PSet(detSelection=cms.uint32(5440),detLabel=cms.string("TECpD4R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090080")),    # TEC+ D4 R4 
    cms.PSet(detSelection=cms.uint32(5450),detLabel=cms.string("TECpD5R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094080")),    # TEC+ D5 R4 
    cms.PSet(detSelection=cms.uint32(5460),detLabel=cms.string("TECpD6R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098080")),    # TEC+ D6 R4 
    cms.PSet(detSelection=cms.uint32(5470),detLabel=cms.string("TECpD7R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c080")),    # TEC+ D7 R4 
    cms.PSet(detSelection=cms.uint32(5480),detLabel=cms.string("TECpD8R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0080")),    # TEC+ D8 R4 
    cms.PSet(detSelection=cms.uint32(5490),detLabel=cms.string("TECpD9R4"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a4080")),    # TEC+ D9 R4 

    cms.PSet(detSelection=cms.uint32(5510),detLabel=cms.string("TECpD1R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840a0")),    # TEC+ D1 R5 
    cms.PSet(detSelection=cms.uint32(5520),detLabel=cms.string("TECpD2R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880a0")),    # TEC+ D2 R5 
    cms.PSet(detSelection=cms.uint32(5530),detLabel=cms.string("TECpD3R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0a0")),    # TEC+ D3 R5 
    cms.PSet(detSelection=cms.uint32(5540),detLabel=cms.string("TECpD4R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900a0")),    # TEC+ D4 R5 
    cms.PSet(detSelection=cms.uint32(5550),detLabel=cms.string("TECpD5R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940a0")),    # TEC+ D5 R5 
    cms.PSet(detSelection=cms.uint32(5560),detLabel=cms.string("TECpD6R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980a0")),    # TEC+ D6 R5 
    cms.PSet(detSelection=cms.uint32(5570),detLabel=cms.string("TECpD7R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0a0")),    # TEC+ D7 R5 
    cms.PSet(detSelection=cms.uint32(5580),detLabel=cms.string("TECpD8R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00a0")),    # TEC+ D8 R5 
    cms.PSet(detSelection=cms.uint32(5590),detLabel=cms.string("TECpD9R5"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40a0")),    # TEC+ D9 R5 

    cms.PSet(detSelection=cms.uint32(5610),detLabel=cms.string("TECpD1R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840c0")),    # TEC+ D1 R6 
    cms.PSet(detSelection=cms.uint32(5620),detLabel=cms.string("TECpD2R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880c0")),    # TEC+ D2 R6 
    cms.PSet(detSelection=cms.uint32(5630),detLabel=cms.string("TECpD3R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0c0")),    # TEC+ D3 R6 
    cms.PSet(detSelection=cms.uint32(5640),detLabel=cms.string("TECpD4R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900c0")),    # TEC+ D4 R6 
    cms.PSet(detSelection=cms.uint32(5650),detLabel=cms.string("TECpD5R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940c0")),    # TEC+ D5 R6 
    cms.PSet(detSelection=cms.uint32(5660),detLabel=cms.string("TECpD6R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980c0")),    # TEC+ D6 R6 
    cms.PSet(detSelection=cms.uint32(5670),detLabel=cms.string("TECpD7R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0c0")),    # TEC+ D7 R6 
    cms.PSet(detSelection=cms.uint32(5680),detLabel=cms.string("TECpD8R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00c0")),    # TEC+ D8 R6 
    cms.PSet(detSelection=cms.uint32(5690),detLabel=cms.string("TECpD9R6"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40c0")),    # TEC+ D9 R6 

    cms.PSet(detSelection=cms.uint32(5710),detLabel=cms.string("TECpD1R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840e0")),    # TEC+ D1 R7 
    cms.PSet(detSelection=cms.uint32(5720),detLabel=cms.string("TECpD2R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880e0")),    # TEC+ D2 R7 
    cms.PSet(detSelection=cms.uint32(5730),detLabel=cms.string("TECpD3R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0e0")),    # TEC+ D3 R7 
    cms.PSet(detSelection=cms.uint32(5740),detLabel=cms.string("TECpD4R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900e0")),    # TEC+ D4 R7 
    cms.PSet(detSelection=cms.uint32(5750),detLabel=cms.string("TECpD5R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940e0")),    # TEC+ D5 R7 
    cms.PSet(detSelection=cms.uint32(5760),detLabel=cms.string("TECpD6R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980e0")),    # TEC+ D6 R7 
    cms.PSet(detSelection=cms.uint32(5770),detLabel=cms.string("TECpD7R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0e0")),    # TEC+ D7 R7 
    cms.PSet(detSelection=cms.uint32(5780),detLabel=cms.string("TECpD8R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00e0")),    # TEC+ D8 R7 
    cms.PSet(detSelection=cms.uint32(5790),detLabel=cms.string("TECpD9R7"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40e0"))    # TEC+ D9 R7 
)

process.p0 = cms.Path( process.seqTrackRefitting
                      + process.overlapproblemtsosanalyzer 
                      )

#----GlobalTag ------------------------

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options.globalTag, '')


process.TFileService = cms.Service('TFileService',
                                   fileName = cms.string('TSOSProblem.root')
                                   )

