import unittest
from table_cipther import vigenere_encrypt


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(vigenere_encrypt('HELLO', 'KEY'), 'RIJVS')
        self.assertEqual(vigenere_encrypt('WORLD', 'KEY'), 'GSPVH')

    def test_encrypt_mixed_case(self):
        self.assertEqual(vigenere_encrypt('Hello', 'KEY'), 'Rijvs')
        self.assertEqual(vigenere_encrypt('World', 'KEY'), 'Gspvh')

    def test_encrypt_empty_string(self):
        self.assertEqual(vigenere_encrypt('', 'KEY'), '')

    def test_encrypt_with_different_key_lengths(self):
        self.assertEqual(vigenere_encrypt('HELLO', 'LONGKEY'), 'SSYRY')
        self.assertEqual(vigenere_encrypt('HELLO', 'KEYL'), 'RIJWY')
