#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 04:00:10 2022

@author: gangxinli
"""
import psutil
 
def getPCInfo():
 
    M = 1024*1024
     
    G = M * 1024
     
    mem = psutil.virtual_memory()
     
    #print('summary: ', mem)
    
    print('total:%dM    %.2fG'%(mem.total//M, mem.total/G))
     
    print('available:%dM    %.2fG'%(mem.available//M, mem.available/G))
     
    print('used:%dM    %.2fG'%(mem.used//M, mem.used/G))
     
    print('free:%dM    %.2fG'%(mem.free//M, mem.free/G))
    
    print('active:%dM    %.2fG'%(mem.active//M, mem.active/G))
    
    print('inactive: %dM    %.2fG'%(mem.inactive//M, mem.inactive/G))
    
    print('percent:%d%%'% mem.percent)
    
    #print('swap memery:', psutil.swap_memory())
