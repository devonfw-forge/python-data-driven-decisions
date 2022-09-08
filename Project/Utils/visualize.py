import os
from scipy import stats
import pandas as pd

write_path = os.getcwd() + '/Output' #Path to the folder you want to store the dataframes
output_path = os.getcwd() + '/Output' #Path to the folder you want to store the dataframes


def search(threshold, mode = 'Region', zone = 'Afganisthan'):   

    """ 
        For every country in the list generate a dataframe with the indicators and the GDP correlation. This correlation must be higher than the given thresold.

        PARAMETERS:
            threshold: float
                Threshold of the GDP correlation.
            mode: str ['Country', 'Region, 'World']
                What dataframe to process.
            zone: str
                The zone to process.
                
        RETURNS:
            DataFrame 

    """


    if mode == 'Country':
        df= pd.read_csv(write_path + '/GoldDataframe.csv')
        df = df.loc[df['Country'] == zone]
        df.set_index(['Country', 'Year', 'Region'], inplace=True)
        

    elif mode == 'Region':
        df= pd.read_csv(write_path + '/AggregatedRegion_DataFrame.csv')
        df = df.loc[df['Region'] == zone]
        df.set_index(['Region', 'Year'], inplace=True)
        
    
    else:
        df= pd.read_csv(write_path + '/AggregatedWorld_DataFrame.csv')
        df.set_index(['Region', 'Year'], inplace=True)
        #df.set_index(['Country', 'Year', 'Region'], inplace=True)



    df_result = pd.DataFrame(columns=['Indicator','GDP Pearson Corr'])
    for column in df.columns:
        if column != 'GDP' and not df[column].isnull().values.any():
            pears = stats.pearsonr(df[column], df['GDP'])
            spear = stats.spearmanr(df[column], df['GDP'])
            

            if (threshold == 0) or (pears[0] >= threshold and spear[0] >= threshold) or (pears[0] <= -threshold and spear[0] <= -threshold) :
                aux  = pd.DataFrame({'Indicator': [column],
                                    'GDP Pearson Corr': [pears[0]],
                                    'P-value Pearson': [pears[1]],
                                    'GDP Spearman Corr': [spear[0]],
                                    'P-value Spearman': [spear[1]]})

                df_result = pd.concat([df_result, aux], ignore_index=False, axis = 0)



    df_result.set_index(['Indicator'], inplace=True)

    df_result = df_result.sort_values(by=["GDP Pearson Corr"], ascending = False)

    return df_result

def searchTimeSeries(threshold, start, end, time, df):   

    """ 
        For every zone in the list generate a dataframe with the indicators and the GDP correlation in the range of years. This correlation must be higher than the given thresold.

        PARAMETERS:
            threshold: float
                Threshold of the GDP correlation.
            mode: str ['Country', 'Region, 'World']
                What dataframe to process.
            zone: str
                The zone to process.
                
        RETURNS:
            DataFrame 

    """

    #Trim the dataframe to the desired range for the window series.
    if time: df = df.loc[df.index.get_level_values('Year').isin(range(start, end + 1))]


    df_result = pd.DataFrame(columns=['Indicator','GDP Spearman Corr'])
    for column in df.columns:
        if column != 'GDP' and not df[column].isnull().values.any():
            spear = stats.spearmanr(df[column], df['GDP'])

            if (threshold == 0) or (spear[0] >= threshold) or (spear[0] <= -threshold) :
                aux  = pd.DataFrame({'Indicator': [column],
                                    'GDP Spearman Corr': [spear[0]],
                                    'P-value Spearman': [spear[1]]})

                df_result = pd.concat([df_result, aux], ignore_index=False, axis = 0)

    df_result.set_index(['Indicator'], inplace=True)

    df_result = df_result.sort_values(by=['GDP Spearman Corr'], ascending = False)


    return df_result




def normalize_by_country (df: pd.DataFrame):
    country_list =  set(df.index.get_level_values('Country'))
    norm_df = pd.DataFrame(index = df.index)
    for country in country_list:
        for col_name in df.columns:
            # Select indicator col_name for country country
            col = df.loc[df.index.get_level_values('Country') == country, col_name]
            # Normalize values
            col = col.map(lambda x: (x - col.min()) / (col.max() - col.min()))
            # Add them to the normalized DataFrameÇ
            norm_df.loc[df.index.get_level_values('Country') == country, col_name] = col
    return norm_df


def get_zone(df, countries_by_region, zone: str, by: str, ):
    if by == 'Country':
        df_zone  = df.loc[df.index.get_level_values('Country') == zone]
    elif by == 'Region':
        df_zone = countries_by_region[zone]
    
    return df_zone

def get_years(df, years):
    df.loc[(df.index.get_level_values("Year") >= years[0]) & (df.index.get_level_values("Year") <= years[1])]
    return df