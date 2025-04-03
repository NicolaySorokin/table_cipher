import random


class TableCipher:
    def __init__(self, key=None):
        self.key = key or ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26))
        self.table = self.create_table()

    def create_table(self):
        table = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, letter in enumerate(alphabet):
            table[letter] = self.key[i]
        return table

    def encrypt(self, text):
        return ''.join(self.table.get(char.upper(), char) for char in text)

    def decrypt(self, text):
        reverse_table = {v: k for k, v in self.table.items()}
        return ''.join(reverse_table.get(char.upper(), char) for char in text)
