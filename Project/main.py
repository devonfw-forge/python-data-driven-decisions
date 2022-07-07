

import os
from Project.Utils.merge_data import merge_data
from Project.Utils.preprocess import preprocess

from Project.Utils.read_data import read_data

from Project.Utils.normalize import normalize


read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes
columns_index = ('Country', 'Year')
indicators = {}
columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], 'Country') #Dictionary to rename all the index columns so they have a common name

year_range = range(1950, 2050)

def main():
    data_dict, _ = read_data(read_path)
    #for df in dict_dataframes.values():
    #    preprocess(df, columns_index, indicators, columns_rename, year_range, inplace = True)
    
    for url, daf in data_dict.items():
        #print(columns_rename)
        #var=preprocess(url = url, df = daf, columns_index = columns_index, columns_rename = columns_rename, inplace = True)
        #var.to_csv(write_path + '/6.csv')
        try:
            daf = preprocess(url = url, df = daf, columns_index = columns_index, columns_rename = columns_rename, inplace = True)
            print('Columnas')
            print(daf.columns)
            daf.to_csv(write_path + '/6.csv')
            normalize(df = daf, columns_index = columns_index, inplace = True)
        except Exception as e:
            print('ERROR')
            print(e)
        else:
            print(url)
    
    data_list = list(data_dict.values())
    df = merge_data(data_list, columns_index)
    print(df)

if __name__ == '__main__':
    main()