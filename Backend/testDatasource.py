import unittest
from datasource import DataSource

class TestDataSource(unittest.TestCase):
    def setUp(self):
        self.test = DataSource()
        self.connection = self.test.connect()
        self.product_list = ['0_bj', '18_bj', '16_hd', '25_bj', '42_bj', '31_hd', '54_hd', '57_breyers']
        self.rank_by_rating_result = ['31_hd','16_hd', '25_bj', '42_bj', '57_breyers', '18_bj', '0_bj', '54_hd']
        self.rank_by_name_result = ['0_bj', '54_hd', '42_bj', '57_breyers','31_hd', '25_bj', '18_bj', '16_hd']
        self.rank_by_rating_count_result = ['0_bj', '18_bj', '31_hd', '16_hd', '54_hd', '42_bj', '57_breyers', '25_bj']
    
    # border case
    def test_null_product_list(self):
        self.assertListEqual(self.test.rank_product(self.connection, [], None), [])
    
    '''
    In our html page, we will prodvide a dropdown box with three options to choose from (as the rank_column parameter for rank_product()): name (alphabetical rank), rating (numerical rank), rating_count(numerical rank). These options will be passed in as strings to rank_product(), therefore we are NOT testing for inputs that are not of type string, or are not one of these options. 
    '''
    
    def test_null_rank_column(self):
        self.assertListEqual(self.test.rank_product(self.connection, self.product_list, None), self.rank_by_name_result)
    
    def test_rank_by_rating_count(self):
        self.assertListEqual(self.test.rank_product(self.connection, self.product_list, "rating_count"), self.rank_by_rating_count_result)

    def test_rank_by_rating(self):
        self.assertListEqual(self.test.rank_product(self.connection, self.product_list, "rating"), self.rank_by_rating_result)
        

if __name__ == '__main__':
    unittest.main()