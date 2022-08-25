#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 01:52:21 2022

@author: gangxinli
"""
import os
import numpy as np
import nibabel as nb
import vtc


# FILE = "/home/faruk/Documents/test_bvbabel/vtc_test.vtc"

# # =============================================================================
# # Load vmr
# header, data = vtc.read_vtc(FILE)

# # See header information
# pprint(header)

# # Export nifti
# basename = FILE.split(os.extsep, 1)[0]
# outname = "{}_bvbabel.nii.gz".format(basename)
# img = nb.Nifti1Image(data, affine=np.eye(4))
# nb.save(img, outname)

# print("Finished.")

def vtc_to_nii(path = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/vtc_vmr"):
    print("Transfering vtc file to nii file")
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.split(".")[-1] == 'vtc':
                FILE = os.path.join(root,file)
         
                header, data = vtc.read_vtc(FILE)
                # Save nifti for testing
                basename = FILE.split(os.extsep, 1)[0]
                outname = "{}.nii.gz".format(basename)
                    
                # Export nifti (assign an identity matrix as affine with default header)
                # np.eye(4)*n, n control the resoultion
                n=header.get('Data type (1:short int, 2:float)')
                print("resolution:"+str(n))
                img = nb.Nifti1Image(data,affine=np.eye(4)*n)
                # img = nb.Nifti1Image(data,affine=np.eye(4))
                nb.save(img, outname)
                print(os.path.join(root,file)+"\nComplete")
    print("Convert Complete!")
    return path

if __name__ =="__main__":
    vtc_to_nii('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/25Aug')



