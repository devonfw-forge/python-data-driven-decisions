# python-data-driven-decisions
Use Python, Pandas, Apache Spark and similars to demonstrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social as well as economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The study is going to be based on the data from [World Bank](https://www.worldbank.org/en/home), updated on June 22, 2022.

The tools used are going to be Python, Pandas and Apache Spark.

## The main steps to follow are going to be:

1- [Data extraction](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Data%20extraction.ipynb): Extract the data from World Bank website. 

2- [Data integration](https://github.com/devonfw-forge/python-data-driven-decisions/blob/2c7a16a66eb542d860c5efe5f31b4c287bac912f/WDI-Data%20integration.ipynb): Filter and select the data we work with to build a complete data table organized by categories (year, country, indicator...). 

3- [Data Normalization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/2c7a16a66eb542d860c5efe5f31b4c287bac912f/WDI-Data%20normalization.ipynb): Normalize data.

4- Perform statistical analysis (through coefficients of correlations and graphs).

5- Basing on previous results, get quantitative and qualitative conclusions grouping by year(s) or region(s).


The record of this project is going to be done weekly (and can be found in the Wiki section). Besides, an in-depth explanation of the programming part can be found on the code file itself.

## Assumptions

For this analysis there have been some assumptions taken, as well as some crucial steps in cleaning of the data.

1- **IQR** . The interquartile range (IQR) measures the spread of the middle half of your data. It is the range for the middle 50% of your sample. Use the IQR to assess the variability where most of your values lie. Larger values indicate that the central portion of your data spread out further. Conversely, smaller values show that the middle values cluster more tightly.

To visualize the interquartile range, imagine dividing your data into quarters. Statisticians refer to these quarters as quartiles and label them from low to high as Q1, Q2, Q3, and Q4. The lowest quartile (Q1) covers the smallest quarter of values in your dataset. The upper quartile (Q4) comprises the highest quarter of values. The interquartile range is the middle half of the data that lies between the upper and lower quartiles. In other words, the interquartile range includes the 50% of data points that are above Q1 and below Q4. The IQR is the red area in the graph below, containing Q2 and Q3 (not labeled).

When measuring variability, statisticians prefer using the interquartile range instead of the full data range because extreme values and outliers affect it less. Typically, use the IQR with a measure of central tendency, such as the median, to understand your data’s center and spread. This combination creates a fuller picture of your data’s distribution.

Therefore it is being utilized to get rid of all the outliers that may come from errors when creating the data or from unexpected years.

2- **Substitution of the NaN values**. The Nan values´ treatment developed has been a mix, between the linear interpolation and backwards filling. The linear interpolation is a form of interpolation, which involves the generation of new values based on an existing set of values. Linear interpolation is achieved by geometrically rendering a straight line between two adjacent points on a graph or plane. Whereas the backwards filling, will help us to arrive to those values which have not been fullfilled with the linear interpolation.

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
