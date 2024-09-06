from django.test import Client
import json

import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToBestKB.settings')
settings.configure()



client = Client()
response = client.post('http://127.0.0.1:8000/sign_up/', data=json.dumps({'account': 'testuser', 'password': 'testpass'}), content_type='application/json')

print(response.status_code)
print(response.json())
