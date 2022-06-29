# python-data-driven-decisions
Use Python, Pandas, Apache Spark and similars to demonstrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social as well as economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The study is going to be based on the data from [World Bank](https://www.worldbank.org/en/home), updated on June 22, 2022.

The tools used are going to be Python, Pandas and Apache Spark.

## The main steps to follow are going to be:

1- [Data extraction][(https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Data%20extraction.ipynb)](https://github.com/devonfw-forge/python-data-driven-decisions/blob/eee0b8391a056ab4836dd705f621c3be6898c865/WDI-Data%20extraction.ipynb): Extract the data from World Bank website. 

2- [Data integration][(https://github.com/devonfw-forge/python-data-driven-decisions/blob/26742264d0f18cd3b3ef80e677df996c3706570b/WDI-Data%20integration.ipynb)](https://github.com/devonfw-forge/python-data-driven-decisions/blob/2c7a16a66eb542d860c5efe5f31b4c287bac912f/WDI-Data%20integration.ipynb): Filter and select the data we work with to build a complete data table organized by categories (year, country, indicator...). 

3- [Data Normalization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/26742264d0f18cd3b3ef80e677df996c3706570b/WDI-Data%20normalization.ipynb): Normalize data.

4- Perform statistical analysis (through coefficients of correlations and graphs).

5- Basing on previous results, get quantitative and qualitative conclusions grouping by year(s) or region(s).


The record of this project is going to be done weekly (and can be found in the Wiki section). Besides, an in-depth explanation of the programming part can be found on the code file itself.

# Run the application
## Dependencies
Dependecies are automatically managed by Poetry and there is NO need to use external dockers for running spark.

To install dependencies run: `poetry install` in same folder where your .toml file is located. 

Poetry will take care of:

- Installing the required Python interpreter
- Installing all the libraries and modules
- Creating the virtual environment for you

## Running on local
Start the Event Ingestion process with the command:

## Repository setup
main.py: Main entrypoint for creating + configuring the Spark session and launching the process.

orchestrator: Contains each of the processing steps of the pipeline. Responsible of managing the load, process and store of the results.

normalizer: Validates and normalizes raw input data. Creates extra columns and renames/formats to align with the normalized events.

processor: Runs the queries over the input datframes to produce the expected outputs.

# Contributing
Open to new improvements/changes 🚀 Just feel free to fork this repository and open a PR back with any changes!
