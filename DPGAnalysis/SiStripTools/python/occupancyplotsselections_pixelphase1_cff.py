import FWCore.ParameterSet.Config as cms

#OccupancyPlotsPixelWantedSubDets = cms.VPSet (
#    cms.PSet(detSelection = cms.uint32(111),detLabel = cms.string("FPIXmD1pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x14810100")),
#    cms.PSet(detSelection = cms.uint32(121),detLabel = cms.string("FPIXmD2pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x14820100")),
#    cms.PSet(detSelection = cms.uint32(131),detLabel = cms.string("FPIXmD3pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x14830100")),
#    cms.PSet(detSelection = cms.uint32(211),detLabel = cms.string("FPIXpD1pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x15010100")),
#    cms.PSet(detSelection = cms.uint32(221),detLabel = cms.string("FPIXpD2pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x15020100")),
#    cms.PSet(detSelection = cms.uint32(231),detLabel = cms.string("FPIXpD3pan1"),selection=cms.untracked.vstring("0x1f8f0300-0x15030100")),
#    cms.PSet(detSelection = cms.uint32(112),detLabel = cms.string("FPIXmD1pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x14810200")),
#    cms.PSet(detSelection = cms.uint32(122),detLabel = cms.string("FPIXmD2pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x14820200")),
#    cms.PSet(detSelection = cms.uint32(132),detLabel = cms.string("FPIXmD3pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x14830200")),
#    cms.PSet(detSelection = cms.uint32(212),detLabel = cms.string("FPIXpD1pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x15010200")),
#    cms.PSet(detSelection = cms.uint32(222),detLabel = cms.string("FPIXpD2pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x15020200")),
#    cms.PSet(detSelection = cms.uint32(232),detLabel = cms.string("FPIXpD3pan2"),selection=cms.untracked.vstring("0x1f8f0300-0x15030200"))
#    )

OccupancyPlotsPixelWantedSubDets = cms.VPSet (
    cms.PSet(detSelection=cms.uint32(111),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100004")),      # BPix L1 mod 1
    cms.PSet(detSelection=cms.uint32(112),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100008")),      # BPix L1 mod 2
    cms.PSet(detSelection=cms.uint32(113),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1210000c")),      # BPix L1 mod 3
    cms.PSet(detSelection=cms.uint32(114),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100010")),      # BPix L1 mod 4
    cms.PSet(detSelection=cms.uint32(115),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100014")),      # BPix L1 mod 5
    cms.PSet(detSelection=cms.uint32(116),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100018")),      # BPix L1 mod 6
    cms.PSet(detSelection=cms.uint32(117),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1210001c")),      # BPix L1 mod 7
    cms.PSet(detSelection=cms.uint32(118),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12100020")),      # BPix L1 mod 8

    cms.PSet(detSelection=cms.uint32(121),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200004")),      # BPix L2 mod 1
    cms.PSet(detSelection=cms.uint32(122),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200008")),      # BPix L2 mod 2
    cms.PSet(detSelection=cms.uint32(123),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1220000c")),      # BPix L2 mod 3
    cms.PSet(detSelection=cms.uint32(124),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200010")),      # BPix L2 mod 4
    cms.PSet(detSelection=cms.uint32(125),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200014")),      # BPix L2 mod 5
    cms.PSet(detSelection=cms.uint32(126),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200018")),      # BPix L2 mod 6
    cms.PSet(detSelection=cms.uint32(127),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1220001c")),      # BPix L2 mod 7
    cms.PSet(detSelection=cms.uint32(128),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12200020")),      # BPix L2 mod 8

    cms.PSet(detSelection=cms.uint32(131),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300004")),      # BPix L3 mod 1
    cms.PSet(detSelection=cms.uint32(132),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300008")),      # BPix L3 mod 2
    cms.PSet(detSelection=cms.uint32(133),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1230000c")),      # BPix L3 mod 3
    cms.PSet(detSelection=cms.uint32(134),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300010")),      # BPix L3 mod 4
    cms.PSet(detSelection=cms.uint32(135),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300014")),      # BPix L3 mod 5
    cms.PSet(detSelection=cms.uint32(136),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300018")),      # BPix L3 mod 6
    cms.PSet(detSelection=cms.uint32(137),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1230001c")),      # BPix L3 mod 7
    cms.PSet(detSelection=cms.uint32(138),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12300020")),      # BPix L3 mod 8

    cms.PSet(detSelection=cms.uint32(141),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400004")),      # BPix L4 mod 1
    cms.PSet(detSelection=cms.uint32(142),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400008")),      # BPix L4 mod 2
    cms.PSet(detSelection=cms.uint32(143),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1240000c")),      # BPix L4 mod 3
    cms.PSet(detSelection=cms.uint32(144),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400010")),      # BPix L4 mod 4
    cms.PSet(detSelection=cms.uint32(145),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400014")),      # BPix L4 mod 5
    cms.PSet(detSelection=cms.uint32(146),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400018")),      # BPix L4 mod 6
    cms.PSet(detSelection=cms.uint32(147),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x1240001c")),      # BPix L4 mod 7
    cms.PSet(detSelection=cms.uint32(148),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef00ffc-0x12400020")),      # BPix L4 mod 8


    cms.PSet(detSelection = cms.uint32(211),detLabel = cms.string("FPIXmD1R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x14841400",
                                                                                                                   "0x1fbffc00-0x14842400",
                                                                                                                   "0x1fbffc00-0x14843400",
                                                                                                                   "0x1fbffc00-0x14844400",
                                                                                                                   "0x1fbffc00-0x14845400",
                                                                                                                   "0x1fbffc00-0x14846400",
                                                                                                                   "0x1fbffc00-0x14847400",
                                                                                                                   "0x1fbffc00-0x14848400",
                                                                                                                   "0x1fbffc00-0x14849400",
                                                                                                                   "0x1fbffc00-0x1484a400",
                                                                                                                   "0x1fbffc00-0x1484b400",
                                                                                                                   "0x1fbffc00-0x1484c400",
                                                                                                                   "0x1fbffc00-0x1484d400",
                                                                                                                   "0x1fbffc00-0x1484e400",
                                                                                                                   "0x1fbffc00-0x1484f400",
                                                                                                                   "0x1fbffc00-0x14850400",
                                                                                                                   "0x1fbffc00-0x14851400",
                                                                                                                   "0x1fbffc00-0x14852400",
                                                                                                                   "0x1fbffc00-0x14853400",
                                                                                                                   "0x1fbffc00-0x14854400",
                                                                                                                   "0x1fbffc00-0x14855400",
                                                                                                                   "0x1fbffc00-0x14856400")),
    cms.PSet(detSelection = cms.uint32(221),detLabel = cms.string("FPIXmD2R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x14881400",
                                                                                                                   "0x1fbffc00-0x14882400",
                                                                                                                   "0x1fbffc00-0x14883400",
                                                                                                                   "0x1fbffc00-0x14884400",
                                                                                                                   "0x1fbffc00-0x14885400",
                                                                                                                   "0x1fbffc00-0x14886400",
                                                                                                                   "0x1fbffc00-0x14887400",
                                                                                                                   "0x1fbffc00-0x14888400",
                                                                                                                   "0x1fbffc00-0x14889400",
                                                                                                                   "0x1fbffc00-0x1488a400",
                                                                                                                   "0x1fbffc00-0x1488b400",
                                                                                                                   "0x1fbffc00-0x1488c400",
                                                                                                                   "0x1fbffc00-0x1488d400",
                                                                                                                   "0x1fbffc00-0x1488e400",
                                                                                                                   "0x1fbffc00-0x1488f400",
                                                                                                                   "0x1fbffc00-0x14890400",
                                                                                                                   "0x1fbffc00-0x14891400",
                                                                                                                   "0x1fbffc00-0x14892400",
                                                                                                                   "0x1fbffc00-0x14893400",
                                                                                                                   "0x1fbffc00-0x14894400",
                                                                                                                   "0x1fbffc00-0x14895400",
                                                                                                                   "0x1fbffc00-0x14896400")),
    cms.PSet(detSelection = cms.uint32(231),detLabel = cms.string("FPIXmD3R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c1400",
                                                                                                                   "0x1fbffc00-0x148c2400",
                                                                                                                   "0x1fbffc00-0x148c3400",
                                                                                                                   "0x1fbffc00-0x148c4400",
                                                                                                                   "0x1fbffc00-0x148c5400",
                                                                                                                   "0x1fbffc00-0x148c6400",
                                                                                                                   "0x1fbffc00-0x148c7400",
                                                                                                                   "0x1fbffc00-0x148c8400",
                                                                                                                   "0x1fbffc00-0x148c9400",
                                                                                                                   "0x1fbffc00-0x148ca400",
                                                                                                                   "0x1fbffc00-0x148cb400",
                                                                                                                   "0x1fbffc00-0x148cc400",
                                                                                                                   "0x1fbffc00-0x148cd400",
                                                                                                                   "0x1fbffc00-0x148ce400",
                                                                                                                   "0x1fbffc00-0x148cf400",
                                                                                                                   "0x1fbffc00-0x148d0400",
                                                                                                                   "0x1fbffc00-0x148d1400",
                                                                                                                   "0x1fbffc00-0x148d2400",
                                                                                                                   "0x1fbffc00-0x148d3400",
                                                                                                                   "0x1fbffc00-0x148d4400",
                                                                                                                   "0x1fbffc00-0x148d5400",
                                                                                                                   "0x1fbffc00-0x148d6400")),
    cms.PSet(detSelection = cms.uint32(241),detLabel = cms.string("FPIXpD1R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x15041400",
                                                                                                                   "0x1fbffc00-0x15042400",
                                                                                                                   "0x1fbffc00-0x15043400",
                                                                                                                   "0x1fbffc00-0x15044400",
                                                                                                                   "0x1fbffc00-0x15045400",
                                                                                                                   "0x1fbffc00-0x15046400",
                                                                                                                   "0x1fbffc00-0x15047400",
                                                                                                                   "0x1fbffc00-0x15048400",
                                                                                                                   "0x1fbffc00-0x15049400",
                                                                                                                   "0x1fbffc00-0x1504a400",
                                                                                                                   "0x1fbffc00-0x1504b400",
                                                                                                                   "0x1fbffc00-0x1504c400",
                                                                                                                   "0x1fbffc00-0x1504d400",
                                                                                                                   "0x1fbffc00-0x1504e400",
                                                                                                                   "0x1fbffc00-0x1504f400",
                                                                                                                   "0x1fbffc00-0x15050400",
                                                                                                                   "0x1fbffc00-0x15051400",
                                                                                                                   "0x1fbffc00-0x15052400",
                                                                                                                   "0x1fbffc00-0x15053400",
                                                                                                                   "0x1fbffc00-0x15054400",
                                                                                                                   "0x1fbffc00-0x15055400",
                                                                                                                   "0x1fbffc00-0x15056400")),
    cms.PSet(detSelection = cms.uint32(251),detLabel = cms.string("FPIXpD2R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x15081400",
                                                                                                                   "0x1fbffc00-0x15082400",
                                                                                                                   "0x1fbffc00-0x15083400",
                                                                                                                   "0x1fbffc00-0x15084400",
                                                                                                                   "0x1fbffc00-0x15085400",
                                                                                                                   "0x1fbffc00-0x15086400",
                                                                                                                   "0x1fbffc00-0x15087400",
                                                                                                                   "0x1fbffc00-0x15088400",
                                                                                                                   "0x1fbffc00-0x15089400",
                                                                                                                   "0x1fbffc00-0x1508a400",
                                                                                                                   "0x1fbffc00-0x1508b400",
                                                                                                                   "0x1fbffc00-0x1508c400",
                                                                                                                   "0x1fbffc00-0x1508d400",
                                                                                                                   "0x1fbffc00-0x1508e400",
                                                                                                                   "0x1fbffc00-0x1508f400",
                                                                                                                   "0x1fbffc00-0x15090400",
                                                                                                                   "0x1fbffc00-0x15091400",
                                                                                                                   "0x1fbffc00-0x15092400",
                                                                                                                   "0x1fbffc00-0x15093400",
                                                                                                                   "0x1fbffc00-0x15094400",
                                                                                                                   "0x1fbffc00-0x15095400",
                                                                                                                   "0x1fbffc00-0x15096400")),
    cms.PSet(detSelection = cms.uint32(261),detLabel = cms.string("FPIXpD3R1pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c1400",
                                                                                                                   "0x1fbffc00-0x150c2400",
                                                                                                                   "0x1fbffc00-0x150c3400",
                                                                                                                   "0x1fbffc00-0x150c4400",
                                                                                                                   "0x1fbffc00-0x150c5400",
                                                                                                                   "0x1fbffc00-0x150c6400",
                                                                                                                   "0x1fbffc00-0x150c7400",
                                                                                                                   "0x1fbffc00-0x150c8400",
                                                                                                                   "0x1fbffc00-0x150c9400",
                                                                                                                   "0x1fbffc00-0x150ca400",
                                                                                                                   "0x1fbffc00-0x150cb400",
                                                                                                                   "0x1fbffc00-0x150cc400",
                                                                                                                   "0x1fbffc00-0x150cd400",
                                                                                                                   "0x1fbffc00-0x150ce400",
                                                                                                                   "0x1fbffc00-0x150cf400",
                                                                                                                   "0x1fbffc00-0x150d0400",
                                                                                                                   "0x1fbffc00-0x150d1400",
                                                                                                                   "0x1fbffc00-0x150d2400",
                                                                                                                   "0x1fbffc00-0x150d3400",
                                                                                                                   "0x1fbffc00-0x150d4400",
                                                                                                                   "0x1fbffc00-0x150d5400",
                                                                                                                   "0x1fbffc00-0x150d6400")),
    cms.PSet(detSelection = cms.uint32(212),detLabel = cms.string("FPIXmD1R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x14841800",
                                                                                                                   "0x1fbffc00-0x14842800",
                                                                                                                   "0x1fbffc00-0x14843800",
                                                                                                                   "0x1fbffc00-0x14844800",
                                                                                                                   "0x1fbffc00-0x14845800",
                                                                                                                   "0x1fbffc00-0x14846800",
                                                                                                                   "0x1fbffc00-0x14847800",
                                                                                                                   "0x1fbffc00-0x14848800",
                                                                                                                   "0x1fbffc00-0x14849800",
                                                                                                                   "0x1fbffc00-0x1484a800",
                                                                                                                   "0x1fbffc00-0x1484b800",
                                                                                                                   "0x1fbffc00-0x1484c800",
                                                                                                                   "0x1fbffc00-0x1484d800",
                                                                                                                   "0x1fbffc00-0x1484e800",
                                                                                                                   "0x1fbffc00-0x1484f800",
                                                                                                                   "0x1fbffc00-0x14850800",
                                                                                                                   "0x1fbffc00-0x14851800",
                                                                                                                   "0x1fbffc00-0x14852800",
                                                                                                                   "0x1fbffc00-0x14853800",
                                                                                                                   "0x1fbffc00-0x14854800",
                                                                                                                   "0x1fbffc00-0x14855800",
                                                                                                                   "0x1fbffc00-0x14856800")),
    cms.PSet(detSelection = cms.uint32(222),detLabel = cms.string("FPIXmD2R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x14881800",
                                                                                                                   "0x1fbffc00-0x14882800",
                                                                                                                   "0x1fbffc00-0x14883800",
                                                                                                                   "0x1fbffc00-0x14884800",
                                                                                                                   "0x1fbffc00-0x14885800",
                                                                                                                   "0x1fbffc00-0x14886800",
                                                                                                                   "0x1fbffc00-0x14887800",
                                                                                                                   "0x1fbffc00-0x14888800",
                                                                                                                   "0x1fbffc00-0x14889800",
                                                                                                                   "0x1fbffc00-0x1488a800",
                                                                                                                   "0x1fbffc00-0x1488b800",
                                                                                                                   "0x1fbffc00-0x1488c800",
                                                                                                                   "0x1fbffc00-0x1488d800",
                                                                                                                   "0x1fbffc00-0x1488e800",
                                                                                                                   "0x1fbffc00-0x1488f800",
                                                                                                                   "0x1fbffc00-0x14890800",
                                                                                                                   "0x1fbffc00-0x14891800",
                                                                                                                   "0x1fbffc00-0x14892800",
                                                                                                                   "0x1fbffc00-0x14893800",
                                                                                                                   "0x1fbffc00-0x14894800",
                                                                                                                   "0x1fbffc00-0x14895800",
                                                                                                                   "0x1fbffc00-0x14896800")),
    cms.PSet(detSelection = cms.uint32(232),detLabel = cms.string("FPIXmD3R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c1800",
                                                                                                                   "0x1fbffc00-0x148c2800",
                                                                                                                   "0x1fbffc00-0x148c3800",
                                                                                                                   "0x1fbffc00-0x148c4800",
                                                                                                                   "0x1fbffc00-0x148c5800",
                                                                                                                   "0x1fbffc00-0x148c6800",
                                                                                                                   "0x1fbffc00-0x148c7800",
                                                                                                                   "0x1fbffc00-0x148c8800",
                                                                                                                   "0x1fbffc00-0x148c9800",
                                                                                                                   "0x1fbffc00-0x148ca800",
                                                                                                                   "0x1fbffc00-0x148cb800",
                                                                                                                   "0x1fbffc00-0x148cc800",
                                                                                                                   "0x1fbffc00-0x148cd800",
                                                                                                                   "0x1fbffc00-0x148ce800",
                                                                                                                   "0x1fbffc00-0x148cf800",
                                                                                                                   "0x1fbffc00-0x148d0800",
                                                                                                                   "0x1fbffc00-0x148d1800",
                                                                                                                   "0x1fbffc00-0x148d2800",
                                                                                                                   "0x1fbffc00-0x148d3800",
                                                                                                                   "0x1fbffc00-0x148d4800",
                                                                                                                   "0x1fbffc00-0x148d5800",
                                                                                                                   "0x1fbffc00-0x148d6800")),
    cms.PSet(detSelection = cms.uint32(242),detLabel = cms.string("FPIXpD1R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x15041800",
                                                                                                                   "0x1fbffc00-0x15042800",
                                                                                                                   "0x1fbffc00-0x15043800",
                                                                                                                   "0x1fbffc00-0x15044800",
                                                                                                                   "0x1fbffc00-0x15045800",
                                                                                                                   "0x1fbffc00-0x15046800",
                                                                                                                   "0x1fbffc00-0x15047800",
                                                                                                                   "0x1fbffc00-0x15048800",
                                                                                                                   "0x1fbffc00-0x15049800",
                                                                                                                   "0x1fbffc00-0x1504a800",
                                                                                                                   "0x1fbffc00-0x1504b800",
                                                                                                                   "0x1fbffc00-0x1504c800",
                                                                                                                   "0x1fbffc00-0x1504d800",
                                                                                                                   "0x1fbffc00-0x1504e800",
                                                                                                                   "0x1fbffc00-0x1504f800",
                                                                                                                   "0x1fbffc00-0x15050800",
                                                                                                                   "0x1fbffc00-0x15051800",
                                                                                                                   "0x1fbffc00-0x15052800",
                                                                                                                   "0x1fbffc00-0x15053800",
                                                                                                                   "0x1fbffc00-0x15054800",
                                                                                                                   "0x1fbffc00-0x15055800",
                                                                                                                   "0x1fbffc00-0x15056800")),
    cms.PSet(detSelection = cms.uint32(252),detLabel = cms.string("FPIXpD2R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x15081800",
                                                                                                                   "0x1fbffc00-0x15082800",
                                                                                                                   "0x1fbffc00-0x15083800",
                                                                                                                   "0x1fbffc00-0x15084800",
                                                                                                                   "0x1fbffc00-0x15085800",
                                                                                                                   "0x1fbffc00-0x15086800",
                                                                                                                   "0x1fbffc00-0x15087800",
                                                                                                                   "0x1fbffc00-0x15088800",
                                                                                                                   "0x1fbffc00-0x15089800",
                                                                                                                   "0x1fbffc00-0x1508a800",
                                                                                                                   "0x1fbffc00-0x1508b800",
                                                                                                                   "0x1fbffc00-0x1508c800",
                                                                                                                   "0x1fbffc00-0x1508d800",
                                                                                                                   "0x1fbffc00-0x1508e800",
                                                                                                                   "0x1fbffc00-0x1508f800",
                                                                                                                   "0x1fbffc00-0x15090800",
                                                                                                                   "0x1fbffc00-0x15091800",
                                                                                                                   "0x1fbffc00-0x15092800",
                                                                                                                   "0x1fbffc00-0x15093800",
                                                                                                                   "0x1fbffc00-0x15094800",
                                                                                                                   "0x1fbffc00-0x15095800",
                                                                                                                   "0x1fbffc00-0x15096800")),
    cms.PSet(detSelection = cms.uint32(262),detLabel = cms.string("FPIXpD3R1pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c1800",
                                                                                                                   "0x1fbffc00-0x150c2800",
                                                                                                                   "0x1fbffc00-0x150c3800",
                                                                                                                   "0x1fbffc00-0x150c4800",
                                                                                                                   "0x1fbffc00-0x150c5800",
                                                                                                                   "0x1fbffc00-0x150c6800",
                                                                                                                   "0x1fbffc00-0x150c7800",
                                                                                                                   "0x1fbffc00-0x150c8800",
                                                                                                                   "0x1fbffc00-0x150c9800",
                                                                                                                   "0x1fbffc00-0x150ca800",
                                                                                                                   "0x1fbffc00-0x150cb800",
                                                                                                                   "0x1fbffc00-0x150cc800",
                                                                                                                   "0x1fbffc00-0x150cd800",
                                                                                                                   "0x1fbffc00-0x150ce800",
                                                                                                                   "0x1fbffc00-0x150cf800",
                                                                                                                   "0x1fbffc00-0x150d0800",
                                                                                                                   "0x1fbffc00-0x150d1800",
                                                                                                                   "0x1fbffc00-0x150d2800",
                                                                                                                   "0x1fbffc00-0x150d3800",
                                                                                                                   "0x1fbffc00-0x150d4800",
                                                                                                                   "0x1fbffc00-0x150d5800",
                                                                                                                   "0x1fbffc00-0x150d6800")),
    
    cms.PSet(detSelection = cms.uint32(213),detLabel = cms.string("FPIXmD1R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x14857400",
                                                                                                                   "0x1fbffc00-0x14858400",
                                                                                                                   "0x1fbffc00-0x14859400",
                                                                                                                   "0x1fbffc00-0x1485a400",
                                                                                                                   "0x1fbffc00-0x1485b400",
                                                                                                                   "0x1fbffc00-0x1485c400",
                                                                                                                   "0x1fbffc00-0x1485d400",
                                                                                                                   "0x1fbffc00-0x1485e400",
                                                                                                                   "0x1fbffc00-0x1485f400",
                                                                                                                   "0x1fbffc00-0x14860400",
                                                                                                                   "0x1fbffc00-0x14861400",
                                                                                                                   "0x1fbffc00-0x14862400",
                                                                                                                   "0x1fbffc00-0x14863400",
                                                                                                                   "0x1fbffc00-0x14864400",
                                                                                                                   "0x1fbffc00-0x14865400",
                                                                                                                   "0x1fbffc00-0x14866400",
                                                                                                                   "0x1fbffc00-0x14867400",
                                                                                                                   "0x1fbffc00-0x14868400",
                                                                                                                   "0x1fbffc00-0x14869400",
                                                                                                                   "0x1fbffc00-0x1486a400",
                                                                                                                   "0x1fbffc00-0x1486b400",
                                                                                                                   "0x1fbffc00-0x1486c400",
                                                                                                                   "0x1fbffc00-0x1486d400",
                                                                                                                   "0x1fbffc00-0x1486e400",
                                                                                                                   "0x1fbffc00-0x1486f400",
                                                                                                                   "0x1fbffc00-0x14870400",
                                                                                                                   "0x1fbffc00-0x14871400",
                                                                                                                   "0x1fbffc00-0x14872400",
                                                                                                                   "0x1fbffc00-0x14873400",
                                                                                                                   "0x1fbffc00-0x14874400",
                                                                                                                   "0x1fbffc00-0x14875400",
                                                                                                                   "0x1fbffc00-0x14876400",
                                                                                                                   "0x1fbffc00-0x14877400",
                                                                                                                   "0x1fbffc00-0x14878400")),
    cms.PSet(detSelection = cms.uint32(223),detLabel = cms.string("FPIXmD2R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x14897400",
                                                                                                                   "0x1fbffc00-0x14898400",
                                                                                                                   "0x1fbffc00-0x14899400",
                                                                                                                   "0x1fbffc00-0x1489a400",
                                                                                                                   "0x1fbffc00-0x1489b400",
                                                                                                                   "0x1fbffc00-0x1489c400",
                                                                                                                   "0x1fbffc00-0x1489d400",
                                                                                                                   "0x1fbffc00-0x1489e400",
                                                                                                                   "0x1fbffc00-0x1489f400",
                                                                                                                   "0x1fbffc00-0x148a0400",
                                                                                                                   "0x1fbffc00-0x148a1400",
                                                                                                                   "0x1fbffc00-0x148a2400",
                                                                                                                   "0x1fbffc00-0x148a3400",
                                                                                                                   "0x1fbffc00-0x148a4400",
                                                                                                                   "0x1fbffc00-0x148a5400",
                                                                                                                   "0x1fbffc00-0x148a6400",
                                                                                                                   "0x1fbffc00-0x148a7400",
                                                                                                                   "0x1fbffc00-0x148a8400",
                                                                                                                   "0x1fbffc00-0x148a9400",
                                                                                                                   "0x1fbffc00-0x148aa400",
                                                                                                                   "0x1fbffc00-0x148ab400",
                                                                                                                   "0x1fbffc00-0x148ac400",
                                                                                                                   "0x1fbffc00-0x148ad400",
                                                                                                                   "0x1fbffc00-0x148ae400",
                                                                                                                   "0x1fbffc00-0x148af400",
                                                                                                                   "0x1fbffc00-0x148b0400",
                                                                                                                   "0x1fbffc00-0x148b1400",
                                                                                                                   "0x1fbffc00-0x148b2400",
                                                                                                                   "0x1fbffc00-0x148b3400",
                                                                                                                   "0x1fbffc00-0x148b4400",
                                                                                                                   "0x1fbffc00-0x148b5400",
                                                                                                                   "0x1fbffc00-0x148b6400",
                                                                                                                   "0x1fbffc00-0x148b7400",
                                                                                                                   "0x1fbffc00-0x148b8400")),
    cms.PSet(detSelection = cms.uint32(233),detLabel = cms.string("FPIXmD3R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d7400",
                                                                                                                   "0x1fbffc00-0x148d8400",
                                                                                                                   "0x1fbffc00-0x148d9400",
                                                                                                                   "0x1fbffc00-0x148da400",
                                                                                                                   "0x1fbffc00-0x148db400",
                                                                                                                   "0x1fbffc00-0x148dc400",
                                                                                                                   "0x1fbffc00-0x148dd400",
                                                                                                                   "0x1fbffc00-0x148de400",
                                                                                                                   "0x1fbffc00-0x148df400",
                                                                                                                   "0x1fbffc00-0x148e0400",
                                                                                                                   "0x1fbffc00-0x148e1400",
                                                                                                                   "0x1fbffc00-0x148e2400",
                                                                                                                   "0x1fbffc00-0x148e3400",
                                                                                                                   "0x1fbffc00-0x148e4400",
                                                                                                                   "0x1fbffc00-0x148e5400",
                                                                                                                   "0x1fbffc00-0x148e6400",
                                                                                                                   "0x1fbffc00-0x148e7400",
                                                                                                                   "0x1fbffc00-0x148e8400",
                                                                                                                   "0x1fbffc00-0x148e9400",
                                                                                                                   "0x1fbffc00-0x148ea400",
                                                                                                                   "0x1fbffc00-0x148eb400",
                                                                                                                   "0x1fbffc00-0x148ec400",
                                                                                                                   "0x1fbffc00-0x148ed400",
                                                                                                                   "0x1fbffc00-0x148ee400",
                                                                                                                   "0x1fbffc00-0x148ef400",
                                                                                                                   "0x1fbffc00-0x148f0400",
                                                                                                                   "0x1fbffc00-0x148f1400",
                                                                                                                   "0x1fbffc00-0x148f2400",
                                                                                                                   "0x1fbffc00-0x148f3400",
                                                                                                                   "0x1fbffc00-0x148f4400",
                                                                                                                   "0x1fbffc00-0x148f5400",
                                                                                                                   "0x1fbffc00-0x148f6400",
                                                                                                                   "0x1fbffc00-0x148f7400",
                                                                                                                   "0x1fbffc00-0x148f8400")),

    cms.PSet(detSelection = cms.uint32(243),detLabel = cms.string("FPIXpD1R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x15057400",
                                                                                                                   "0x1fbffc00-0x15058400",
                                                                                                                   "0x1fbffc00-0x15059400",
                                                                                                                   "0x1fbffc00-0x1505a400",
                                                                                                                   "0x1fbffc00-0x1505b400",
                                                                                                                   "0x1fbffc00-0x1505c400",
                                                                                                                   "0x1fbffc00-0x1505d400",
                                                                                                                   "0x1fbffc00-0x1505e400",
                                                                                                                   "0x1fbffc00-0x1505f400",
                                                                                                                   "0x1fbffc00-0x15060400",
                                                                                                                   "0x1fbffc00-0x15061400",
                                                                                                                   "0x1fbffc00-0x15062400",
                                                                                                                   "0x1fbffc00-0x15063400",
                                                                                                                   "0x1fbffc00-0x15064400",
                                                                                                                   "0x1fbffc00-0x15065400",
                                                                                                                   "0x1fbffc00-0x15066400",
                                                                                                                   "0x1fbffc00-0x15067400",
                                                                                                                   "0x1fbffc00-0x15068400",
                                                                                                                   "0x1fbffc00-0x15069400",
                                                                                                                   "0x1fbffc00-0x1506a400",
                                                                                                                   "0x1fbffc00-0x1506b400",
                                                                                                                   "0x1fbffc00-0x1506c400",
                                                                                                                   "0x1fbffc00-0x1506d400",
                                                                                                                   "0x1fbffc00-0x1506e400",
                                                                                                                   "0x1fbffc00-0x1506f400",
                                                                                                                   "0x1fbffc00-0x15070400",
                                                                                                                   "0x1fbffc00-0x15071400",
                                                                                                                   "0x1fbffc00-0x15072400",
                                                                                                                   "0x1fbffc00-0x15073400",
                                                                                                                   "0x1fbffc00-0x15074400",
                                                                                                                   "0x1fbffc00-0x15075400",
                                                                                                                   "0x1fbffc00-0x15076400",
                                                                                                                   "0x1fbffc00-0x15077400",
                                                                                                                   "0x1fbffc00-0x15078400")),
    cms.PSet(detSelection = cms.uint32(253),detLabel = cms.string("FPIXpD2R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x15097400",
                                                                                                                   "0x1fbffc00-0x15098400",
                                                                                                                   "0x1fbffc00-0x15099400",
                                                                                                                   "0x1fbffc00-0x1509a400",
                                                                                                                   "0x1fbffc00-0x1509b400",
                                                                                                                   "0x1fbffc00-0x1509c400",
                                                                                                                   "0x1fbffc00-0x1509d400",
                                                                                                                   "0x1fbffc00-0x1509e400",
                                                                                                                   "0x1fbffc00-0x1509f400",
                                                                                                                   "0x1fbffc00-0x150a0400",
                                                                                                                   "0x1fbffc00-0x150a1400",
                                                                                                                   "0x1fbffc00-0x150a2400",
                                                                                                                   "0x1fbffc00-0x150a3400",
                                                                                                                   "0x1fbffc00-0x150a4400",
                                                                                                                   "0x1fbffc00-0x150a5400",
                                                                                                                   "0x1fbffc00-0x150a6400",
                                                                                                                   "0x1fbffc00-0x150a7400",
                                                                                                                   "0x1fbffc00-0x150a8400",
                                                                                                                   "0x1fbffc00-0x150a9400",
                                                                                                                   "0x1fbffc00-0x150aa400",
                                                                                                                   "0x1fbffc00-0x150ab400",
                                                                                                                   "0x1fbffc00-0x150ac400",
                                                                                                                   "0x1fbffc00-0x150ad400",
                                                                                                                   "0x1fbffc00-0x150ae400",
                                                                                                                   "0x1fbffc00-0x150af400",
                                                                                                                   "0x1fbffc00-0x150b0400",
                                                                                                                   "0x1fbffc00-0x150b1400",
                                                                                                                   "0x1fbffc00-0x150b2400",
                                                                                                                   "0x1fbffc00-0x150b3400",
                                                                                                                   "0x1fbffc00-0x150b4400",
                                                                                                                   "0x1fbffc00-0x150b5400",
                                                                                                                   "0x1fbffc00-0x150b6400",
                                                                                                                   "0x1fbffc00-0x150b7400",
                                                                                                                   "0x1fbffc00-0x150b8400")),
    cms.PSet(detSelection = cms.uint32(263),detLabel = cms.string("FPIXpD3R2pan1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d7400",
                                                                                                                   "0x1fbffc00-0x150d8400",
                                                                                                                   "0x1fbffc00-0x150d9400",
                                                                                                                   "0x1fbffc00-0x150da400",
                                                                                                                   "0x1fbffc00-0x150db400",
                                                                                                                   "0x1fbffc00-0x150dc400",
                                                                                                                   "0x1fbffc00-0x150dd400",
                                                                                                                   "0x1fbffc00-0x150de400",
                                                                                                                   "0x1fbffc00-0x150df400",
                                                                                                                   "0x1fbffc00-0x150e0400",
                                                                                                                   "0x1fbffc00-0x150e1400",
                                                                                                                   "0x1fbffc00-0x150e2400",
                                                                                                                   "0x1fbffc00-0x150e3400",
                                                                                                                   "0x1fbffc00-0x150e4400",
                                                                                                                   "0x1fbffc00-0x150e5400",
                                                                                                                   "0x1fbffc00-0x150e6400",
                                                                                                                   "0x1fbffc00-0x150e7400",
                                                                                                                   "0x1fbffc00-0x150e8400",
                                                                                                                   "0x1fbffc00-0x150e9400",
                                                                                                                   "0x1fbffc00-0x150ea400",
                                                                                                                   "0x1fbffc00-0x150eb400",
                                                                                                                   "0x1fbffc00-0x150ec400",
                                                                                                                   "0x1fbffc00-0x150ed400",
                                                                                                                   "0x1fbffc00-0x150ee400",
                                                                                                                   "0x1fbffc00-0x150ef400",
                                                                                                                   "0x1fbffc00-0x150f0400",
                                                                                                                   "0x1fbffc00-0x150f1400",
                                                                                                                   "0x1fbffc00-0x150f2400",
                                                                                                                   "0x1fbffc00-0x150f3400",
                                                                                                                   "0x1fbffc00-0x150f4400",
                                                                                                                   "0x1fbffc00-0x150f5400",
                                                                                                                   "0x1fbffc00-0x150f6400",
                                                                                                                   "0x1fbffc00-0x150f7400",
                                                                                                                   "0x1fbffc00-0x150f8400")),

    cms.PSet(detSelection = cms.uint32(214),detLabel = cms.string("FPIXmD1R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x14857800",
                                                                                                                   "0x1fbffc00-0x14858800",
                                                                                                                   "0x1fbffc00-0x14859800",
                                                                                                                   "0x1fbffc00-0x1485a800",
                                                                                                                   "0x1fbffc00-0x1485b800",
                                                                                                                   "0x1fbffc00-0x1485c800",
                                                                                                                   "0x1fbffc00-0x1485d800",
                                                                                                                   "0x1fbffc00-0x1485e800",
                                                                                                                   "0x1fbffc00-0x1485f800",
                                                                                                                   "0x1fbffc00-0x14860800",
                                                                                                                   "0x1fbffc00-0x14861800",
                                                                                                                   "0x1fbffc00-0x14862800",
                                                                                                                   "0x1fbffc00-0x14863800",
                                                                                                                   "0x1fbffc00-0x14864800",
                                                                                                                   "0x1fbffc00-0x14865800",
                                                                                                                   "0x1fbffc00-0x14866800",
                                                                                                                   "0x1fbffc00-0x14867800",
                                                                                                                   "0x1fbffc00-0x14868800",
                                                                                                                   "0x1fbffc00-0x14869800",
                                                                                                                   "0x1fbffc00-0x1486a800",
                                                                                                                   "0x1fbffc00-0x1486b800",
                                                                                                                   "0x1fbffc00-0x1486c800",
                                                                                                                   "0x1fbffc00-0x1486d800",
                                                                                                                   "0x1fbffc00-0x1486e800",
                                                                                                                   "0x1fbffc00-0x1486f800",
                                                                                                                   "0x1fbffc00-0x14870800",
                                                                                                                   "0x1fbffc00-0x14871800",
                                                                                                                   "0x1fbffc00-0x14872800",
                                                                                                                   "0x1fbffc00-0x14873800",
                                                                                                                   "0x1fbffc00-0x14874800",
                                                                                                                   "0x1fbffc00-0x14875800",
                                                                                                                   "0x1fbffc00-0x14876800",
                                                                                                                   "0x1fbffc00-0x14877800",
                                                                                                                   "0x1fbffc00-0x14878800")),
    cms.PSet(detSelection = cms.uint32(224),detLabel = cms.string("FPIXmD2R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x14897800",
                                                                                                                   "0x1fbffc00-0x14898800",
                                                                                                                   "0x1fbffc00-0x14899800",
                                                                                                                   "0x1fbffc00-0x1489a800",
                                                                                                                   "0x1fbffc00-0x1489b800",
                                                                                                                   "0x1fbffc00-0x1489c800",
                                                                                                                   "0x1fbffc00-0x1489d800",
                                                                                                                   "0x1fbffc00-0x1489e800",
                                                                                                                   "0x1fbffc00-0x1489f800",
                                                                                                                   "0x1fbffc00-0x148a0800",
                                                                                                                   "0x1fbffc00-0x148a1800",
                                                                                                                   "0x1fbffc00-0x148a2800",
                                                                                                                   "0x1fbffc00-0x148a3800",
                                                                                                                   "0x1fbffc00-0x148a4800",
                                                                                                                   "0x1fbffc00-0x148a5800",
                                                                                                                   "0x1fbffc00-0x148a6800",
                                                                                                                   "0x1fbffc00-0x148a7800",
                                                                                                                   "0x1fbffc00-0x148a8800",
                                                                                                                   "0x1fbffc00-0x148a9800",
                                                                                                                   "0x1fbffc00-0x148aa800",
                                                                                                                   "0x1fbffc00-0x148ab800",
                                                                                                                   "0x1fbffc00-0x148ac800",
                                                                                                                   "0x1fbffc00-0x148ad800",
                                                                                                                   "0x1fbffc00-0x148ae800",
                                                                                                                   "0x1fbffc00-0x148af800",
                                                                                                                   "0x1fbffc00-0x148b0800",
                                                                                                                   "0x1fbffc00-0x148b1800",
                                                                                                                   "0x1fbffc00-0x148b2800",
                                                                                                                   "0x1fbffc00-0x148b3800",
                                                                                                                   "0x1fbffc00-0x148b4800",
                                                                                                                   "0x1fbffc00-0x148b5800",
                                                                                                                   "0x1fbffc00-0x148b6800",
                                                                                                                   "0x1fbffc00-0x148b7800",
                                                                                                                   "0x1fbffc00-0x148b8800")),
    cms.PSet(detSelection = cms.uint32(234),detLabel = cms.string("FPIXmD3R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d7800",
                                                                                                                   "0x1fbffc00-0x148d8800",
                                                                                                                   "0x1fbffc00-0x148d9800",
                                                                                                                   "0x1fbffc00-0x148da800",
                                                                                                                   "0x1fbffc00-0x148db800",
                                                                                                                   "0x1fbffc00-0x148dc800",
                                                                                                                   "0x1fbffc00-0x148dd800",
                                                                                                                   "0x1fbffc00-0x148de800",
                                                                                                                   "0x1fbffc00-0x148df800",
                                                                                                                   "0x1fbffc00-0x148e0800",
                                                                                                                   "0x1fbffc00-0x148e1800",
                                                                                                                   "0x1fbffc00-0x148e2800",
                                                                                                                   "0x1fbffc00-0x148e3800",
                                                                                                                   "0x1fbffc00-0x148e4800",
                                                                                                                   "0x1fbffc00-0x148e5800",
                                                                                                                   "0x1fbffc00-0x148e6800",
                                                                                                                   "0x1fbffc00-0x148e7800",
                                                                                                                   "0x1fbffc00-0x148e8800",
                                                                                                                   "0x1fbffc00-0x148e9800",
                                                                                                                   "0x1fbffc00-0x148ea800",
                                                                                                                   "0x1fbffc00-0x148eb800",
                                                                                                                   "0x1fbffc00-0x148ec800",
                                                                                                                   "0x1fbffc00-0x148ed800",
                                                                                                                   "0x1fbffc00-0x148ee800",
                                                                                                                   "0x1fbffc00-0x148ef800",
                                                                                                                   "0x1fbffc00-0x148f0800",
                                                                                                                   "0x1fbffc00-0x148f1800",
                                                                                                                   "0x1fbffc00-0x148f2800",
                                                                                                                   "0x1fbffc00-0x148f3800",
                                                                                                                   "0x1fbffc00-0x148f4800",
                                                                                                                   "0x1fbffc00-0x148f5800",
                                                                                                                   "0x1fbffc00-0x148f6800",
                                                                                                                   "0x1fbffc00-0x148f7800",
                                                                                                                   "0x1fbffc00-0x148f8800")),

    cms.PSet(detSelection = cms.uint32(244),detLabel = cms.string("FPIXpD1R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x15057800",
                                                                                                                   "0x1fbffc00-0x15058800",
                                                                                                                   "0x1fbffc00-0x15059800",
                                                                                                                   "0x1fbffc00-0x1505a800",
                                                                                                                   "0x1fbffc00-0x1505b800",
                                                                                                                   "0x1fbffc00-0x1505c800",
                                                                                                                   "0x1fbffc00-0x1505d800",
                                                                                                                   "0x1fbffc00-0x1505e800",
                                                                                                                   "0x1fbffc00-0x1505f800",
                                                                                                                   "0x1fbffc00-0x15060800",
                                                                                                                   "0x1fbffc00-0x15061800",
                                                                                                                   "0x1fbffc00-0x15062800",
                                                                                                                   "0x1fbffc00-0x15063800",
                                                                                                                   "0x1fbffc00-0x15064800",
                                                                                                                   "0x1fbffc00-0x15065800",
                                                                                                                   "0x1fbffc00-0x15066800",
                                                                                                                   "0x1fbffc00-0x15067800",
                                                                                                                   "0x1fbffc00-0x15068800",
                                                                                                                   "0x1fbffc00-0x15069800",
                                                                                                                   "0x1fbffc00-0x1506a800",
                                                                                                                   "0x1fbffc00-0x1506b800",
                                                                                                                   "0x1fbffc00-0x1506c800",
                                                                                                                   "0x1fbffc00-0x1506d800",
                                                                                                                   "0x1fbffc00-0x1506e800",
                                                                                                                   "0x1fbffc00-0x1506f800",
                                                                                                                   "0x1fbffc00-0x15070800",
                                                                                                                   "0x1fbffc00-0x15071800",
                                                                                                                   "0x1fbffc00-0x15072800",
                                                                                                                   "0x1fbffc00-0x15073800",
                                                                                                                   "0x1fbffc00-0x15074800",
                                                                                                                   "0x1fbffc00-0x15075800",
                                                                                                                   "0x1fbffc00-0x15076800",
                                                                                                                   "0x1fbffc00-0x15077800",
                                                                                                                   "0x1fbffc00-0x15078800")),
    cms.PSet(detSelection = cms.uint32(254),detLabel = cms.string("FPIXpD2R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x15097800",
                                                                                                                   "0x1fbffc00-0x15098800",
                                                                                                                   "0x1fbffc00-0x15099800",
                                                                                                                   "0x1fbffc00-0x1509a800",
                                                                                                                   "0x1fbffc00-0x1509b800",
                                                                                                                   "0x1fbffc00-0x1509c800",
                                                                                                                   "0x1fbffc00-0x1509d800",
                                                                                                                   "0x1fbffc00-0x1509e800",
                                                                                                                   "0x1fbffc00-0x1509f800",
                                                                                                                   "0x1fbffc00-0x150a0800",
                                                                                                                   "0x1fbffc00-0x150a1800",
                                                                                                                   "0x1fbffc00-0x150a2800",
                                                                                                                   "0x1fbffc00-0x150a3800",
                                                                                                                   "0x1fbffc00-0x150a4800",
                                                                                                                   "0x1fbffc00-0x150a5800",
                                                                                                                   "0x1fbffc00-0x150a6800",
                                                                                                                   "0x1fbffc00-0x150a7800",
                                                                                                                   "0x1fbffc00-0x150a8800",
                                                                                                                   "0x1fbffc00-0x150a9800",
                                                                                                                   "0x1fbffc00-0x150aa800",
                                                                                                                   "0x1fbffc00-0x150ab800",
                                                                                                                   "0x1fbffc00-0x150ac800",
                                                                                                                   "0x1fbffc00-0x150ad800",
                                                                                                                   "0x1fbffc00-0x150ae800",
                                                                                                                   "0x1fbffc00-0x150af800",
                                                                                                                   "0x1fbffc00-0x150b0800",
                                                                                                                   "0x1fbffc00-0x150b1800",
                                                                                                                   "0x1fbffc00-0x150b2800",
                                                                                                                   "0x1fbffc00-0x150b3800",
                                                                                                                   "0x1fbffc00-0x150b4800",
                                                                                                                   "0x1fbffc00-0x150b5800",
                                                                                                                   "0x1fbffc00-0x150b6800",
                                                                                                                   "0x1fbffc00-0x150b7800",
                                                                                                                   "0x1fbffc00-0x150b8800")),
    cms.PSet(detSelection = cms.uint32(264),detLabel = cms.string("FPIXpD3R2pan2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d7800",
                                                                                                                   "0x1fbffc00-0x150d8800",
                                                                                                                   "0x1fbffc00-0x150d9800",
                                                                                                                   "0x1fbffc00-0x150da800",
                                                                                                                   "0x1fbffc00-0x150db800",
                                                                                                                   "0x1fbffc00-0x150dc800",
                                                                                                                   "0x1fbffc00-0x150dd800",
                                                                                                                   "0x1fbffc00-0x150de800",
                                                                                                                   "0x1fbffc00-0x150df800",
                                                                                                                   "0x1fbffc00-0x150e0800",
                                                                                                                   "0x1fbffc00-0x150e1800",
                                                                                                                   "0x1fbffc00-0x150e2800",
                                                                                                                   "0x1fbffc00-0x150e3800",
                                                                                                                   "0x1fbffc00-0x150e4800",
                                                                                                                   "0x1fbffc00-0x150e5800",
                                                                                                                   "0x1fbffc00-0x150e6800",
                                                                                                                   "0x1fbffc00-0x150e7800",
                                                                                                                   "0x1fbffc00-0x150e8800",
                                                                                                                   "0x1fbffc00-0x150e9800",
                                                                                                                   "0x1fbffc00-0x150ea800",
                                                                                                                   "0x1fbffc00-0x150eb800",
                                                                                                                   "0x1fbffc00-0x150ec800",
                                                                                                                   "0x1fbffc00-0x150ed800",
                                                                                                                   "0x1fbffc00-0x150ee800",
                                                                                                                   "0x1fbffc00-0x150ef800",
                                                                                                                   "0x1fbffc00-0x150f0800",
                                                                                                                   "0x1fbffc00-0x150f1800",
                                                                                                                   "0x1fbffc00-0x150f2800",
                                                                                                                   "0x1fbffc00-0x150f3800",
                                                                                                                   "0x1fbffc00-0x150f4800",
                                                                                                                   "0x1fbffc00-0x150f5800",
                                                                                                                   "0x1fbffc00-0x150f6800",
                                                                                                                   "0x1fbffc00-0x150f7800",
                                                                                                                   "0x1fbffc00-0x150f8800"))
    )

OccupancyPlotsStripWantedSubDets = cms.VPSet (
     cms.PSet(detSelection=cms.uint32(1101),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600640c")),     # TIB+ L1 int m3
     cms.PSet(detSelection=cms.uint32(1102),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600680c")),     # TIB+ L1 ext m3
     cms.PSet(detSelection=cms.uint32(1103),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16006408")),     # TIB+ L1 int m2
     cms.PSet(detSelection=cms.uint32(1104),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16006808")),     # TIB+ L1 ext m2
     cms.PSet(detSelection=cms.uint32(1105),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16006404")),     # TIB+ L1 int m1
     cms.PSet(detSelection=cms.uint32(1106),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16006804")),     # TIB+ L1 ext m1
     cms.PSet(detSelection=cms.uint32(1107),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16005404")),     # TIB- L1 int m1
     cms.PSet(detSelection=cms.uint32(1108),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16005804")),     # TIB- L1 ext m1
     cms.PSet(detSelection=cms.uint32(1109),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16005408")),     # TIB- L1 int m2
     cms.PSet(detSelection=cms.uint32(1110),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16005808")),     # TIB- L1 ext m2
     cms.PSet(detSelection=cms.uint32(1111),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600540c")),     # TIB- L1 int m3
     cms.PSet(detSelection=cms.uint32(1112),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600580c")),     # TIB- L1 ext m3
     cms.PSet(detSelection=cms.uint32(1201),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a80c")),     # TIB+ L2 ext m3
     cms.PSet(detSelection=cms.uint32(1202),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a40c")),     # TIB+ L2 int m3
     cms.PSet(detSelection=cms.uint32(1203),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a808")),     # TIB+ L2 ext m2
     cms.PSet(detSelection=cms.uint32(1204),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a408")),     # TIB+ L2 int m2
     cms.PSet(detSelection=cms.uint32(1205),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a804")),     # TIB+ L2 ext m1
     cms.PSet(detSelection=cms.uint32(1206),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600a404")),     # TIB+ L2 int m1
     cms.PSet(detSelection=cms.uint32(1207),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16009804")),     # TIB- L2 ext m1
     cms.PSet(detSelection=cms.uint32(1208),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16009404")),     # TIB- L2 int m1
     cms.PSet(detSelection=cms.uint32(1209),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16009808")),     # TIB- L2 ext m2
     cms.PSet(detSelection=cms.uint32(1210),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16009408")),     # TIB- L2 int m2
     cms.PSet(detSelection=cms.uint32(1211),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600980c")),     # TIB- L2 ext m3
     cms.PSet(detSelection=cms.uint32(1212),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600940c")),     # TIB- L2 int m3
     cms.PSet(detSelection=cms.uint32(1301),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e40c")),     # TIB+ L3 int m3
     cms.PSet(detSelection=cms.uint32(1302),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e80c")),     # TIB+ L3 ext m3
     cms.PSet(detSelection=cms.uint32(1303),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e408")),     # TIB+ L3 int m2
     cms.PSet(detSelection=cms.uint32(1304),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e808")),     # TIB+ L3 ext m2
     cms.PSet(detSelection=cms.uint32(1305),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e404")),     # TIB+ L3 int m1
     cms.PSet(detSelection=cms.uint32(1306),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600e804")),     # TIB+ L3 ext m1
     cms.PSet(detSelection=cms.uint32(1307),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d404")),     # TIB- L3 int m1
     cms.PSet(detSelection=cms.uint32(1308),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d804")),     # TIB- L3 ext m1
     cms.PSet(detSelection=cms.uint32(1309),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d408")),     # TIB- L3 int m2
     cms.PSet(detSelection=cms.uint32(1310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d808")),     # TIB- L3 ext m2
     cms.PSet(detSelection=cms.uint32(1311),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d40c")),     # TIB- L3 int m3
     cms.PSet(detSelection=cms.uint32(1312),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1600d80c")),     # TIB- L3 ext m3
     cms.PSet(detSelection=cms.uint32(1401),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1601280c")),     # TIB+ L4 ext m3
     cms.PSet(detSelection=cms.uint32(1402),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1601240c")),     # TIB+ L4 int m3
     cms.PSet(detSelection=cms.uint32(1403),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16012808")),     # TIB+ L4 ext m2
     cms.PSet(detSelection=cms.uint32(1404),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16012408")),     # TIB+ L4 int m2
     cms.PSet(detSelection=cms.uint32(1405),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16012804")),     # TIB+ L4 ext m1
     cms.PSet(detSelection=cms.uint32(1406),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16012404")),     # TIB+ L4 int m1
     cms.PSet(detSelection=cms.uint32(1407),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16011804")),     # TIB- L4 ext m1
     cms.PSet(detSelection=cms.uint32(1408),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16011404")),     # TIB- L4 int m1
     cms.PSet(detSelection=cms.uint32(1409),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16011808")),     # TIB- L4 ext m2
     cms.PSet(detSelection=cms.uint32(1410),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x16011408")),     # TIB- L4 int m2
     cms.PSet(detSelection=cms.uint32(1411),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1601180c")),     # TIB- L4 ext m3
     cms.PSet(detSelection=cms.uint32(1412),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01fc0c-0x1601140c")),     # TIB- L4 int m3

     cms.PSet(detSelection=cms.uint32(2110),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18002a00")),     # TID- D1 R1 Front
     cms.PSet(detSelection=cms.uint32(2120),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003200")),     # TID- D2 R1 Front
     cms.PSet(detSelection=cms.uint32(2130),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003a00")),     # TID- D3 R1 Front
     cms.PSet(detSelection=cms.uint32(2140),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18004a00")),     # TID+ D1 R1 Front
     cms.PSet(detSelection=cms.uint32(2150),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005200")),     # TID+ D2 R1 Front
     cms.PSet(detSelection=cms.uint32(2160),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005a00")),     # TID+ D3 R1 Front

     cms.PSet(detSelection=cms.uint32(2210),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18002c00")),     # TID- D1 R2 Front
     cms.PSet(detSelection=cms.uint32(2220),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003400")),     # TID- D2 R2 Front
     cms.PSet(detSelection=cms.uint32(2230),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003c00")),     # TID- D3 R2 Front
     cms.PSet(detSelection=cms.uint32(2240),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18004c00")),     # TID+ D1 R2 Front
     cms.PSet(detSelection=cms.uint32(2250),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005400")),     # TID+ D2 R2 Front
     cms.PSet(detSelection=cms.uint32(2260),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005c00")),     # TID+ D3 R2 Front

     cms.PSet(detSelection=cms.uint32(2310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18002e00")),     # TID- D1 R3 Front
     cms.PSet(detSelection=cms.uint32(2320),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003600")),     # TID- D2 R3 Front
     cms.PSet(detSelection=cms.uint32(2330),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18003e00")),     # TID- D3 R3 Front
     cms.PSet(detSelection=cms.uint32(2340),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18004e00")),     # TID+ D1 R3 Front
     cms.PSet(detSelection=cms.uint32(2350),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005600")),     # TID+ D2 R3 Front
     cms.PSet(detSelection=cms.uint32(2360),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e007e00-0x18005e00")),     # TID+ D3 R3 Front

    cms.PSet(detSelection=cms.uint32(3101),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a006018")),     # TOB+ L1 m6
    cms.PSet(detSelection=cms.uint32(3102),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a006014")),     # TOB+ L1 m5
    cms.PSet(detSelection=cms.uint32(3103),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a006010")),     # TOB+ L1 m4
    cms.PSet(detSelection=cms.uint32(3104),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00600c")),     # TOB+ L1 m3
    cms.PSet(detSelection=cms.uint32(3105),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a006008")),     # TOB+ L1 m2
    cms.PSet(detSelection=cms.uint32(3106),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a006004")),     # TOB+ L1 m1
    cms.PSet(detSelection=cms.uint32(3107),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a005004")),     # TOB- L1 m1
    cms.PSet(detSelection=cms.uint32(3108),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a005008")),     # TOB- L1 m2
    cms.PSet(detSelection=cms.uint32(3109),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00500c")),     # TOB- L1 m3
    cms.PSet(detSelection=cms.uint32(3110),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a005010")),     # TOB- L1 m4
    cms.PSet(detSelection=cms.uint32(3111),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a005014")),     # TOB- L1 m5
    cms.PSet(detSelection=cms.uint32(3112),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a005018")),     # TOB- L1 m6

    cms.PSet(detSelection=cms.uint32(3201),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a018")),     # TOB+ L2 m6
    cms.PSet(detSelection=cms.uint32(3202),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a014")),     # TOB+ L2 m5
    cms.PSet(detSelection=cms.uint32(3203),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a010")),     # TOB+ L2 m4
    cms.PSet(detSelection=cms.uint32(3204),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a00c")),     # TOB+ L2 m3
    cms.PSet(detSelection=cms.uint32(3205),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a008")),     # TOB+ L2 m2
    cms.PSet(detSelection=cms.uint32(3206),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00a004")),     # TOB+ L2 m1
    cms.PSet(detSelection=cms.uint32(3207),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a009004")),     # TOB- L2 m1
    cms.PSet(detSelection=cms.uint32(3208),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a009008")),     # TOB- L2 m2
    cms.PSet(detSelection=cms.uint32(3209),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00900c")),     # TOB- L2 m3
    cms.PSet(detSelection=cms.uint32(3210),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a009010")),     # TOB- L2 m4
    cms.PSet(detSelection=cms.uint32(3211),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a009014")),     # TOB- L2 m5
    cms.PSet(detSelection=cms.uint32(3212),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a009018")),     # TOB- L2 m6

    cms.PSet(detSelection=cms.uint32(3301),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e018")),     # TOB+ L3 m6
    cms.PSet(detSelection=cms.uint32(3302),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e014")),     # TOB+ L3 m5
    cms.PSet(detSelection=cms.uint32(3303),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e010")),     # TOB+ L3 m4
    cms.PSet(detSelection=cms.uint32(3304),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e00c")),     # TOB+ L3 m3
    cms.PSet(detSelection=cms.uint32(3305),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e008")),     # TOB+ L3 m2
    cms.PSet(detSelection=cms.uint32(3306),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00e004")),     # TOB+ L3 m1
    cms.PSet(detSelection=cms.uint32(3307),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d004")),     # TOB- L3 m1
    cms.PSet(detSelection=cms.uint32(3308),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d008")),     # TOB- L3 m2
    cms.PSet(detSelection=cms.uint32(3309),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d00c")),     # TOB- L3 m3
    cms.PSet(detSelection=cms.uint32(3310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d010")),     # TOB- L3 m4
    cms.PSet(detSelection=cms.uint32(3311),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d014")),     # TOB- L3 m5
    cms.PSet(detSelection=cms.uint32(3312),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a00d018")),     # TOB- L3 m6

    cms.PSet(detSelection=cms.uint32(3401),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a012018")),     # TOB+ L4 m6
    cms.PSet(detSelection=cms.uint32(3402),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a012014")),     # TOB+ L4 m5
    cms.PSet(detSelection=cms.uint32(3403),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a012010")),     # TOB+ L4 m4
    cms.PSet(detSelection=cms.uint32(3404),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01200c")),     # TOB+ L4 m3
    cms.PSet(detSelection=cms.uint32(3405),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a012008")),     # TOB+ L4 m2
    cms.PSet(detSelection=cms.uint32(3406),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a012004")),     # TOB+ L4 m1
    cms.PSet(detSelection=cms.uint32(3407),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a011004")),     # TOB- L4 m1
    cms.PSet(detSelection=cms.uint32(3408),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a011008")),     # TOB- L4 m2
    cms.PSet(detSelection=cms.uint32(3409),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01100c")),     # TOB- L4 m3
    cms.PSet(detSelection=cms.uint32(3410),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a011010")),     # TOB- L4 m4
    cms.PSet(detSelection=cms.uint32(3411),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a011014")),     # TOB- L4 m5
    cms.PSet(detSelection=cms.uint32(3412),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a011018")),     # TOB- L4 m6

    cms.PSet(detSelection=cms.uint32(3501),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a016018")),     # TOB+ L5 m6
    cms.PSet(detSelection=cms.uint32(3502),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a016014")),     # TOB+ L5 m5
    cms.PSet(detSelection=cms.uint32(3503),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a016010")),     # TOB+ L5 m4
    cms.PSet(detSelection=cms.uint32(3504),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01600c")),     # TOB+ L5 m3
    cms.PSet(detSelection=cms.uint32(3505),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a016008")),     # TOB+ L5 m2
    cms.PSet(detSelection=cms.uint32(3506),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a016004")),     # TOB+ L5 m1
    cms.PSet(detSelection=cms.uint32(3507),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a015004")),     # TOB- L5 m1
    cms.PSet(detSelection=cms.uint32(3508),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a015008")),     # TOB- L5 m2
    cms.PSet(detSelection=cms.uint32(3509),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01500c")),     # TOB- L5 m3
    cms.PSet(detSelection=cms.uint32(3510),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a015010")),     # TOB- L5 m4
    cms.PSet(detSelection=cms.uint32(3511),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a015014")),     # TOB- L5 m5
    cms.PSet(detSelection=cms.uint32(3512),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a015018")),     # TOB- L5 m6

    cms.PSet(detSelection=cms.uint32(3601),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a018")),     # TOB+ L6 m6
    cms.PSet(detSelection=cms.uint32(3602),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a014")),     # TOB+ L6 m5
    cms.PSet(detSelection=cms.uint32(3603),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a010")),     # TOB+ L6 m4
    cms.PSet(detSelection=cms.uint32(3604),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a00c")),     # TOB+ L6 m3
    cms.PSet(detSelection=cms.uint32(3605),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a008")),     # TOB+ L6 m2
    cms.PSet(detSelection=cms.uint32(3606),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01a004")),     # TOB+ L6 m1
    cms.PSet(detSelection=cms.uint32(3607),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a019004")),     # TOB- L6 m1
    cms.PSet(detSelection=cms.uint32(3608),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a019008")),     # TOB- L6 m2
    cms.PSet(detSelection=cms.uint32(3609),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a01900c")),     # TOB- L6 m3
    cms.PSet(detSelection=cms.uint32(3610),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a019010")),     # TOB- L6 m4
    cms.PSet(detSelection=cms.uint32(3611),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a019014")),     # TOB- L6 m5
    cms.PSet(detSelection=cms.uint32(3612),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e01f01c-0x1a019018"))     # TOB- L6 m6
    )

OccupancyPlotsStripWantedSubDets.extend(
    cms.VPSet(
    cms.PSet(detSelection=cms.uint32(4110),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044020")),    # TEC- D1 R1 back
    cms.PSet(detSelection=cms.uint32(4120),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048020")),    # TEC- D2 R1 back
    cms.PSet(detSelection=cms.uint32(4130),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c020")),    # TEC- D3 R1 back
#    cms.PSet(detSelection=cms.uint32(4140),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050020")),    # TEC- D4 R1 back
#    cms.PSet(detSelection=cms.uint32(4150),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054020")),    # TEC- D5 R1 back
#    cms.PSet(detSelection=cms.uint32(4160),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058020")),    # TEC- D6 R1 back
#    cms.PSet(detSelection=cms.uint32(4170),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c020")),    # TEC- D7 R1 back
#    cms.PSet(detSelection=cms.uint32(4180),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060020")),    # TEC- D8 R1 back
#    cms.PSet(detSelection=cms.uint32(4190),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c064020")),    # TEC- D9 R1 back

    cms.PSet(detSelection=cms.uint32(4210),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044040")),    # TEC- D1 R2 back
    cms.PSet(detSelection=cms.uint32(4220),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048040")),    # TEC- D2 R2 back
    cms.PSet(detSelection=cms.uint32(4230),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c040")),    # TEC- D3 R2 back
    cms.PSet(detSelection=cms.uint32(4240),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050040")),    # TEC- D4 R2 back
    cms.PSet(detSelection=cms.uint32(4250),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054040")),    # TEC- D5 R2 back
    cms.PSet(detSelection=cms.uint32(4260),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058040")),    # TEC- D6 R2 back
#    cms.PSet(detSelection=cms.uint32(4270),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c040")),    # TEC- D7 R2 back
#    cms.PSet(detSelection=cms.uint32(4280),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060040")),    # TEC- D8 R2 back
#    cms.PSet(detSelection=cms.uint32(4290),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c064040")),    # TEC- D9 R2 back

    cms.PSet(detSelection=cms.uint32(4310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044060")),    # TEC- D1 R3 back
    cms.PSet(detSelection=cms.uint32(4320),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048060")),    # TEC- D2 R3 back
    cms.PSet(detSelection=cms.uint32(4330),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c060")),    # TEC- D3 R3 back
    cms.PSet(detSelection=cms.uint32(4340),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050060")),    # TEC- D4 R3 back
    cms.PSet(detSelection=cms.uint32(4350),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054060")),    # TEC- D5 R3 back
    cms.PSet(detSelection=cms.uint32(4360),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058060")),    # TEC- D6 R3 back
    cms.PSet(detSelection=cms.uint32(4370),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c060")),    # TEC- D7 R3 back
    cms.PSet(detSelection=cms.uint32(4380),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060060")),    # TEC- D8 R3 back
#    cms.PSet(detSelection=cms.uint32(4390),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c064060")),    # TEC- D9 R3 back

    cms.PSet(detSelection=cms.uint32(4410),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c044080")),    # TEC- D1 R4 back
    cms.PSet(detSelection=cms.uint32(4420),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c048080")),    # TEC- D2 R4 back
    cms.PSet(detSelection=cms.uint32(4430),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c080")),    # TEC- D3 R4 back
    cms.PSet(detSelection=cms.uint32(4440),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c050080")),    # TEC- D4 R4 back
    cms.PSet(detSelection=cms.uint32(4450),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c054080")),    # TEC- D5 R4 back
    cms.PSet(detSelection=cms.uint32(4460),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c058080")),    # TEC- D6 R4 back
    cms.PSet(detSelection=cms.uint32(4470),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c080")),    # TEC- D7 R4 back
    cms.PSet(detSelection=cms.uint32(4480),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c060080")),    # TEC- D8 R4 back
    cms.PSet(detSelection=cms.uint32(4490),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c064080")),    # TEC- D9 R4 back
    
    cms.PSet(detSelection=cms.uint32(4510),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440a0")),    # TEC- D1 R5 back
    cms.PSet(detSelection=cms.uint32(4520),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480a0")),    # TEC- D2 R5 back
    cms.PSet(detSelection=cms.uint32(4530),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0a0")),    # TEC- D3 R5 back
    cms.PSet(detSelection=cms.uint32(4540),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500a0")),    # TEC- D4 R5 back
    cms.PSet(detSelection=cms.uint32(4550),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540a0")),    # TEC- D5 R5 back
    cms.PSet(detSelection=cms.uint32(4560),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580a0")),    # TEC- D6 R5 back
    cms.PSet(detSelection=cms.uint32(4570),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0a0")),    # TEC- D7 R5 back
    cms.PSet(detSelection=cms.uint32(4580),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600a0")),    # TEC- D8 R5 back
    cms.PSet(detSelection=cms.uint32(4590),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640a0")),    # TEC- D9 R5 back

    cms.PSet(detSelection=cms.uint32(4610),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440c0")),    # TEC- D1 R6 back
    cms.PSet(detSelection=cms.uint32(4620),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480c0")),    # TEC- D2 R6 back
    cms.PSet(detSelection=cms.uint32(4630),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0c0")),    # TEC- D3 R6 back
    cms.PSet(detSelection=cms.uint32(4640),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500c0")),    # TEC- D4 R6 back
    cms.PSet(detSelection=cms.uint32(4650),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540c0")),    # TEC- D5 R6 back
    cms.PSet(detSelection=cms.uint32(4660),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580c0")),    # TEC- D6 R6 back
    cms.PSet(detSelection=cms.uint32(4670),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0c0")),    # TEC- D7 R6 back
    cms.PSet(detSelection=cms.uint32(4680),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600c0")),    # TEC- D8 R6 back
    cms.PSet(detSelection=cms.uint32(4690),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640c0")),    # TEC- D9 R6 back

    cms.PSet(detSelection=cms.uint32(4710),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0440e0")),    # TEC- D1 R7 back
    cms.PSet(detSelection=cms.uint32(4720),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0480e0")),    # TEC- D2 R7 back
    cms.PSet(detSelection=cms.uint32(4730),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c04c0e0")),    # TEC- D3 R7 back
    cms.PSet(detSelection=cms.uint32(4740),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0500e0")),    # TEC- D4 R7 back
    cms.PSet(detSelection=cms.uint32(4750),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0540e0")),    # TEC- D5 R7 back
    cms.PSet(detSelection=cms.uint32(4760),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0580e0")),    # TEC- D6 R7 back
    cms.PSet(detSelection=cms.uint32(4770),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c05c0e0")),    # TEC- D7 R7 back
    cms.PSet(detSelection=cms.uint32(4780),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0600e0")),    # TEC- D8 R7 back
    cms.PSet(detSelection=cms.uint32(4790),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0640e0")),    # TEC- D9 R7 back



    cms.PSet(detSelection=cms.uint32(5110),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084020")),    # TEC+ D1 R1 back
    cms.PSet(detSelection=cms.uint32(5120),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088020")),    # TEC+ D2 R1 back
    cms.PSet(detSelection=cms.uint32(5130),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c020")),    # TEC+ D3 R1 back
#    cms.PSet(detSelection=cms.uint32(5140),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090020")),    # TEC+ D4 R1 back
#    cms.PSet(detSelection=cms.uint32(5150),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094020")),    # TEC+ D5 R1 back
#    cms.PSet(detSelection=cms.uint32(5160),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098020")),    # TEC+ D6 R1 back
#    cms.PSet(detSelection=cms.uint32(5170),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c020")),    # TEC+ D7 R1 back
#    cms.PSet(detSelection=cms.uint32(5180),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0020")),    # TEC+ D8 R1 back
#    cms.PSet(detSelection=cms.uint32(5190),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a4020")),    # TEC+ D9 R1 back


    cms.PSet(detSelection=cms.uint32(5210),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084040")),    # TEC+ D1 R2 back
    cms.PSet(detSelection=cms.uint32(5220),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088040")),    # TEC+ D2 R2 back
    cms.PSet(detSelection=cms.uint32(5230),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c040")),    # TEC+ D3 R2 back
    cms.PSet(detSelection=cms.uint32(5240),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090040")),    # TEC+ D4 R2 back
    cms.PSet(detSelection=cms.uint32(5250),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094040")),    # TEC+ D5 R2 back
    cms.PSet(detSelection=cms.uint32(5260),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098040")),    # TEC+ D6 R2 back
#    cms.PSet(detSelection=cms.uint32(5270),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c040")),    # TEC+ D7 R2 back
#    cms.PSet(detSelection=cms.uint32(5280),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0040")),    # TEC+ D8 R2 back
#    cms.PSet(detSelection=cms.uint32(5290),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a4040")),    # TEC+ D9 R2 back

    cms.PSet(detSelection=cms.uint32(5310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084060")),    # TEC+ D1 R3 back
    cms.PSet(detSelection=cms.uint32(5320),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088060")),    # TEC+ D2 R3 back
    cms.PSet(detSelection=cms.uint32(5330),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c060")),    # TEC+ D3 R3 back
    cms.PSet(detSelection=cms.uint32(5340),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090060")),    # TEC+ D4 R3 back
    cms.PSet(detSelection=cms.uint32(5350),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094060")),    # TEC+ D5 R3 back
    cms.PSet(detSelection=cms.uint32(5360),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098060")),    # TEC+ D6 R3 back
    cms.PSet(detSelection=cms.uint32(5370),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c060")),    # TEC+ D7 R3 back
    cms.PSet(detSelection=cms.uint32(5380),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0060")),    # TEC+ D8 R3 back
#    cms.PSet(detSelection=cms.uint32(5390),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a4060")),    # TEC+ D9 R3 back

    cms.PSet(detSelection=cms.uint32(5410),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c084080")),    # TEC+ D1 R4 back
    cms.PSet(detSelection=cms.uint32(5420),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c088080")),    # TEC+ D2 R4 back
    cms.PSet(detSelection=cms.uint32(5430),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c080")),    # TEC+ D3 R4 back
    cms.PSet(detSelection=cms.uint32(5440),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c090080")),    # TEC+ D4 R4 back
    cms.PSet(detSelection=cms.uint32(5450),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c094080")),    # TEC+ D5 R4 back
    cms.PSet(detSelection=cms.uint32(5460),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c098080")),    # TEC+ D6 R4 back
    cms.PSet(detSelection=cms.uint32(5470),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c080")),    # TEC+ D7 R4 back
    cms.PSet(detSelection=cms.uint32(5480),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a0080")),    # TEC+ D8 R4 back
    cms.PSet(detSelection=cms.uint32(5490),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a4080")),    # TEC+ D9 R4 back

    cms.PSet(detSelection=cms.uint32(5510),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840a0")),    # TEC+ D1 R5 back
    cms.PSet(detSelection=cms.uint32(5520),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880a0")),    # TEC+ D2 R5 back
    cms.PSet(detSelection=cms.uint32(5530),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0a0")),    # TEC+ D3 R5 back
    cms.PSet(detSelection=cms.uint32(5540),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900a0")),    # TEC+ D4 R5 back
    cms.PSet(detSelection=cms.uint32(5550),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940a0")),    # TEC+ D5 R5 back
    cms.PSet(detSelection=cms.uint32(5560),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980a0")),    # TEC+ D6 R5 back
    cms.PSet(detSelection=cms.uint32(5570),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0a0")),    # TEC+ D7 R5 back
    cms.PSet(detSelection=cms.uint32(5580),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00a0")),    # TEC+ D8 R5 back
    cms.PSet(detSelection=cms.uint32(5590),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40a0")),    # TEC+ D9 R5 back

    cms.PSet(detSelection=cms.uint32(5610),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840c0")),    # TEC+ D1 R6 back
    cms.PSet(detSelection=cms.uint32(5620),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880c0")),    # TEC+ D2 R6 back
    cms.PSet(detSelection=cms.uint32(5630),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0c0")),    # TEC+ D3 R6 back
    cms.PSet(detSelection=cms.uint32(5640),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900c0")),    # TEC+ D4 R6 back
    cms.PSet(detSelection=cms.uint32(5650),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940c0")),    # TEC+ D5 R6 back
    cms.PSet(detSelection=cms.uint32(5660),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980c0")),    # TEC+ D6 R6 back
    cms.PSet(detSelection=cms.uint32(5670),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0c0")),    # TEC+ D7 R6 back
    cms.PSet(detSelection=cms.uint32(5680),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00c0")),    # TEC+ D8 R6 back
    cms.PSet(detSelection=cms.uint32(5690),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40c0")),    # TEC+ D9 R6 back

    cms.PSet(detSelection=cms.uint32(5710),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0840e0")),    # TEC+ D1 R7 back
    cms.PSet(detSelection=cms.uint32(5720),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0880e0")),    # TEC+ D2 R7 back
    cms.PSet(detSelection=cms.uint32(5730),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c08c0e0")),    # TEC+ D3 R7 back
    cms.PSet(detSelection=cms.uint32(5740),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0900e0")),    # TEC+ D4 R7 back
    cms.PSet(detSelection=cms.uint32(5750),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0940e0")),    # TEC+ D5 R7 back
    cms.PSet(detSelection=cms.uint32(5760),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0980e0")),    # TEC+ D6 R7 back
    cms.PSet(detSelection=cms.uint32(5770),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c09c0e0")),    # TEC+ D7 R7 back
    cms.PSet(detSelection=cms.uint32(5780),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a00e0")),    # TEC+ D8 R7 back
    cms.PSet(detSelection=cms.uint32(5790),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1e0fc0e0-0x1c0a40e0"))    # TEC+ D9 R7 back



    )
    )
