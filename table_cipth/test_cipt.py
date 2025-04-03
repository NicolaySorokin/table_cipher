import unittest
from table_cipth import TableCipher


class TestTableCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = TableCipher('QWERTYUIOPASDFGHJKLZXCVBNM')

    def test_encryption(self):
        self.assertEqual(self.cipher.encrypt('HELLO'), 'ITSSG')

    def test_decryption(self):
        self.assertEqual(self.cipher.decrypt('ITSSG'), 'HELLO')
