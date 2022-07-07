import os #quitar cuando funcione
import pandas as pd

from Project.Utils.rename_value_column import rename_value_column

SPECIAL_SOURCE = ('databank', 'faostat', 'kaggle', 'un_data', 'worldbank', 'WID')

write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes

#DEFAULT_RENAME = ['Area', 'Entity', 'Country or Area', 'Name', 'Country Name']


indicators = {
    
    #databank
    'CPIA gender equality rating (1=low to 6=high)': 'Gender Equality',
    'Prevalence of undernourishment (% of population)': '% Undernourishment',
    
    #faostat
    'Credit to Agriculture, Forestry and Fishing': 'CreditToAgriFishForest',
    '2.a.1 Agriculture value added share of GDP (%)': 'AgriShareGDP',
    'Employment by status of employment, total, rural areas': 'EmploymentRural',
    'Gross Domestic Product': 'GDP',
    'Share of employment in agriculture, forestry and fishing in total employment': '%EmploymentAgriFishForest',
    'Agriculture': 'TotalAgri',
    
    #kaggle
    'Gender Inequality': 'Gender Inequality',
    
    #ourworldindata
    'Armed forces personnel (% of total labor force)': '% Soldiers', 
    'Crude marriage rate (per 1,000 inhabitants)': 'Marriage Rate',
    
    #theworldbank  
    'Birth rate, crude (per 1,000 people)': 'Birth Rate',
    'Death rate, crude (per 1,000 people)': 'Death Rate',
    'Intentional homicides (per 100,000 people)': 'Homicides',
    'Life expectancy at birth, total (years)': 'Life Expectancy',
    'Lifetime risk of maternal death (%)': 'Maternal Death Risk',
    'Literacy rate, adult total (% of people ages 15 and above)': 'Literacy Rate',
    'Mortality rate, infant (per 1,000 live births)': 'Infant Mortality',
    'Population growth (annual %)': '% Population Growth',
    'Rural population (% of total population)': '% Rural Population',
    'Suicide mortality rate (per 100,000 population)': 'Suicide Rate',
    
    #UN_Data
    'Value': 'Gini',
    
    #WID
    #(To Do)
    
    #WorldInData
    'civlib_vdem_owid': 'Civil Liberties',
    'Employment-to-population ratio, men (%)': '% Men Employment',
    'Employment-to-population ratio, women (%)': '% Women Employment',
    'Population (historical estimates)': 'Population',
    'freeexpr_vdem_owid': 'Freedom of Expression',
    'Indicator:Domestic general government health expenditure (GGHE-D) as percentage of general government expenditure (GGE) (%)': '% Healthcare Investment',
    'Industry as % of total employment -- ILO modelled estimates, May 2017': '% Employment Industry',
    'UIS: Mean years of schooling of the population age 25+. Female': 'Women Schooling Years',
    'UIS: Mean years of schooling of the population age 25+. Male': 'Men Schooling Years',
    'Government expenditure on education, total (% of government expenditure)': '% Education Expenditure'

}

def preprocess (url: str, df: pd.DataFrame, columns_index, *, columns_rename = None, treatment = '', melt_on_value = None, rename_value_columns = False, inplace = False):
    
    """
        Take a dataframe and reshape it to match the desired format.
        Based on the source, rearrange its columns or rows and rename them if needed.
        Return dataframe if inplace is False.
        
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

    df.to_csv(write_path + '/1.csv')

    #year_min, year_max = year_range

    for treatment in SPECIAL_SOURCE:
        if treatment in url.lower():                    #Any way to do it more efficiently?
            match treatment:
                
                case 'databank':
                    melt_on_value = df.loc[:, 'Series Name'][1]
                    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace = inplace)
                
                case 'faostat':
                    rename_value_columns = True
                
                case 'kaggle':            
                    df.drop(['HDI Rank'], axis=1, inplace = inplace)
                    melt_on_value = 'Gender Inequality'
                
                case 'un_data':
                    df = df[pd.to_numeric(df[column_year], errors='coerce').notnull()] #Here or in normalize?

                case 'worldbank':
                    melt_on_value = df.loc[:, 'Series Name'][1]
                    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace = inplace)
            break
    #if not columns_rename:
        #columns_rename = dict.fromkeys(DEFAULT_RENAME: column_country)        
    df.to_csv(write_path + '/2.csv')
    
    df.rename(columns = columns_rename, inplace = inplace)

    df.to_csv(write_path + '/3.csv')

    if rename_value_columns:
        rename_value_column(df, inplace = inplace)

    if melt_on_value:
        df = pd.melt(df, id_vars = column_country, var_name = column_year, value_name = melt_on_value)

    df.to_csv(write_path + '/4.csv')

    df.rename(columns = indicators, inplace = inplace)
    
    df.drop(df.columns.difference(list(columns_index) + list(indicators.values())), axis = 1, inplace = inplace)
    #df.drop(df.columns.difference(list(columns_index) + list(indicators.keys())), axis = 1, inplace=inplace)

    df.to_csv(write_path + '/5.csv')

    return df #if not inplace else None
    
    
    

