#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:29:09 2022

@author: gangxinli
"""
import struct
import numpy as np
from bvbabel.utils import read_variable_length_string
from bvbabel.utils import write_variable_length_string
import nibabel as nib



# =============================================================================
def read_nii_write_vmp(filename,header_path):
    """Protocol to write Brainvoyager VTC file.

    Parameters
    ----------
    filename : string
        Path to file.
    header : dictionary
        Pre-data and post-data headers.
    data_img : 3D numpy.array
        Image data.

    """
    img=nib.load(filename)
    header = img.header
    affine = img.affine
    zooms = header.get_zooms()
    data_img=img.dataobj
    header = read_header(header_path)

    with open(filename+'.vmp', 'wb') as f:
        data = header["File version"]
        f.write(struct.pack('<h', data))
        for key,value in header.items:
            f.write(struct.pack('<h',value)
        
        
        # The spatial dimensions can be computed from the header info as follows (Resolution should be "1" at present):
        
        # DimX = (XEnd - XStart + 1) / Resolution
        # DimY = (YEnd - YStart + 1) / Resolution
        # DimZ = (ZEnd - ZStart + 1) / Resolution
        
        # Note that the axes terminology follows the internal BrainVoyager format. The mapping to Talairach axes is as follows:
        
        # BV X front -> back = Y in Tal space
        # BV Y top -> bottom = Z in Tal space
        # BV Z left -> right = X in Tal space
        # ---------------------------------------------------------------------
        # Write VTC data
        # ---------------------------------------------------------------------
       
        
       
        
       
        
        
        data_img = data_img[::-1, ::-1, ::-1, :]  # Flip BV axes
        data_img = np.transpose(data_img, (0, 2, 1, 3))  # Tal to BV
        data_img = np.reshape(data_img, data_img.size)

        if int(header["Data type (1:short int, 2:float)"]) == 1:
            for i in range(data_img.size):
                f.write(struct.pack('<h', data_img[i]))
        elif int(header["Data type (1:short int, 2:float)"]) == 2:
            for i in range(data_img.size):
                f.write(struct.pack('<f', data_img[i]))
        else:
            raise("Unrecognized VMP data_img type.")

def read_header(path):
    raw =[]
    with open(path,'r') as f:
        raw = f.readlines()
    f.close()
    header = {}
    raw = raw[0].split('/n')
    for row in raw[:-1]:
        row = row.rsplit(":",1)
        header[row[0]]=row[1]
      
    return header



if __name__ == '__main__':
    filename = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/VMP_Test/Hook_header_test/sub-sid000013_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii'
    header_path='/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/VMP_Test/Hook_header_test/header'
    read_nii_write_vmp(filename,header_path)

    
    
    
    
    
    
    