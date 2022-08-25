#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:19:01 2022

@author: gangxinli
"""
import gzip
import os

def un_gz(file_name):
    """
    Input -- file path
    
    Result:
        Get Unzip file on the same path
    """
    f_name = file_name.replace(".gz", "")
    g_file = gzip.GzipFile(file_name)
    open(f_name, "wb+").write(g_file.read())
    g_file.close()


def un_zip(path = './../Data/INDI_Lite_NIFTI'):
    """
    Input -- file path, a folder contais all of the data
    
    Result:
        Unzip all the gz file among the path
    """
    print("Unziping....")
    for root,dirs,files in os.walk(path):
        #print("11111root:"+root) 
        #print(dirs)
        for file in files:
            if file.split(".")[-1] == 'gz':
                #print("222root file: "+os.path.join(root,file))
                un_gz(os.path.join(root,file))
    print("Unzip complete!")



if __name__ == "__main__":
    un_zip('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/25Aug')




