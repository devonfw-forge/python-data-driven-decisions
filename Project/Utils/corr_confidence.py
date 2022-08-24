import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from typing import Callable

VALID_LIST = (pearsonr, spearmanr)

def corr_confidence (s1: pd.Series, s2: pd.Series, confidence: float = 0.05, method: Callable = spearmanr):
    """ 
        Compute the correlation between two series.

        PARAMETERS:
            s1, s2: pd.Series
                Series whose correlation will be computed.
            confidence: float, default = 0.05
                Level of confidence for the correlation. If the resulting p-value is higher than the confidence level, the correlation value will be returned as NaN.
            method: pearsonr | spearmanr, default spearmanr
                Correlation formula to be used for the compute. Only admits pearsonr or spearmanr.
        RETURNS:
            float
                Value of the correlation. If it could not be computed or if the p-value was higher than the confidence level, it will return a NaN.

    """

    if method not in VALID_LIST:
        raise Exception('Method \'' + method.__name__ + '\' is not a valid function for correlations.')
    
    else: 
        try:
            # Calculate correlation using specified method. Return that value or NaN depending on the confidence level and the obtained p-value.
            corr, pval = s1.corr(s2, method = method)
            return corr if pval <= confidence else np.NaN
        except:
            return np.NaN