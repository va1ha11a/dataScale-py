import unittest
import filecmp
import os

from contextlib import suppress

from main import store_file, restore_file
from meta import redis_graph


class WholeFileTests(unittest.TestCase):
    def setUp(self):
        self.graph_obj = redis_graph
        self.store_file_name = 'tests/data/test.csv'
        self.restore_file_name = 'tests/rdata/test.csv'

    def tearDown(self):
        ## Clean Up ##
        # Delete restored file to clean up
        with suppress(FileNotFoundError):
            os.remove(self.restore_file_name)
        # Remove metadata from graph
        self.graph_obj.delete()

    def test_store_restore(self):
        test_bucket_loc = 'test'
        self.assertTrue(
            store_file(self.store_file_name, test_bucket_loc, self.graph_obj))
        self.assertTrue(restore_file(self.restore_file_name, self.graph_obj))

        # Check files exist and are the same
        self.assertTrue(os.path.isfile(self.restore_file_name),
                        "Restore file does not exist")
        filecmp.clear_cache()
        self.assertTrue(
            filecmp.cmp(self.store_file_name,
                        self.restore_file_name,
                        shallow=True), "Files signatures do not match:\n"
            f"{self.store_file_name}: {os.stat(self.store_file_name)}\n"
            f"{self.restore_file_name}: {os.stat(self.restore_file_name)}")
        self.assertTrue(
            filecmp.cmp(self.store_file_name,
                        self.restore_file_name,
                        shallow=False), "Files contents do not match")
