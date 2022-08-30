#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:24:19 2022

@author: gangxinli
"""


def write_header(header,path):
    
    with open(path,'w+') as f:
        for value in header:
            f.write(str(value)+":"+str(header[value])+"/n")
        f.close()
    



if __name__ == '__main__':
    write_header("","")