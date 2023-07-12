# Data Driven Decisions
Use Python, Pandas, Spark etc to demontrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social and economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The project will be developed by 2 teams in parallel. You can find more information in their main branches:

- [The Big Three](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-the-big-three)
- [Data Sharks](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-data-sharks)
- [Data Training](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-data-training)

____________________________________________________________________________________________________________________
# Execute the project
Download the files in the 6  branch (Datraining_load_1 to Datatraining_visualization_6), and place them in separate folders
Execute the notebooks in the following order: 

[Data_load](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_load_1/Data_load.ipynb)

[Data_integration](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_integration_2/Data_integration.ipynb)

[Data_normalization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_normalization_3/Data_normalization.ipynb)

[Data_outliers](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_outliers_4/Data_outliers.ipynb) 

[Data_filling](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_filling_5/Data_filling.ipynb) 

[Data_visualization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/Datatraining_visualization_6/Data_visualization.ipynb) 

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

 _______________________________________________________________________________
#  Libraries

### pandas 
It is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.

### numpy 
It is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transformations, and matrices. It is the base for pandas.

### scipy
It provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems. Extends NumPy providing additional tools for array computing and provides specialized data structures, such as sparse matrices and k-dimensional trees. Mainly used for statistical calculations.

### plotly.express 
This module (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or PX. Plotly Express is a built-in part of the plotly library, and is the recommended starting point for creating most common figures. Every Plotly Express function uses graph objects internally and returns a plotly.graph_objects.Figure instance. Throughout the plotly documentation, you will find the Plotly Express way of building figures at the top of any applicable page, followed by a section on how to use graph objects to build similar figures. Therefore it will allow for interacting graphs.

### seaborn
It is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Used for the correlations matrix.

The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application. It allows for downloading data from the websites.

