import FWCore.ParameterSet.Config as cms

from TrackingPFG.Configuration.conversionNtuplizer_cfi import *

conversionntuplizer.simulation = cms.bool(True)

seqConversion = cms.Sequence(conversionntuplizer)
