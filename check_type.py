import requests

param = {"param1": "value1"}
url = "https://playground.learnqa.ru/api/check_type"

response = requests.get(url, data=param)

print(response.text)

# При использовании метода отличного от GET, при использовании params, все равно приходит ответ с указанными параметрами,
# хотя ответ с параметрами должен приходить только при использовании параметра data. Нужно найти на это ответ.
