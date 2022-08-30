#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 23:17:56 2022

@author: gangxinli
"""


import os
import glob
import numpy as np
from numpy.fft import fft, ifft, fftfreq
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.animation import FuncAnimation
import seaborn as sns
from nltools.data import Brain_Data, Adjacency
from nltools.mask import expand_mask, roi_to_brain
from nltools.stats import isc, isfc, isps, fdr, threshold, phase_randomize, circle_shift, _butter_bandpass_filter, _phase_mean_angle, _phase_vector_length
from nilearn.plotting import view_img_on_surf, view_img
from sklearn.metrics import pairwise_distances
from sklearn.utils import check_random_state
from scipy.stats import ttest_1samp
from scipy.signal import hilbert
import networkx as nx
from IPython.display import HTML
import warnings

warnings.filterwarnings('ignore')
# import nest_asyncio
# nest_asyncio.apply()
import datalad.api as dl


import nibabel as nib
# import skimage.io as io
# import numpy as np


# from glob import glob
# import numpy as np
# import nibabel as nib
# from nilearn.plotting import (find_xyz_cut_coords,
#                               plot_connectome,
#                               plot_stat_map)
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import pearsonr
# from scipy.spatial.distance import squareform
# from brainiak.isc import isc, isfc




# img=nib.load('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/25Aug/VTC_TALmask.nii')
# header = img.header
# print(header["File version"])

# print(str(header).split('/n')[0].split('/n')[0])


# img_arr=img.get_fdata()
# print(img_arr.shape)
# img_arr=np.squeeze(img_arr)

# mask = Brain_Data('http://neurovault.org/media/images/2099/Neurosynth%20Parcellation_0.nii.gz')
# mask_x = expand_mask(mask)

# mask.plot()

# mask = Brain_Data('http://neurovault.org/media/images/2099/Neurosynth%20Parcellation_0.nii.gz')
img=nib.load('/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/30Aug/1610/0100.nii')

# print(img.header)
# print(img.get_fdata())
filepath = "/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/30Aug/1610/0100.txt"
with open(filepath,'w+') as f:
    data = img.get_fdata()
    data = np.array(data)
    for value in data:
        for v in value:
            for vv in v:
                f.write(str(vv[0]))
    f.close()
# data = img.get_fdata()
# print(data)
# for value in data:
#     for v in value:
#         for vv in v:
#             print(vv)
   

# data_dir = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/Sherlock'

# # If dataset hasn't been installed, clone from GIN repository
# if not os.path.exists(data_dir):
#     dl.clone(source='https://gin.g-node.org/ljchang/Sherlock', path=data_dir)

# # Initialize dataset
# ds = dl.Dataset(data_dir)

# # Get Cropped & Denoised CSV Files
# result = ds.get(glob.glob(os.path.join(da/ta_dir, 'fmriprep', '*', 'func', f'*Average_ROI*csv')))



# mask = Brain_Data('http://neurovault.org/media/images/2099/Neurosynth%20Parcellation_0.nii.gz')
# mask_x = expand_mask(mask)

# mask.plot()


