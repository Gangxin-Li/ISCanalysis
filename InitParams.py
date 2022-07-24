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
    #Settings regarding inter-subject synchronization:
    Params['subjectSource'][1]  = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/movie_8/sub005_M/sub-sid000005_task-movie_run-01_bold_bvbabel.nii'
    Params['subjectSource'][2]  = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/movie_8/sub005_M/sub-sid000005_task-movie_run-01_bold_firstvol_bvbabel.nii'
    Params['subjectSource'][3]  = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/movie_8/sub005_M/sub-sid000005_task-movie_run-01_bold_SCCAI_3DMCTS_THPGLMF3c_bvbabel.nii'  

    #% Select intersubject similarity criteria that are calculated:
    Params['ssiOn'] = 0# % sign-similarity index
    Params['nmiOn'] = 0# % mutual information based index
    Params['corOn'] = 1# % Pearson's correlation based index (recommended!)
    Params['kenOn'] = 0# % Kendall's W based index
    
    #% Determine parts of the analysis that will be performed:
    Params['calcStandard'] = 1# % standard analysis
    Params['calcStats'] = 0# % median, quartile, t and variance ISC maps
    Params['calcCorMatrices'] = 0# % save full correlation matrices
    Params['calcPhase'] = 0
    
    
    
    
    return Params

if __name__ =='__main__':
    init = InitParams()
  
    
    
    
    
    
    