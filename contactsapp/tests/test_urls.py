import uuid
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from django.contrib.auth import get_user_model

from contactsapp.views import (HomepageView, ContactsListView,
                               ContactDetailView, CreateContact, UpdateContact,
                               DeleteContact)


class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_contact_urls_resolves(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func.view_class, ContactsListView)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=[uuid.uuid4()])
        self.assertEquals(resolve(url).func.view_class, ContactDetailView)

    def test_create_url_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, CreateContact)

    def test_update_url_resolves(self):
        url = reverse('update', args=[1234])
        self.assertEquals(resolve(url).func.view_class, UpdateContact)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=[1234])
        self.assertEquals(resolve(url).func.view_class, DeleteContact)
