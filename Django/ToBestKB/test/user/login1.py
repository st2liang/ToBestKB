import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {
    'account': 'c',
    'password': '123'
}

response = requests.post(url, json=data)
print(response.text)
print(f'Status Code: {response.status_code}')
if response.content:
    print(f'Response JSON: {response.json()}')
else:
    print('No response content')

