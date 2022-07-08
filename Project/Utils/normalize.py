
import pandas as pd




def normalize(df: pd.DataFrame, columns_index, *, inplace = False):

    
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
    

    df[column_year]= df[column_year].astype(int)
    
    
    return df if not inplace else None