import os
from scipy import stats
import pandas as pd

write_path = os.getcwd() + '/Output' #Path to the folder you want to store the dataframes

def search_indicators(threshold, corr_df):   

    """ 
        For every country in the list generate a dataframe with the indicators and the GDP correlation. This correlation must be higher than the given thresold.

        PARAMETERS:
            threshold: float
                Threshold of the GDP correlation.
            corr_df: pd.Dataframe()
                Dataframe of the correlations for every country.
                
        RETURNS:
            DataFrame 

    """
    countryList = corr_df.index.tolist() 
    bestIndicators = {}
    transp_corr = corr_df.transpose()

    for country in countryList:
        dataAux = pd.DataFrame()
        dataAux = pd.concat([dataAux, transp_corr.loc[transp_corr[country] >= threshold, [country]]], ignore_index=False, axis=0)
        dataAux = pd.concat([dataAux, transp_corr.loc[transp_corr[country] <= -threshold, [country]]], ignore_index=False, axis=0)
        dataAux.rename(columns={ dataAux.columns[0]: "GDP Correlation" }, inplace = True)
        bestIndicators[country] = dataAux.sort_values(by=["GDP Correlation"], ascending = False)
    return bestIndicators


def search(threshold, country):   

    """ 
        For every country in the list generate a dataframe with the indicators and the GDP correlation. This correlation must be higher than the given thresold.

        PARAMETERS:
            threshold: float
                Threshold of the GDP correlation.
            corr_df: pd.Dataframe()
                Dataframe of the correlations for every country.
                
        RETURNS:
            DataFrame 

    """
    df= pd.read_csv(write_path + '/Country/' + country + '.csv')
    df.set_index(['Country', 'Year', 'Region'], inplace=True)

    df_result = pd.DataFrame()
    for column in df.columns:
        if column != 'GDP' and not df[column].isnull().values.any():
            pears = stats.pearsonr(df[column], df['GDP'])
            spear = stats.spearmanr(df[column], df['GDP'])
            
            if (pears[0] >= threshold and spear[0] >= threshold) or (pears[0] <= -threshold and spear[0] <= -threshold) :
                aux  = pd.DataFrame({'Indicator': [column],
                                    'GDP Pearson Corr': [pears[0]],
                                    'P-value Pearson': [pears[1]],
                                    'GDP Spearman Corr': [spear[0]],
                                    'P-value Spearman': [spear[1]]})

                df_result = pd.concat([df_result, aux], ignore_index=False, axis = 0)


   
    df_result.set_index(['Indicator'], inplace=True)

    df_result = df_result.sort_values(by=["GDP Pearson Corr"], ascending = False)

    return df_result

   



def pvalue(country):

    """ 
        For every indicator of a country generate the p-value and concatenate it into a dataframe.

        PARAMETERS:
            country:
                Target country to generate the p-values of the indicators.
        RETURNS:
            DataFrame 

    """
    df= pd.read_csv(write_path + '/GoldDataframe.csv')
    country_df = df.loc[df['Country'] == country]
    country_df.set_index(['Country', 'Year', 'Region'], inplace=True)

    column_pvalues = pd.DataFrame(columns=['Column', 'P-value'])

    for column in country_df.columns:
        if not country_df[column].isnull().values.any():
            aux  = pd.DataFrame({'Column': [column],
                                 'P-value': [stats.spearmanr(country_df[column], country_df['GDP'])[1]]})
            column_pvalues = pd.concat([column_pvalues, aux], ignore_index=False, axis = 0)
    column_pvalues.set_index(['Column'], inplace=True)
    return column_pvalues
