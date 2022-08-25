import os
import random
import unittest
import numpy as np
import pandas as pd
from datetime import datetime
from Project.Utils.norm import norm
from Project.Utils.corr_confidence import corr_confidence
from Project.Utils.shift_corr import shift_corr
from Project.Utils.max_corr import max_corr

read_path = os.getcwd() + '/Output/'
write_path = os.getcwd() + '/Tests/'
source_df = 'GoldDataframe.csv'

col_country = 'Country'
col_year = 'Year'
col_region = 'Region'
col_index = [col_country, col_year, col_region]

col_gdp = 'GDP'
col_shift = 'Shift'

class Test_Gold(unittest.TestCase):
    def test_region(self):
        df = pd.read_csv(read_path + source_df, index_col = col_index)
        region = random.choice(df.index.get_level_values(col_region).unique())
        df_region = df.loc[df.index.get_level_values(col_region) == region]
        #country = random.choice(df.index.get_level_values(col_country).unique())

        print('Region: ' + region)

        st_time = datetime.now()
        norm_df_region = norm(df_region)
        f_time = datetime.now()
        total_time = f_time - st_time

        max_s = pd.Series(df_region.apply(lambda x: x.max()))
        min_s = pd.Series(df_region.apply(lambda x: x.min()))

        max_norm_s = pd.Series(norm_df_region.apply(lambda x: x.max()))
        min_norm_s = pd.Series(norm_df_region.apply(lambda x: x.min()))

        """ max_s_index = max_s.map(lambda x: df_region.get_loc(x))
        min_s_index = min_s.map(lambda x: df_region.get_loc(x))

        max_norm_s_index = max_norm_s.map(lambda x: df_region.get_loc(x))
        min_norm_s_index = min_norm_s.map(lambda x: df_region.get_loc(x))
 """
        np.testing.assert_array_equal(df.columns, df_region.columns)
        np.testing.assert_array_equal(df_region.columns, norm_df_region.columns)

        print(max_norm_s.map(lambda x: x == 1.0))

        self.assertTrue(all(max_norm_s.map(lambda x: x == 1.0)))
        self.assertTrue(all(min_norm_s.map(lambda x: x == 0.0)))

        """ np.testing.assert_array_equal(max_s_index, max_norm_s_index)
        np.testing.assert_array_equal(min_s_index, min_norm_s_index) """

        print('Time: ' + str(total_time.total_seconds()))

    """ def test_aggregate_region(self):
        df = pd.read_csv(read_path + source_df)
        df.set_index(columns_index, inplace = True)
        region_list = set(df.index.get_level_values(df.index.names.index(column_region)))

        for region in region_list:
            region_df = df.loc[df.index.get_level_values(column_region) == region]
            st_time = datetime.now()
            aggregated_region_df = aggregate(region_df, aggregate_by = column_country, for_index = column_year, new_group_col_name = column_region, group_name = region, abs_indicators = abs_indicators)
            f_time = datetime.now()
            total_time = f_time - st_time
            np.testing.assert_array_equal(df.columns, aggregated_region_df.columns)
            np.testing.assert_array_equal(list(set(df.index.get_level_values(df.index.names.index(column_year)).astype(np.int64))), aggregated_region_df.index.get_level_values(df.index.names.index(column_year)))
            #self.assertEqual(aggregated_region_df.columns, df.columns)
            #self.assertEqual(set(df.index.get_level_values(df.index.names.index(column_year))), aggregated_region_df.index.get_level_values(df.index.names.index(column_year)))
            print('Region: ' + region)
            print('Time: ' + str(total_time.total_seconds()))

    def test_aggregate_pipeline(self):
        df = pd.read_csv(read_path + source_df)
        df.set_index(columns_index, inplace = True)
        region_list = set(df.index.get_level_values(df.index.names.index(column_region)))
        aggregate_df = pd.DataFrame()
        for region in region_list:
            region_df = df.loc[df.index.get_level_values(column_region) == region]
            aggregated_region_df = aggregate(region_df, aggregate_by = column_country, for_index = column_year, new_group_col_name = column_region, group_name = region, abs_indicators = abs_indicators)
            aggregate_df = pd.concat([aggregate_df, aggregated_region_df])
        st_time = datetime.now()
        world_df = aggregate(aggregate_df, column_region, column_year, new_group_col_name = column_region, group_name = 'World', abs_indicators = abs_indicators)
        f_time = datetime.now()
        total_time = f_time - st_time
        np.testing.assert_array_equal(df.columns, world_df.columns)
        np.testing.assert_array_equal(list(set(df.index.get_level_values(df.index.names.index(column_year)).astype(np.int64))), world_df.index.get_level_values(df.index.names.index(column_year)))
        #self.assertEqual(world_df.columns, df.columns)
        #self.assertEqual(set(df.index.get_level_values(df.index.names.index(column_year))), world_df.index.get_level_values(df.index.names.index(column_year)))
        print('Region: World')
        print('Time: ' + str(total_time.total_seconds()))

    def test_aggregate(self):
        time = datetime.now()
        
        df = pd.read_csv(read_path + 'GoldDataframe.csv')
        df.set_index(['Country', 'Year', 'Region'], inplace = True)

        region_list = set(df.index.get_level_values(2))

        st_time = datetime.now()
        aggregate_df = aggregate(df, column_region, column_year, abs_indicators= abs_indicators)
        f_time = datetime.now()
        total_time = f_time - st_time

        print('Time required for an aggregation of the whole Dataframe: ' + str(total_time.total_seconds()))
        print('\n\n\nStarting loop...')
        for region in region_list:
            region_df = df.loc[df.index.get_level_values(column_region) == region]
            print(region_df)
            st_time = datetime.now()
            aggregated_region_df = aggregate(region_df, aggregate_by = column_country, for_index = column_year, new_group_col_name = column_region, group_name = region, abs_indicators = abs_indicators)
            f_time = datetime.now()
            total_time = f_time - st_time
            print('Iteration for region: ' + region)
            print('Total iteration time: ' + str(total_time.total_seconds()))
            print('\n\n')
            aggregate_df = pd.concat([aggregate_df, aggregated_region_df])

        self.assertTrue(1==1)
        print(datetime.now() - time)
        aggregate_df.to_csv(write_path + 'Agg_Test_Fast.csv') """

if __name__ == '__main__':
    unittest.main()