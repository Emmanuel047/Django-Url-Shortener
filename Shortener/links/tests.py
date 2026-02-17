from django.test import TestCase
from django.urls import reverse
from .models import Links

class LinksTests(TestCase): 
    def test_create_new_short_link(self):  
        response = self.client.post('/', {'link': 'https://www.google.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/')
        self.assertEqual(Links.objects.count(), 1)

    def test_duplicate_url_reuses_code(self):
        self.client.post('/', {'link': 'https://google.com'})
        response = self.client.post('/', {'link': 'https://google.com'})
        self.assertEqual(Links.objects.count(), 1)

    def test_redirect_and_click_count(self):
        self.client.post('/', {'link': 'https://google.com'})
        short_code = Links.objects.first().short_code
        response = self.client.get(f'/{short_code}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Links.objects.first().on_click, 1)

    def test_stats_page(self):
        self.client.post('/', {'link': 'https://google.com'})
        short_code = Links.objects.first().short_code
        response = self.client.get(f'/{short_code}/stats/')
        self.assertContains(response, 'google.com')

    def test_invalid_url_error(self):
        response = self.client.post('/', {'link': 'invalid'})
        self.assertContains(response, 'Enter full URL')
