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
