# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:47:02 2019

@author: nsde
"""

#%%
import os, requests
import numpy as np
import pandas as pd

#%%
def get_path(file):
    """ Get the path of the input file """
    return os.path.realpath(file)

#%%
def get_dir(file):
    """ Get directory of the input file """
    return os.path.dirname(os.path.realpath(file))

#%%
def create_dir(direc):
    """ Create a dir if it does not already exists """
    if not os.path.exists(direc):
        os.mkdir(direc)

#%%
def check_if_file_exist(file):
    return os.path.isfile(file)

#%%
def get_uci_table():
    try:
        d = get_dir(__file__)
        if not check_if_file_exist(d + '/' + 'database.csv'):
            print('Initializing dataset table')
            df = pd.read_html('https://archive.ics.uci.edu/ml/datasets.php')
            df = df[5] # all the dataset information is stored here
            header = df.iloc[0]
            header[0] = 'Name'
            df = pd.DataFrame(df.values[1:], columns=header.values)
            df.to_csv(d + '/' + 'database.csv', sep=',', na_rep='nan', index=False)
        else:
            df = pd.read_csv(d + '/' + 'database.csv', sep=',')
        return df
    except:
        print('Could not initialize database of datasets')
        
#%%
def add_and_clean_uci_table(uci_table):
    df = pd.DataFrame(
            [
             ['Housing', 'Multivariate', 'Regression', 'Real', 506, 14, 1993],
             ['Wine Red', 'Multivariate', 'Regression', 'Real', 4898, 13, 1991],
             ['Wine White', 'Multivariate', 'Regression', 'Real', 1599, 13, 1991]
            ], 
            columns=uci_table.columns)
    df['download_link'] = 

#%%
def download_file(url,directory):
    """
    Downloads a file from a given url into the given directory.
    """
    local_filename = directory+'/'+url.split('/')[-1]
    if not check_if_file_exist(local_filename):
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        try:
            print('Downloading file: ', url)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
        except:
            print("Sorry could not write this particular file:")
            print(url)
    return local_filename
            
#%% 
def convert_to_numeric(input_target):
    if input_target.dtype == 'object':
        out_target = np.zeros_like(input_target)
        labels = np.unique(input_target)
        for i, l in enumerate(labels):
            out_target[np.where(input_target==l)] = i
        return out_target
    else:
        return input_target
