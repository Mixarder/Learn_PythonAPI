import requests

url = "https://playground.learnqa.ru/api/hello"
payload = {"name": "Mike"}
response = requests.get(url, params=payload)
# response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
