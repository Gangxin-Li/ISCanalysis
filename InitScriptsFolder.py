#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:57:43 2022

@author: gangxinli
"""
import shutil
import os
import time
from InitParams import InitParams


def InitScriptsFolder(Params):
    scriptspath = Params['destinationPath'] + 'scripts'+Params['slash']
    if not os.path.exists(scriptspath):
        os.makedirs(scriptspath)
    else:
        localtime = time.localtime(time.time())
        file_destination = Params['destinationPath'] + str(localtime[0:6])
        get_files = os.listdir(scriptspath)
        if len(get_files)!=0:
            os.makedirs(file_destination)
            for g in get_files:
                shutil.move(scriptspath + g, file_destination)
    
    temp_path = Params['destinationPath'] + 'temp'+Params['slash']
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    else:
        shutil.rmtree(temp_path)
        os.makedirs(temp_path)
    
    log_path = scriptspath
    return log_path,temp_path

if __name__ == '__main__':
    Params = InitParams()
    initfolder = InitScriptsFolder(Params)