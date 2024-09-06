import requests
import json

# 登录请求
login_url = 'http://127.0.0.1:8000/login/'
login_data = {
    'account': 'd',
    'password': '123456'
}

session = requests.Session()
session.post(login_url, json=login_data)  # 登录

# 获取用户信息
conversationid = 3
query = "你好"
url = f'http://127.0.0.1:8000/conversation/ask/?conversationid={conversationid}&query={query}'

response = session.get(url)

print(response.text)
print(f'Status Code: {response.status_code}')
if response.content:
    print(f'Response JSON: {response.json()}')
else:
    print('No response content')
