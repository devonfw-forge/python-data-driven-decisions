

import os
import sys
import unittest
import logging
from numpy import not_equal

import pandas as pd
from pandas.testing import assert_frame_equal
from Project.Utils.preprocess import preprocess
from Project.Utils.data_treat import iqr_treatment, nan_treatment
from Project.Utils.read_data import read_data

read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes

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



class TestLoadProcess(unittest.TestCase):
    
    """ def test_un_data(self):
        file_path = 'C:\\Users\\smanoles\\Documents\\GitHub\\python-data-driven-decisions\\Databases\\UN_Data_Gini.csv'
        source = pd.read_csv(file_path)
        prevalue = source.count()
        

        tested = preprocess(source, ['Country', 'Year'], {'Value': 'Gini'}, dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], 'Country'), treatment='un_data' )
        output_columns = list(tested.columns)
        postvalue = tested.count()
        self.assertIn('Gini', output_columns, 'GINI column not found')
        print(prevalue)
        print(postvalue)
        self.assertNotEqual(prevalue, postvalue, 'No son iguales') """


        #read_databases(read_path, special_source, False)
    def test_melt(self):
        file_path = read_path + '/DataBank-gender-equality-rating-CPIA.csv'
        source = pd.read_csv(file_path)
        tested = preprocess(file_path, source, ['Country', 'Year'], columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], 'Country'))
        print(tested)
        self.assertListEqual(['Country', 'Year', 'Gender Equality'], list(tested.columns))

    def test_data_treat(self):
        log = logging.getLogger('TestDataTreat')
        log.setLevel(logging.DEBUG)
        file_path = write_path  + '/BronzeDataframe.csv'

        source = pd.read_csv(file_path) 

        aux = source.loc[source['Country'] == 'Spain']
        aux = iqr_treatment(aux)
        aux = nan_treatment(aux)

        for column in aux.columns[3:]:
            self.assertNotEqual((aux[column].notna().sum() != len(aux)), (aux[column].isna().sum() != len(aux)), 'Error in data treat')
        
        auxRetreat = iqr_treatment(aux)

        assert_frame_equal(aux, auxRetreat)
            
                            



                

        



if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    unittest.main()

    #tambien puedes que no haya ningun nulo, assert para ver que todos los años sean ints, .....