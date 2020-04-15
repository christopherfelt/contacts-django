from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from contactsapp.models import Contact


class TestViews(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="johnsmith1",
            email="johnsmith1@email.com",
            password="testpass123"
        )
        self.contact = Contact.objects.create(
            username=self.user,
            name="Jane Smith",
            number="1231231234",
            emergency=True
        )
        
        self.client = Client()
        self.client.login(username="johnsmith1", password="testpass123")
        self.homepage_url = reverse('homepage')
        self.contacts_url = reverse('contacts')
        self.delete_url = reverse('delete', args=[self.contact.pk])
        self.update_url = reverse('update', args=[self.contact.pk])

    def test_homepage_GET(self):
        response = self.client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_contact_GET(self):
        response = self.client.get(self.contacts_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')

    def test_detail_GET(self):
        new_contact = Contact.objects.create(
            username=self.user,
            name="Josh Smith",
            number='0987654321',
            emergency=True

        )
        url = reverse('detail', args=[new_contact.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_contact.html')
        self.assertContains(response, "Josh Smith")
        self.assertContains(response, "987654321")
        self.assertContains(response, "Yes")

    def test_create_GET(self):
        url = reverse('add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_contact.html')
    
    def test_create_POST(self):
        url = reverse('add')
        response = self.client.post(url, {
            'name': "Jack Smith",
            'number': "2084310069",
            'emergency': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contacts'))
        self.assertEqual(Contact.objects.all()[1].name, "Jack Smith")

    def test_update_GET(self):
        url = reverse('update', args=[self.contact.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_contact.html')
    
    def test_update_POST(self):
        url = reverse('update', args=[self.contact.pk])
        response = self.client.post(url, {
            'name': "Jack Smith",
            'number': "2084316969",
            'emergency': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contacts'))
        self.assertEquals(Contact.objects.all()[0].name, "Jack Smith")

    def test_delete_GET(self):
        url = reverse('delete', args=[self.contact.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_contact.html')

    def test_delete_POST(self):
        url = reverse('delete', args=[self.contact.pk])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contacts'))
        self.assertEqual(Contact.objects.count(), 0)
