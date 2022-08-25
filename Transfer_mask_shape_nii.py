#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 15:57:51 2022

@author: gangxinli
"""
import os
import numpy as np
import nibabel as nb
import msk
from nibabel import analyze

def msk_shape_nii(path = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/vtc_vmr"):
    print("Transfering msk file to nii file")
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.split(".")[-1] == 'msk':
                FILE = os.path.join(root,file)
         
                header, data = msk.read_msk(FILE)
                # reshape the nifti for testing
                print(data.shape)
                #header.set_data_dtype(np.uint8) 
                #80, 71, 96
                #data = data.reshape(87,69,60)
                print(data.shape)
                #End
                
                basename = FILE.split(os.extsep, 1)[0]
                outname = "{}.nii.gz".format(basename)
                # Export nifti (assign an identity matrix as affine with default header)
                img = nb.Nifti1Image(data, affine=np.eye(4))
                nb.save(img, outname)
                print(os.path.join(root,file)+"\nComplete")
    print("Convert Complete!")
    return path

if __name__ =="__main__":
    msk_shape_nii('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/15Aug/msk transfer')

