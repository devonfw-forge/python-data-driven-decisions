#||||||||||START OF MAIN CODE|||||||||||||

#Explore all the files from the specified directory in read_path
#If the file is a .csv, try to read it, preprocess it and append it to the list of dataframes
#If any error is raised during the process, it appends the url to the list of discarded files and shows a warning at the end


from os import listdir
from os.path import isfile, join
import warnings

import pandas as pd

from Project.Utils.preprocess import preprocess

def read_databases(read_path: str, special_source = None, verbose = False):

    #url_list = []
    data_dict = {}
    discarded_urls = []
    columns_index = ('Country', 'Year') #Dupe, original in main class

    #Hierarchy to be determined
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
    
    special_source = ['databank', 'faostat', 'kaggle', 'un_data', 'worldbank', 'WID'] #List with all the sources that need special treatment

    columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], columns_index[0]) #Dictionary to rename all the index columns so 
    
    for element in listdir(read_path):
            url = join(read_path, element)
            if isfile(url) and url.endswith('.csv'):
                #url_list.append(url)
                if 'WID' in url:
                    continue
                try:
                    dataframe = pd.read_csv(url)
                except:
                    print('Unable to read dataframe: ' + url)
                    discarded_urls.append(url)
                else:
                    special = None
                    for source in special_source:
                        if source in url.lower():
                            special = source
                            break
                    dataframe = preprocess(dataframe, columns_index, columns_rename, treatment = special)
                    try:
                        #dataframe = preprocess(dataframe, columns_index, columns_rename, treatment = special)
                        i=1
                    except Exception as e:
                        print('Unexpected error when preprocessing the dataframe: ' + url)
                        discarded_urls.append(url)
                    else:
                        #url_list.append(url)
                        data_dict[url] = dataframe

    if len(discarded_urls) > 0:
            warn = 'Unable to read the following files:'
            for url in discarded_urls:
                warn += '\n' + url
            warnings.warn(warn)                    
                        
    if (verbose):
        for data in data_dict.values():
            print(data)
            print('\n' + '----------------------------------------------------------' + '\n')
    #else:
    #    print('Done')
    
    return data_dict