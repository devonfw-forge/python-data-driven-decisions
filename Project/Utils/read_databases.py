#||||||||||START OF MAIN CODE|||||||||||||

#Explore all the files from the specified directory in read_path
#If the file is a .csv, try to read it, preprocess it and append it to the list of dataframes
#If any error is raised during the process, it appends the url to the list of discarded files and shows a warning at the end


from os import listdir
from os.path import isfile, join
import warnings

import pandas as pd

from Utils.preprocess import preprocess

def read_databases(read_path: str, special_source = None, verbose = False):

    url_list = []
    discarded_urls = []
    data_list = []
    data_dict = {}
    
    for element in listdir(read_path):
            url = join(read_path, element)
            if isfile(url) and url.endswith('.csv'):
                url_list.append(url)
                if 'WID' in url:
                    continue
                try:
                    dataframe = pd.read_csv(url)
                except:
                    print('Unable to read dataframe: ' + url)
                    discarded_urls.append(url)
                else:
                    special = None
                    for source in special_source:
                        if source in url.lower():
                            special = source
                            break
                    
                    try:
                        dataframe = preprocess(dataframe, treatment = special)
                    except:
                        print('Unexpected error when preprocessing the dataframe: ' + url)
                        discarded_urls.append(url)
                    else:
                        url_list.append(url)
                        data_list.append(dataframe)
                        data_dict[url] = dataframe

    if len(discarded_urls) > 0:
            warn = 'Unable to read the following files:'
            for url in discarded_urls:
                warn += '\n' + url
            warnings.warn(warn)                    
                        
    if (verbose):
        for data in data_list:
            print(data)
            print('\n' + '----------------------------------------------------------' + '\n')
    else:
        print('Done')
    
    return data_dict, data_list