#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:57:43 2022

@author: gangxinli
"""

import os
from InitParams import InitParams

Params = InitParams()
def InitScriptsFolder(Params):
    scriptspath = Params['destinationPath'] + 'scripts'
    if not os.path.exists(scriptspath):
        os.makedirs(scriptspath)
    else:
        file_source = 'Path/Of/Directory'
        file_destination = 'Path/Of/Directory'
 
        get_files = os.listdir(file_source)
 
        for g in get_files:
            shutil.move(file_source + g, file_destination)
    
    
    log_path = scriptspath
    return log_path

if __name__ == '__main__':
    initfolder = InitScriptsFolder(Params)