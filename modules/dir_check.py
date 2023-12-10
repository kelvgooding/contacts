#!/bin/usr/python3

"""
Author: Kelvin Gooding
Created: 2023-12-05
Updated: 2023-12-05
Version: 1.0
"""

# Modules

import os

def check_dir(base_path, dir_name):
    
    filepath = os.path.join(base_path, dir_name)

    if dir_name in os.listdir(base_path):
        print('Directory already exists. No action required.')
    else:
        print(f'This directory does not exist. Creating directory - {dir_name}')
        os.mkdir(f'{filepath}')
