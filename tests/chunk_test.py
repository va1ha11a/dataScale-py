import unittest

from chunk_tools import hash_chunk, get_chunks, store_chunk, restore_chunk


class ChunkTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hash_chunk(self):
        chunk = "dsfsdfsdfsdfdarffrsdgertqaertaEW".encode()
        hashed = hash_chunk(chunk)
        self.assertEqual(
            hashed,
            '3c962b55b7186874511c922277196e8483774b73251814cfd5c4297f76f063ae',
            "Hash is not what is expected")
