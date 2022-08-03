# python-data-driven-decisions
Use Python, Pandas, Apache Spark and similars to demonstrate that correlation can be used as a basis for decision making.

This project consists of finding the correlation between the GDP (Gross Domestic Product) and social as well as economical indicators, such as population growth, fertility rates, investment in specific sectors or prices.

The study is going to be based on the data from [World Bank](https://www.worldbank.org/en/home), updated on June 22, 2022.

The tools used are going to be Python, Pandas and Apache Spark.

<div>

<img src="https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Logos/Python.png" width="25%" />

<img src="https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Logos/Pandas.jpg" width="40%"  />

<img src="https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Logos/pyspark.png" width="30%" align="right"/>

</div>

## The main steps to follow are going to be:

1- [Data extraction](https://github.com/devonfw-forge/python-data-driven-decisions/blob/main-the-big-three/Data%20extraction.ipynb): Extract the data from World Bank website. 

2- [Data integration](https://github.com/devonfw-forge/python-data-driven-decisions/blob/2c7a16a66eb542d860c5efe5f31b4c287bac912f/WDI-Data%20integration.ipynb): Filter and select the data we work with to build a complete data table organized by categories (year, country, indicator...). 

3- [Data normalization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/2c7a16a66eb542d860c5efe5f31b4c287bac912f/WDI-Data%20normalization.ipynb): Normalize data.

4- [Perform statistical analysis and visualization](https://github.com/devonfw-forge/python-data-driven-decisions/blob/7db85005073c68e3e9b8c9a7c5620748b6d755b5/Visualization%20of%20correlation%20(Global).ipynb): Through coefficients of correlations and graphs for univariable studies and for multivariable, modeling.

5- Basing on previous results, get quantitative and qualitative conclusions grouping by year(s) or region(s).


The record of this project is going to be done weekly (and can be found in the Wiki section). Besides, an in-depth explanation of the programming part can be found on the code file itself.

## Assumptions & theory used

For this analysis there have been some assumptions taken, as well as some  theoretical steps that have been crucial in cleaning the data.

1- **IQR** . The interquartile range (IQR) measures the spread of the middle half of your data. It is the range for the middle 50% of a sample, so we use the IQR to assess the variability where most of our values lie. Larger values indicate that the central portion of our data spread out further. Conversely, smaller values show that the middle values cluster more tightly.

To visualize the interquartile range, imagine dividing your data into quarters. Statisticians refer to these quarters as quartiles and label them from low to high as Q1, Q2, Q3, and Q4. The lowest quartile (Q1) covers the smallest quarter of values in your dataset. The upper quartile (Q4) comprises the highest quarter of values. The interquartile range is the middle half of the data that lies between the upper and lower quartiles. In other words, the interquartile range includes the 50% of data points that are above Q1 and below Q4. The IQR is the red area in the graph below, containing Q2 and Q3 (not labeled).

![IQR](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2018/03/interquartile_range.png?w=576&ssl=1 )

When measuring variability, statisticians prefer using the interquartile range instead of the full data range because extreme values and outliers affect it less. Typically, using the IQR with a measure of central tendency, such as the median, to understand our data’s center and spread. This combination creates a fuller picture of our data’s distribution.

Therefore it is being utilized to get rid of all the outliers that may come from errors when creating the data or from unexpected years.

2- **Substitution of the NaN values**. The developed Nan values´ treatment has been a mix, between the linear interpolation and backwards filling. The linear interpolation is a form of interpolation, which involves the generation of new values based on an existing set of values. Linear interpolation is achieved by geometrically rendering a straight line between two adjacent points on a graph or plane. On the other side, the backwards filling will help us to arrive to those values which have not been fullfilled with the linear interpolation.

3- **Scaling method**. The escalation process has been done dividing each value by the initial one of an indicator (value in 1990). Considering the start point as 1 (initial value divided by itself), each result will show the growth respect to the initial data.

4- **Removing indicators**. 
- Those indicators which have 20% of missing values of its total have been removed because a lack of data shows unreliable results.
- There are some indicators which represent exactly the same through different units, so, we are going to select only one type. For example, in monetary cases, indicators which are expressed with current US $ has been selected. Then, which are showed with the percentage and the total value, we have programmed to selct which ones which show a greater value.


# Run the application
## Dependencies
Dependecies are automatically managed by Poetry and there is NO need to use external dockers for running spark.

To install dependencies run: `poetry install` in same folder where your .toml file is located. 

Poetry will take care of:

- Installing the required Python interpreter
- Installing all the libraries and modules
- Creating the virtual environment for you

## Libraries

- `os`, this module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system. It is used to access to the directories used in each of the notebooks.
- The `glob` module is used to retrieve files/pathnames matching a specified pattern. The pattern rules of glob follow standard Unix path expansion rules. It is also predicted that according to benchmarks it is faster than other methods to match pathnames in directories.

- `pandas`  is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.
- `numpy` is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transformations, and matrices. It is the base for `pandas`.

- From `scipy` import `stats` and `shapiro`. Scipy provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems. Extends NumPy providing additional tools for array computing and provides specialized data structures, such as sparse matrices and k-dimensional trees. Mainly used for statistical calculations.

- The `plotly.express`  module (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or PX. Plotly Express is a built-in part of the plotly library, and is the recommended starting point for creating most common figures. Every Plotly Express function uses graph objects internally and returns a plotly.graph_objects.Figure instance. Throughout the plotly documentation, you will find the Plotly Express way of building figures at the top of any applicable page, followed by a section on how to use graph objects to build similar figures. Therefore it will allow for interacting graphs.

- `seaborn` is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Used for the correlations matrix. 

- The `requests` library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application. It allows for downloading data from the websites.

- The `functools` is a module for higher-order functions: functions that act on or return other functions.

- The `ipywidgets` allows us having interactive widgets (sliders, buttons, dropdowns...) with which we can control and customize the display of our data.

- `warnings` to avoid warning messages when showing the notebook.

- `dash` and `itables`: both libraries can be used for making interactive tables designed for viewing, editing, and exploring large datasets in Python. At the begginning, we started with `dash` (which is a scratch in React.js) but as it is rendered with semantic HTML, we looked for an alternative that visualizes inside our notebook, so we found `itables`, which have a similar functionality.

## Running on local
To start the execution of our code, you can directly run the notebooks on Visual Studio Code opening the files .ipynb, or with the command `poetry run jupyter notebook`.


## Assumptions of Correlation Conclusions Study
- In some graphs we have observed that data follows a very strict flow (very straight and without any deviation representation). In this case we have concluded that we are in front of a lack of data and the interpolation and backward filling have made that this phenomenon occurs. Moreover, these representations don't allow us to extraxt clear conclusions, in some cases they don't have any sense with reality.

- The Net Migration indicator measures the difference between the number of immigrants and emigrants, so the number of people entering the country minus the number of people leaving it. As the difference is measured, it is necessary to see the original data to draw the conclusions correctly. Taking into account whether this net value is positive or negative and extract conclusions according the type of correlation. 

- Something similar occurs with the indicator Direct Foreign Investment. This one shows us the    difference between outflows and inflows, so, if countries invest outside more or less than which is invested in them. Again we should see which are the net values to extract conclusions 	correctly. 
 

## Repository setup
The code is divided in several notebooks that need to be excuted following the corresponding order, which coincides with the one described above in the main steps section.


# Contributing
Open to new improvements/changes 🚀 Just feel free to fork this repository and open a PR back with any changes!
