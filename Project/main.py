

import os
from Project.Utils.merge_data import merge_data

from Project.Utils.read_databases import read_databases


read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes
columns_index = ('Country', 'Year')

def main(self):
    dict_dataframes = read_databases(read_path)
    df = merge_data(dict_dataframes.values(), )

