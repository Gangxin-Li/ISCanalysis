#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:09:12 2022

@author: gangxinli
"""

"""Read BrainVoyager FMR file format."""

import os
import numpy as np
import nibabel as nb
import fmr

FILE = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/movie_8/sub005_M/sub-sid000005_task-movie_run-01_bold_SCCAI_3DMCTS_THPGLMF3c.fmr"

# # =============================================================================
# # Load fmr
# header, data = fmr.read_fmr(FILE)

# # Save nifti for testing
# basename = FILE.split(os.extsep, 1)[0]
# outname = "{}_bvbabel.nii.gz".format(basename)

# # Export nifti (assign an identity matrix as affine with default header)
# img = nb.Nifti1Image(data, affine=np.eye(4))
# nb.save(img, outname)

# # -----------------------------------------------------------------------------
# # NOTE[Faruk]: I need to think about exporting nifti with a header that matches
# # the fmr header fields

# # Export nifti (Pull affine matrix from fmr header)
# # affine = header["Transformation information"]["Transformation matrix"]
# # img = nb.Nifti1Image(data, affine=affine)
# # nb.save(img, outname)
# # -----------------------------------------------------------------------------

# print("Finished.")


def fmr_to_nii(path = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/movie_8/"):
    print("Transfering fmr file to nii file")
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.split(".")[-1] == 'fmr':
                FILE = os.path.join(root,file)
         
                header, data = fmr.read_fmr(FILE)
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
    fmr_to_nii()









