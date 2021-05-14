from django.test import SimpleTestCase
from django.urls import reverse, resolve
from resale.views import index, indexlogin, signin, signup, postad, AllAdsView, ProductView, CategoryView

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_indexlogin_url_is_resolved(self):
        url = reverse('indexlogin')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, indexlogin)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, signup)

    def test_signin_url_is_resolved(self):
        url = reverse('signin')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, signin)

    def test_category_url_is_resolved(self):
        url = reverse('category', args=['Mattress'])
        #print(resolve(url))
        self.assertEquals(resolve(url).func, CategoryView)

    def test_allads_url_is_resolved(self):
        url = reverse('allads')
        #print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AllAdsView)

    def test_productdetails_url_is_resolved(self):
        url = reverse('product-details', args=['1'])
        #print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProductView)