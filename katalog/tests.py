from django.test import TestCase, Client

# Create your tests here.
class Tugas2UnitTesting(TestCase):
    def test_hello_is_exist(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code,200)