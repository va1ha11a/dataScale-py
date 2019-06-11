import unittest
from types import GeneratorType
from chunk_tools import hash_chunk, get_chunks


class ChunkTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hash_chunk(self):
        self.assertEqual(
            hash_chunk("dsfsdfsdfsdfdarffrsdgertqaertaEW".encode()),
            '3c962b55b7186874511c922277196e8483774b73251814cfd5c4297f76f063ae',
            "Hash is not what is expected")

    def test_get_file_chunks(self):
        test_file_name = 'tests/data/test.csv'
        chks = get_chunks(test_file_name)
        self.assertIsInstance(chks, GeneratorType)
        as_list = list(chks)
        self.assertEqual(len(as_list), 26, "Number of cunks incorrect")
        self.assertEqual(as_list[0][:25], b'Reference,Animal_Name,Bre',
                         "First chunk in file incorrect")
        self.assertEqual(as_list[-1][:25], b'ALE,NORMAL,NORTH ADELAIDE',
                         "Last chunk in file incorrect")
