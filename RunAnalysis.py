#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:56:07 2022

@author: gangxinli
"""
from InitParams import InitParams
from InitScriptsFolder import InitScriptsFolder
from GetPCInfo import getPCInfo


def RunAnalysis(Params):
    log_path,temp_path = InitScriptsFolder(Params)
    
    gridOff = Params['disableGrid'] #assume always be true
    
    #Stage 1
    getPCInfo()
    #Stage 2
    #skip
    #Stage 3
    
    
    
    return 




if __name__ =='__main__':
    Params = InitParams()
    res = RunAnalysis(Params)