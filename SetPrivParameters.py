#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:53:13 2022

@author: gangxinli
"""



def SetPrivParams(Params):
    
    
    PrivateParams = {}
    PrivateParams['subjectDestination'] = Params.dataDestination + 'fMRIpreprocessed' + Params['slash']
    PrivateParams['subjectFiltDestination'] = Params.dataDestination +'fMRIfiltered' + Params['slash']
    PrivateParams['resultsDestination'] = Params.dataDestination+'results'+ Params['slash']
    PrivateParams['statsDestination'] = Params.dataDestination+ 'stats'+ Params['slash']
    PrivateParams['PFDestination'] = Params.dataDestination +'PF'+ Params['slash']
    PrivateParams['PFsessionDestination'] = Params.dataDestination+ 'PFsession'+ Params['slash']
    PrivateParams['withinDestination'] = Params.dataDestination +'within'+ Params['slash']
    PrivateParams['phaseDifDestination'] = Params.dataDestination +'phase'+ Params['slash']
    
    PrivateParams['prefixResults'] = 'simMeasure'
    PrivateParams['prefixSubject'] = 'fMRIpreproc'
    PrivateParams['prefixSubjectFilt'] = 'fMRIfilt'
    PrivateParams['prefixSyncResults'] = 'synch'
    PrivateParams['prefixPhaseSyncResults'] = 'phaseSynch'
    PrivateParams['prefixLUT'] = 'LUT'
    PrivateParams['prefixTimeVal'] = 'timeInt'
    PrivateParams['prefixPF'] = 'PF'
    PrivateParams['prefixPFMat'] = 'PFMat'
    PrivateParams['prefixSessComp'] = 'sessComp'
    
    
    PrivateParams['prefixCorMat'] = 'corMat'
    PrivateParams['prefixFreqComp'] = 'freqComp'
    PrivateParams['prefixTMap'] = 'tstats'
    PrivateParams['prefixWithin'] = 'within'
    PrivateParams['prefixPhaseDif'] = 'phase'
    
    PrivateParams['prefixSession'] = 'Session'
    PrivateParams['prefixFreqBand'] = 'band'
    
    PrivateParams['simM'] = ['ssi','nmi','cor','ken']

    PrivateParams['nrSubjects'] = size(Params.subjectSource,2)
    PrivateParams['nrSessions'] = size(Params.subjectSource,1)
    PrivateParams['transformType'] = 'DWT'
    PrivateParams['resultMapName'] = 'resultMap'
    PrivateParams['origMapName'] = 'origMap'
    PrivateParams['filtMapName'] = 'filtMap'
    PrivateParams['synchMapName'] = 'synchMap'
    PrivateParams['phaseSynchMapName'] = 'phaseSynchMap'
    PrivateParams['statMapName'] = 'statMap'
    PrivateParams['cormatMapName'] = 'cormatMap'
    PrivateParams['PFMapName'] = 'PFMap'
    PrivateParams['PFmatMapName'] = 'PFmatMap'
    PrivateParams['withinMapName'] = 'withinMap'
    PrivateParams['phaseMapName'] = 'phaseMap'
    
    PrivateParams.PFMapSessionName = 'PFMapSession'
    PrivateParams.PFmatMapSessionName = 'PFMatMapSession'
    
    if Params['corOn']==0:
      Params['calcStats'] = 0;
      Params['calcCorMatrices'] = 0;
    
    
    
    
    return PrivateParams,Params

















