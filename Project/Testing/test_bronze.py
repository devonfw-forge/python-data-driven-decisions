

import os
import unittest
import numpy as np

import pandas as pd
from Project.Utils.preprocess import preprocess

from Project.Utils.read_data import read_data
from Project.Utils.rename_value_column import rename_value_column
from Project.Utils.standardize import standardize

df_standardize = pd.DataFrame({'Country': ['Russian Federation', 'Russia', 'United States of America', 'United States', 'United Kingdom of Great Britain and Northern Ireland', 'United Kingdom', 'United States Virgin Islands'], 'Year': ['2000 aaa', '2001 bbb', '2002 lorem ipsum dolor sit amet', '2003', '2004', '2005', '2006'], 'Number': [1, 2, 3, 4, 5, 6, 7]})
df_rename_value = pd.DataFrame({'Country' : ['República Independiente de Mi Casa'], 'Year': [2000], 'Name': ['Number of beds'], 'Quantity': ['4']})

df_preprocess_faostat = pd.DataFrame({'Country' : ['República Independiente de Mi Casa'], 'Year': [2000], 'Item': ['Birth Rate'], 'Value': ['4']})
df_preprocess_kaggle = pd.DataFrame({'HDI Rank': [1],'Country' : ['República Independiente de Mi Casa'], '1995': ['4 camas'], '2010': ['4'], '2020': ['4']})
df_preprocess_worldbank = pd.DataFrame({'Country' : ['República Independiente de Mi Casa'], 'Country Code': ['RIC'], 'Series Name': ['Death Rate'], 'Series Code': ['DRt'], '2010': ['4'], '2020': ['4']})

column_country = 'Country'
column_year = 'Year'
columns_index = [column_country, column_year]
columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], column_country)

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



class Test_Bronze(unittest.TestCase):
    def test_read_data(self):
        path = os.getcwd() + '/Tests/'

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            for filename in os.listdir(path):
                os.remove(path + '' + filename)

        with open(path + 'dummy.txt', 'x') as f:
            f.write('This file is not suitable to be read as a .csv')
        with open(path + 'dummy.csv', 'x') as f:
            f.write('This file could be treated as a .csv')
        
        df_dict = read_data(path)
        url_list = list(df_dict.keys())

        self.assertEqual(len(url_list), 1)
        self.assertEqual(url_list[-1][-4:], '.csv' )



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
        file_path = os.getcwd() + '/Databases/DataBank-gender-equality-rating-CPIA.csv'
        source = pd.read_csv(file_path)
        tested = preprocess(file_path, source, ['Country', 'Year'], columns_rename = dict.fromkeys(['Area', 'Entity', 'Country or Area', 'Name', 'Country Name'], 'Country'))
        #print(tested)
        self.assertListEqual(['Country', 'Year', 'Gender Equality'], list(tested.columns))

    def test_standardize(self):
        df = df_standardize.copy()
        test_df = standardize(df, ['Country', 'Year'])
        #Check that the countries to be renamed are in the df to test
        self.assertIn('Russian Federation', df['Country'].to_list(), 'Test Case definition error')
        self.assertIn('United States of America', df['Country'].to_list(), 'Test Case definition error')
        self.assertIn('United Kingdom of Great Britain and Northern Ireland', df['Country'].to_list(), 'Test Case definition error')
        #Check that the countries to be renamed are no longer in the df_test
        self.assertNotIn('Russian Federation', test_df['Country'].to_list())
        self.assertNotIn('United States of America', test_df['Country'].to_list())
        self.assertNotIn('United Kingdom of Great Britain and Northern Ireland', test_df['Country'].to_list())
        #Check no other countries have been renamed nor deleted
        self.assertIn('United States Virgin Islands', test_df['Country'].to_list(), 'Test Case definition error')
        self.assertEqual(len(test_df['Country']), len(df['Country']))
    
    def test_rename_value(self):
        df = df_rename_value.copy()
        test_df = rename_value_column(df, column_indicator = 'Name', column_value = 'Quantity')
        self.assertEqual(df['Name'][0], test_df.columns[3])
        
        with self.assertRaises(Exception):
            test_df = rename_value_column(df, column_indicator = 'Name')
        with self.assertRaises(Exception):
            test_df = rename_value_column(df, column_value = 'Quantity')

    def test_preprocess_faostat(self):
        df_faostat = df_preprocess_faostat.copy()
        test_df_faostat = preprocess('faostat', df_faostat, columns_index)
        np.testing.assert_array_equal(test_df_faostat.columns[:2], columns_index)
        self.assertEqual(len(test_df_faostat.columns), 3)
        self.assertIn(test_df_faostat.columns[2], list(indicators.values()))
    
    def test_preprocess_kaggle(self):
        df_kaggle = df_preprocess_kaggle.copy()
        test_df_kaggle = preprocess('kaggle', df_kaggle, columns_index)
        np.testing.assert_array_equal(test_df_kaggle.columns[:2], columns_index)
        self.assertEqual(len(test_df_kaggle.columns), 3)
        self.assertIn(test_df_kaggle.columns[2], list(indicators.values()))
    
    def test_preprocess_worldbank(self):
        df_worldbank = df_preprocess_worldbank.copy()
        test_df_worldbank = preprocess('worldbank', df_worldbank, columns_index)
        np.testing.assert_array_equal(test_df_worldbank.columns[:2], columns_index)
        self.assertEqual(len(test_df_worldbank.columns), 3)
        self.assertIn(test_df_worldbank.columns[2], list(indicators.values()))
    
    """ def test_preprocess(self):
        df_faostat = df_preprocess_faostat.copy()
        df_kaggle = df_preprocess_kaggle.copy()
        df_worldbank = df_preprocess_worldbank.copy()
        test_df_faostat = preprocess('faostat', df_faostat, columns_index)
        test_df_kaggle = preprocess('kaggle', df_kaggle, columns_index)
        test_df_worldbank = preprocess('worldbank', df_worldbank, columns_index)

        np.testing.assert_array_equal(test_df_faostat.columns[:2], columns_index)
        self.assertEqual(len(test_df_faostat.columns), 3)
        self.assertIn(test_df_faostat.columns[2], list(indicators.values()))
        np.testing.assert_array_equal(test_df_kaggle.columns[:2], columns_index)
        self.assertEqual(len(test_df_kaggle.columns), 3)
        self.assertIn(test_df_kaggle.columns[2], list(indicators.values()))
        np.testing.assert_array_equal(test_df_worldbank.columns[:2], columns_index)
        self.assertEqual(len(test_df_worldbank.columns), 3)
        self.assertIn(test_df_worldbank.columns[2], list(indicators.values())) """
        
if __name__ == '__main__':
    unittest.main()