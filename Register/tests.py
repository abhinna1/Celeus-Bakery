from turtle import reset
from django.shortcuts import resolve_url
from django.test import SimpleTestCase, TestCase
from django.test import Client
from django.urls import reverse
from django.urls import resolve

from .models import User
from django.urls import reverse
from Login.views import renderLogin
# Create your tests here.

class LoginTest(TestCase):
    def test_login_url(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,renderLogin)
        # url = reverse('login')
        # self.assertEquals(resolve(url).func, renderLogin)
