import os
import numpy as np
import pandas as pd

COUNTRY = 0
YEAR = 1
POPULATION = 'Population'

def aggregate(df: pd.DataFrame, aggregate_by: str, for_index: str, weight: str = POPULATION, new_group_col_name: str = 'GROUP', group_name: str = 'New Group', abs_indicators: list = []):
    
    """
        Take a DataFrame and calculate the estimated weighted average or summatory for its columns.
        The resulting DataFrame will have an entry for each member of for_index, and will have the aggregated vaalues for every aggregate_by members.
        The data will be aggregated using a weighted average by default, except for the columns in abs_indicators, which will be aggregated as a summatory.
        Return dataframe if inplace is False.
        
        PARAMETERS:
            dataframe: df
                the source DataFrame. It must be multi-index, of which aggregate_by and for_index must be names of members of said multi-index
            aggregate_by: str
                name of the multi-index column which will be aggregated by.
            for_index: str
                name of the multi-index column which will be respected during the aggregation, resulting in a row in the aggregated DataFrame for each of its values.
            weight: str, default POPULATION
                name of the column which will have the values used to weight the mean. If no absolute indicator is used, the result can be unexpected.
            new_group_col_name: str, default 'GROUP
                name of the multi-index member in the new DataFrame, altogether with for_index.
            group_name: str, default 'New Group'
                value to be written in the new_group_col_name multi-index member.
            abs_indicators: list, default []
                list with the names of the columns whose aggregate will be calculated as a summatory instead of a weighted average.
        
        RETURNS:
            DataFrame
                Return a DataFrame with the multi-index (new_group_col_name, for_index) and a row for each different for_index value. It will have the same number of columns as the original, with the values estimated as the weighted average or a summatory of its original values. 
    """
    
    res_df = pd.DataFrame()
    group_pos = df.index.names.index(aggregate_by)
    entry_pos = df.index.names.index(for_index)

    #Save the names that will be used for the result DataFrame multi-index
    group_col_name = df.index.names[group_pos]
    entry_col_name = df.index.names[entry_pos]

    member_list = set(df.index.get_level_values(group_pos))
    entry_list = set(df.index.get_level_values(for_index))
    indicator_list = df.columns
    
    for entry in entry_list:

        #Create an empty dictionary that will be filled with the calculated value for each indicator
        indicator_dict = {}

        for indicator in indicator_list:
            sum = 0
            #For absolute indicators, apply the normal summatory of all terms
            if indicator in abs_indicators:
                for member in member_list:
                    c_val = df.loc[(df.index.get_level_values(group_col_name) == member) & (df.index.get_level_values(entry_col_name) == entry)].iloc[0][indicator]
                    #Ignore if None or NaN
                    if c_val is None or np.isnan(c_val):
                        continue
                    else:
                        sum += c_val

                indicator_dict[indicator] = sum
            #For relative indicators, calculate the weighted average based on population
            else:
                t_pop = 0
                for member in member_list:
                    c_ind = df.loc[(df.index.get_level_values(group_col_name) == member) & (df.index.get_level_values(entry_col_name) == entry)].iloc[0][indicator]
                    c_pop = df.loc[(df.index.get_level_values(group_col_name) == member) & (df.index.get_level_values(entry_col_name) == entry)].iloc[0][weight]
                    

                    #Ignore if any is None or NaN
                    if c_ind is None or c_pop is None or np.isnan(c_ind) or np.isnan(c_pop):
                        continue
                    else:
                        sum += c_ind*c_pop
                        t_pop += c_pop
                #If no data available, write a None to avoid dividing by 0
                if t_pop == 0 or sum == 0:
                    mean_value = None
                

                else:
                    mean_value = sum / t_pop
                #Fill the dictionary with the values calculated
                indicator_dict[indicator] = mean_value
            
        #Create a Series from the dictionary, including a column for the region and year, and append it to the aggregated DataFrame    
        entry_series = pd.Series({new_group_col_name: group_name, entry_col_name: entry} | indicator_dict)
        res_df = pd.concat([res_df, entry_series], axis = 1)
    #Transpose to respect the original format of the DataFrame, set the multi-index and return the result DataFrame
    res_df = res_df.transpose()
    res_df.set_index([new_group_col_name, entry_col_name], inplace = True)
    return res_df