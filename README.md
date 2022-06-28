# Project steps
# Execute the project

1) Download databases.zip and Python_Code.ipynb
2) Unzip databases in a folder
3) Open Python_Code.ipynb in Jupyter Notebook
4) Run the whole project


# Explanation of the followed process

The Hypothesis:

It is assumed that there exists a correlation between economic growth (positive, negative) and birth rate, (infant) mortality, number of marriages etc. Demonstrate the validity of this assumption based on available datasets. 

In order to check the veracity of this hypothesis the following steps are going to be followed:

1) Select source of information
     To perform this analysis different trustworthy databases organisations have been selected, such as: The World Data Bank, FAOSTAT, OURWORLDINDATA, UN and WID.
     30 indicators are selected from these databases and a correlation analysis will be executed later.
     
2) Extract and import the database  

3) Definition of Normalized Data Model
      All the files.csv used in the project use different formats to present the data and for this reason the tables have to be adjusted. For example, 
      in FAOSTAT countries are collected under the column of "Area", whereas in Databank is "Country". Through Python all columns will be renamed to 
      use a common name among all files.

      The format of the tables will be the following:

      Country | Year | Value

4) Data normalization

5) Definition of Normalized Integrated Data Model 
      On the other hand, the integration is an easier process. Consists in merging the different normalized files in to a single csv containing all
      the data.

6) Data Integration
 
7) Preprocess the database deleting irrelevant information
      Erase variables that dont have enough information or irrelevant entries.

8) Data analysis

9) Report

<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://lucid.app/documents/embedded/0eda53cd-9794-4807-ad95-66074ec37cb8" id="kUGti82~Js8k"></iframe></div>
