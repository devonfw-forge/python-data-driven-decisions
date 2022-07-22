#Explore all the files from the specified directory in read_path
#If the file is a .csv, try to read it, preprocess it and append it to the list of dataframes
#If any error is raised during the process, it appends the url to the list of discarded files

import pandas as pd
import warnings
from os import listdir
from os.path import isfile, join

def read_data(read_path: str, warn = False):
    """
        Explore all the files in read_path.
        If the file is .csv and can be read, add it to a dictionary which key is the url of the file.
        If it could not be read, append it to a discarded url list.
        Return both the dictionary {url:df} and the list with unreadable urls.

        PARAMETERS:
            read_path: str,
                string containing the path to the directory to be exploring.
            warn: bool, default False
                wether it will raise a warning if any file detected as .csv could not be read.
        
        RETURNS:
            data_dict: Dict,
                a dictionary with keys as successfully read urls and the corresponding dataframe as its value.
            discarded_urls: List,
                a list with all the discarded urls that could not be read.
     """

    #The dict and list that will be returned.
    data_dict = {}
    
    #Explore the directory, read csv and save the dataframes into the dictionary.
    #Write in a list the faulty urls.
    for element in listdir(read_path):
            url = join(read_path, element)
            if isfile(url) and url.endswith('.csv'):
                data_dict[url] = pd.read_csv(url, on_bad_lines = 'warn')
    
    return data_dict