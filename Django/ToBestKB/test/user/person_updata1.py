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

# 修改用户信息
info_url = 'http://127.0.0.1:8000/person/change/'
info_data ={
    'name': "张三",
    "password" : "123456",
    "phone":12345678912
}
response = session.put(info_url,json=info_data )

print(response.text)
print(f'Status Code: {response.status_code}')
if response.content:
    print(f'Response JSON: {response.json()}')
else:
    print('No response content')
