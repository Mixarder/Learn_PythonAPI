import requests

payload = {"login": "secret_login", "password": "secret_pass"}  # Готовим данные для авторизации
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)  # Передаем данные в data

print(response.text)  # При успешной авторизации сервер в отет ничего не присылает
print(
    response.status_code)  # При успешной авторизации или не усешной код 200, тк сервер корректно отработал усешную авторизацию и не успешную.
# print(response.cookies)   # cookies в переменной, хранится в виде объекта. Поэтому нужно использовать функцию dict()
print(dict(response.cookies))  # Если пароль не верный, вместо ключ:значение, словарь будет пустой {}
print(response.headers)  # Получаем все заголовки в том числе и cookie
