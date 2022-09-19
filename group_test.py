#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:50:17 2022

@author: gangxinli
"""
from isc_standalone import (isc, isfc, bootstrap_isc, permutation_isc,
                            timeshift_isc, phaseshift_isc,
                            compute_summary_statistic, load_images,
                            load_boolean_mask, mask_images,
                            MaskedMultiSubjectData)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, pearsonr, zscore
from scipy.spatial.distance import squareform
from statsmodels.stats.multitest import multipletests
import nibabel as nib

from isc_cli import load_data


data0path = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal/sub-sid000007_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii'
data1path = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal/sub-sid000009_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii'
data2path = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal/sub-sid000010_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii'
data3path = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal/sub-sid000005_task-movie_run-05_bold_SCCAI_3DMCTS_THPGLMF3c_256_trilin_2x1.nii'
mask = '/Users/gangxinli/Desktop/Internship/Neuro/Neuro_ISC/Data/11Sep/vtc_tal/VTC_TALmask.nii'
data, affine, header, input_fns = load_data([data0path,data1path,data2path,data3path],mask=mask)


iscs = isc(data, pairwise=True, summary_statistic=None)





# #movie comparation
# # iscs = isc(data, pairwise=True)
# # observed, p, distribution = permutation_isc(iscs, pairwise=True,
# #                                             summary_statistic='median',
# #                                             n_permutations=200)

# # Inspect shape of null distribution
# # print(f"Null distribution shape = {distribution.shape}"
# #       f"\ni.e., {distribution.shape[0]} permutations "
# #       f"and {distribution.shape[1]} voxels")

# # # Get actual ISC value and p-value for first voxel
# # print(f"Actual observed ISC value for first voxel = {observed[0][0]:.3f},"
# #       f"\np-value from permutation test = {p[0]:.3f}")


# #groupd comparation

# # Create data with noisy subset of subjects
# data1=[data0path,data1path]
# data2=[data2path,data3path]
# data1 = load_data(data1,mask=mask)
# data2 = load_data(data2,mask=mask)

# n_subjects = 4
# n_TRs = 1000
# n_voxels = 803

# noisy_data = np.dstack((np.dstack((
#     simulated_timeseries(n_subjects // 2, n_TRs,
#                          n_voxels=n_voxels, noise=1))),
#                         np.dstack((
#     simulated_timeseries(n_subjects // 2, n_TRs,
#                          n_voxels=n_voxels, noise=5)))))

# noisy_data = np.dstack((np.dstack((data1[0],data2[0]))))
                                   
                                   
                    

# # Create group_assignment variable with group labels
# group_assignment = [1]*10 + [2]*10
# print(f"Group assignments: \n{group_assignment}")

# # Compute ISCs and then run two-sample permutation test on ISCs
# iscs = isc(noisy_data, pairwise=True, summary_statistic=None)
# observed, p, distribution = permutation_isc(iscs,
#                                             group_assignment=group_assignment,
#                                             pairwise=True,
#                                             summary_statistic='median',
#                                             n_permutations=200)




