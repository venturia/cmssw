import FWCore.ParameterSet.Config as cms

localV0Candidates = cms.EDProducer("V0Producer",
                                     
    # InputTag that tells which TrackCollection to use for vertexing
    trackRecoAlgorithm = cms.InputTag('generalTracks'),

    # These bools decide whether or not to reconstruct
    #  specific V0 particles
    selectKshorts = cms.bool(True),
    selectLambdas = cms.bool(True),

    # Recommend leaving this one as is.
    vertexFitter = cms.InputTag('KalmanVertexFitter'),

    # set to true, uses tracks refit by the KVF for V0Candidate kinematics
    #  NOTE: useSmoothing is automatically set to FALSE
    #  if using the AdaptiveVertexFitter (which is NOT recommended)
    useSmoothing = cms.bool(True),
                                     
    # Select tracks using TrackBase::TrackQuality.
    # Select ALL tracks by leaving this vstring empty, which
    #   is equivalent to using 'loose'
    #trackQualities = cms.vstring('highPurity', 'goodIterative'),
    trackQualities = cms.vstring('loose'),
                                     
    # The next parameters are cut values.
    # All distances are in cm, all energies in GeV, as usual.

    # --Track quality/compatibility cuts--
    #   Normalized track Chi2 <
    tkChi2Cut = cms.double(5.0),
    #   Number of valid hits on track >=
    tkNhitsCut = cms.int32(6),
    #   Track impact parameter significance >
    impactParameterSigCut = cms.double(0.5),
    # We calculate the PCA of the tracks quickly in RPhi, extrapolating
    # the z position as well, before vertexing.  Used in the following 2 cuts:
    #   m_pipi calculated at PCA of tracks <
    mPiPiCut = cms.double(1.),
    #   PCA distance between tracks <
    tkDCACut = cms.double(1.),

    # --V0 Vertex cuts--
    #   Vertex chi2 < 
    vtxChi2Cut = cms.double(7.0),
    #   Lambda collinearity cut
    #   (UNUSED)
    collinearityCut = cms.double(0.02),
    #   Vertex radius cut >
    #   (UNUSED)
    rVtxCut = cms.double(0.0),
    #   V0 decay length from primary cut >
    #   (UNUSED)
    lVtxCut = cms.double(0.0),
    #   Radial vertex significance >
    vtxSignificance2DCut = cms.double(15.0),
    #   3D vertex significance using primary vertex
    #   (UNUSED)
    vtxSignificance3DCut = cms.double(0.0),
    #   V0 mass window, Candidate mass must be within these values of
    #     the PDG mass to be stored in the collection
    kShortMassCut = cms.double(1.),
    lambdaMassCut = cms.double(1.),
    #   Mass window cut using normalized mass (mass / massError)
    #   (UNUSED)
    kShortNormalizedMassCut = cms.double(0.0),
    lambdaNormalizedMassCut = cms.double(0.0),
    # We check if either track has a hit inside (radially) the vertex position
    #  minus this number times the sigma of the vertex fit
    #  NOTE: Set this to -1 to disable this cut, which MUST be done
    #  if you want to run V0Producer on the AOD track collection!
    innerHitPosCut = cms.double(4.)
)


#localV0Candidates = cms.EDProducer("V0Producer",
#    trackRecoAlgorithm = cms.InputTag('generalTracks'),
#    useSmoothing = cms.bool(True),
#    storeSmoothedTracksInRecoVertex = cms.bool(False),
#    doPostFitCuts = cms.bool(True),
#    doTrackQualityCuts = cms.bool(True),
#    # The next parameters are cut values
#    # Track quality cuts
#    #   Normalized track Chi2:
#    tkChi2Cut = cms.double(5.0),
#    #   Number of valid hits on track:
#    tkNhitsCut = cms.int32(6),
#
#    # Vertex cuts
#    vtxChi2Cut = cms.double(7.0),
#    collinearityCut = cms.double(0.02),
#    #  Setting this one to zero; significance cut is sufficient
#    rVtxCut = cms.double(0.0),
##    vtxSignificanceCut = cms.double(22.0),
##    vtxSignificanceCut = cms.double(15.0),
#    vtxSignificanceCut = cms.double(15.0),
#    kShortMassCut = cms.double(1.),
#    lambdaMassCut = cms.double(1.),
#    impactParameterSigCut = cms.double(0.5),
#    mPiPiCut = cms.double(1.),
#    tkDCACut = cms.double(1.),
#
#    # These parameters decide whether or not to reconstruct
#    #  specific V0 particles
#    selectKshorts = cms.bool(True),
#    selectLambdas = cms.bool(True),
#
#    vertexFitter = cms.InputTag('KalmanVertexFitter')
#
#)

produceV0PATCands = cms.EDProducer("V0CandProducer",
    kShortCollection = cms.InputTag('localV0Candidates:Kshort'),
    lambdaCollection = cms.InputTag('localV0Candidates:Lambda')
)

