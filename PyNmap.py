#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Chris Patrick"
__email__ = "chrisbp@yahoo.com"
__date_ = "Spring 2020"
__version__ = "0.0.1"

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

# SET VARIABLES
my_dir = 'D:/Chris school/Logon ID'
my_pickle = '.pickle.xml'
nmap_path = 'C:/Program Files (x86)/Nmap/nmap.exe'
nmap_network = '192.168.1.0/24'

def create_directory():
    if(os.path.isdir(my_dir)) == False:
        try:
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir)
        except OSError:
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir)

def write_files(data):
    # write the pickle file
    with open(my_dir + '/' + date.today().strftime("%m%d%y") + my_pickle, 'wb') as fp:
        pickle.dump(data, fp)
    fp.close()

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4 -oX -", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    print(nmap_data)
    return nmap_data


create_directory()
nmap_data = run_nmap()
write_files(nmap_data)
