import requests
payload = {"name": "Mike"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
