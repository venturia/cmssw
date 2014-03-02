import FWCore.ParameterSet.Config as cms

from TrackingPFG.TrackJets.TrackJetsValidation_threecases_cfi import *

seqTrackJets = cms.Sequence(trackjetsak5 +
                            trackjetskt4 +
                            trackjetssc5 )

