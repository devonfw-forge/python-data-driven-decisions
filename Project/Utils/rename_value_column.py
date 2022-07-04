def rename_value_column(dataframe, column_value = None, column_indicator = None, indicator_index = 1, row_index = 1, inplace = False):
    """
        Method that takes a dataframe and renames the value column with the name of the indicator
        
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
    
    #If no column name specified, iterate over the list of possible names.
    col_values = ['Value']
    col_indicators = ['Item', 'Indicator']
    
    #Try to find
    if not column_indicator:
        for indicator in col_indicators:
            if indicator in dataframe:
                column_indicator = indicator
    
    if not column_value:
        for value in col_values:
            if value in dataframe:
                column_value = value             
       
    if not column_indicator:
        raise Exception('Unable to determine indicator column')
    if not column_value:
        raise Exception('Unable to determine value column')
        
    dataframe.rename(columns = {column_value: dataframe.loc[:, column_indicator][indicator_index]}, inplace = inplace)
    
    return dataframe if not inplace else None