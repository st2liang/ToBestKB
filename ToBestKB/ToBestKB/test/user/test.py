from django.test import TestCase, Client
from django.urls import reverse
import json
from unittest.mock import patch

class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('sign_up')  # 替换为你的 URL 名称

    def test_sign_up_success(self):
        # 模拟 UsersServices.create_user 方法
        with patch('ToBestKB.UsersServices.create_user') as mock_create_user:
            mock_create_user.return_value = 1  # 模拟返回的用户 ID
            response = self.client.post(
                self.url,
                data=json.dumps({'account': 'testuser', 'password': 'testpass'}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            self.assertJSONEqual(response.content, {'returnid': 1})

    def test_sign_up_json_decode_error(self):
        response = self.client.post(
            self.url,
            data='invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "sign_up JSONDecodeError"})

    def test_sign_up_method_not_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"error": "sign_up request methed is not POST"})
