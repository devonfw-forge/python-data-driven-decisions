

import os
import unittest

import pandas as pd
from Project.Utils.preprocess import preprocess

from Project.Utils.read_data import read_data



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
        file_path = 'c:/Users/vperezlo/Documents/GitHub/python-data-driven-decisions/Databases/DataBank-gender-equality-rating-CPIA.csv'
        source = pd.read_csv(file_path)
        tested = preprocess(file_path, source, ['Country', 'Year'], columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], 'Country'), inplace = True)
        print(tested)
        self.assertListEqual(['Country', 'Year', 'Gender Equality'], list(tested.columns))

    def test_iqr(self):
        file_path = 'c:/Users/vperezlo/Documents/GitHub/python-data-driven-decisions/Output/IQR-test.csv'
        source = pd.read_csv(file_path)
        



if __name__ == '__main__':
    unittest.main()

    #tambien puedes que no haya ningun nulo, assert para ver que todos los años sean ints, .....