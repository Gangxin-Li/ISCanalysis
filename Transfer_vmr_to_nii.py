#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 03:39:55 2022

@author: gangxinli
"""
import os
import numpy as np
import nibabel as nb
import vmr

# FILE = "/home/faruk/Documents/test_bvbabel/derivatives/T1_int16.vmr"

# # =============================================================================
# # Load vmr
# header, data = bvbabel.vmr.read_vmr(FILE)

# # See header information
# pprint.pprint(header)

# # Export nifti
# basename = FILE.split(os.extsep, 1)[0]
# outname = "{}_bvbabel.nii.gz".format(basename)
# img = nb.Nifti1Image(data, affine=np.eye(4))
# nb.save(img, outname)

# print("Finished.")



def vmr_to_nii(path = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/vtc_vmr"):
    print("Transfering vmr file to nii file")
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.split(".")[-1] == 'vmr':
                FILE = os.path.join(root,file)
         
                header, data = vmr.read_vmr(FILE)
                # Save nifti for testing
                basename = FILE.split(os.extsep, 1)[0]
                outname = "{}_bvbabel.nii.gz".format(basename)
                # Export nifti (assign an identity matrix as affine with default header)
                img = nb.Nifti1Image(data, affine=np.eye(4))
                nb.save(img, outname)
                print(os.path.join(root,file)+"\nComplete")
    print("Convert Complete!")
    return path

if __name__ =="__main__":
    vmr_to_nii()




