import requests

url = "https://playground.learnqa.ru/api/compare_query_type"
payload = [{"method": "CGETT"}, {"method": "CPOSTT"}, {"method": "CPUTT"}, {"method": "CDELETET"}, {"method": "HEAD"}]
response = requests.get(url, data=payload[1])
print(response.text)
print(response.status_code)
