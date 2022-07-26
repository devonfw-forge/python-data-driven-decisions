import os
from scipy import stats
import pandas as pd

write_path = os.getcwd() + '/Output' #Path to the folder you want to store the dataframes

def search_indicators(threshold, corr_df):   
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



def pvalue(country):
    df= pd.read_csv(write_path + '/GoldDataframe.csv')
    country_df = df.loc[df['Country'] == country]
    country_df.set_index(['Country', 'Year', 'Region'], inplace=True)

    column_pvalues = pd.DataFrame(columns=['Column', 'P-value'])

    for column in country_df.columns:
        if not country_df[column].isnull().values.any():
            column_pvalues= column_pvalues.append({'Column': column,
                                                    'P-value': stats.pearsonr(country_df[column], country_df['GDP'])[1]},
                                                    ignore_index=True) 
    column_pvalues.set_index(['Column'], inplace=True)
    return column_pvalues

def sig_df(df: pd.DataFrame, index: str = 'Country'):
    corr_df = pd.DataFrame()
    corr_df.index.names = [index]
    aux_df = pd.DataFrame()

    #List all the countries, none repeated
    countries = set(df[index].to_list())

    country_dict = {}
    corr_dict = {}

    for country in countries:

        #Get the DataFrame for a given country
        country_df = df.loc[df[index] == country]

        #Correlation matrix for that country
        country_corr_df = country_df.corr()

        #Trim it into a single row
        country_corr_df = country_corr_df.rename(columns = {'GDP': country}).drop(index = ['Year', 'GDP'])

        #Add the row to a new DataFrame with the correlations for each country
        corr_df = pd.concat([corr_df, country_corr_df[country]], axis = 1)

    #Transpose the resulting DataFrame to have the desired format and show it
    corr_df = corr_df.transpose()
    corr_df

