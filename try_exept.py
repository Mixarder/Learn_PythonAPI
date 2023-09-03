from json.decoder import JSONDecodeError  # Импорт ошибки, который мы будем ожидать
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()  # Код с парсингом текста ответа и его выводом, поместили в блок try
    print(parsed_response_text)  # это означает, что мы попробуем его выполнить
except JSONDecodeError:
    print("Response is not a JSON format")
