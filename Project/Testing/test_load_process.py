

import os
import unittest

from Project.Utils.read_databases import read_databases

class TestLoadProcess(unittest.TestCase):
    
    def test_un_data(self):
        read_path = os.getcwd() + '\Databases' #Path to your databases folder to be read
        special_source = ['databank', 'faostat', 'kaggle', 'un_data', 'worldbank', 'WID'] #List with all the sources that need special treatment
        read_databases(read_path, special_source, False)

if __name__ == '__main__':
    unittest.main()