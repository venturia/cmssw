import FWCore.ParameterSet.Config as cms

# Pixel barrel : 4 layers x 8 modules x 2 ladder types
OccupancyPlotsBPIXOddEvenWantedSubDets = cms.VPSet (
    cms.PSet(detSelection=cms.uint32(111),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101004")),      # BPix L1 mod 1 odd ladders
    cms.PSet(detSelection=cms.uint32(112),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101008")),      # BPix L1 mod 2 odd ladders
    cms.PSet(detSelection=cms.uint32(113),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1210100c")),      # BPix L1 mod 3 odd ladders
    cms.PSet(detSelection=cms.uint32(114),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101010")),      # BPix L1 mod 4 odd ladders
    cms.PSet(detSelection=cms.uint32(115),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101014")),      # BPix L1 mod 5 odd ladders
    cms.PSet(detSelection=cms.uint32(116),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101018")),      # BPix L1 mod 6 odd ladders
    cms.PSet(detSelection=cms.uint32(117),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1210101c")),      # BPix L1 mod 7 odd ladders
    cms.PSet(detSelection=cms.uint32(118),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12101020")),      # BPix L1 mod 8 odd ladders
    cms.PSet(detSelection=cms.uint32(121),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100004")),      # BPix L1 mod 1 even ladders
    cms.PSet(detSelection=cms.uint32(122),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100008")),      # BPix L1 mod 2 even ladders
    cms.PSet(detSelection=cms.uint32(123),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1210000c")),      # BPix L1 mod 3 even ladders
    cms.PSet(detSelection=cms.uint32(124),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100010")),      # BPix L1 mod 4 even ladders
    cms.PSet(detSelection=cms.uint32(125),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100014")),      # BPix L1 mod 5 even ladders
    cms.PSet(detSelection=cms.uint32(126),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100018")),      # BPix L1 mod 6 even ladders
    cms.PSet(detSelection=cms.uint32(127),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1210001c")),      # BPix L1 mod 7 even ladders
    cms.PSet(detSelection=cms.uint32(128),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12100020")),      # BPix L1 mod 8 even ladders
    cms.PSet(detSelection=cms.uint32(131),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201004")),      # BPix L2 mod 1 odd ladders
    cms.PSet(detSelection=cms.uint32(132),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201008")),      # BPix L2 mod 2 odd ladders
    cms.PSet(detSelection=cms.uint32(133),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1220100c")),      # BPix L2 mod 3 odd ladders
    cms.PSet(detSelection=cms.uint32(134),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201010")),      # BPix L2 mod 4 odd ladders
    cms.PSet(detSelection=cms.uint32(135),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201014")),      # BPix L2 mod 5 odd ladders
    cms.PSet(detSelection=cms.uint32(136),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201018")),      # BPix L2 mod 6 odd ladders
    cms.PSet(detSelection=cms.uint32(137),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1220101c")),      # BPix L2 mod 7 odd ladders
    cms.PSet(detSelection=cms.uint32(138),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12201020")),      # BPix L2 mod 8 odd ladders
    cms.PSet(detSelection=cms.uint32(141),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200004")),      # BPix L2 mod 1 even ladders
    cms.PSet(detSelection=cms.uint32(142),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200008")),      # BPix L2 mod 2 even ladders
    cms.PSet(detSelection=cms.uint32(143),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1220000c")),      # BPix L2 mod 3 even ladders
    cms.PSet(detSelection=cms.uint32(144),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200010")),      # BPix L2 mod 4 even ladders
    cms.PSet(detSelection=cms.uint32(145),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200014")),      # BPix L2 mod 5 even ladders
    cms.PSet(detSelection=cms.uint32(146),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200018")),      # BPix L2 mod 6 even ladders
    cms.PSet(detSelection=cms.uint32(147),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1220001c")),      # BPix L2 mod 7 even ladders
    cms.PSet(detSelection=cms.uint32(148),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12200020")),      # BPix L2 mod 8 even ladders
    cms.PSet(detSelection=cms.uint32(151),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301004")),      # BPix L3 mod 1 odd ladders
    cms.PSet(detSelection=cms.uint32(152),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301008")),      # BPix L3 mod 2 odd ladders
    cms.PSet(detSelection=cms.uint32(153),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1230100c")),      # BPix L3 mod 3 odd ladders
    cms.PSet(detSelection=cms.uint32(154),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301010")),      # BPix L3 mod 4 odd ladders
    cms.PSet(detSelection=cms.uint32(155),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301014")),      # BPix L3 mod 5 odd ladders
    cms.PSet(detSelection=cms.uint32(156),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301018")),      # BPix L3 mod 6 odd ladders
    cms.PSet(detSelection=cms.uint32(157),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1230101c")),      # BPix L3 mod 7 odd ladders
    cms.PSet(detSelection=cms.uint32(158),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12301020")),      # BPix L3 mod 8 odd ladders
    cms.PSet(detSelection=cms.uint32(161),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300004")),      # BPix L3 mod 1 even ladders
    cms.PSet(detSelection=cms.uint32(162),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300008")),      # BPix L3 mod 2 even ladders
    cms.PSet(detSelection=cms.uint32(163),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1230000c")),      # BPix L3 mod 3 even ladders
    cms.PSet(detSelection=cms.uint32(164),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300010")),      # BPix L3 mod 4 even ladders
    cms.PSet(detSelection=cms.uint32(165),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300014")),      # BPix L3 mod 5 even ladders
    cms.PSet(detSelection=cms.uint32(166),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300018")),      # BPix L3 mod 6 even ladders
    cms.PSet(detSelection=cms.uint32(167),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1230001c")),      # BPix L3 mod 7 even ladders
    cms.PSet(detSelection=cms.uint32(168),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12300020")),      # BPix L3 mod 8 even ladders
    cms.PSet(detSelection=cms.uint32(171),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401004")),      # BPix L4 mod 1 odd ladders
    cms.PSet(detSelection=cms.uint32(172),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401008")),      # BPix L4 mod 2 odd ladders
    cms.PSet(detSelection=cms.uint32(173),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1240100c")),      # BPix L4 mod 3 odd ladders
    cms.PSet(detSelection=cms.uint32(174),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401010")),      # BPix L4 mod 4 odd ladders
    cms.PSet(detSelection=cms.uint32(175),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401014")),      # BPix L4 mod 5 odd ladders
    cms.PSet(detSelection=cms.uint32(176),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401018")),      # BPix L4 mod 6 odd ladders
    cms.PSet(detSelection=cms.uint32(177),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1240101c")),      # BPix L4 mod 7 odd ladders
    cms.PSet(detSelection=cms.uint32(178),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12401020")),      # BPix L4 mod 8 odd ladders
    cms.PSet(detSelection=cms.uint32(181),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400004")),      # BPix L4 mod 1 even ladders
    cms.PSet(detSelection=cms.uint32(182),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400008")),      # BPix L4 mod 2 even ladders
    cms.PSet(detSelection=cms.uint32(183),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1240000c")),      # BPix L4 mod 3 even ladders
    cms.PSet(detSelection=cms.uint32(184),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400010")),      # BPix L4 mod 4 even ladders
    cms.PSet(detSelection=cms.uint32(185),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400014")),      # BPix L4 mod 5 even ladders
    cms.PSet(detSelection=cms.uint32(186),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400018")),      # BPix L4 mod 6 even ladders
    cms.PSet(detSelection=cms.uint32(187),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x1240001c")),      # BPix L4 mod 7 even ladders
    cms.PSet(detSelection=cms.uint32(188),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1ef01ffc-0x12400020"))      # BPix L4 mod 8 even ladders
)
# BPIX ladders
OccupancyPlotsBPIXLaddersWantedSubDets = cms.VPSet (
    cms.PSet(detSelection=cms.uint32(301),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12101000")),      # BPix L1 ladder 1
    cms.PSet(detSelection=cms.uint32(302),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12102000")),      # BPix L1 ladder 2
    cms.PSet(detSelection=cms.uint32(303),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12103000")),      # BPix L1 ladder 3
    cms.PSet(detSelection=cms.uint32(304),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12104000")),      # BPix L1 ladder 4
    cms.PSet(detSelection=cms.uint32(305),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12105000")),      # BPix L1 ladder 5
    cms.PSet(detSelection=cms.uint32(306),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12106000")),      # BPix L1 ladder 6
    cms.PSet(detSelection=cms.uint32(307),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12107000")),      # BPix L1 ladder 7
    cms.PSet(detSelection=cms.uint32(308),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12108000")),      # BPix L1 ladder 8
    cms.PSet(detSelection=cms.uint32(309),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12109000")),      # BPix L1 ladder 9
    cms.PSet(detSelection=cms.uint32(310),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1210a000")),      # BPix L1 ladder 10
    cms.PSet(detSelection=cms.uint32(311),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1210b000")),      # BPix L1 ladder 11
    cms.PSet(detSelection=cms.uint32(312),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1210c000")),      # BPix L1 ladder 12
    cms.PSet(detSelection=cms.uint32(401),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12201000")),      # BPix L2 ladder 1
    cms.PSet(detSelection=cms.uint32(402),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12202000")),      # BPix L2 ladder 2
    cms.PSet(detSelection=cms.uint32(403),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12203000")),      # BPix L2 ladder 3
    cms.PSet(detSelection=cms.uint32(404),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12204000")),      # BPix L2 ladder 4
    cms.PSet(detSelection=cms.uint32(405),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12205000")),      # BPix L2 ladder 5
    cms.PSet(detSelection=cms.uint32(406),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12206000")),      # BPix L2 ladder 6
    cms.PSet(detSelection=cms.uint32(407),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12207000")),      # BPix L2 ladder 7
    cms.PSet(detSelection=cms.uint32(408),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12208000")),      # BPix L2 ladder 8
    cms.PSet(detSelection=cms.uint32(409),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12209000")),      # BPix L2 ladder 9
    cms.PSet(detSelection=cms.uint32(410),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220a000")),      # BPix L2 ladder 10
    cms.PSet(detSelection=cms.uint32(411),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220b000")),      # BPix L2 ladder 11
    cms.PSet(detSelection=cms.uint32(412),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220c000")),      # BPix L2 ladder 12
    cms.PSet(detSelection=cms.uint32(413),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220d000")),      # BPix L2 ladder 13
    cms.PSet(detSelection=cms.uint32(414),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220e000")),      # BPix L2 ladder 14
    cms.PSet(detSelection=cms.uint32(415),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1220f000")),      # BPix L2 ladder 15
    cms.PSet(detSelection=cms.uint32(416),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12210000")),      # BPix L2 ladder 16
    cms.PSet(detSelection=cms.uint32(417),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12211000")),      # BPix L2 ladder 17
    cms.PSet(detSelection=cms.uint32(418),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12212000")),      # BPix L2 ladder 18
    cms.PSet(detSelection=cms.uint32(419),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12213000")),      # BPix L2 ladder 19
    cms.PSet(detSelection=cms.uint32(420),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12214000")),      # BPix L2 ladder 20
    cms.PSet(detSelection=cms.uint32(421),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12215000")),      # BPix L2 ladder 21
    cms.PSet(detSelection=cms.uint32(422),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12216000")),      # BPix L2 ladder 22
    cms.PSet(detSelection=cms.uint32(423),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12217000")),      # BPix L2 ladder 23
    cms.PSet(detSelection=cms.uint32(424),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12218000")),      # BPix L2 ladder 24
    cms.PSet(detSelection=cms.uint32(425),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12219000")),      # BPix L2 ladder 25
    cms.PSet(detSelection=cms.uint32(426),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1221a000")),      # BPix L2 ladder 26
    cms.PSet(detSelection=cms.uint32(427),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1221b000")),      # BPix L2 ladder 27
    cms.PSet(detSelection=cms.uint32(428),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1221c000")),      # BPix L2 ladder 28
    cms.PSet(detSelection=cms.uint32(501),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12301000")),      # BPix L3 ladder 1
    cms.PSet(detSelection=cms.uint32(502),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12302000")),      # BPix L3 ladder 2
    cms.PSet(detSelection=cms.uint32(503),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12303000")),      # BPix L3 ladder 3
    cms.PSet(detSelection=cms.uint32(504),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12304000")),      # BPix L3 ladder 4
    cms.PSet(detSelection=cms.uint32(505),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12305000")),      # BPix L3 ladder 5
    cms.PSet(detSelection=cms.uint32(506),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12306000")),      # BPix L3 ladder 6
    cms.PSet(detSelection=cms.uint32(507),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12307000")),      # BPix L3 ladder 7
    cms.PSet(detSelection=cms.uint32(508),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12308000")),      # BPix L3 ladder 8
    cms.PSet(detSelection=cms.uint32(509),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12309000")),      # BPix L3 ladder 9
    cms.PSet(detSelection=cms.uint32(510),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230a000")),      # BPix L3 ladder 10
    cms.PSet(detSelection=cms.uint32(511),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230b000")),      # BPix L3 ladder 11
    cms.PSet(detSelection=cms.uint32(512),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230c000")),      # BPix L3 ladder 12
    cms.PSet(detSelection=cms.uint32(513),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230d000")),      # BPix L3 ladder 13
    cms.PSet(detSelection=cms.uint32(514),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230e000")),      # BPix L3 ladder 14
    cms.PSet(detSelection=cms.uint32(515),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1230f000")),      # BPix L3 ladder 15
    cms.PSet(detSelection=cms.uint32(516),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12310000")),      # BPix L3 ladder 16
    cms.PSet(detSelection=cms.uint32(517),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12311000")),      # BPix L3 ladder 17
    cms.PSet(detSelection=cms.uint32(518),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12312000")),      # BPix L3 ladder 18
    cms.PSet(detSelection=cms.uint32(519),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12313000")),      # BPix L3 ladder 19
    cms.PSet(detSelection=cms.uint32(520),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12314000")),      # BPix L3 ladder 20
    cms.PSet(detSelection=cms.uint32(521),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12315000")),      # BPix L3 ladder 21
    cms.PSet(detSelection=cms.uint32(522),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12316000")),      # BPix L3 ladder 22
    cms.PSet(detSelection=cms.uint32(523),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12317000")),      # BPix L3 ladder 23
    cms.PSet(detSelection=cms.uint32(524),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12318000")),      # BPix L3 ladder 24
    cms.PSet(detSelection=cms.uint32(525),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12319000")),      # BPix L3 ladder 25
    cms.PSet(detSelection=cms.uint32(526),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231a000")),      # BPix L3 ladder 26
    cms.PSet(detSelection=cms.uint32(527),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231b000")),      # BPix L3 ladder 27
    cms.PSet(detSelection=cms.uint32(528),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231c000")),      # BPix L3 ladder 28
    cms.PSet(detSelection=cms.uint32(529),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231d000")),      # BPix L3 ladder 29
    cms.PSet(detSelection=cms.uint32(530),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231e000")),      # BPix L3 ladder 30
    cms.PSet(detSelection=cms.uint32(531),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1231f000")),      # BPix L3 ladder 31
    cms.PSet(detSelection=cms.uint32(532),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12320000")),      # BPix L3 ladder 32
    cms.PSet(detSelection=cms.uint32(533),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12321000")),      # BPix L3 ladder 33
    cms.PSet(detSelection=cms.uint32(534),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12322000")),      # BPix L3 ladder 34
    cms.PSet(detSelection=cms.uint32(535),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12323000")),      # BPix L3 ladder 35
    cms.PSet(detSelection=cms.uint32(536),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12324000")),      # BPix L3 ladder 36
    cms.PSet(detSelection=cms.uint32(537),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12325000")),      # BPix L3 ladder 37
    cms.PSet(detSelection=cms.uint32(538),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12326000")),      # BPix L3 ladder 38
    cms.PSet(detSelection=cms.uint32(539),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12327000")),      # BPix L3 ladder 39
    cms.PSet(detSelection=cms.uint32(540),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12328000")),      # BPix L3 ladder 40
    cms.PSet(detSelection=cms.uint32(541),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12329000")),      # BPix L3 ladder 41
    cms.PSet(detSelection=cms.uint32(542),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1232a000")),      # BPix L3 ladder 42
    cms.PSet(detSelection=cms.uint32(543),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1232b000")),      # BPix L3 ladder 43
    cms.PSet(detSelection=cms.uint32(544),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1232c000")),      # BPix L3 ladder 44
    cms.PSet(detSelection=cms.uint32(601),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12401000")),      # BPix L4 ladder 1
    cms.PSet(detSelection=cms.uint32(602),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12402000")),      # BPix L4 ladder 2
    cms.PSet(detSelection=cms.uint32(603),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12403000")),      # BPix L4 ladder 3
    cms.PSet(detSelection=cms.uint32(604),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12404000")),      # BPix L4 ladder 4
    cms.PSet(detSelection=cms.uint32(605),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12405000")),      # BPix L4 ladder 5
    cms.PSet(detSelection=cms.uint32(606),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12406000")),      # BPix L4 ladder 6
    cms.PSet(detSelection=cms.uint32(607),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12407000")),      # BPix L4 ladder 7
    cms.PSet(detSelection=cms.uint32(608),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12408000")),      # BPix L4 ladder 8
    cms.PSet(detSelection=cms.uint32(609),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12409000")),      # BPix L4 ladder 9
    cms.PSet(detSelection=cms.uint32(610),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240a000")),      # BPix L4 ladder 10
    cms.PSet(detSelection=cms.uint32(611),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240b000")),      # BPix L4 ladder 11
    cms.PSet(detSelection=cms.uint32(612),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240c000")),      # BPix L4 ladder 12
    cms.PSet(detSelection=cms.uint32(613),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240d000")),      # BPix L4 ladder 13
    cms.PSet(detSelection=cms.uint32(614),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240e000")),      # BPix L4 ladder 14
    cms.PSet(detSelection=cms.uint32(615),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1240f000")),      # BPix L4 ladder 15
    cms.PSet(detSelection=cms.uint32(616),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12410000")),      # BPix L4 ladder 16
    cms.PSet(detSelection=cms.uint32(617),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12411000")),      # BPix L4 ladder 17
    cms.PSet(detSelection=cms.uint32(618),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12412000")),      # BPix L4 ladder 18
    cms.PSet(detSelection=cms.uint32(619),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12413000")),      # BPix L4 ladder 19
    cms.PSet(detSelection=cms.uint32(620),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12414000")),      # BPix L4 ladder 20
    cms.PSet(detSelection=cms.uint32(621),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12415000")),      # BPix L4 ladder 21
    cms.PSet(detSelection=cms.uint32(622),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12416000")),      # BPix L4 ladder 22
    cms.PSet(detSelection=cms.uint32(623),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12417000")),      # BPix L4 ladder 23
    cms.PSet(detSelection=cms.uint32(624),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12418000")),      # BPix L4 ladder 24
    cms.PSet(detSelection=cms.uint32(625),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12419000")),      # BPix L4 ladder 25
    cms.PSet(detSelection=cms.uint32(626),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241a000")),      # BPix L4 ladder 26
    cms.PSet(detSelection=cms.uint32(627),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241b000")),      # BPix L4 ladder 27
    cms.PSet(detSelection=cms.uint32(628),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241c000")),      # BPix L4 ladder 28
    cms.PSet(detSelection=cms.uint32(629),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241d000")),      # BPix L4 ladder 29
    cms.PSet(detSelection=cms.uint32(630),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241e000")),      # BPix L4 ladder 30
    cms.PSet(detSelection=cms.uint32(631),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1241f000")),      # BPix L4 ladder 31
    cms.PSet(detSelection=cms.uint32(632),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12420000")),      # BPix L4 ladder 32
    cms.PSet(detSelection=cms.uint32(633),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12421000")),      # BPix L4 ladder 33
    cms.PSet(detSelection=cms.uint32(634),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12422000")),      # BPix L4 ladder 34
    cms.PSet(detSelection=cms.uint32(635),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12423000")),      # BPix L4 ladder 35
    cms.PSet(detSelection=cms.uint32(636),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12424000")),      # BPix L4 ladder 36
    cms.PSet(detSelection=cms.uint32(637),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12425000")),      # BPix L4 ladder 37
    cms.PSet(detSelection=cms.uint32(638),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12426000")),      # BPix L4 ladder 38
    cms.PSet(detSelection=cms.uint32(639),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12427000")),      # BPix L4 ladder 39
    cms.PSet(detSelection=cms.uint32(640),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12428000")),      # BPix L4 ladder 40
    cms.PSet(detSelection=cms.uint32(641),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12429000")),      # BPix L4 ladder 41
    cms.PSet(detSelection=cms.uint32(642),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242a000")),      # BPix L4 ladder 42
    cms.PSet(detSelection=cms.uint32(643),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242b000")),      # BPix L4 ladder 43
    cms.PSet(detSelection=cms.uint32(644),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242c000")),      # BPix L4 ladder 44
    cms.PSet(detSelection=cms.uint32(645),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242d000")),      # BPix L4 ladder 45
    cms.PSet(detSelection=cms.uint32(646),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242e000")),      # BPix L4 ladder 46
    cms.PSet(detSelection=cms.uint32(647),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1242f000")),      # BPix L4 ladder 47
    cms.PSet(detSelection=cms.uint32(648),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12430000")),      # BPix L4 ladder 48
    cms.PSet(detSelection=cms.uint32(649),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12431000")),      # BPix L4 ladder 49
    cms.PSet(detSelection=cms.uint32(650),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12432000")),      # BPix L4 ladder 50
    cms.PSet(detSelection=cms.uint32(651),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12433000")),      # BPix L4 ladder 51
    cms.PSet(detSelection=cms.uint32(652),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12434000")),      # BPix L4 ladder 52
    cms.PSet(detSelection=cms.uint32(653),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12435000")),      # BPix L4 ladder 53
    cms.PSet(detSelection=cms.uint32(654),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12436000")),      # BPix L4 ladder 54
    cms.PSet(detSelection=cms.uint32(655),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12437000")),      # BPix L4 ladder 55
    cms.PSet(detSelection=cms.uint32(656),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12438000")),      # BPix L4 ladder 56
    cms.PSet(detSelection=cms.uint32(657),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12439000")),      # BPix L4 ladder 57
    cms.PSet(detSelection=cms.uint32(658),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243a000")),      # BPix L4 ladder 58
    cms.PSet(detSelection=cms.uint32(659),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243b000")),      # BPix L4 ladder 59
    cms.PSet(detSelection=cms.uint32(660),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243c000")),      # BPix L4 ladder 60
    cms.PSet(detSelection=cms.uint32(661),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243d000")),      # BPix L4 ladder 61
    cms.PSet(detSelection=cms.uint32(662),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243e000")),      # BPix L4 ladder 62
    cms.PSet(detSelection=cms.uint32(663),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x1243f000")),      # BPix L4 ladder 63
    cms.PSet(detSelection=cms.uint32(664),detLabel=cms.string("Dummy"),selection=cms.untracked.vstring("0x1efff000-0x12440000")),      # BPix L4 ladder 64
)
OccupancyPlotsFPIXmD1DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(1),detLabel = cms.string("FPIXmD1R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14841400")),
    cms.PSet(detSelection = cms.uint32(2),detLabel = cms.string("FPIXmD1R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14842400")),
    cms.PSet(detSelection = cms.uint32(3),detLabel = cms.string("FPIXmD1R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14843400")),
    cms.PSet(detSelection = cms.uint32(4),detLabel = cms.string("FPIXmD1R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14844400")),
    cms.PSet(detSelection = cms.uint32(5),detLabel = cms.string("FPIXmD1R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14845400")),
    cms.PSet(detSelection = cms.uint32(6),detLabel = cms.string("FPIXmD1R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14846400")),
    cms.PSet(detSelection = cms.uint32(7),detLabel = cms.string("FPIXmD1R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14847400")),
    cms.PSet(detSelection = cms.uint32(8),detLabel = cms.string("FPIXmD1R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14848400")),
    cms.PSet(detSelection = cms.uint32(9),detLabel = cms.string("FPIXmD1R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14849400")),
    cms.PSet(detSelection = cms.uint32(10),detLabel = cms.string("FPIXmD1R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484a400")),
    cms.PSet(detSelection = cms.uint32(11),detLabel = cms.string("FPIXmD1R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484b400")),
    cms.PSet(detSelection = cms.uint32(12),detLabel = cms.string("FPIXmD1R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484c400")),
    cms.PSet(detSelection = cms.uint32(13),detLabel = cms.string("FPIXmD1R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484d400")),
    cms.PSet(detSelection = cms.uint32(14),detLabel = cms.string("FPIXmD1R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484e400")),
    cms.PSet(detSelection = cms.uint32(15),detLabel = cms.string("FPIXmD1R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1484f400")),
    cms.PSet(detSelection = cms.uint32(16),detLabel = cms.string("FPIXmD1R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14850400")),
    cms.PSet(detSelection = cms.uint32(17),detLabel = cms.string("FPIXmD1R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14851400")),
    cms.PSet(detSelection = cms.uint32(18),detLabel = cms.string("FPIXmD1R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14852400")),
    cms.PSet(detSelection = cms.uint32(19),detLabel = cms.string("FPIXmD1R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14853400")),
    cms.PSet(detSelection = cms.uint32(20),detLabel = cms.string("FPIXmD1R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14854400")),
    cms.PSet(detSelection = cms.uint32(21),detLabel = cms.string("FPIXmD1R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14855400")),
    cms.PSet(detSelection = cms.uint32(22),detLabel = cms.string("FPIXmD1R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14856400")),
    cms.PSet(detSelection = cms.uint32(23),detLabel = cms.string("FPIXmD1R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14857400")),
    cms.PSet(detSelection = cms.uint32(24),detLabel = cms.string("FPIXmD1R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14858400")),
    cms.PSet(detSelection = cms.uint32(25),detLabel = cms.string("FPIXmD1R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14859400")),
    cms.PSet(detSelection = cms.uint32(26),detLabel = cms.string("FPIXmD1R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485a400")),
    cms.PSet(detSelection = cms.uint32(27),detLabel = cms.string("FPIXmD1R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485b400")),
    cms.PSet(detSelection = cms.uint32(28),detLabel = cms.string("FPIXmD1R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485c400")),
    cms.PSet(detSelection = cms.uint32(29),detLabel = cms.string("FPIXmD1R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485d400")),
    cms.PSet(detSelection = cms.uint32(30),detLabel = cms.string("FPIXmD1R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485e400")),
    cms.PSet(detSelection = cms.uint32(31),detLabel = cms.string("FPIXmD1R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1485f400")),
    cms.PSet(detSelection = cms.uint32(32),detLabel = cms.string("FPIXmD1R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14860400")),
    cms.PSet(detSelection = cms.uint32(33),detLabel = cms.string("FPIXmD1R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14861400")),
    cms.PSet(detSelection = cms.uint32(34),detLabel = cms.string("FPIXmD1R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14862400")),
    cms.PSet(detSelection = cms.uint32(35),detLabel = cms.string("FPIXmD1R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14863400")),
    cms.PSet(detSelection = cms.uint32(36),detLabel = cms.string("FPIXmD1R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14864400")),
    cms.PSet(detSelection = cms.uint32(37),detLabel = cms.string("FPIXmD1R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14865400")),
    cms.PSet(detSelection = cms.uint32(38),detLabel = cms.string("FPIXmD1R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14866400")),
    cms.PSet(detSelection = cms.uint32(39),detLabel = cms.string("FPIXmD1R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14867400")),
    cms.PSet(detSelection = cms.uint32(40),detLabel = cms.string("FPIXmD1R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14868400")),
    cms.PSet(detSelection = cms.uint32(41),detLabel = cms.string("FPIXmD1R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14869400")),
    cms.PSet(detSelection = cms.uint32(42),detLabel = cms.string("FPIXmD1R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486a400")),
    cms.PSet(detSelection = cms.uint32(43),detLabel = cms.string("FPIXmD1R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486b400")),
    cms.PSet(detSelection = cms.uint32(44),detLabel = cms.string("FPIXmD1R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486c400")),
    cms.PSet(detSelection = cms.uint32(45),detLabel = cms.string("FPIXmD1R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486d400")),
    cms.PSet(detSelection = cms.uint32(46),detLabel = cms.string("FPIXmD1R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486e400")),
    cms.PSet(detSelection = cms.uint32(47),detLabel = cms.string("FPIXmD1R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1486f400")),
    cms.PSet(detSelection = cms.uint32(48),detLabel = cms.string("FPIXmD1R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14870400")),
    cms.PSet(detSelection = cms.uint32(49),detLabel = cms.string("FPIXmD1R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14871400")),
    cms.PSet(detSelection = cms.uint32(50),detLabel = cms.string("FPIXmD1R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14872400")),
    cms.PSet(detSelection = cms.uint32(51),detLabel = cms.string("FPIXmD1R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14873400")),
    cms.PSet(detSelection = cms.uint32(52),detLabel = cms.string("FPIXmD1R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14874400")),
    cms.PSet(detSelection = cms.uint32(53),detLabel = cms.string("FPIXmD1R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14875400")),
    cms.PSet(detSelection = cms.uint32(54),detLabel = cms.string("FPIXmD1R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14876400")),
    cms.PSet(detSelection = cms.uint32(55),detLabel = cms.string("FPIXmD1R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14877400")),
    cms.PSet(detSelection = cms.uint32(56),detLabel = cms.string("FPIXmD1R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14878400")),
#
    cms.PSet(detSelection = cms.uint32(101),detLabel = cms.string("FPIXmD1R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14841800")),
    cms.PSet(detSelection = cms.uint32(102),detLabel = cms.string("FPIXmD1R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14842800")),
    cms.PSet(detSelection = cms.uint32(103),detLabel = cms.string("FPIXmD1R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14843800")),
    cms.PSet(detSelection = cms.uint32(104),detLabel = cms.string("FPIXmD1R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14844800")),
    cms.PSet(detSelection = cms.uint32(105),detLabel = cms.string("FPIXmD1R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14845800")),
    cms.PSet(detSelection = cms.uint32(106),detLabel = cms.string("FPIXmD1R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14846800")),
    cms.PSet(detSelection = cms.uint32(107),detLabel = cms.string("FPIXmD1R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14847800")),
    cms.PSet(detSelection = cms.uint32(108),detLabel = cms.string("FPIXmD1R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14848800")),
    cms.PSet(detSelection = cms.uint32(109),detLabel = cms.string("FPIXmD1R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14849800")),
    cms.PSet(detSelection = cms.uint32(110),detLabel = cms.string("FPIXmD1R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484a800")),
    cms.PSet(detSelection = cms.uint32(111),detLabel = cms.string("FPIXmD1R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484b800")),
    cms.PSet(detSelection = cms.uint32(112),detLabel = cms.string("FPIXmD1R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484c800")),
    cms.PSet(detSelection = cms.uint32(113),detLabel = cms.string("FPIXmD1R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484d800")),
    cms.PSet(detSelection = cms.uint32(114),detLabel = cms.string("FPIXmD1R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484e800")),
    cms.PSet(detSelection = cms.uint32(115),detLabel = cms.string("FPIXmD1R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1484f800")),
    cms.PSet(detSelection = cms.uint32(116),detLabel = cms.string("FPIXmD1R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14850800")),
    cms.PSet(detSelection = cms.uint32(117),detLabel = cms.string("FPIXmD1R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14851800")),
    cms.PSet(detSelection = cms.uint32(118),detLabel = cms.string("FPIXmD1R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14852800")),
    cms.PSet(detSelection = cms.uint32(119),detLabel = cms.string("FPIXmD1R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14853800")),
    cms.PSet(detSelection = cms.uint32(120),detLabel = cms.string("FPIXmD1R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14854800")),
    cms.PSet(detSelection = cms.uint32(121),detLabel = cms.string("FPIXmD1R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14855800")),
    cms.PSet(detSelection = cms.uint32(122),detLabel = cms.string("FPIXmD1R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14856800")),
    cms.PSet(detSelection = cms.uint32(123),detLabel = cms.string("FPIXmD1R1m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14857800")),
    cms.PSet(detSelection = cms.uint32(124),detLabel = cms.string("FPIXmD1R1m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14858800")),
    cms.PSet(detSelection = cms.uint32(125),detLabel = cms.string("FPIXmD1R1m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14859800")),
    cms.PSet(detSelection = cms.uint32(126),detLabel = cms.string("FPIXmD1R1m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485a800")),
    cms.PSet(detSelection = cms.uint32(127),detLabel = cms.string("FPIXmD1R1m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485b800")),
    cms.PSet(detSelection = cms.uint32(128),detLabel = cms.string("FPIXmD1R1m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485c800")),
    cms.PSet(detSelection = cms.uint32(129),detLabel = cms.string("FPIXmD1R1m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485d800")),
    cms.PSet(detSelection = cms.uint32(130),detLabel = cms.string("FPIXmD1R1m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485e800")),
    cms.PSet(detSelection = cms.uint32(131),detLabel = cms.string("FPIXmD1R1m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1485f800")),
    cms.PSet(detSelection = cms.uint32(132),detLabel = cms.string("FPIXmD1R1m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14860800")),
    cms.PSet(detSelection = cms.uint32(133),detLabel = cms.string("FPIXmD1R1m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14861800")),
    cms.PSet(detSelection = cms.uint32(134),detLabel = cms.string("FPIXmD1R1m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14862800")),
    cms.PSet(detSelection = cms.uint32(135),detLabel = cms.string("FPIXmD1R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14863800")),
    cms.PSet(detSelection = cms.uint32(136),detLabel = cms.string("FPIXmD1R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14864800")),
    cms.PSet(detSelection = cms.uint32(137),detLabel = cms.string("FPIXmD1R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14865800")),
    cms.PSet(detSelection = cms.uint32(138),detLabel = cms.string("FPIXmD1R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14866800")),
    cms.PSet(detSelection = cms.uint32(139),detLabel = cms.string("FPIXmD1R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14867800")),
    cms.PSet(detSelection = cms.uint32(140),detLabel = cms.string("FPIXmD1R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14868800")),
    cms.PSet(detSelection = cms.uint32(141),detLabel = cms.string("FPIXmD1R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14869800")),
    cms.PSet(detSelection = cms.uint32(142),detLabel = cms.string("FPIXmD1R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486a800")),
    cms.PSet(detSelection = cms.uint32(143),detLabel = cms.string("FPIXmD1R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486b800")),
    cms.PSet(detSelection = cms.uint32(144),detLabel = cms.string("FPIXmD1R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486c800")),
    cms.PSet(detSelection = cms.uint32(145),detLabel = cms.string("FPIXmD1R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486d800")),
    cms.PSet(detSelection = cms.uint32(146),detLabel = cms.string("FPIXmD1R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486e800")),
    cms.PSet(detSelection = cms.uint32(147),detLabel = cms.string("FPIXmD1R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1486f800")),
    cms.PSet(detSelection = cms.uint32(148),detLabel = cms.string("FPIXmD1R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14870800")),
    cms.PSet(detSelection = cms.uint32(149),detLabel = cms.string("FPIXmD1R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14871800")),
    cms.PSet(detSelection = cms.uint32(150),detLabel = cms.string("FPIXmD1R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14872800")),
    cms.PSet(detSelection = cms.uint32(151),detLabel = cms.string("FPIXmD1R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14873800")),
    cms.PSet(detSelection = cms.uint32(152),detLabel = cms.string("FPIXmD1R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14874800")),
    cms.PSet(detSelection = cms.uint32(153),detLabel = cms.string("FPIXmD1R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14875800")),
    cms.PSet(detSelection = cms.uint32(154),detLabel = cms.string("FPIXmD1R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14876800")),
    cms.PSet(detSelection = cms.uint32(155),detLabel = cms.string("FPIXmD1R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14877800")),
    cms.PSet(detSelection = cms.uint32(156),detLabel = cms.string("FPIXmD1R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14878800")),
)
#
OccupancyPlotsFPIXmD2DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(201),detLabel = cms.string("FPIXmD2R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14881400")),
    cms.PSet(detSelection = cms.uint32(202),detLabel = cms.string("FPIXmD2R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14882400")),
    cms.PSet(detSelection = cms.uint32(203),detLabel = cms.string("FPIXmD2R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14883400")),
    cms.PSet(detSelection = cms.uint32(204),detLabel = cms.string("FPIXmD2R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14884400")),
    cms.PSet(detSelection = cms.uint32(205),detLabel = cms.string("FPIXmD2R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14885400")),
    cms.PSet(detSelection = cms.uint32(206),detLabel = cms.string("FPIXmD2R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14886400")),
    cms.PSet(detSelection = cms.uint32(207),detLabel = cms.string("FPIXmD2R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14887400")),
    cms.PSet(detSelection = cms.uint32(208),detLabel = cms.string("FPIXmD2R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14888400")),
    cms.PSet(detSelection = cms.uint32(209),detLabel = cms.string("FPIXmD2R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14889400")),
    cms.PSet(detSelection = cms.uint32(210),detLabel = cms.string("FPIXmD2R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488a400")),
    cms.PSet(detSelection = cms.uint32(211),detLabel = cms.string("FPIXmD2R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488b400")),
    cms.PSet(detSelection = cms.uint32(212),detLabel = cms.string("FPIXmD2R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488c400")),
    cms.PSet(detSelection = cms.uint32(213),detLabel = cms.string("FPIXmD2R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488d400")),
    cms.PSet(detSelection = cms.uint32(214),detLabel = cms.string("FPIXmD2R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488e400")),
    cms.PSet(detSelection = cms.uint32(215),detLabel = cms.string("FPIXmD2R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1488f400")),
    cms.PSet(detSelection = cms.uint32(216),detLabel = cms.string("FPIXmD2R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14890400")),
    cms.PSet(detSelection = cms.uint32(217),detLabel = cms.string("FPIXmD2R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14891400")),
    cms.PSet(detSelection = cms.uint32(218),detLabel = cms.string("FPIXmD2R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14892400")),
    cms.PSet(detSelection = cms.uint32(219),detLabel = cms.string("FPIXmD2R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14893400")),
    cms.PSet(detSelection = cms.uint32(220),detLabel = cms.string("FPIXmD2R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14894400")),
    cms.PSet(detSelection = cms.uint32(221),detLabel = cms.string("FPIXmD2R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14895400")),
    cms.PSet(detSelection = cms.uint32(222),detLabel = cms.string("FPIXmD2R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14896400")),
    cms.PSet(detSelection = cms.uint32(223),detLabel = cms.string("FPIXmD2R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14897400")),
    cms.PSet(detSelection = cms.uint32(224),detLabel = cms.string("FPIXmD2R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14898400")),
    cms.PSet(detSelection = cms.uint32(225),detLabel = cms.string("FPIXmD2R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x14899400")),
    cms.PSet(detSelection = cms.uint32(226),detLabel = cms.string("FPIXmD2R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489a400")),
    cms.PSet(detSelection = cms.uint32(227),detLabel = cms.string("FPIXmD2R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489b400")),
    cms.PSet(detSelection = cms.uint32(228),detLabel = cms.string("FPIXmD2R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489c400")),
    cms.PSet(detSelection = cms.uint32(229),detLabel = cms.string("FPIXmD2R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489d400")),
    cms.PSet(detSelection = cms.uint32(230),detLabel = cms.string("FPIXmD2R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489e400")),
    cms.PSet(detSelection = cms.uint32(231),detLabel = cms.string("FPIXmD2R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1489f400")),
    cms.PSet(detSelection = cms.uint32(232),detLabel = cms.string("FPIXmD2R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a0400")),
    cms.PSet(detSelection = cms.uint32(233),detLabel = cms.string("FPIXmD2R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a1400")),
    cms.PSet(detSelection = cms.uint32(234),detLabel = cms.string("FPIXmD2R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a2400")),
    cms.PSet(detSelection = cms.uint32(235),detLabel = cms.string("FPIXmD2R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a3400")),
    cms.PSet(detSelection = cms.uint32(236),detLabel = cms.string("FPIXmD2R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a4400")),
    cms.PSet(detSelection = cms.uint32(237),detLabel = cms.string("FPIXmD2R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a5400")),
    cms.PSet(detSelection = cms.uint32(238),detLabel = cms.string("FPIXmD2R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a6400")),
    cms.PSet(detSelection = cms.uint32(239),detLabel = cms.string("FPIXmD2R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a7400")),
    cms.PSet(detSelection = cms.uint32(240),detLabel = cms.string("FPIXmD2R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a8400")),
    cms.PSet(detSelection = cms.uint32(241),detLabel = cms.string("FPIXmD2R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148a9400")),
    cms.PSet(detSelection = cms.uint32(242),detLabel = cms.string("FPIXmD2R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148aa400")),
    cms.PSet(detSelection = cms.uint32(243),detLabel = cms.string("FPIXmD2R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ab400")),
    cms.PSet(detSelection = cms.uint32(244),detLabel = cms.string("FPIXmD2R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ac400")),
    cms.PSet(detSelection = cms.uint32(245),detLabel = cms.string("FPIXmD2R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ad400")),
    cms.PSet(detSelection = cms.uint32(246),detLabel = cms.string("FPIXmD2R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ae400")),
    cms.PSet(detSelection = cms.uint32(247),detLabel = cms.string("FPIXmD2R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148af400")),
    cms.PSet(detSelection = cms.uint32(248),detLabel = cms.string("FPIXmD2R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b0400")),
    cms.PSet(detSelection = cms.uint32(249),detLabel = cms.string("FPIXmD2R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b1400")),
    cms.PSet(detSelection = cms.uint32(250),detLabel = cms.string("FPIXmD2R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b2400")),
    cms.PSet(detSelection = cms.uint32(251),detLabel = cms.string("FPIXmD2R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b3400")),
    cms.PSet(detSelection = cms.uint32(252),detLabel = cms.string("FPIXmD2R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b4400")),
    cms.PSet(detSelection = cms.uint32(253),detLabel = cms.string("FPIXmD2R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b5400")),
    cms.PSet(detSelection = cms.uint32(254),detLabel = cms.string("FPIXmD2R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b6400")),
    cms.PSet(detSelection = cms.uint32(255),detLabel = cms.string("FPIXmD2R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b7400")),
    cms.PSet(detSelection = cms.uint32(256),detLabel = cms.string("FPIXmD2R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148b8400")),
#
    cms.PSet(detSelection = cms.uint32(301),detLabel = cms.string("FPIXmD2R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14881800")),
    cms.PSet(detSelection = cms.uint32(302),detLabel = cms.string("FPIXmD2R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14882800")),
    cms.PSet(detSelection = cms.uint32(303),detLabel = cms.string("FPIXmD2R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14883800")),
    cms.PSet(detSelection = cms.uint32(304),detLabel = cms.string("FPIXmD2R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14884800")),
    cms.PSet(detSelection = cms.uint32(305),detLabel = cms.string("FPIXmD2R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14885800")),
    cms.PSet(detSelection = cms.uint32(306),detLabel = cms.string("FPIXmD2R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14886800")),
    cms.PSet(detSelection = cms.uint32(307),detLabel = cms.string("FPIXmD2R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14887800")),
    cms.PSet(detSelection = cms.uint32(308),detLabel = cms.string("FPIXmD2R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14888800")),
    cms.PSet(detSelection = cms.uint32(309),detLabel = cms.string("FPIXmD2R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14889800")),
    cms.PSet(detSelection = cms.uint32(310),detLabel = cms.string("FPIXmD2R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488a800")),
    cms.PSet(detSelection = cms.uint32(311),detLabel = cms.string("FPIXmD2R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488b800")),
    cms.PSet(detSelection = cms.uint32(312),detLabel = cms.string("FPIXmD2R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488c800")),
    cms.PSet(detSelection = cms.uint32(313),detLabel = cms.string("FPIXmD2R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488d800")),
    cms.PSet(detSelection = cms.uint32(314),detLabel = cms.string("FPIXmD2R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488e800")),
    cms.PSet(detSelection = cms.uint32(315),detLabel = cms.string("FPIXmD2R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1488f800")),
    cms.PSet(detSelection = cms.uint32(316),detLabel = cms.string("FPIXmD2R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14890800")),
    cms.PSet(detSelection = cms.uint32(317),detLabel = cms.string("FPIXmD2R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14891800")),
    cms.PSet(detSelection = cms.uint32(318),detLabel = cms.string("FPIXmD2R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14892800")),
    cms.PSet(detSelection = cms.uint32(319),detLabel = cms.string("FPIXmD2R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14893800")),
    cms.PSet(detSelection = cms.uint32(320),detLabel = cms.string("FPIXmD2R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14894800")),
    cms.PSet(detSelection = cms.uint32(321),detLabel = cms.string("FPIXmD2R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14895800")),
    cms.PSet(detSelection = cms.uint32(322),detLabel = cms.string("FPIXmD2R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14896800")),
    cms.PSet(detSelection = cms.uint32(323),detLabel = cms.string("FPIXmD2R1m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14897800")),
    cms.PSet(detSelection = cms.uint32(324),detLabel = cms.string("FPIXmD2R1m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14898800")),
    cms.PSet(detSelection = cms.uint32(325),detLabel = cms.string("FPIXmD2R1m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x14899800")),
    cms.PSet(detSelection = cms.uint32(326),detLabel = cms.string("FPIXmD2R1m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489a800")),
    cms.PSet(detSelection = cms.uint32(327),detLabel = cms.string("FPIXmD2R1m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489b800")),
    cms.PSet(detSelection = cms.uint32(328),detLabel = cms.string("FPIXmD2R1m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489c800")),
    cms.PSet(detSelection = cms.uint32(329),detLabel = cms.string("FPIXmD2R1m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489d800")),
    cms.PSet(detSelection = cms.uint32(330),detLabel = cms.string("FPIXmD2R1m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489e800")),
    cms.PSet(detSelection = cms.uint32(331),detLabel = cms.string("FPIXmD2R1m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1489f800")),
    cms.PSet(detSelection = cms.uint32(332),detLabel = cms.string("FPIXmD2R1m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a0800")),
    cms.PSet(detSelection = cms.uint32(333),detLabel = cms.string("FPIXmD2R1m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a1800")),
    cms.PSet(detSelection = cms.uint32(334),detLabel = cms.string("FPIXmD2R1m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a2800")),
    cms.PSet(detSelection = cms.uint32(335),detLabel = cms.string("FPIXmD2R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a3800")),
    cms.PSet(detSelection = cms.uint32(336),detLabel = cms.string("FPIXmD2R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a4800")),
    cms.PSet(detSelection = cms.uint32(337),detLabel = cms.string("FPIXmD2R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a5800")),
    cms.PSet(detSelection = cms.uint32(338),detLabel = cms.string("FPIXmD2R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a6800")),
    cms.PSet(detSelection = cms.uint32(339),detLabel = cms.string("FPIXmD2R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a7800")),
    cms.PSet(detSelection = cms.uint32(340),detLabel = cms.string("FPIXmD2R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a8800")),
    cms.PSet(detSelection = cms.uint32(341),detLabel = cms.string("FPIXmD2R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148a9800")),
    cms.PSet(detSelection = cms.uint32(342),detLabel = cms.string("FPIXmD2R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148aa800")),
    cms.PSet(detSelection = cms.uint32(343),detLabel = cms.string("FPIXmD2R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ab800")),
    cms.PSet(detSelection = cms.uint32(344),detLabel = cms.string("FPIXmD2R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ac800")),
    cms.PSet(detSelection = cms.uint32(345),detLabel = cms.string("FPIXmD2R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ad800")),
    cms.PSet(detSelection = cms.uint32(346),detLabel = cms.string("FPIXmD2R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ae800")),
    cms.PSet(detSelection = cms.uint32(347),detLabel = cms.string("FPIXmD2R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148af800")),
    cms.PSet(detSelection = cms.uint32(348),detLabel = cms.string("FPIXmD2R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b0800")),
    cms.PSet(detSelection = cms.uint32(349),detLabel = cms.string("FPIXmD2R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b1800")),
    cms.PSet(detSelection = cms.uint32(350),detLabel = cms.string("FPIXmD2R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b2800")),
    cms.PSet(detSelection = cms.uint32(351),detLabel = cms.string("FPIXmD2R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b3800")),
    cms.PSet(detSelection = cms.uint32(352),detLabel = cms.string("FPIXmD2R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b4800")),
    cms.PSet(detSelection = cms.uint32(353),detLabel = cms.string("FPIXmD2R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b5800")),
    cms.PSet(detSelection = cms.uint32(354),detLabel = cms.string("FPIXmD2R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b6800")),
    cms.PSet(detSelection = cms.uint32(355),detLabel = cms.string("FPIXmD2R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b7800")),
    cms.PSet(detSelection = cms.uint32(356),detLabel = cms.string("FPIXmD2R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148b8800")),
)
#
OccupancyPlotsFPIXmD3DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(401),detLabel = cms.string("FPIXmD3R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c1400")),
    cms.PSet(detSelection = cms.uint32(402),detLabel = cms.string("FPIXmD3R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c2400")),
    cms.PSet(detSelection = cms.uint32(403),detLabel = cms.string("FPIXmD3R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c3400")),
    cms.PSet(detSelection = cms.uint32(404),detLabel = cms.string("FPIXmD3R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c4400")),
    cms.PSet(detSelection = cms.uint32(405),detLabel = cms.string("FPIXmD3R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c5400")),
    cms.PSet(detSelection = cms.uint32(406),detLabel = cms.string("FPIXmD3R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c6400")),
    cms.PSet(detSelection = cms.uint32(407),detLabel = cms.string("FPIXmD3R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c7400")),
    cms.PSet(detSelection = cms.uint32(408),detLabel = cms.string("FPIXmD3R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c8400")),
    cms.PSet(detSelection = cms.uint32(409),detLabel = cms.string("FPIXmD3R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148c9400")),
    cms.PSet(detSelection = cms.uint32(410),detLabel = cms.string("FPIXmD3R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ca400")),
    cms.PSet(detSelection = cms.uint32(411),detLabel = cms.string("FPIXmD3R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148cb400")),
    cms.PSet(detSelection = cms.uint32(412),detLabel = cms.string("FPIXmD3R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148cc400")),
    cms.PSet(detSelection = cms.uint32(413),detLabel = cms.string("FPIXmD3R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148cd400")),
    cms.PSet(detSelection = cms.uint32(414),detLabel = cms.string("FPIXmD3R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ce400")),
    cms.PSet(detSelection = cms.uint32(415),detLabel = cms.string("FPIXmD3R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148cf400")),
    cms.PSet(detSelection = cms.uint32(416),detLabel = cms.string("FPIXmD3R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d0400")),
    cms.PSet(detSelection = cms.uint32(417),detLabel = cms.string("FPIXmD3R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d1400")),
    cms.PSet(detSelection = cms.uint32(418),detLabel = cms.string("FPIXmD3R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d2400")),
    cms.PSet(detSelection = cms.uint32(419),detLabel = cms.string("FPIXmD3R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d3400")),
    cms.PSet(detSelection = cms.uint32(420),detLabel = cms.string("FPIXmD3R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d4400")),
    cms.PSet(detSelection = cms.uint32(421),detLabel = cms.string("FPIXmD3R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d5400")),
    cms.PSet(detSelection = cms.uint32(422),detLabel = cms.string("FPIXmD3R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d6400")),
    cms.PSet(detSelection = cms.uint32(423),detLabel = cms.string("FPIXmD3R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d7400")),
    cms.PSet(detSelection = cms.uint32(424),detLabel = cms.string("FPIXmD3R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d8400")),
    cms.PSet(detSelection = cms.uint32(425),detLabel = cms.string("FPIXmD3R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148d9400")),
    cms.PSet(detSelection = cms.uint32(426),detLabel = cms.string("FPIXmD3R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148da400")),
    cms.PSet(detSelection = cms.uint32(427),detLabel = cms.string("FPIXmD3R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148db400")),
    cms.PSet(detSelection = cms.uint32(428),detLabel = cms.string("FPIXmD3R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148dc400")),
    cms.PSet(detSelection = cms.uint32(429),detLabel = cms.string("FPIXmD3R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148dd400")),
    cms.PSet(detSelection = cms.uint32(430),detLabel = cms.string("FPIXmD3R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148de400")),
    cms.PSet(detSelection = cms.uint32(431),detLabel = cms.string("FPIXmD3R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148df400")),
    cms.PSet(detSelection = cms.uint32(432),detLabel = cms.string("FPIXmD3R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e0400")),
    cms.PSet(detSelection = cms.uint32(433),detLabel = cms.string("FPIXmD3R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e1400")),
    cms.PSet(detSelection = cms.uint32(434),detLabel = cms.string("FPIXmD3R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e2400")),
    cms.PSet(detSelection = cms.uint32(435),detLabel = cms.string("FPIXmD3R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e3400")),
    cms.PSet(detSelection = cms.uint32(436),detLabel = cms.string("FPIXmD3R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e4400")),
    cms.PSet(detSelection = cms.uint32(437),detLabel = cms.string("FPIXmD3R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e5400")),
    cms.PSet(detSelection = cms.uint32(438),detLabel = cms.string("FPIXmD3R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e6400")),
    cms.PSet(detSelection = cms.uint32(439),detLabel = cms.string("FPIXmD3R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e7400")),
    cms.PSet(detSelection = cms.uint32(440),detLabel = cms.string("FPIXmD3R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e8400")),
    cms.PSet(detSelection = cms.uint32(441),detLabel = cms.string("FPIXmD3R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148e9400")),
    cms.PSet(detSelection = cms.uint32(442),detLabel = cms.string("FPIXmD3R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ea400")),
    cms.PSet(detSelection = cms.uint32(443),detLabel = cms.string("FPIXmD3R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148eb400")),
    cms.PSet(detSelection = cms.uint32(444),detLabel = cms.string("FPIXmD3R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ec400")),
    cms.PSet(detSelection = cms.uint32(445),detLabel = cms.string("FPIXmD3R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ed400")),
    cms.PSet(detSelection = cms.uint32(446),detLabel = cms.string("FPIXmD3R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ee400")),
    cms.PSet(detSelection = cms.uint32(447),detLabel = cms.string("FPIXmD3R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148ef400")),
    cms.PSet(detSelection = cms.uint32(448),detLabel = cms.string("FPIXmD3R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f0400")),
    cms.PSet(detSelection = cms.uint32(449),detLabel = cms.string("FPIXmD3R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f1400")),
    cms.PSet(detSelection = cms.uint32(450),detLabel = cms.string("FPIXmD3R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f2400")),
    cms.PSet(detSelection = cms.uint32(451),detLabel = cms.string("FPIXmD3R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f3400")),
    cms.PSet(detSelection = cms.uint32(452),detLabel = cms.string("FPIXmD3R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f4400")),
    cms.PSet(detSelection = cms.uint32(453),detLabel = cms.string("FPIXmD3R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f5400")),
    cms.PSet(detSelection = cms.uint32(454),detLabel = cms.string("FPIXmD3R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f6400")),
    cms.PSet(detSelection = cms.uint32(455),detLabel = cms.string("FPIXmD3R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f7400")),
    cms.PSet(detSelection = cms.uint32(456),detLabel = cms.string("FPIXmD3R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x148f8400")),
#
    cms.PSet(detSelection = cms.uint32(501),detLabel = cms.string("FPIXmD3R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c1800")),
    cms.PSet(detSelection = cms.uint32(502),detLabel = cms.string("FPIXmD3R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c2800")),
    cms.PSet(detSelection = cms.uint32(503),detLabel = cms.string("FPIXmD3R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c3800")),
    cms.PSet(detSelection = cms.uint32(504),detLabel = cms.string("FPIXmD3R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c4800")),
    cms.PSet(detSelection = cms.uint32(505),detLabel = cms.string("FPIXmD3R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c5800")),
    cms.PSet(detSelection = cms.uint32(506),detLabel = cms.string("FPIXmD3R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c6800")),
    cms.PSet(detSelection = cms.uint32(507),detLabel = cms.string("FPIXmD3R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c7800")),
    cms.PSet(detSelection = cms.uint32(508),detLabel = cms.string("FPIXmD3R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c8800")),
    cms.PSet(detSelection = cms.uint32(509),detLabel = cms.string("FPIXmD3R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148c9800")),
    cms.PSet(detSelection = cms.uint32(510),detLabel = cms.string("FPIXmD3R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ca800")),
    cms.PSet(detSelection = cms.uint32(511),detLabel = cms.string("FPIXmD3R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148cb800")),
    cms.PSet(detSelection = cms.uint32(512),detLabel = cms.string("FPIXmD3R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148cc800")),
    cms.PSet(detSelection = cms.uint32(513),detLabel = cms.string("FPIXmD3R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148cd800")),
    cms.PSet(detSelection = cms.uint32(514),detLabel = cms.string("FPIXmD3R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ce800")),
    cms.PSet(detSelection = cms.uint32(515),detLabel = cms.string("FPIXmD3R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148cf800")),
    cms.PSet(detSelection = cms.uint32(516),detLabel = cms.string("FPIXmD3R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d0800")),
    cms.PSet(detSelection = cms.uint32(517),detLabel = cms.string("FPIXmD3R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d1800")),
    cms.PSet(detSelection = cms.uint32(518),detLabel = cms.string("FPIXmD3R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d2800")),
    cms.PSet(detSelection = cms.uint32(519),detLabel = cms.string("FPIXmD3R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d3800")),
    cms.PSet(detSelection = cms.uint32(520),detLabel = cms.string("FPIXmD3R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d4800")),
    cms.PSet(detSelection = cms.uint32(521),detLabel = cms.string("FPIXmD3R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d5800")),
    cms.PSet(detSelection = cms.uint32(522),detLabel = cms.string("FPIXmD3R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d6800")),
    cms.PSet(detSelection = cms.uint32(523),detLabel = cms.string("FPIXmD3R1m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d7800")),
    cms.PSet(detSelection = cms.uint32(524),detLabel = cms.string("FPIXmD3R1m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d8800")),
    cms.PSet(detSelection = cms.uint32(525),detLabel = cms.string("FPIXmD3R1m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148d9800")),
    cms.PSet(detSelection = cms.uint32(526),detLabel = cms.string("FPIXmD3R1m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148da800")),
    cms.PSet(detSelection = cms.uint32(527),detLabel = cms.string("FPIXmD3R1m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148db800")),
    cms.PSet(detSelection = cms.uint32(528),detLabel = cms.string("FPIXmD3R1m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148dc800")),
    cms.PSet(detSelection = cms.uint32(529),detLabel = cms.string("FPIXmD3R1m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148dd800")),
    cms.PSet(detSelection = cms.uint32(530),detLabel = cms.string("FPIXmD3R1m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148de800")),
    cms.PSet(detSelection = cms.uint32(531),detLabel = cms.string("FPIXmD3R1m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148df800")),
    cms.PSet(detSelection = cms.uint32(532),detLabel = cms.string("FPIXmD3R1m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e0800")),
    cms.PSet(detSelection = cms.uint32(533),detLabel = cms.string("FPIXmD3R1m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e1800")),
    cms.PSet(detSelection = cms.uint32(534),detLabel = cms.string("FPIXmD3R1m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e2800")),
    cms.PSet(detSelection = cms.uint32(535),detLabel = cms.string("FPIXmD3R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e3800")),
    cms.PSet(detSelection = cms.uint32(536),detLabel = cms.string("FPIXmD3R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e4800")),
    cms.PSet(detSelection = cms.uint32(537),detLabel = cms.string("FPIXmD3R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e5800")),
    cms.PSet(detSelection = cms.uint32(538),detLabel = cms.string("FPIXmD3R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e6800")),
    cms.PSet(detSelection = cms.uint32(539),detLabel = cms.string("FPIXmD3R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e7800")),
    cms.PSet(detSelection = cms.uint32(540),detLabel = cms.string("FPIXmD3R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e8800")),
    cms.PSet(detSelection = cms.uint32(541),detLabel = cms.string("FPIXmD3R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148e9800")),
    cms.PSet(detSelection = cms.uint32(542),detLabel = cms.string("FPIXmD3R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ea800")),
    cms.PSet(detSelection = cms.uint32(543),detLabel = cms.string("FPIXmD3R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148eb800")),
    cms.PSet(detSelection = cms.uint32(544),detLabel = cms.string("FPIXmD3R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ec800")),
    cms.PSet(detSelection = cms.uint32(545),detLabel = cms.string("FPIXmD3R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ed800")),
    cms.PSet(detSelection = cms.uint32(546),detLabel = cms.string("FPIXmD3R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ee800")),
    cms.PSet(detSelection = cms.uint32(547),detLabel = cms.string("FPIXmD3R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148ef800")),
    cms.PSet(detSelection = cms.uint32(548),detLabel = cms.string("FPIXmD3R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f0800")),
    cms.PSet(detSelection = cms.uint32(549),detLabel = cms.string("FPIXmD3R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f1800")),
    cms.PSet(detSelection = cms.uint32(550),detLabel = cms.string("FPIXmD3R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f2800")),
    cms.PSet(detSelection = cms.uint32(551),detLabel = cms.string("FPIXmD3R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f3800")),
    cms.PSet(detSelection = cms.uint32(552),detLabel = cms.string("FPIXmD3R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f4800")),
    cms.PSet(detSelection = cms.uint32(553),detLabel = cms.string("FPIXmD3R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f5800")),
    cms.PSet(detSelection = cms.uint32(554),detLabel = cms.string("FPIXmD3R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f6800")),
    cms.PSet(detSelection = cms.uint32(555),detLabel = cms.string("FPIXmD3R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f7800")),
    cms.PSet(detSelection = cms.uint32(556),detLabel = cms.string("FPIXmD3R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x148f8800")),
)

OccupancyPlotsFPIXmDetailedWantedSubDets = OccupancyPlotsFPIXmD1DetailedWantedSubDets
OccupancyPlotsFPIXmDetailedWantedSubDets.extend(OccupancyPlotsFPIXmD2DetailedWantedSubDets)
OccupancyPlotsFPIXmDetailedWantedSubDets.extend(OccupancyPlotsFPIXmD3DetailedWantedSubDets)

OccupancyPlotsFPIXpD1DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(2001),detLabel = cms.string("FPIXpD1R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15041400")),
    cms.PSet(detSelection = cms.uint32(2002),detLabel = cms.string("FPIXpD1R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15042400")),
    cms.PSet(detSelection = cms.uint32(2003),detLabel = cms.string("FPIXpD1R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15043400")),
    cms.PSet(detSelection = cms.uint32(2004),detLabel = cms.string("FPIXpD1R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15044400")),
    cms.PSet(detSelection = cms.uint32(2005),detLabel = cms.string("FPIXpD1R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15045400")),
    cms.PSet(detSelection = cms.uint32(2006),detLabel = cms.string("FPIXpD1R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15046400")),
    cms.PSet(detSelection = cms.uint32(2007),detLabel = cms.string("FPIXpD1R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15047400")),
    cms.PSet(detSelection = cms.uint32(2008),detLabel = cms.string("FPIXpD1R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15048400")),
    cms.PSet(detSelection = cms.uint32(2009),detLabel = cms.string("FPIXpD1R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15049400")),
    cms.PSet(detSelection = cms.uint32(2010),detLabel = cms.string("FPIXpD1R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504a400")),
    cms.PSet(detSelection = cms.uint32(2011),detLabel = cms.string("FPIXpD1R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504b400")),
    cms.PSet(detSelection = cms.uint32(2012),detLabel = cms.string("FPIXpD1R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504c400")),
    cms.PSet(detSelection = cms.uint32(2013),detLabel = cms.string("FPIXpD1R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504d400")),
    cms.PSet(detSelection = cms.uint32(2014),detLabel = cms.string("FPIXpD1R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504e400")),
    cms.PSet(detSelection = cms.uint32(2015),detLabel = cms.string("FPIXpD1R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1504f400")),
    cms.PSet(detSelection = cms.uint32(2016),detLabel = cms.string("FPIXpD1R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15050400")),
    cms.PSet(detSelection = cms.uint32(2017),detLabel = cms.string("FPIXpD1R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15051400")),
    cms.PSet(detSelection = cms.uint32(2018),detLabel = cms.string("FPIXpD1R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15052400")),
    cms.PSet(detSelection = cms.uint32(2019),detLabel = cms.string("FPIXpD1R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15053400")),
    cms.PSet(detSelection = cms.uint32(2020),detLabel = cms.string("FPIXpD1R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15054400")),
    cms.PSet(detSelection = cms.uint32(2021),detLabel = cms.string("FPIXpD1R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15055400")),
    cms.PSet(detSelection = cms.uint32(2022),detLabel = cms.string("FPIXpD1R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15056400")),
    cms.PSet(detSelection = cms.uint32(2023),detLabel = cms.string("FPIXpD1R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15057400")),
    cms.PSet(detSelection = cms.uint32(2024),detLabel = cms.string("FPIXpD1R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15058400")),
    cms.PSet(detSelection = cms.uint32(2025),detLabel = cms.string("FPIXpD1R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15059400")),
    cms.PSet(detSelection = cms.uint32(2026),detLabel = cms.string("FPIXpD1R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505a400")),
    cms.PSet(detSelection = cms.uint32(2027),detLabel = cms.string("FPIXpD1R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505b400")),
    cms.PSet(detSelection = cms.uint32(2028),detLabel = cms.string("FPIXpD1R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505c400")),
    cms.PSet(detSelection = cms.uint32(2029),detLabel = cms.string("FPIXpD1R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505d400")),
    cms.PSet(detSelection = cms.uint32(2030),detLabel = cms.string("FPIXpD1R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505e400")),
    cms.PSet(detSelection = cms.uint32(2031),detLabel = cms.string("FPIXpD1R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1505f400")),
    cms.PSet(detSelection = cms.uint32(2032),detLabel = cms.string("FPIXpD1R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15060400")),
    cms.PSet(detSelection = cms.uint32(2033),detLabel = cms.string("FPIXpD1R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15061400")),
    cms.PSet(detSelection = cms.uint32(2034),detLabel = cms.string("FPIXpD1R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15062400")),
    cms.PSet(detSelection = cms.uint32(2035),detLabel = cms.string("FPIXpD1R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15063400")),
    cms.PSet(detSelection = cms.uint32(2036),detLabel = cms.string("FPIXpD1R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15064400")),
    cms.PSet(detSelection = cms.uint32(2037),detLabel = cms.string("FPIXpD1R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15065400")),
    cms.PSet(detSelection = cms.uint32(2038),detLabel = cms.string("FPIXpD1R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15066400")),
    cms.PSet(detSelection = cms.uint32(2039),detLabel = cms.string("FPIXpD1R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15067400")),
    cms.PSet(detSelection = cms.uint32(2040),detLabel = cms.string("FPIXpD1R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15068400")),
    cms.PSet(detSelection = cms.uint32(2041),detLabel = cms.string("FPIXpD1R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15069400")),
    cms.PSet(detSelection = cms.uint32(2042),detLabel = cms.string("FPIXpD1R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506a400")),
    cms.PSet(detSelection = cms.uint32(2043),detLabel = cms.string("FPIXpD1R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506b400")),
    cms.PSet(detSelection = cms.uint32(2044),detLabel = cms.string("FPIXpD1R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506c400")),
    cms.PSet(detSelection = cms.uint32(2045),detLabel = cms.string("FPIXpD1R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506d400")),
    cms.PSet(detSelection = cms.uint32(2046),detLabel = cms.string("FPIXpD1R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506e400")),
    cms.PSet(detSelection = cms.uint32(2047),detLabel = cms.string("FPIXpD1R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1506f400")),
    cms.PSet(detSelection = cms.uint32(2048),detLabel = cms.string("FPIXpD1R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15070400")),
    cms.PSet(detSelection = cms.uint32(2049),detLabel = cms.string("FPIXpD1R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15071400")),
    cms.PSet(detSelection = cms.uint32(2050),detLabel = cms.string("FPIXpD1R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15072400")),
    cms.PSet(detSelection = cms.uint32(2051),detLabel = cms.string("FPIXpD1R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15073400")),
    cms.PSet(detSelection = cms.uint32(2052),detLabel = cms.string("FPIXpD1R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15074400")),
    cms.PSet(detSelection = cms.uint32(2053),detLabel = cms.string("FPIXpD1R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15075400")),
    cms.PSet(detSelection = cms.uint32(2054),detLabel = cms.string("FPIXpD1R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15076400")),
    cms.PSet(detSelection = cms.uint32(2055),detLabel = cms.string("FPIXpD1R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15077400")),
    cms.PSet(detSelection = cms.uint32(2056),detLabel = cms.string("FPIXpD1R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15078400")),
#
    cms.PSet(detSelection = cms.uint32(2101),detLabel = cms.string("FPIXpD1R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15041800")),
    cms.PSet(detSelection = cms.uint32(2102),detLabel = cms.string("FPIXpD1R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15042800")),
    cms.PSet(detSelection = cms.uint32(2103),detLabel = cms.string("FPIXpD1R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15043800")),
    cms.PSet(detSelection = cms.uint32(2104),detLabel = cms.string("FPIXpD1R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15044800")),
    cms.PSet(detSelection = cms.uint32(2105),detLabel = cms.string("FPIXpD1R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15045800")),
    cms.PSet(detSelection = cms.uint32(2106),detLabel = cms.string("FPIXpD1R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15046800")),
    cms.PSet(detSelection = cms.uint32(2107),detLabel = cms.string("FPIXpD1R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15047800")),
    cms.PSet(detSelection = cms.uint32(2108),detLabel = cms.string("FPIXpD1R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15048800")),
    cms.PSet(detSelection = cms.uint32(2109),detLabel = cms.string("FPIXpD1R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15049800")),
    cms.PSet(detSelection = cms.uint32(2110),detLabel = cms.string("FPIXpD1R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504a800")),
    cms.PSet(detSelection = cms.uint32(2111),detLabel = cms.string("FPIXpD1R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504b800")),
    cms.PSet(detSelection = cms.uint32(2112),detLabel = cms.string("FPIXpD1R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504c800")),
    cms.PSet(detSelection = cms.uint32(2113),detLabel = cms.string("FPIXpD1R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504d800")),
    cms.PSet(detSelection = cms.uint32(2114),detLabel = cms.string("FPIXpD1R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504e800")),
    cms.PSet(detSelection = cms.uint32(2115),detLabel = cms.string("FPIXpD1R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1504f800")),
    cms.PSet(detSelection = cms.uint32(2116),detLabel = cms.string("FPIXpD1R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15050800")),
    cms.PSet(detSelection = cms.uint32(2117),detLabel = cms.string("FPIXpD1R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15051800")),
    cms.PSet(detSelection = cms.uint32(2118),detLabel = cms.string("FPIXpD1R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15052800")),
    cms.PSet(detSelection = cms.uint32(2119),detLabel = cms.string("FPIXpD1R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15053800")),
    cms.PSet(detSelection = cms.uint32(2120),detLabel = cms.string("FPIXpD1R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15054800")),
    cms.PSet(detSelection = cms.uint32(2121),detLabel = cms.string("FPIXpD1R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15055800")),
    cms.PSet(detSelection = cms.uint32(2122),detLabel = cms.string("FPIXpD1R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15056800")),
    cms.PSet(detSelection = cms.uint32(2123),detLabel = cms.string("FPIXpD1R2m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15057800")),
    cms.PSet(detSelection = cms.uint32(2124),detLabel = cms.string("FPIXpD1R2m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15058800")),
    cms.PSet(detSelection = cms.uint32(2125),detLabel = cms.string("FPIXpD1R2m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15059800")),
    cms.PSet(detSelection = cms.uint32(2126),detLabel = cms.string("FPIXpD1R2m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505a800")),
    cms.PSet(detSelection = cms.uint32(2127),detLabel = cms.string("FPIXpD1R2m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505b800")),
    cms.PSet(detSelection = cms.uint32(2128),detLabel = cms.string("FPIXpD1R2m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505c800")),
    cms.PSet(detSelection = cms.uint32(2129),detLabel = cms.string("FPIXpD1R2m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505d800")),
    cms.PSet(detSelection = cms.uint32(2130),detLabel = cms.string("FPIXpD1R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505e800")),
    cms.PSet(detSelection = cms.uint32(2131),detLabel = cms.string("FPIXpD1R2m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1505f800")),
    cms.PSet(detSelection = cms.uint32(2132),detLabel = cms.string("FPIXpD1R2m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15060800")),
    cms.PSet(detSelection = cms.uint32(2133),detLabel = cms.string("FPIXpD1R2m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15061800")),
    cms.PSet(detSelection = cms.uint32(2134),detLabel = cms.string("FPIXpD1R2m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15062800")),
    cms.PSet(detSelection = cms.uint32(2135),detLabel = cms.string("FPIXpD1R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15063800")),
    cms.PSet(detSelection = cms.uint32(2136),detLabel = cms.string("FPIXpD1R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15064800")),
    cms.PSet(detSelection = cms.uint32(2137),detLabel = cms.string("FPIXpD1R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15065800")),
    cms.PSet(detSelection = cms.uint32(2138),detLabel = cms.string("FPIXpD1R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15066800")),
    cms.PSet(detSelection = cms.uint32(2139),detLabel = cms.string("FPIXpD1R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15067800")),
    cms.PSet(detSelection = cms.uint32(2140),detLabel = cms.string("FPIXpD1R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15068800")),
    cms.PSet(detSelection = cms.uint32(2141),detLabel = cms.string("FPIXpD1R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15069800")),
    cms.PSet(detSelection = cms.uint32(2142),detLabel = cms.string("FPIXpD1R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506a800")),
    cms.PSet(detSelection = cms.uint32(2143),detLabel = cms.string("FPIXpD1R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506b800")),
    cms.PSet(detSelection = cms.uint32(2144),detLabel = cms.string("FPIXpD1R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506c800")),
    cms.PSet(detSelection = cms.uint32(2145),detLabel = cms.string("FPIXpD1R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506d800")),
    cms.PSet(detSelection = cms.uint32(2146),detLabel = cms.string("FPIXpD1R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506e800")),
    cms.PSet(detSelection = cms.uint32(2147),detLabel = cms.string("FPIXpD1R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1506f800")),
    cms.PSet(detSelection = cms.uint32(2148),detLabel = cms.string("FPIXpD1R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15070800")),
    cms.PSet(detSelection = cms.uint32(2149),detLabel = cms.string("FPIXpD1R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15071800")),
    cms.PSet(detSelection = cms.uint32(2150),detLabel = cms.string("FPIXpD1R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15072800")),
    cms.PSet(detSelection = cms.uint32(2151),detLabel = cms.string("FPIXpD1R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15073800")),
    cms.PSet(detSelection = cms.uint32(2152),detLabel = cms.string("FPIXpD1R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15074800")),
    cms.PSet(detSelection = cms.uint32(2153),detLabel = cms.string("FPIXpD1R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15075800")),
    cms.PSet(detSelection = cms.uint32(2154),detLabel = cms.string("FPIXpD1R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15076800")),
    cms.PSet(detSelection = cms.uint32(2155),detLabel = cms.string("FPIXpD1R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15077800")),
    cms.PSet(detSelection = cms.uint32(2156),detLabel = cms.string("FPIXpD1R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15078800")),
)
OccupancyPlotsFPIXpD2DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(2201),detLabel = cms.string("FPIXpD2R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15081400")),
    cms.PSet(detSelection = cms.uint32(2202),detLabel = cms.string("FPIXpD2R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15082400")),
    cms.PSet(detSelection = cms.uint32(2203),detLabel = cms.string("FPIXpD2R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15083400")),
    cms.PSet(detSelection = cms.uint32(2204),detLabel = cms.string("FPIXpD2R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15084400")),
    cms.PSet(detSelection = cms.uint32(2205),detLabel = cms.string("FPIXpD2R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15085400")),
    cms.PSet(detSelection = cms.uint32(2206),detLabel = cms.string("FPIXpD2R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15086400")),
    cms.PSet(detSelection = cms.uint32(2207),detLabel = cms.string("FPIXpD2R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15087400")),
    cms.PSet(detSelection = cms.uint32(2208),detLabel = cms.string("FPIXpD2R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15088400")),
    cms.PSet(detSelection = cms.uint32(2209),detLabel = cms.string("FPIXpD2R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15089400")),
    cms.PSet(detSelection = cms.uint32(2210),detLabel = cms.string("FPIXpD2R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508a400")),
    cms.PSet(detSelection = cms.uint32(2211),detLabel = cms.string("FPIXpD2R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508b400")),
    cms.PSet(detSelection = cms.uint32(2212),detLabel = cms.string("FPIXpD2R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508c400")),
    cms.PSet(detSelection = cms.uint32(2213),detLabel = cms.string("FPIXpD2R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508d400")),
    cms.PSet(detSelection = cms.uint32(2214),detLabel = cms.string("FPIXpD2R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508e400")),
    cms.PSet(detSelection = cms.uint32(2215),detLabel = cms.string("FPIXpD2R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1508f400")),
    cms.PSet(detSelection = cms.uint32(2216),detLabel = cms.string("FPIXpD2R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15090400")),
    cms.PSet(detSelection = cms.uint32(2217),detLabel = cms.string("FPIXpD2R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15091400")),
    cms.PSet(detSelection = cms.uint32(2218),detLabel = cms.string("FPIXpD2R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15092400")),
    cms.PSet(detSelection = cms.uint32(2219),detLabel = cms.string("FPIXpD2R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15093400")),
    cms.PSet(detSelection = cms.uint32(2220),detLabel = cms.string("FPIXpD2R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15094400")),
    cms.PSet(detSelection = cms.uint32(2221),detLabel = cms.string("FPIXpD2R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15095400")),
    cms.PSet(detSelection = cms.uint32(2222),detLabel = cms.string("FPIXpD2R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15096400")),
    cms.PSet(detSelection = cms.uint32(2223),detLabel = cms.string("FPIXpD2R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15097400")),
    cms.PSet(detSelection = cms.uint32(2224),detLabel = cms.string("FPIXpD2R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15098400")),
    cms.PSet(detSelection = cms.uint32(2225),detLabel = cms.string("FPIXpD2R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x15099400")),
    cms.PSet(detSelection = cms.uint32(2226),detLabel = cms.string("FPIXpD2R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509a400")),
    cms.PSet(detSelection = cms.uint32(2227),detLabel = cms.string("FPIXpD2R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509b400")),
    cms.PSet(detSelection = cms.uint32(2228),detLabel = cms.string("FPIXpD2R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509c400")),
    cms.PSet(detSelection = cms.uint32(2229),detLabel = cms.string("FPIXpD2R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509d400")),
    cms.PSet(detSelection = cms.uint32(2230),detLabel = cms.string("FPIXpD2R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509e400")),
    cms.PSet(detSelection = cms.uint32(2231),detLabel = cms.string("FPIXpD2R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x1509f400")),
    cms.PSet(detSelection = cms.uint32(2232),detLabel = cms.string("FPIXpD2R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a0400")),
    cms.PSet(detSelection = cms.uint32(2233),detLabel = cms.string("FPIXpD2R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a1400")),
    cms.PSet(detSelection = cms.uint32(2234),detLabel = cms.string("FPIXpD2R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a2400")),
    cms.PSet(detSelection = cms.uint32(2235),detLabel = cms.string("FPIXpD2R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a3400")),
    cms.PSet(detSelection = cms.uint32(2236),detLabel = cms.string("FPIXpD2R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a4400")),
    cms.PSet(detSelection = cms.uint32(2237),detLabel = cms.string("FPIXpD2R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a5400")),
    cms.PSet(detSelection = cms.uint32(2238),detLabel = cms.string("FPIXpD2R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a6400")),
    cms.PSet(detSelection = cms.uint32(2239),detLabel = cms.string("FPIXpD2R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a7400")),
    cms.PSet(detSelection = cms.uint32(2240),detLabel = cms.string("FPIXpD2R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a8400")),
    cms.PSet(detSelection = cms.uint32(2241),detLabel = cms.string("FPIXpD2R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150a9400")),
    cms.PSet(detSelection = cms.uint32(2242),detLabel = cms.string("FPIXpD2R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150aa400")),
    cms.PSet(detSelection = cms.uint32(2243),detLabel = cms.string("FPIXpD2R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ab400")),
    cms.PSet(detSelection = cms.uint32(2244),detLabel = cms.string("FPIXpD2R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ac400")),
    cms.PSet(detSelection = cms.uint32(2245),detLabel = cms.string("FPIXpD2R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ad400")),
    cms.PSet(detSelection = cms.uint32(2246),detLabel = cms.string("FPIXpD2R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ae400")),
    cms.PSet(detSelection = cms.uint32(2247),detLabel = cms.string("FPIXpD2R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150af400")),
    cms.PSet(detSelection = cms.uint32(2248),detLabel = cms.string("FPIXpD2R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b0400")),
    cms.PSet(detSelection = cms.uint32(2249),detLabel = cms.string("FPIXpD2R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b1400")),
    cms.PSet(detSelection = cms.uint32(2250),detLabel = cms.string("FPIXpD2R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b2400")),
    cms.PSet(detSelection = cms.uint32(2251),detLabel = cms.string("FPIXpD2R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b3400")),
    cms.PSet(detSelection = cms.uint32(2252),detLabel = cms.string("FPIXpD2R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b4400")),
    cms.PSet(detSelection = cms.uint32(2253),detLabel = cms.string("FPIXpD2R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b5400")),
    cms.PSet(detSelection = cms.uint32(2254),detLabel = cms.string("FPIXpD2R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b6400")),
    cms.PSet(detSelection = cms.uint32(2255),detLabel = cms.string("FPIXpD2R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b7400")),
    cms.PSet(detSelection = cms.uint32(2256),detLabel = cms.string("FPIXpD2R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150b8400")),
#
    cms.PSet(detSelection = cms.uint32(2301),detLabel = cms.string("FPIXpD2R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15081800")),
    cms.PSet(detSelection = cms.uint32(2302),detLabel = cms.string("FPIXpD2R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15082800")),
    cms.PSet(detSelection = cms.uint32(2303),detLabel = cms.string("FPIXpD2R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15083800")),
    cms.PSet(detSelection = cms.uint32(2304),detLabel = cms.string("FPIXpD2R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15084800")),
    cms.PSet(detSelection = cms.uint32(2305),detLabel = cms.string("FPIXpD2R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15085800")),
    cms.PSet(detSelection = cms.uint32(2306),detLabel = cms.string("FPIXpD2R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15086800")),
    cms.PSet(detSelection = cms.uint32(2307),detLabel = cms.string("FPIXpD2R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15087800")),
    cms.PSet(detSelection = cms.uint32(2308),detLabel = cms.string("FPIXpD2R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15088800")),
    cms.PSet(detSelection = cms.uint32(2309),detLabel = cms.string("FPIXpD2R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15089800")),
    cms.PSet(detSelection = cms.uint32(2310),detLabel = cms.string("FPIXpD2R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508a800")),
    cms.PSet(detSelection = cms.uint32(2311),detLabel = cms.string("FPIXpD2R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508b800")),
    cms.PSet(detSelection = cms.uint32(2312),detLabel = cms.string("FPIXpD2R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508c800")),
    cms.PSet(detSelection = cms.uint32(2313),detLabel = cms.string("FPIXpD2R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508d800")),
    cms.PSet(detSelection = cms.uint32(2314),detLabel = cms.string("FPIXpD2R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508e800")),
    cms.PSet(detSelection = cms.uint32(2315),detLabel = cms.string("FPIXpD2R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1508f800")),
    cms.PSet(detSelection = cms.uint32(2316),detLabel = cms.string("FPIXpD2R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15090800")),
    cms.PSet(detSelection = cms.uint32(2317),detLabel = cms.string("FPIXpD2R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15091800")),
    cms.PSet(detSelection = cms.uint32(2318),detLabel = cms.string("FPIXpD2R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15092800")),
    cms.PSet(detSelection = cms.uint32(2319),detLabel = cms.string("FPIXpD2R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15093800")),
    cms.PSet(detSelection = cms.uint32(2320),detLabel = cms.string("FPIXpD2R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15094800")),
    cms.PSet(detSelection = cms.uint32(2321),detLabel = cms.string("FPIXpD2R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15095800")),
    cms.PSet(detSelection = cms.uint32(2322),detLabel = cms.string("FPIXpD2R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15096800")),
    cms.PSet(detSelection = cms.uint32(2323),detLabel = cms.string("FPIXpD2R1m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15097800")),
    cms.PSet(detSelection = cms.uint32(2324),detLabel = cms.string("FPIXpD2R1m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15098800")),
    cms.PSet(detSelection = cms.uint32(2325),detLabel = cms.string("FPIXpD2R1m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x15099800")),
    cms.PSet(detSelection = cms.uint32(2326),detLabel = cms.string("FPIXpD2R1m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509a800")),
    cms.PSet(detSelection = cms.uint32(2327),detLabel = cms.string("FPIXpD2R1m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509b800")),
    cms.PSet(detSelection = cms.uint32(2328),detLabel = cms.string("FPIXpD2R1m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509c800")),
    cms.PSet(detSelection = cms.uint32(2329),detLabel = cms.string("FPIXpD2R1m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509d800")),
    cms.PSet(detSelection = cms.uint32(2330),detLabel = cms.string("FPIXpD2R1m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509e800")),
    cms.PSet(detSelection = cms.uint32(2331),detLabel = cms.string("FPIXpD2R1m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x1509f800")),
    cms.PSet(detSelection = cms.uint32(2332),detLabel = cms.string("FPIXpD2R1m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a0800")),
    cms.PSet(detSelection = cms.uint32(2333),detLabel = cms.string("FPIXpD2R1m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a1800")),
    cms.PSet(detSelection = cms.uint32(2334),detLabel = cms.string("FPIXpD2R1m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a2800")),
    cms.PSet(detSelection = cms.uint32(2335),detLabel = cms.string("FPIXpD2R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a3800")),
    cms.PSet(detSelection = cms.uint32(2336),detLabel = cms.string("FPIXpD2R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a4800")),
    cms.PSet(detSelection = cms.uint32(2337),detLabel = cms.string("FPIXpD2R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a5800")),
    cms.PSet(detSelection = cms.uint32(2338),detLabel = cms.string("FPIXpD2R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a6800")),
    cms.PSet(detSelection = cms.uint32(2339),detLabel = cms.string("FPIXpD2R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a7800")),
    cms.PSet(detSelection = cms.uint32(2340),detLabel = cms.string("FPIXpD2R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a8800")),
    cms.PSet(detSelection = cms.uint32(2341),detLabel = cms.string("FPIXpD2R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150a9800")),
    cms.PSet(detSelection = cms.uint32(2342),detLabel = cms.string("FPIXpD2R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150aa800")),
    cms.PSet(detSelection = cms.uint32(2343),detLabel = cms.string("FPIXpD2R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ab800")),
    cms.PSet(detSelection = cms.uint32(2344),detLabel = cms.string("FPIXpD2R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ac800")),
    cms.PSet(detSelection = cms.uint32(2345),detLabel = cms.string("FPIXpD2R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ad800")),
    cms.PSet(detSelection = cms.uint32(2346),detLabel = cms.string("FPIXpD2R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ae800")),
    cms.PSet(detSelection = cms.uint32(2347),detLabel = cms.string("FPIXpD2R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150af800")),
    cms.PSet(detSelection = cms.uint32(2348),detLabel = cms.string("FPIXpD2R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b0800")),
    cms.PSet(detSelection = cms.uint32(2349),detLabel = cms.string("FPIXpD2R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b1800")),
    cms.PSet(detSelection = cms.uint32(2350),detLabel = cms.string("FPIXpD2R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b2800")),
    cms.PSet(detSelection = cms.uint32(2351),detLabel = cms.string("FPIXpD2R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b3800")),
    cms.PSet(detSelection = cms.uint32(2352),detLabel = cms.string("FPIXpD2R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b4800")),
    cms.PSet(detSelection = cms.uint32(2353),detLabel = cms.string("FPIXpD2R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b5800")),
    cms.PSet(detSelection = cms.uint32(2354),detLabel = cms.string("FPIXpD2R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b6800")),
    cms.PSet(detSelection = cms.uint32(2355),detLabel = cms.string("FPIXpD2R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b7800")),
    cms.PSet(detSelection = cms.uint32(2356),detLabel = cms.string("FPIXpD2R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150b8800")),
)
#
OccupancyPlotsFPIXpD3DetailedWantedSubDets = cms.VPSet(
    cms.PSet(detSelection = cms.uint32(2401),detLabel = cms.string("FPIXpD3R1m1p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c1400")),
    cms.PSet(detSelection = cms.uint32(2402),detLabel = cms.string("FPIXpD3R1m2p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c2400")),
    cms.PSet(detSelection = cms.uint32(2403),detLabel = cms.string("FPIXpD3R1m3p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c3400")),
    cms.PSet(detSelection = cms.uint32(2404),detLabel = cms.string("FPIXpD3R1m4p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c4400")),
    cms.PSet(detSelection = cms.uint32(2405),detLabel = cms.string("FPIXpD3R1m5p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c5400")),
    cms.PSet(detSelection = cms.uint32(2406),detLabel = cms.string("FPIXpD3R1m6p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c6400")),
    cms.PSet(detSelection = cms.uint32(2407),detLabel = cms.string("FPIXpD3R1m7p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c7400")),
    cms.PSet(detSelection = cms.uint32(2408),detLabel = cms.string("FPIXpD3R1m8p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c8400")),
    cms.PSet(detSelection = cms.uint32(2409),detLabel = cms.string("FPIXpD3R1m9p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150c9400")),
    cms.PSet(detSelection = cms.uint32(2410),detLabel = cms.string("FPIXpD3R1m10p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ca400")),
    cms.PSet(detSelection = cms.uint32(2411),detLabel = cms.string("FPIXpD3R1m11p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150cb400")),
    cms.PSet(detSelection = cms.uint32(2412),detLabel = cms.string("FPIXpD3R1m12p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150cc400")),
    cms.PSet(detSelection = cms.uint32(2413),detLabel = cms.string("FPIXpD3R1m13p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150cd400")),
    cms.PSet(detSelection = cms.uint32(2414),detLabel = cms.string("FPIXpD3R1m14p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ce400")),
    cms.PSet(detSelection = cms.uint32(2415),detLabel = cms.string("FPIXpD3R1m15p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150cf400")),
    cms.PSet(detSelection = cms.uint32(2416),detLabel = cms.string("FPIXpD3R1m16p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d0400")),
    cms.PSet(detSelection = cms.uint32(2417),detLabel = cms.string("FPIXpD3R1m17p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d1400")),
    cms.PSet(detSelection = cms.uint32(2418),detLabel = cms.string("FPIXpD3R1m18p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d2400")),
    cms.PSet(detSelection = cms.uint32(2419),detLabel = cms.string("FPIXpD3R1m19p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d3400")),
    cms.PSet(detSelection = cms.uint32(2420),detLabel = cms.string("FPIXpD3R1m20p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d4400")),
    cms.PSet(detSelection = cms.uint32(2421),detLabel = cms.string("FPIXpD3R1m21p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d5400")),
    cms.PSet(detSelection = cms.uint32(2422),detLabel = cms.string("FPIXpD3R1m22p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d6400")),
    cms.PSet(detSelection = cms.uint32(2423),detLabel = cms.string("FPIXpD3R2m23p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d7400")),
    cms.PSet(detSelection = cms.uint32(2424),detLabel = cms.string("FPIXpD3R2m24p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d8400")),
    cms.PSet(detSelection = cms.uint32(2425),detLabel = cms.string("FPIXpD3R2m25p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150d9400")),
    cms.PSet(detSelection = cms.uint32(2426),detLabel = cms.string("FPIXpD3R2m26p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150da400")),
    cms.PSet(detSelection = cms.uint32(2427),detLabel = cms.string("FPIXpD3R2m27p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150db400")),
    cms.PSet(detSelection = cms.uint32(2428),detLabel = cms.string("FPIXpD3R2m28p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150dc400")),
    cms.PSet(detSelection = cms.uint32(2429),detLabel = cms.string("FPIXpD3R2m29p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150dd400")),
    cms.PSet(detSelection = cms.uint32(2430),detLabel = cms.string("FPIXpD3R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150de400")),
    cms.PSet(detSelection = cms.uint32(2431),detLabel = cms.string("FPIXpD3R2m31p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150df400")),
    cms.PSet(detSelection = cms.uint32(2432),detLabel = cms.string("FPIXpD3R2m32p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e0400")),
    cms.PSet(detSelection = cms.uint32(2433),detLabel = cms.string("FPIXpD3R2m33p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e1400")),
    cms.PSet(detSelection = cms.uint32(2434),detLabel = cms.string("FPIXpD3R2m34p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e2400")),
    cms.PSet(detSelection = cms.uint32(2435),detLabel = cms.string("FPIXpD3R2m35p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e3400")),
    cms.PSet(detSelection = cms.uint32(2436),detLabel = cms.string("FPIXpD3R2m36p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e4400")),
    cms.PSet(detSelection = cms.uint32(2437),detLabel = cms.string("FPIXpD3R2m37p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e5400")),
    cms.PSet(detSelection = cms.uint32(2438),detLabel = cms.string("FPIXpD3R2m38p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e6400")),
    cms.PSet(detSelection = cms.uint32(2439),detLabel = cms.string("FPIXpD3R2m39p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e7400")),
    cms.PSet(detSelection = cms.uint32(2440),detLabel = cms.string("FPIXpD3R2m30p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e8400")),
    cms.PSet(detSelection = cms.uint32(2441),detLabel = cms.string("FPIXpD3R2m41p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150e9400")),
    cms.PSet(detSelection = cms.uint32(2442),detLabel = cms.string("FPIXpD3R2m42p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ea400")),
    cms.PSet(detSelection = cms.uint32(2443),detLabel = cms.string("FPIXpD3R2m43p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150eb400")),
    cms.PSet(detSelection = cms.uint32(2444),detLabel = cms.string("FPIXpD3R2m44p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ec400")),
    cms.PSet(detSelection = cms.uint32(2445),detLabel = cms.string("FPIXpD3R2m45p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ed400")),
    cms.PSet(detSelection = cms.uint32(2446),detLabel = cms.string("FPIXpD3R2m46p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ee400")),
    cms.PSet(detSelection = cms.uint32(2447),detLabel = cms.string("FPIXpD3R2m47p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150ef400")),
    cms.PSet(detSelection = cms.uint32(2448),detLabel = cms.string("FPIXpD3R2m48p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f0400")),
    cms.PSet(detSelection = cms.uint32(2449),detLabel = cms.string("FPIXpD3R2m49p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f1400")),
    cms.PSet(detSelection = cms.uint32(2450),detLabel = cms.string("FPIXpD3R2m50p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f2400")),
    cms.PSet(detSelection = cms.uint32(2451),detLabel = cms.string("FPIXpD3R2m51p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f3400")),
    cms.PSet(detSelection = cms.uint32(2452),detLabel = cms.string("FPIXpD3R2m52p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f4400")),
    cms.PSet(detSelection = cms.uint32(2453),detLabel = cms.string("FPIXpD3R2m53p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f5400")),
    cms.PSet(detSelection = cms.uint32(2454),detLabel = cms.string("FPIXpD3R2m54p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f6400")),
    cms.PSet(detSelection = cms.uint32(2455),detLabel = cms.string("FPIXpD3R2m55p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f7400")),
    cms.PSet(detSelection = cms.uint32(2456),detLabel = cms.string("FPIXpD3R2m56p1"),selection=cms.untracked.vstring("0x1fbffc00-0x150f8400")),
#
    cms.PSet(detSelection = cms.uint32(2501),detLabel = cms.string("FPIXpD3R1m1p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c1800")),
    cms.PSet(detSelection = cms.uint32(2502),detLabel = cms.string("FPIXpD3R1m2p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c2800")),
    cms.PSet(detSelection = cms.uint32(2503),detLabel = cms.string("FPIXpD3R1m3p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c3800")),
    cms.PSet(detSelection = cms.uint32(2504),detLabel = cms.string("FPIXpD3R1m4p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c4800")),
    cms.PSet(detSelection = cms.uint32(2505),detLabel = cms.string("FPIXpD3R1m5p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c5800")),
    cms.PSet(detSelection = cms.uint32(2506),detLabel = cms.string("FPIXpD3R1m6p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c6800")),
    cms.PSet(detSelection = cms.uint32(2507),detLabel = cms.string("FPIXpD3R1m7p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c7800")),
    cms.PSet(detSelection = cms.uint32(2508),detLabel = cms.string("FPIXpD3R1m8p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c8800")),
    cms.PSet(detSelection = cms.uint32(2509),detLabel = cms.string("FPIXpD3R1m9p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150c9800")),
    cms.PSet(detSelection = cms.uint32(2510),detLabel = cms.string("FPIXpD3R1m10p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ca800")),
    cms.PSet(detSelection = cms.uint32(2511),detLabel = cms.string("FPIXpD3R1m11p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150cb800")),
    cms.PSet(detSelection = cms.uint32(2512),detLabel = cms.string("FPIXpD3R1m12p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150cc800")),
    cms.PSet(detSelection = cms.uint32(2513),detLabel = cms.string("FPIXpD3R1m13p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150cd800")),
    cms.PSet(detSelection = cms.uint32(2514),detLabel = cms.string("FPIXpD3R1m14p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ce800")),
    cms.PSet(detSelection = cms.uint32(2515),detLabel = cms.string("FPIXpD3R1m15p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150cf800")),
    cms.PSet(detSelection = cms.uint32(2516),detLabel = cms.string("FPIXpD3R1m16p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d0800")),
    cms.PSet(detSelection = cms.uint32(2517),detLabel = cms.string("FPIXpD3R1m17p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d1800")),
    cms.PSet(detSelection = cms.uint32(2518),detLabel = cms.string("FPIXpD3R1m18p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d2800")),
    cms.PSet(detSelection = cms.uint32(2519),detLabel = cms.string("FPIXpD3R1m19p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d3800")),
    cms.PSet(detSelection = cms.uint32(2520),detLabel = cms.string("FPIXpD3R1m20p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d4800")),
    cms.PSet(detSelection = cms.uint32(2521),detLabel = cms.string("FPIXpD3R1m21p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d5800")),
    cms.PSet(detSelection = cms.uint32(2522),detLabel = cms.string("FPIXpD3R1m22p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d6800")),
    cms.PSet(detSelection = cms.uint32(2523),detLabel = cms.string("FPIXpD3R1m23p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d7800")),
    cms.PSet(detSelection = cms.uint32(2524),detLabel = cms.string("FPIXpD3R1m24p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d8800")),
    cms.PSet(detSelection = cms.uint32(2525),detLabel = cms.string("FPIXpD3R1m25p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150d9800")),
    cms.PSet(detSelection = cms.uint32(2526),detLabel = cms.string("FPIXpD3R1m26p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150da800")),
    cms.PSet(detSelection = cms.uint32(2527),detLabel = cms.string("FPIXpD3R1m27p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150db800")),
    cms.PSet(detSelection = cms.uint32(2528),detLabel = cms.string("FPIXpD3R1m28p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150dc800")),
    cms.PSet(detSelection = cms.uint32(2529),detLabel = cms.string("FPIXpD3R1m29p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150dd800")),
    cms.PSet(detSelection = cms.uint32(2530),detLabel = cms.string("FPIXpD3R1m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150de800")),
    cms.PSet(detSelection = cms.uint32(2531),detLabel = cms.string("FPIXpD3R1m31p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150df800")),
    cms.PSet(detSelection = cms.uint32(2532),detLabel = cms.string("FPIXpD3R1m32p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e0800")),
    cms.PSet(detSelection = cms.uint32(2533),detLabel = cms.string("FPIXpD3R1m33p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e1800")),
    cms.PSet(detSelection = cms.uint32(2534),detLabel = cms.string("FPIXpD3R1m34p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e2800")),
    cms.PSet(detSelection = cms.uint32(2535),detLabel = cms.string("FPIXpD3R2m35p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e3800")),
    cms.PSet(detSelection = cms.uint32(2536),detLabel = cms.string("FPIXpD3R2m36p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e4800")),
    cms.PSet(detSelection = cms.uint32(2537),detLabel = cms.string("FPIXpD3R2m37p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e5800")),
    cms.PSet(detSelection = cms.uint32(2538),detLabel = cms.string("FPIXpD3R2m38p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e6800")),
    cms.PSet(detSelection = cms.uint32(2539),detLabel = cms.string("FPIXpD3R2m39p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e7800")),
    cms.PSet(detSelection = cms.uint32(2540),detLabel = cms.string("FPIXpD3R2m30p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e8800")),
    cms.PSet(detSelection = cms.uint32(2541),detLabel = cms.string("FPIXpD3R2m41p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150e9800")),
    cms.PSet(detSelection = cms.uint32(2542),detLabel = cms.string("FPIXpD3R2m42p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ea800")),
    cms.PSet(detSelection = cms.uint32(2543),detLabel = cms.string("FPIXpD3R2m43p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150eb800")),
    cms.PSet(detSelection = cms.uint32(2544),detLabel = cms.string("FPIXpD3R2m44p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ec800")),
    cms.PSet(detSelection = cms.uint32(2545),detLabel = cms.string("FPIXpD3R2m45p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ed800")),
    cms.PSet(detSelection = cms.uint32(2546),detLabel = cms.string("FPIXpD3R2m46p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ee800")),
    cms.PSet(detSelection = cms.uint32(2547),detLabel = cms.string("FPIXpD3R2m47p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150ef800")),
    cms.PSet(detSelection = cms.uint32(2548),detLabel = cms.string("FPIXpD3R2m48p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f0800")),
    cms.PSet(detSelection = cms.uint32(2549),detLabel = cms.string("FPIXpD3R2m49p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f1800")),
    cms.PSet(detSelection = cms.uint32(2550),detLabel = cms.string("FPIXpD3R2m50p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f2800")),
    cms.PSet(detSelection = cms.uint32(2551),detLabel = cms.string("FPIXpD3R2m51p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f3800")),
    cms.PSet(detSelection = cms.uint32(2552),detLabel = cms.string("FPIXpD3R2m52p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f4800")),
    cms.PSet(detSelection = cms.uint32(2553),detLabel = cms.string("FPIXpD3R2m53p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f5800")),
    cms.PSet(detSelection = cms.uint32(2554),detLabel = cms.string("FPIXpD3R2m54p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f6800")),
    cms.PSet(detSelection = cms.uint32(2555),detLabel = cms.string("FPIXpD3R2m55p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f7800")),
    cms.PSet(detSelection = cms.uint32(2556),detLabel = cms.string("FPIXpD3R2m56p2"),selection=cms.untracked.vstring("0x1fbffc00-0x150f8800")),
)
 
OccupancyPlotsFPIXpDetailedWantedSubDets = OccupancyPlotsFPIXpD1DetailedWantedSubDets
OccupancyPlotsFPIXpDetailedWantedSubDets.extend(OccupancyPlotsFPIXpD2DetailedWantedSubDets)
OccupancyPlotsFPIXpDetailedWantedSubDets.extend(OccupancyPlotsFPIXpD3DetailedWantedSubDets)

