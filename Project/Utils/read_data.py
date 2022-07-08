#||||||||||START OF MAIN CODE|||||||||||||

#Explore all the files from the specified directory in read_path
#If the file is a .csv, try to read it, preprocess it and append it to the list of dataframes
#If any error is raised during the process, it appends the url to the list of discarded files and shows a warning at the end

import pandas as pd

from os import listdir
from os.path import isfile, join
import warnings


#from Project.Utils.preprocess import preprocess

def read_data(read_path: str, warn = False):

    data_dict = {}
    discarded_urls = []
    #columns_index = ('Country', 'Year') #Dupe, original in main class
    
    #special_source = ['databank', 'faostat', 'kaggle', 'un_data', 'worldbank', 'WID'] #List with all the sources that need special treatment

    #columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], columns_index[0]) #Dictionary to rename all the index columns so 
    
    for element in listdir(read_path):
            url = join(read_path, element)
            if isfile(url) and url.endswith('.csv'):
                if 'WID' in url:
                    continue
                try:
                    dataframe = pd.read_csv(url)
                except:
                    print('Unable to read dataframe: ' + url)
                    discarded_urls.append(url)
                else:
                    data_dict[url] = dataframe

    if warn and len(discarded_urls) > 0:
            warn = 'Unable to read the following files:'
            for url in discarded_urls:
                warn += '\n' + url
            warnings.warn(warn)                    
                        
    #if (verbose):
        #for data in data_dict.values():
         #   print(data)
          #  print('\n' + '----------------------------------------------------------' + '\n')
    #else:
    #    print('Done')
    
    return data_dict, discarded_urls