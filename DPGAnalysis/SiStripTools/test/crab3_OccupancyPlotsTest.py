from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'OccupancyPlotsTest_2017B_express_298678_fromRAW_v14'
config.General.workArea = '/afs/cern.ch/work/v/venturia/crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DPGAnalysis/SiStripTools/test/OccupancyPlotsTest_pixelphase1_cfg.py'
config.JobType.pyCfgParams = ['globalTag=92X_dataRun2_Express_v2','fromRAW=1','withTracks=1','tag=2017B_express_298678_fromRAW_v14','triggerPath=HLT_ZeroBias*','triggerPaths=HLT_ZeroBias_v*,HLT_ZeroBias_FirstBXAfterTrain_*,HLT_ZeroBias_FirstCollision*,HLT_ZeroBias_IsolatedBunches_*,HLT_Random*','triggerLabels=ZeroBias,FirstAfterTrain,FirstBunch,Isobunch,Random','negateFlags=0,0,0,0,0']

config.Data.inputDataset = '/ExpressPhysics/Run2017B-Express-v2/FEVT'

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/DCSOnly/json_DCSONLY.txt'
config.Data.runRange = '298678' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_Data_analysis'

config.Site.storageSite = 'T2_IT_Pisa'

