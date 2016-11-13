# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:53:11 2016

@author: nazario
"""

import os
import shutil

work_dir = '/media/nazario/SAMSUNG/COSMIC'
sr_dir='cosmic2013 (4)'
ds_dir='cosmic2013 (3)'
root_src_dir = os.path.join(work_dir,sr_dir)
root_dst_dir = os.path.join(work_dir,ds_dir)
print(root_src_dir)

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)