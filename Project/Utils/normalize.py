
import pandas as pd

def normalize(df: pd.DataFrame, columns_index, *, inplace = False):

    """ 
        Standardize the formats of the cells of a DataFrame so it can be merged to others.

        PARAMETERS:
            df: pd.DataFrame,
                The DataFrame to be standardized.
            columns_index: list[str, str, ..., str] | (str, str, ..., str)
                Structure of strings with the names of the columns that will be the index and need to be standardized.
            inplace: bool, default = False
                Wether it returns a copy or makes the changes in the DataFrame itself.
        RETURNS:
            DataFrame | None
                The modified DataFrame if inplace is False

    """

    column_country, column_year = columns_index    

    for value in df[column_year]: #Normalize year format
                if type(value) is not int and len(value) > 4:
                    df[column_year].replace({value: str(value[:4])}, inplace = inplace)
    
    for column in df.columns: #Drop completely empty columns
                if (len(df.loc[:, column].value_counts()) == 1):
                    df.drop(column, axis = 1, inplace = inplace)
    
    #Remove rows with no country
    df.dropna(subset = column_country, inplace = inplace)
    
    #Normalize all countries name, removing blank spaces before and after the string
    df[column_country] = df[column_country].str.strip()
    df.replace(['..'], '', inplace = inplace)
    
    #Narrow the range of the data to the years selected
    df[column_year]= df[column_year].astype(int)
    
    return df if not inplace else None