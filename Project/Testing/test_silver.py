

import os
import sys
import unittest
import logging

import pandas as pd
from pandas.testing import assert_frame_equal
from Project.Utils.data_treat import iqr_treatment, nan_treatment

read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
write_path = os.getcwd() + '\Output' #Path to the folder you want to store the dataframes


class TestLoadProcess(unittest.TestCase):

    def test_data_treat(self):
        log = logging.getLogger('TestDataTreat')
        log.setLevel(logging.DEBUG)
        file_path = write_path  + '/BronzeDataframe.csv'

        source = pd.read_csv(file_path) 

        aux = source.loc[source['Country'] == 'Spain']
        aux = iqr_treatment(aux)
        aux = nan_treatment(aux)

        for column in aux.columns[3:]:
            self.assertNotEqual((aux[column].notna().sum() != len(aux)), (aux[column].isna().sum() != len(aux)), 'Error in data treat')
        
        auxRetreat = iqr_treatment(aux)

        assert_frame_equal(aux, auxRetreat)
            
                            


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    unittest.main()
