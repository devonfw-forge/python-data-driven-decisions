from numpy import percentile
import pandas as pd
import numpy as np

def iqr_treatment(data):
    """ Method that identifies the outliers and replaces them with a Nan value
        PARAMTERS:
            data: dataframe
                the dataframe to be modified 
    """

    for columna in data.columns[2:]:

        count = 0
        outliers = []
        auxOutliers = []

        # calculate interquartile range
        q25, q75 = percentile(data[columna], 25), percentile(data[columna], 75)
        iqr = q75 - q25
        # calculate the outlier cutoff
        cut_off = iqr * 1.5
        lower, upper = q25 - cut_off, q75 + cut_off
        # identify true outliers and replaces them with nan (if there are > 3 outliers  consecutive it's considered as a fake outlier)
        for pos,x in enumerate(data[columna]):
            outlierIndex = data[columna].index[pos]
            if x < lower or x > upper:
                auxOutliers.append(outlierIndex)
                count += 1
            else:
                if count >=3:
                    del auxOutliers[-count:]
                count = 0
        if count >=3:
                    del auxOutliers[-count:]
            
        for elem in auxOutliers:
            data.loc[elem, columna]= np.nan

    
    return data
            


def nan_treatment(data):
    """ Method that interpolates replacing Nan values
        PARAMTERS:
            data: dataframe
                the dataframe to be modified 
    """
    data = data.interpolate(limit_direction='both')
    return data