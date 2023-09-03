import requests

response = requests.post("https://playground.learnqa.ru/api/get_301")

print(response.status_code)
print(response.text)

# # Для показа истории при редиректе на другой ресурс
#
# response = requests.post("https://playground.learnqa.ru/api/get_301")
# first_respose = response.history[0]
# second_response = response
#
# print(first_respose.url)
# print(second_response.url)
