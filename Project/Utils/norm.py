import pandas as pd
col_country = 'Country'

def norm (df: pd.DataFrame, level: str = col_country):

    """ 
        Compute the correlation between two series.

        PARAMETERS:
            df: pd.DataFrame
                DataFrame whose values will be normalized.
            level: str, default col_country
                Level of the index for which elements wil be normalized.
        RETURNS:
            DataFrame
                Normalized DataFrame.

    """

    # Create an empty DataFrame which will be returned as a result. It will have the same index as the original.
    norm_df = pd.DataFrame(index = df.index)
    element_list = list(set(df.index.get_level_values(level)))
    element_list.sort()
    for element in element_list:
        for col_name in df.columns:
            # Select indicator for element.
            col = df.loc[df.index.get_level_values(level) == element, col_name]
            # Normalize values.
            col = col.map(lambda x: (x - col.min()) / (col.max() - col.min()))
            # Add them to the normalized DataFrame.
            norm_df.loc[df.index.get_level_values(level) == element, col_name] = col

    return norm_df