
import pandas as pd

def standardize(df: pd.DataFrame, columns_index):

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
    country_rename = {'United States of America': 'United States', 'Russian Federation': 'Russia', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom'}

    column_country, column_year = columns_index    

    for value in df[column_year]: #Normalize year format
                if type(value) is not int and len(value) > 4:
                    df[column_year].replace({value: str(value[:4])}, inplace = True)
    
    """ for column in df.columns: #Drop completely empty columns
                if (len(df.loc[:, column].value_counts()) == 1):
                    df.drop(column, axis = 1, inplace = inplace) """
    
    #Remove rows with no country
    df.dropna(subset = column_country, inplace = True)
    
    #Normalize all countries name, removing blank spaces before and after the string
    df[column_country] = df[column_country].str.strip()
    df[column_country]= df[column_country].astype(str)
    df.replace(['..'], '', inplace = True)
    
    for country in country_rename.keys():
        if country in df[column_country].to_list():
            df = df.replace(to_replace = country, value = country_rename[country])


    #Narrow the range of the data to the years selected
    df[column_year]= df[column_year].astype(int)

    #Convert all the indicators to numeric values, either int or float.
    #As the column country contains strings, it will be completely ignored.
    df = df.apply(pd.to_numeric, errors = 'ignore')
    
    return df #if not inplace else None