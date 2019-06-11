import my_app
import unittest

class MyTestCase(unittest.TestCase):
	def setUp(self):
		my_app.app.Testing = True
		self.app = my_app.app.test_client()

	def test_home(self):
		result = self.app.get('/')
		assert result.status_code == 200

	def test_bad_type(self):
		data = "banana"
		with self.assertRaises(TypeError):
			result = sum(data)
