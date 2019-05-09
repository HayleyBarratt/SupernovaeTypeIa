#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:23:36 2019

@author: hayleybarratt-bentley
"""

from astropy.io import fits
import shutil
import os 

### So if you input your folder path for where your fits folders are located over my path in this code it should work


files_in_dir = os.listdir("/Users/hayleybarratt-bentley/Documents/Data")
fits_in_dir = [file for file in files_in_dir if file.endswith("fits")]
for file in fits_in_dir:
    file_path = os.path.join("/Users/hayleybarratt-bentley/Documents/Data", file)
    with fits.open(file_path) as f:
        hdr = f[0].header
        fltr = hdr["FILTER"]
        date = hdr["DATE"]
        obj="Gaia18ccw"
        
    #For new path post the path you wish your new file to go into (it can be a completely new folder if you wish, just ensure it
    # is followed by /{obj}_{fltr}_{date}.fits )
    new_path = f"/Users/hayleybarratt-bentley/Documents/Data/{obj}_{fltr}_{date}.fits"
    shutil.move(file_path, new_path)
    
    
#This version below is for single files rather than a folder so shouldn't be needed anymore
'''
with fits.open("/Users/hayleybarratt-bentley/Documents/2019 observables/Gaia19AMJ/new-image (5).fits") as f:
    hdr = f[0].header
    fltr = hdr["FILTER"]
    date = hdr["DATE"]
    obj="Gaia19amj"

shutil.move("/Users/hayleybarratt-bentley/Documents/2019 observables/Gaia19AMJ/new-image (5).fits", f"/Users/hayleybarratt-bentley/Documents/2019 observables/Gaia19AMJ/{obj}_{fltr}_{date}")
'''