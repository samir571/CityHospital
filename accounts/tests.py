from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .views import about,delete_contact,get_FAQ
from .models import Contact_Us, Profile

class TestUrls(SimpleTestCase):
    def test_about(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_delete_contact_url(self):
        url = reverse('delete_contact', args=[1])
        self.assertEquals(resolve(url).func, delete_contact)

    def test_get_FAQ_url(self):
        url = reverse('get_FAQ')
        self.assertEquals(resolve(url).func, get_FAQ)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_news_url = reverse('home_news')
        self.contact_form_url = reverse('contact_form')
    def test_home_news(self):
        response = self.client.get(self.home_news_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/index.html')
    def test_contact_form(self):
        response = self.client.get(self.contact_form_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/contact.html')

class TestModels(TestCase):
    def setUp(self):
        self.contact_us = Contact_Us.objects.create(
            full_name='shishir',
            subject="lmao"
        )
        self.profile = Profile.objects.create(
            firstname='Shishir',
            lastname="Kandel",
        )
    def test_contact_us_model(self):
        self.assertEquals(self.contact_us.full_name, 'shishir')
    def test_profile_model(self):
        self.assertEquals(self.profile.firstname, 'Shishir')