import requests
import json

url = 'http://127.0.0.1:8000/sign_up/'
data = {
    'account': 'd',
    'password': '1234'
}

response = requests.post(url, json=data)
print(response.text)
print(f'Status Code: {response.status_code}')
if response.content:
    print(f'Response JSON: {response.json()}')
else:
    print('No response content')

