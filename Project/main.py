

import os
from Project.Utils.merge_data import merge_data
from Project.Utils.preprocess import preprocess

from Project.Utils.read_databases import read_databases
from Project.Utils.divide_country import country_divider

read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes
columns_index = ('Country', 'Year')
indicators = {}
columns_rename = {}
year_range = range(1950, 2050)
dict_df_countries = {} #Dictionary that relates each country to its dataframe

def main():
    dict_dataframes = read_databases(read_path)
    #for df in dict_dataframes.values():
    #    preprocess(df, columns_index, indicators, columns_rename, year_range, inplace = True)
    data_list = list(dict_dataframes.values())
    df = merge_data(data_list, columns_index)
    
    country_divider(df, dict_df_countries)

    dict_df_countries['Spain'].to_csv(write_path + '/Finaldf.csv')

    print(dict_df_countries.get('Spain').corr())





if __name__ == '__main__':
    main()