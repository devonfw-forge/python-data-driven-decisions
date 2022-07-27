# Execute the project

1) Download [databases.zip](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-sharks/Databases.zip) and [Project](https://github.com/devonfw-forge/python-data-driven-decisions/tree/main-data-sharks/Project), and place them in the same folder
2) Extract the databases
3) Execute the notebooks in the following order: [Notebook_Bronze](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-sharks/Notebook_Bronze.ipynb), [Notebook_Silver](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-sharks/Notebook_Silver.ipynb) and [Notebook_Gold](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-sharks/Notebook_Golden.ipynb). This will create a series of output DataFrames as .csv files.
4) Execute any other notebook if desired.


# Explanation of the followed process

### The Hypothesis:

It is assumed that there exists a correlation between economic growth (positive, negative) and birth rate, (infant) mortality, number of marriages etc. Demonstrate the validity of this assumption based on available datasets. 

In order to check the veracity of this hypothesis the following steps are going to be followed:

## 1) Choose the indicators

In order to study the correlation between the economic indicators and some socio-demographic indicators, we have to select both the indicators to be studied and how we are going to measure the economic growth. While the first issue will be resolved by a number of iterations in which we will remove the less significative indicators and try to add different ones, the second was decided to be masured with the GDP of the country.

## 2) Select source of information

This process included both deciding where from and how. The how was decided to be .csv as it is a common and simple standard, while the origin of the data was chose to be a number of wide range databases such as those from the World Bank, UN or the FAO, but also some more niche ones like OurWorldInData or some example DataFrames from Kaggle.

## 3) Definition of Normalized Data Model

This is, how we want our Dataframes to look: name and number of columns, the index to be used and other aspects that will allow for a standardized manipulation and merging of them.

In our case, we opted for a format with a multi-index formed by Country and Year, and a column titled as the indicator it contained. Or in a more visual way, the format will be the following:

{Country | Year} | Indicator

## 4) Data Normalization

To achieve the desired format, it was necessary to drop irrelevant columns, pivot or melt some dataframes, rename the columns and standardize the format of the years to integers and the values to floats.

## 5) Definition of Normalized Integrated Data Model

Same process as step 3, the multi-index would be respected, and all the columns with the indicators would be appended one behind the other until all the indicators were integrated into this new, bigger dataframe.

## 6) Integration

The integration process merely consisted on using the merge function for Pandas Dataframes until all our data had been integrated into the new database, which would later be exported as a .csv.

![image](https://github.com/devonfw-forge/python-data-driven-decisions/blob/aaa43f45b6e6f46b5596aefec8942fa4f2131aad/model-definition-diagram%20(1).png)

## 7) Establishing the range

Once we had a single Dataframe with a more global vision of our data, we proceeded to treat it. First, we needed to set the boundaries of what years would we study. At first, it was decided the range would go from 1990 to 2020, but later, we decided it was worth it to reduce it to 2000-2020, so even though we were dropping some valuabke data, we also made sure that for our range, the Dataframe would be the most complete possible, with the least amount of missing values.

## 7) Identifying and removing outliers

Secondly, we implemented a rudimentary method that allowed us to remove values considered outliers. To be considered an outlier, a value must be higher or lower than the range between the third and first quartile multiplied by 1,5 and, also, not be part of a tendency, this is, not be part of a group of three or more consecutive values that would otherwise be considered outliers.

## 8) Interpolating values

Some countries would have missing values for some indicators on given years. In order to be able to work with this incomplete data, we interpolated some of the missing values when possible.

## 9) Dropping indicators and countries

Some countries would have missing values for most of the indicators, and also some indicators would only have values for a couple of countries. Since interpolating with only a few values for column would mean virtually making the data up, we decided to remove them.

Also, we decided to drop countries with no GDP information available.

Once the Dataframe had been condensed and only contained useful data, we exported it to a second .csv.

## 10) Dividing by region

From the condensated Dataframe, we created other smaller Dataframes divided by regions, so each one of them could be studied separately. To do this, we merged the big dataframe with the one containing the regions for each country, effectively adding a new column with the region that would allow us to filter them based on that.

## 11) Aggregating values

We thought it could be interesting to have entries for the aggregates of each region, so we wrote a method that would calculate it. For absolute values, it would provide the summatory of all the elements, while for relative ones, we calculated the weighted average based on the population of the countries.

This aggregation also allowed us to estimate a number of entries for the whole world.

## 12) Analysing the data

After the long process of preparing the data, we started to analyse the correlations between the indicators and the GDP.

## 13) Showing the charts

[WIP]


## Testing

The code is being tested along the development of the project. This is the result of the last coverage:

![image](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-data-sharks/image.png)



# Run the application
## Poetry
All dependencies are controled by Poetry by simply executing the command "poetry install" in the same folder.

## Running on local
To execute the code you can download the code project and databases.zip. Save them in the same folder, extract the databases and execute the notebooks.

## Repository setup
The notebooks contain the main flow of the data preparation process, but there also are some python classes where auxiliary methods have been defined to keep the notebooks clean.
