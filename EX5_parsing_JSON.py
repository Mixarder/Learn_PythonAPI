# Ваша задача с помощью библиотеки JSON,  распарсить  переменную json_text и вывести текст второго сообщения с помощью функции print.


import json

json_text = '''
{
    "messages": [
        {"message": "This is the first message", "timestamp": "2021-06-04 16:40:53"},
        {"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}
    ]
}
'''

try:
    data = json.loads(json_text)
    messages = data.get("messages", [])

    message_index = 3  # Указываем желаемый индекс сообщения (считая с 1)

    selected_message = messages[message_index - 1] if 0 <= message_index - 1 < len(messages) else None

    if selected_message:
        message_text = selected_message.get("message")
        if message_text:
            print(message_text)
        else:
            print("Selected message has no 'message' key")
    else:
        print("Invalid message index")
except json.JSONDecodeError:
    print("Invalid JSON format")

    # В этом коде:
    #
    # Мы используем многострочную строку (тройные одинарные кавычки ''') для хранения JSON-текста.
    # Мы пытаемся распарсить JSON и получить объект данных.
    # Затем извлекаем массив messages из объекта данных.
    # Задаем желаемый индекс сообщения, которое хотим получить (считая с 1).
    # Проверяем, что индекс находится в допустимом диапазоне и извлекаем соответствующее сообщение из массива.
    # Если сообщение было успешно извлечено, мы получаем текст сообщения и выводим его. Если ключ "message" отсутствует, выводится соответствующее сообщение.
    # Если индекс недопустим, выводится сообщение об ошибке.
    # Такой код обрабатывает JSON-формат, извлекает сообщение по индексу и обеспечивает более общий и унифицированный подход к решению задачи.
