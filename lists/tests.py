from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_processes_POST_request(self):
        item_message = "A new list item"
        response = self.client.post('/', data={'item_text': item_message})
        self.assertIn(item_message, response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
