from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from Home.views import homepage


# Create your tests here.
class TestUrls(SimpleTestCase):
    # def test_home_url(self):
    #     url=reverse('home')
    #     print(url)
    #     self.assertEqual(resolve(url).func,homepage)
    
    # # incorrect URL 
    def test_home_url2(self):
        url=reverse('asasdasd')
        print(url)
        self.assertEqual(resolve(url).func,homepage)