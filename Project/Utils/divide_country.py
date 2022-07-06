from Project.Utils.data_treat import iqr_treatment, nan_treatment



def country_divider(df, dict_df_countries):
    """ Method that takes the merged dataframe and divides in smaller dataframes by countries. Also it discards countries with unsuficient data.
        PARAMTERS:
            df: dataframe
                The dataframe to be modified
            dict_df_countries: dataframe dictionary
                Where all countries df will be saved
    """
    dict_country = {} #Ad-hoc dictionary to count the number of entries for each country
    VALUE = 1
    THRESHOLD = 15 #Minimum number of entries a country needs to have to be included into our research
    
    #Counts all the entries for each country and stores into the dictionary with countries as keys and the count as its associated value    
    for country in df['Country']:
        if country not in dict_country:
            dict_country[country] = VALUE
        else:
            dict_country[country] += VALUE

    #Removes all the countries that do no meet the minimun entries requirement        
    dict_country = {country:num for country, num in dict_country.items() if num >= THRESHOLD}

    for country in dict_country.keys():
        dict_df_countries[country] = df.loc[df['Country'] == country]
    
    for country in dict_df_countries.keys():
        #Treat the dataframe
        df = dict_df_countries[country]
        df = iqr_treatment(df)
        df.set_index(['Country', 'Year'], inplace=True)
        dict_df_countries[country] = nan_treatment(df)
