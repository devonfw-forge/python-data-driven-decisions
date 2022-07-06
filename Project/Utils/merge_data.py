

import pandas as pd


def merge_data(data_list, columns_index):

    final_df = data_list[0]
    column_country, column_year = columns_index


    #Merge all the different databases into one single dataframe with the format: columns_index + indicators
    for data in data_list[1:]:
        final_df = pd.merge(final_df, data, on = columns_index, how = "outer")

    #final_df contains the whole merged dataframe
    return final_df