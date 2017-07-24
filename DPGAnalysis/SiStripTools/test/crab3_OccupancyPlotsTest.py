from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'OccupancyPlotsTest_2017B_express_297664_297671_fromRAW_v17'
config.General.workArea = '/afs/cern.ch/work/v/venturia/crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 6000
config.JobType.psetName = 'DPGAnalysis/SiStripTools/test/OccupancyPlotsTest_pixelphase1_cfg.py'
config.JobType.pyCfgParams = ['globalTag=92X_dataRun2_Express_v2','fromRAW=1','withTracks=1','triggerPath=HLT_ZeroBias_v*','triggerPaths=HLT_ZeroBias_FirstCollisionAfterAbortGap_*,HLT_ZeroBias_FirstCollisionInTrain_*,HLT_ZeroBias_FirstBXAfterTrain_*,HLT_ZeroBias_IsolatedBunches*','triggerLabels=FirstBunchInOrbit,FirstBunchInTrain,FirstBunchAfterTrain,Isobunch','negateFlags=0,0,0,0']

config.Data.inputDataset = '/ExpressPhysics/Run2017B-Express-v1/FEVT'
#config.Data.inputDataset = '/ExpressPhysics/Run2017B-Express-v2/FEVT'
#config.Data.inputDataset = '/ExpressPhysics/Run2017A-Express-v2/FEVT'

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/DCSOnly/json_DCSONLY.txt'
config.Data.runRange = '297664,297671' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_Data_analysis'

config.Site.storageSite = 'T2_IT_Pisa'

