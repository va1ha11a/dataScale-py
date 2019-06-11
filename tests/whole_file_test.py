import unittest

from main import store_file, restore_file
from meta import redis_graph


class WholeFileTests(unittest.TestCase):
    def setUp(self):
        self.graph_obj = redis_graph

    def tearDown(self):
        pass

    def test_store_restore(self):
        store_file_name = 'tests/data/test.csv'
        restore_file_name = 'tests/rdata/test.csv'
        test_bucket_loc = 'test'
        self.assertTrue(
            store_file(store_file_name, test_bucket_loc, self.graph_obj))
        self.assertTrue(restore_file(restore_file_name, self.graph_obj))
        self.graph_obj.delete()
        # TODO Check files are the same
        # TODO Delete restored file to clean up
