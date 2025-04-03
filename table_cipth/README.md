Описание: Программа шифрует сообщения используя табличный шифр.
Установка и запуск:

1. Убедитесь, что у вас установлен Python 3 и выше
2. Склонируйте репозиторий
3. Для использования шифра в своей программе, создайте экземпляр класса TableCipher с нужным ключом и вызывайте методы encrypt() и decrypt()
    ```bash
    cipher = TableCipher('QWERTYUIOPASDFGHJKLZXCVBNM')
    encrypted_text = cipher.encrypt('HELLO')
    print(encrypted_text)
    decrypted_text = cipher.decrypt('ITSSG')
    print(decrypted_text)
4. Для запуска тестов выполните команду
    ```bash
    python -m unittest test_cipt.py
