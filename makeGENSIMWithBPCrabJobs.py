import os
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'Upsilon_15GeV_GS_STEP_test'
config.General.workArea = 'Upsilon_15GeV_GS_STEP_test'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'run_cfg_withBP.py'
config.JobType.numCores =  8
config.JobType.maxMemoryMB = 5000 
#config.JobType.inputFiles = ['', '']
config.JobType.outputFiles = ['GENSIM_withBP.root']

#config.Data.inputDBS = 'global'
#config.Data.inputDataset = ''
#config.Data.splitting = 'Automatic'
NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line. Was 5000 for Jordan
config.Data.unitsPerJob = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.splitting = 'EventBased' # for MC
config.Data.publishDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/mhadley/Upsilon_15GeV_GS_STEP_test/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'Upsilon_15GeV_GS_STEP_test'
config.Data.outputDatasetTag= 'Upsilon_15GeV_GS_STEP_test'


#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.storageSite     = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Brown'
#config.Site.storageSite     = 'T2_CH_CERNBOX'
