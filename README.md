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

The indicators we will use are:

- [Gender Equality](https://data.worldbank.org/indicator/IQ.CPA.GNDR.XQ): CPIA Ranking on Gender Equality, from 1 to 6. The higher, the better. CPIA is short for Country Policy and Institutional Assessment.
- [% Undernourishment](https://data.worldbank.org/indicator/SN.ITK.DEFC.ZS): % of the population whose habitual food consumption is insufficient to provide the dietary energy levels that are required to maintain a normal active and healthy life. A value of 10 means 10%.
- [Credit to Agri-Fish-Forest](https://www.fao.org/faostat/en/#data/IC/metadata): amount of loans provided by the private/commercial banking sector to producers in agriculture, forestry and fishing, including household producers, cooperatives, and agro-businesses.
- [Agriculture Share of GDP](https://www.fao.org/faostat/en/#data/MK): % of the GDP that comes from agricultural activity.
- [Rural Employment](https://www.fao.org/faostat/en/#data/OER): total number of the population that work in rural areas, in 1000 people.
- [Gross Domestic Product](https://www.fao.org/faostat/en/#data/MK): total value of the production of a country in million US$.
- [Employment in Agri-Fish-Forest](https://www.fao.org/faostat/en/#data/OER): % of the employed population that works in the primary sector.
- [Total Agriculture](https://www.fao.org/faostat/en/#data/MK): total value of the agricultural value of a country in thousand US$.
- [Gender Inequality](https://www.kaggle.com/datasets/jorgegarciainiguez/genderinequalityindex): how steep is the inequality between men and women, measured from 0 (none) to 1 (maximum).
- [% Soldiers](https://ourworldindata.org/grapher/armed-forces-personnel): % of the workforce employed by the armed forces of the country.
- [Marriage Rate](https://ourworldindata.org/marriages-and-divorces): Number of marriages in each year per 1,000 people in the population.
- [Birth Rate](https://data.worldbank.org/indicator/SP.DYN.CBRT.IN): Number of births per 1000 people.
- [Death Rate](https://data.worldbank.org/indicator/SP.DYN.CDRT.IN): Number of deaths per 1000 people.
- [Homicides](https://data.worldbank.org/indicator/VC.IHR.PSRC.P5): Number of intentional homicides per 100,000 people.
- [Life Expectancy](https://data.worldbank.org/indicator/SP.DYN.LE00.IN): Number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.
- [Maternal Death Risk](https://data.worldbank.org/indicator/SH.MMR.RISK.ZS): Probability that a 15-year-old female will die eventually from a maternal cause assuming that current levels of fertility and mortality (including maternal mortality) do not change in the future.
- [Literacy Rate](https://data.worldbank.org/indicator/SE.ADT.LITR.ZS): Percentage of people ages 15 and above who can both read and write with understanding a short simple statement about their everyday life.
- [Infant Mortality](https://data.worldbank.org/indicator/SP.DYN.IMRT.IN): Number of infant deaths per 1000 live births.
- [% Population Growth](https://data.worldbank.org/indicator/SP.POP.GROW): Annual population growth rate for year t is the exponential rate of growth of midyear population from year t-1 to t, expressed as a percentage . Population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship.
- [% Rural Population](https://data.worldbank.org/indicator/SP.RUR.TOTL.ZS): % of people living in rural areas as defined by national statistical offices. It is calculated as the difference between total population and urban population.
- [Suicide Rate](https://data.worldbank.org/indicator/SH.STA.SUIC.P5): Number of suicide deaths in a year per 100,000 population. Crude suicide rate (not age-adjusted).
- [Gini](http://data.un.org/Data.aspx?d=WDI&f=Indicator_Code%3ASI.POV.GINI): Gini index measures the extent to which the distribution of income (or, in some cases, consumption expenditure) among individuals or households within an economy deviates from a perfectly equal distribution. A Lorenz curve plots the cumulative percentages of total income received against the cumulative number of recipients, starting with the poorest individual or household. The Gini index measures the area between the Lorenz curve and a hypothetical line of absolute equality, expressed as a percentage of the maximum area under the line. Thus a Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality.
- [Civil Liberties](https://ourworldindata.org/grapher/civil-liberties-eiu?country=SLE~LTU~LBY~LBR~LVA~LSO~LBN~LAO~LKA~LUX): Index that ranges from 0 (no liberties) to 10 (most liberties). It is based on the expert assessments and index by the Economist Intelligence Unit (2022).
- [% Men Employment](https://ourworldindata.org/female-labor-supply): Proportion of the male population ages 15 and over that is economically active. Data is available for OECD member countries, as well as for non-member countries publishing statistics in OECD.stats.
- [% Women Employment](https://ourworldindata.org/female-labor-supply): Proportion of the female population ages 15 and over that is economically active. Data is available for OECD member countries, as well as for non-member countries publishing statistics in OECD.stats.
- [Population](https://ourworldindata.org/grapher/population-past-future?country=CHN~IND~USA~NGA~BRA~JPN~IDN): Historical estimates of population, combined with the projected population to 2100 based on the UN's medium variant scenario.
- [Freedom of Expression](https://ourworldindata.org/grapher/freedom-of-expression-bti?country=ARG~BWA~CHN~CZE): Index that indicates the extent to which individuals, groups, and the press can express their views free from government interference. Ranges from 0 (no freedom) to 10 (most fredom). It is based on the expert assessments and scoring by the Bertelsmann Transformation Index (2022).
- [% Health Expenditure](https://ourworldindata.org/grapher/public-health-expenditure-share-GDP-OWID): This metric captures spending on government funded health care systems and social health insurance, as well as compulsory health insurance.
- [% Industry Employment](https://ourworldindata.org/grapher/industry-share-of-total-emplyoment?country=~COD): Employment refers to all persons of working age who, during a specified brief period, were in paid employment (whether at work or with a job but not at work) or in self-employment (whether at work or with an enterprise but not at work).
- [Women Schooling Years](https://ourworldindata.org/grapher/mean-years-of-schooling-female): Average number of years women older than 25 participated in formal education.
- [Men Schooling Years](https://ourworldindata.org/grapher/mean-years-of-schooling-male): Average number of years men older than 25 participated in formal education.
- [% Education Expenditure](https://ourworldindata.org/grapher/share-of-education-in-government-expenditure): Total general government expenditure on education, expressed as a percentage of total general government expenditure on all sectors.

## 2) Select source of information

This process included both deciding where from and how. The how was decided to be .csv as it is a common and simple standard, while the origin of the data was chose to be a number of wide range databases such as those from the World Bank, UN, OurWorldInData or the FAO, but also some more niche ones like some example DataFrames from Kaggle.

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

However, this method of aggregation resulted in very sharp correlation, both positive and negatives, very likely due to the direct correlation between the GDP and the weight used, the population. Thus, we also used a median of the correlations to show a represantative value of the correlations between GDP and indicators for each region.

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
