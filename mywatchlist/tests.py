from django.test import TestCase, Client

# Create your tests here.
class WatchListUnitTesting(TestCase):
    def setUp(self):
        self.client = Client()

    def view_url(self):
        response = self.client.get('/katalog/')
        self.assertEqual(response.status_code,200)

    def test_view_html(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_view_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_view_json(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def view_template(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mywatchlist.html')