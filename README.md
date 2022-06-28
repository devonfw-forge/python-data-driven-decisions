# python-data-driven-decisions
Use Python, Pandas, Apache Spark and similars to demontrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social as well as economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The study is going to be based on the data from [World Bank](https://www.worldbank.org/en/home), updated on June 22, 2022.

The tools used are going to be Python, Pandas and Apache Spark.

The main steps to follow are going to be:

1- Extract the data from World Bank website. ([Data extraction](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Data%20extraction.ipynb))

2- Filter and select the data we work with to build a complete data table organized by categories (year, country, indicator...). ([Data integration] (https://github.com/devonfw-forge/python-data-driven-decisions/blob/26742264d0f18cd3b3ef80e677df996c3706570b/WDI-Data%20integration.ipynb))

3- Normalize data. 

4- Perform statistical analysis (through coefficients and graphs).

5- Basing on previous results, find more specific correlations grouping by year(s) or region(s).

6- Get quantitative and qualitative conclusions. 


The record of this project is going to be done weekly (and can be found in the Wiki section). Besides, an in-depth explanation of the programming part can be found on the code file itself.

# Run the application
## Dependencies
Dependecies are automatically managed by Poetry and there is NO need to use external dockers for running spark.

To install dependencies run: `poetry install` in same folder where your .toml file is located. 

Poetry will take care of:

- Installing the required Python interpreter
- Installing all the libraries and modules
- Creating the virtual environment for you

# Contributing
Open to new improvements/changes 🚀 Just feel free to fork this repository and open a PR back with any changes!
