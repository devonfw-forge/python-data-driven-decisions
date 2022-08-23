import pandas as pd
from Project.Utils.shift_corr import shift_corr

col_country = 'Country'
col_region = 'Region'

def max_corr(df: pd.DataFrame, level: str, confidence: float = 0.05, raw: bool = True):

    """ 
        Find the maximum values of the correlations for each member in the specified level of the index.

        PARAMETERS:
            df: pd.DataFrame
                The DataFrame to read from.
            level: str
                Name of the index level that contains the element for which the correlations have been computed.
            confidence: float, default = 0.05
                Level of confidence for the correlation. It is passed to the shift_corr method if raw is True.
            raw: bool, default = True
                Wether df contains data that needs to be processed by shift_corr, or already has been computed.
        RETURNS:
            (pd.DataFrame, pd.DataFrame)
                A tuple of DataFrames. The first ones will contain the maximum correlation value for each element; and the second one, the shift of the maximum correlation value for said element.

    """

    # If the df DataFrame contains raw data, apply shift_corr to obtain the correlations. Otherwise, proceed with df.
    if raw:
        corr_df = shift_corr(df, level, confidence)
    else:
        corr_df = df.copy()

    # Initialize the lists to create the Dataframes at the end of the cell.
    max_corr_list = []
    max_corr_index_list = []

    area_list = list(set(df.index.get_level_values(level)))
    area_list.sort()

    for area in area_list:
        # Select the rows belonging to the area.
        area_df = corr_df.loc[corr_df.index.get_level_values(level) == area].reset_index(level, drop = True)

        # Find the max correlations, either positive or negative, and their index. Name the resulting series and store them into their respective lists.
        max_area_s = area_df.apply(lambda x: max(x.min(), x.max(), key=abs))
        max_area_index_s = area_df.apply(lambda x: x.idxmax() if max(x.min(), x.max(), key=abs) == x.max() else x.idxmin())

        max_area_s.name = area
        max_area_index_s.name = area

        max_corr_list.append(max_area_s)
        max_corr_index_list.append(max_area_index_s) 

    # Concatenate the max correlations series to create the Dataframe.
    max_corr_df = pd.concat(max_corr_list, axis = 1).transpose().sort_index()
    max_corr_index_df = pd.concat(max_corr_index_list, axis = 1).transpose().sort_index()

    max_corr_df.index.name = level
    max_corr_index_df.index.name = level

    return max_corr_df, max_corr_index_df