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
def read_nii_write_vmp(filename):
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
    
    with open(filename, 'wb') as f:
        data = header["sizeof_hdr"]
        f.write(struct.pack('<h', data))


        data = header["data_type"]
        write_variable_length_string(f, data)


        data = header["db_name"]
        f.write(struct.pack('<h', data))
        

        data = header["extents"]
        f.write(struct.pack('<h', data))
        

        data = header["session_error"]
        f.write(struct.pack('<h', data))
        

        data = header["regular"]
        f.write(struct.pack('<h', data))
        

        data = header["dim_info"]
        f.write(struct.pack('<h', data))
        

        data = header["dim"]
        f.write(struct.pack('<h', data))
        

        data = header["intent_p1"]
        f.write(struct.pack('<h', data))
                

        data = header["intent_p2"]
        f.write(struct.pack('<h', data))
                

        data = header["intent_p3"]
        f.write(struct.pack('<h', data))
                

        data = header["intent_code"]
        f.write(struct.pack('<h', data))
                

        data = header["datatype"]
        f.write(struct.pack('<h', data))
                

        data = header["bitpix"]
        f.write(struct.pack('<h', data))
                

        data = header["slice_start"]
        f.write(struct.pack('<h', data))
                

        data = header["pixdim"]
        f.write(struct.pack('<h', data))
                

        data = header["vox_offset"]
        f.write(struct.pack('<h', data))
                

        data = header["scl_slope"]
        f.write(struct.pack('<h', data))
                

        data = header["scl_inter"]
        f.write(struct.pack('<h', data))
                        

        data = header["slice_end"]
        f.write(struct.pack('<h', data))
                        

        data = header["slice_code"]
        f.write(struct.pack('<h', data))
                        

        data = header["xyzt_units"]
        f.write(struct.pack('<h', data))
                        

        data = header["cal_max"]
        f.write(struct.pack('<h', data))
                        

        data = header["cal_min"]
        f.write(struct.pack('<h', data))
                        

        data = header["slice_duration"]
        f.write(struct.pack('<h', data))
                        

        data = header["toffset"]
        f.write(struct.pack('<h', data))
                        

        data = header["glmax"]
        f.write(struct.pack('<h', data))
                        

        data = header["glmin"]
        f.write(struct.pack('<h', data))
                        

        data = header["descrip"]
        f.write(struct.pack('<h', data))
                        

        data = header["aux_file"]
        f.write(struct.pack('<h', data))
                        

        data = header["qform_code"]
        f.write(struct.pack('<h', data))
                        

        data = header["quatern_b"]
        f.write(struct.pack('<h', data))
                        

        data = header["sform_code"]
        f.write(struct.pack('<h', data))
                        

        data = header["quatern_b"]
        f.write(struct.pack('<h', data))
                        

        data = header["quatern_c"]
        f.write(struct.pack('<h', data))
                        

        data = header["quatern_d"]
        f.write(struct.pack('<h', data))
                        

        data = header["qoffset_x"]
        f.write(struct.pack('<h', data))
                        

        data = header["qoffset_y"]
        f.write(struct.pack('<h', data))
                        

        data = header["qoffset_z"]
        f.write(struct.pack('<h', data))
                        

        data = header["srow_x"]
        f.write(struct.pack('<h', data))
                        

        data = header["srow_y"]
        f.write(struct.pack('<h', data))
                        

        data = header["srow_z"]
        f.write(struct.pack('<h', data))
                        

        data = header["intent_name"]
        f.write(struct.pack('<h', data))
                        

        data = header["magic"]
        f.write(struct.pack('<h', data))

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

        if header["Data type (1:short int, 2:float)"] == 1:
            for i in range(data_img.size):
                f.write(struct.pack('<h', data_img[i]))
        elif header["Data type (1:short int, 2:float)"] == 2:
            for i in range(data_img.size):
                f.write(struct.pack('<f', data_img[i]))
        else:
            raise("Unrecognized VTC data_img type.")

if __name__ == '__main__':
    read_nii_write_vmp('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/VMP_Test/sub-sid000278_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii')