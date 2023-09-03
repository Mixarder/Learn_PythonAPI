import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
print(response.text)

# При использовании метода отличного от GET, при использовании params, все равно приходит ответ с указанными параметрами,
# хотя ответ с параметрами должен приходить только при использовании параметра data. Нужно найти на это ответ.
