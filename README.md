# Data Driven Decisions
Use Python, Pandas, Spark etc to demontrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social and economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The project will be developed by 2 teams in parallel. You can find more information in their main branches:

- [The Big Three](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-the-big-three)
- [Data Sharks](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-data-sharks)
- [Data Training](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-data-training)

____________________________________________________________________________________________________________________
# Execute the project
Execute the notebooks in the following order: 

[Data_load](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-training/Data_load.ipynb)    
[Data_normalization and outliers](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-training/Data_normalization_outliers.ipynb)       
[Data_filling](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-training/Data_filling_NaN_values.ipynb)     
[Data clustering by countries](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-training/Data_clustering_countries.ipynb)   
[Data clustering by indicators](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-training/Data_clustering_indicators.ipynb)
Data predictions

This will create a series of output DataFrames as .csv files.

# Explanation of the followed process
The Hypothesis:
It is assumed that there exists a correlation between economic growth and indicators as infant mortality, access to education... 
We want to demonstarte the validity of this assumption based on available datasets.

In order to check the veracity of this hypothesis the following steps are going to be followed:

# <u>  First step : Choose the indicators  
In order to study the correlation between the economic indicators and some socio-demographic indicators, we have to choose the different indicators :    

1) Gdp from 1850 to 2020 in pounds

2) Infant mortality of children under 5 years old

3) Percentage of population age 15+ with tertiary schooling. 

4) Fertility rate

5) gender inequality

6) Life expectancy

I choose to measure the economic growth to compare the indicators with the GDP of the country.

# 2nd step : Select source of information
 I chose to extract datasets about these indicators from the website [Our world in data](https://ourworldindata.org/)

