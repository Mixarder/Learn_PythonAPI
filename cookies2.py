import requests

payload = {"login":"secret_login", "password":"secret_pass"}   #Готовим данные для авторизации

# Так как ответов будет 2, ответ 1го кладем  в веременную response1
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)  # Шлем запрос, положив данные в payload

# Затем из  переменной response1 с помощью get мы получаем переменную auth_cookie которую кладем в переменную cookie_value
cookie_value = response1.cookies.get('auth_cookie')


cookies = {}   # Создаем массив
if cookie_value is not None:    # Через if убедились, что cookie_values не None,
    # только в этом случае добавляем ее значение в переменную cookies с помощью функции .updade
    cookies.update({'auth_cookie': cookie_value})    # Подготовили словарь для авторизованной cookie.

# Делаем сам запрос, а результат запроса кладем в response2
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)   # Печатаем текст response2

# Если все правильно: You are autorized, если логин и пароль не верный You are not auth