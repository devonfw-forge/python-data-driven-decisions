import pandas as pd

from Project.Utils.norm import norm
from Project.Utils.corr_confidence import corr_confidence

col_country = 'Country'
col_year = 'Year'
col_shift = 'Shift'
col_gdp = 'GDP'

def shift_corr (df: pd.DataFrame, level: str, col: str = col_gdp, confidence: float = 0.05, shifts: range = None):

    """ 
        Apply time shifting and find the correlations between the GDP and the rest of the columns.

        PARAMETERS:
            df: pd.DataFrame
                The DataFrame to read the data from.
            level: str
                Name of the index level that contains the element for which the correlations will be computed.
            col: str, default = col_gdp
                Name of the column that whose correlation with all others will be computed.
            confidence: float, default = 0.05
                Level of confidence for the correlation. It is passed to the corr_confidence method to filter out non-significative correlations.
            shifts: range, default = None
                The range of shifts to be used to compute correlations. By default, it will be the whole possible range.
        RETURNS:
            pd.DataFrame
                DataFrame with the correlations for each element and each shift as its index.

    """

    # Normalize the values of the DataFrame.
    norm_df = norm(df)

    # Identify the range of years in our Dataframe.
    min_year = df.index.get_level_values(col_year).min()
    max_year = df.index.get_level_values(col_year).max()

    area_list = list(set(df.index.get_level_values(level)))
    area_list.sort()

    # Initialize a list to store the correlations for each area. They will then be concatenated.
    corr_df_list = []

    if shifts is None:
        shifts = range(min_year - max_year + 1, max_year - min_year)

    for shift in shifts:
        # Initialize a list to store the correlations for each time shift. They will then be concatenated.
        corr_s_list = []
        for area in area_list:
            # In order to study the effects over the time, we need to analyse the correlation between two different periods shifted X years from each other.
            # A positive shift studies the effect of the indicators on the GDP.
            # A negative shift studies the effect of the GDP on the indicators.
            min_year_gdp = min_year + max(shift, 0)
            max_year_gdp = max_year - min(shift, 0)

            min_year_ind = min_year + min(shift, 0)
            max_year_ind = max_year - max(shift, 0)

            # Store a Series for the GDP column and a Dataframe for all the other columns with indicators.
            col_s = norm_df.loc[(df.index.get_level_values(col_year) >= min_year_gdp) & (norm_df.index.get_level_values(level) == area), col]
            ind_df = norm_df.loc[(df.index.get_level_values(col_year) <= max_year_ind) & (norm_df.index.get_level_values(level) == area)].drop(columns = col)

            # Sort both so they have the same order and can have their index dropped. This is mandatory to calculate the correlation having different years in their index.
            col_s.sort_index(level = [col_country, col_year])
            ind_df.sort_index(level = [col_country, col_year])

            col_s = col_s.reset_index(drop = True)
            ind_df = ind_df.reset_index(drop = True)

            # Calculate the correlation and append the result series to the list so it can be concatenated below.
            corr_s = ind_df.apply(corr_confidence, s2 = col_s, confidence = confidence, axis = 0)
            corr_s.name = (area, shift)
            corr_s_list.append(corr_s)

        # Concat all the series for that area and add them to a list to later concatenate them all.    
        aux_corr_df = pd.concat(corr_s_list, axis = 1)
        corr_df_list.append(aux_corr_df)

    # Concatenate the correlation of all regions, rename the index and return the DataFrame.    
    corr_df = pd.concat(corr_df_list, axis = 1).transpose().sort_index()
    corr_df.index.names = [level, col_shift]
    return corr_df
