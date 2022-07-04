

import pandas as pd


def merge_data(data_list, columns_index):

    final_df = data_list[0]
    column_country, column_year = columns_index

    final_df[column_year]= final_df[column_year].astype(str)
    final_df[column_country]= final_df[column_country].astype(str)

    #Merge all the different databases into one single dataframe with the format: columns_index + indicators
    for data in data_list[1:]:
        data[column_year]= data[column_year].astype(str)
        data[column_country]= data[column_country].astype(str)
        final_df = pd.merge(final_df, data, on = columns_index, how = "outer")

    #final_df contains the whole merged dataframe
    return final_df