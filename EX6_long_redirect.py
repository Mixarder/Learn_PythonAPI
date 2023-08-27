import requests

url = "https://playground.learnqa.ru/api/long_redirect"

response = requests.get(url, allow_redirects=True)

print(f'First URL: {url}')
print(f'Last Url: {response.url}')
print(f'Number of Redirects: {len(response.history)}')
for redirect in response.history:
    print(f"Redirect URL: {redirect.url}")