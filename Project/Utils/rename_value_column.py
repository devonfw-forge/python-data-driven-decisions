import pandas as pd

COL_VALUES = ['Value']
COL_INDICATORS = ['Item', 'Indicator']

def rename_value_column(df: pd.DataFrame, *, column_indicator = None, column_value = None, indicator_index = 0):
    """
        Rename the value column of a dataframe with the name of the indicator.
        
        PARAMETERS:
            dataframe: dataframe
                the dataframe to be modified
            column_value: str, default None
                the name of the column that contains the values and whose name will be changed. If not specified, it will try to search for it
            column_indicator: str, default None
                the name of the column that contains the name of the indicator of the dataframe. If not specified, it will try to search for it
            indicator_index: int, default 1
                the index of the line where the indicator name will be fetched from
            row_index: int, default 1
                0 to apply the changes to the rows, 1 to apply the changes to the columns
            inplace: bool, default False
                determines if the changes will be made in the same dataframe or returned as a result
        
        RETURNS:
            DataFrame or None
                If inplace = False, it will return the modified dataframe. Else, the return will be None and the dataframe
        
        RAISES:
            Exception
                If either column_value or column_indicator was not specified, and it was unable to find them itself 
    """    
    
    #If no column name specified, try to find the value column or the indicator column.
    if column_indicator is None:
        for indicator in COL_INDICATORS:
            if indicator in df:
                column_indicator = indicator
    
    if column_value is None:
        for value in COL_VALUES:
            if value in df:
                column_value = value             

    #If unable to find either column, raise an exception.   
    if column_indicator is None:
        raise Exception('Unable to rename: could not determine indicator column')
    if column_value is None:
        raise Exception('Unable to rename: could not determine value column')
        
    df.rename(columns = {column_value: df.loc[:, column_indicator][indicator_index]}, inplace = True)
    
    return df# if not inplace else None