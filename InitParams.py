#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:56:41 2022

@author: gangxinli
"""
import os

print(os.getcwd())
def InitParams(atlasPath="",destinationPath=""):
    
    
    Params = {}
    Params['dataDescription'] = 'DevelopmentTest'
    
    Params['slash'] = '/' if os.name =='posix' else '\\'
    Params['path0'] = os.getcwd()+Params['slash']
    Params['path1'] = Params['path0'] + 'templates' + Params['slash']
    Params['path2'] = Params['path0'] + 'results' + Params['slash']
    Params['atlasPath'] = Params['path1'] if atlasPath=="" else atlasPath
    Params['destinationPath'] = Params['path2'] if destinationPath=="" else destinationPath
    
    
    
    #Default grid computation settings:
    Params['disableGrid'] = True
    
    
    
    
    
    return Params

if __name__ =='__main__':
    init = InitParams()
  
    
    
    
    
    
    