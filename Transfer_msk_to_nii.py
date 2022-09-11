#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:49:04 2022

@author: gangxinli
"""
import os
import numpy as np
import nibabel as nb
import vtc
import msk

def msk_to_nii(path = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/vtc_vmr"):
    print("Transfering msk file to nii file")
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.split(".")[-1] == 'msk':
                FILE = os.path.join(root,file)
         
                header, data = msk.read_msk(FILE)
                # Save nifti for testing
                basename = FILE.split(os.extsep, 1)[0]
                outname = "{}.nii".format(basename)
                # Export nifti (assign an identity matrix as affine with default header)
                # n=header.get('Data type (1:short int, 2:float)')
                # print("resolution:"+str(n))
                # img = nb.Nifti1Image(data,affine=np.eye(4)*n)
                img = nb.Nifti1Image(data, affine=np.eye(4))
                nb.save(img, outname)
                print(os.path.join(root,file)+"\nComplete")
    print("Convert Complete!")
    return path

if __name__ =="__main__":
    msk_to_nii('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal')

