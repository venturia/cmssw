from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'OccupancyPlotsTest_2016H_isolatedbunches_v5'
config.General.requestName = 'OccupancyPlotsTest_2016H_ZB_pilot_Bari_v5'
#config.General.requestName = 'OccupancyPlotsTest_2016F_ZB_isolatedbunches_v5'
config.General.workArea = '/afs/cern.ch/work/v/venturia/crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DPGAnalysis/SiStripTools/test/OccupancyPlotsTest_cfg.py'
config.JobType.pyCfgParams = ['globalTag=80X_dataRun2_Prompt_v14','fromRAW=1','tag=2016H_ZB_pilot','triggerPath=HLT_ZeroBias_v*','triggerPaths=HLT_ZeroBias_v*,HLT_ZeroBias_*,HLT_ZeroBias*','triggerLabels=ZeroBias,AllZeroBias,MoreZeroBias','negateFlags=0,0,0']
#config.JobType.pyCfgParams = ['globalTag=80X_dataRun2_Prompt_v14','fromRAW=1','tag=2016H_isolatedbunches']

#config.Data.inputDataset = '/MinimumBias/Run2012A-22Jan2013-v1/RECO'
config.Data.inputDataset = '/ZeroBias/Run2016H-v1/RAW'
#config.Data.inputDataset = '/ZeroBias/Run2016F-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
#config.Data.totalUnits = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
#config.Data.lumiMask = 'JSON_2016_isolatedbunches.txt'
config.Data.runRange = '284035,284036,284037,284038' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_Data_analysis'

#config.Site.storageSite = 'T2_IT_Pisa'
config.Site.storageSite = 'T2_IT_Bari'

