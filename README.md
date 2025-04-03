Описание:
Программа шифрует сообщения используя шифр Виженера.

Установка и запуск:
1. Убедитесь, что у вас установлен Python 3 и выше
2. Склонируйте репозиторий
3. Для использования шифра Виженера в своей программе, используйте функцию vigenere_encrypt для шифрования сообщений
Пример:
    ```bash
    message = "HELLO"
    key = "KEY"

    encrypt = vigenere_encrypt(message, key)
    print(encrypt)