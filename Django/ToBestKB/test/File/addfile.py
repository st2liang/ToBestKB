import requests

# 登录请求
login_url = 'http://127.0.0.1:8000/login/'
login_data = {
    'account': 'd',
    'password': '123456'
}

session = requests.Session()
session.post(login_url, json=login_data)  # 登录

# 文件上传请求
kdbid=7
upload_url = f'http://127.0.0.1:8000/kdb/upload/?kdbid={kdbid}'  # 替换为文件上传的实际 URL
print(upload_url)
files = {'file': ('v1.pdf', open('v1.pdf', 'rb'))}  # 上传的文件路径和文件名
response = session.post(upload_url, files=files)

print(response.text)
print(f'Status Code: {response.status_code}')
if response.content:
    print(f'Response JSON: {response.json()}')
else:
    print('No response content')
