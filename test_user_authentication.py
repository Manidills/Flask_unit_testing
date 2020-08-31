import requests
import unittest

class TestAuthenticationRestApi(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAuthenticationRestApi, self).__init__(*args, **kwargs)
		self.__api_base_url = "http://localhost:5000"
		self.__secret_url = "/secret"
		self.__user_url = "/user"

	def test_authentication_fail(self):
		r = requests.get(self.__api_base_url + self.__secret_url, auth=('user', 'pass'))
		self.assertEqual(r.status_code, 401)

	def test_authentication_default_user(self):
		r = requests.get(self.__api_base_url + self.__secret_url, auth=('admin', 'root'))
		self.assertEqual(r.status_code, 201)

	def test_user_add(self):
		payload = {'pwd': '123456789'}
		user = '/test_user'
		r = requests.post(self.__api_base_url + self.__user_url + user, data=payload)
		self.assertEqual(r.status_code, 200)
		
	
	
	
	
