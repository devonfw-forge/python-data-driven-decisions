import pandas as pd

from Project.Utils.rename_value_column import rename_value_column


def preprocess (dataframe, columns_index, indicators, columns_rename, year_range = (1990,2020),treatment = '', melt_on_value = None, rename_value_columns = False, inplace = False):
    
    """
        Take a dataframe, rearrange its columns or rows, rename them if needed, and return the resulting dataframe
        
        PARAMETERS:
            dataframe: dataframe
                the dataframe to be modified
            treatment: str, default ''
                a flag-like string to indicate that the dataframe must be treated according to a predefined protocol
            melt_on_value: str, default None
                determines wether the dataframe must be melted on the value specified as the string. If not specified, it will ignore it unless the treatment determines otherwise
            rename_value_columns: bool, default False
                determines wether the dataframe has a column with values whose header needs to be renamed. If not specified, it will ignore it unless the treatment determines otherwise
            inplace: bool, default False
                determines if the changes will be made in the same dataframe or returned as a result
        
        RETURNS:
            DataFrame
                Return the modified dataframe  
    """
    
    column_country = columns_index[0]
    column_year = columns_index[1]

    year_min = year_range[0]

    match treatment:
        
        case 'databank':
            melt_on_value = dataframe.loc[:, 'Series Name'][1]
            dataframe.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace = True)
        
        case 'faostat':
            rename_value_columns = True
        
        case 'kaggle':            
            dataframe.drop(['HDI Rank'], axis=1, inplace = True)
            melt_on_value = 'Gender Inequality'
        
        case 'un_data':
            dataframe = dataframe[pd.to_numeric(dataframe[column_year], errors='coerce').notnull()]

        case 'worldbank':
            melt_on_value = dataframe.loc[:, 'Series Name'][1]
            dataframe.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace = True)
            
    dataframe.rename(columns = columns_rename, inplace = True)
    
    if rename_value_columns:
        rename_value_column(dataframe, inplace = True)
    
    if melt_on_value:
        dataframe = pd.melt(dataframe, id_vars=column_country, var_name = column_year, value_name = melt_on_value)
    
    for value in dataframe[column_year]: #Normalize year format
                if type(value) is not int and len(value) > 4:
                    dataframe[column_year].replace({value: str(value[:4])}, inplace = True)
    
    for column in dataframe.columns: #Drop completely empty columns
                if (len(dataframe.loc[:, column].value_counts()) == 1):
                    dataframe.drop(column, axis=1, inplace = True) 
    
    #Shorten indicators column name and remove all the other columns except for the index columns
    dataframe.rename(columns = indicators, inplace = True)
    dataframe.drop(dataframe.columns.difference(columns_index + list(indicators.values())), axis = 1, inplace=True)
    
    #Remove rows with no country
    dataframe.dropna(subset=column_country, inplace=True)
    
    #Normalize all countries name, removing blank spaces before and after the string
    dataframe[column_country] = dataframe[column_country].str.strip()
    dataframe.replace(['..'], '', inplace=True)
    
    #Narrow the range of the data to the years selected
    dataframe[column_year]= dataframe[column_year].astype(int)
    dataframe.drop(dataframe[dataframe[column_year] < year_min].index, inplace=True)
    
    return dataframe
