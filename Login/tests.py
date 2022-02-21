from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from .views import renderLogin
# Create your tests here.

class LoginTest(TestCase):
    def test_case_detail_url(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,renderLogin)