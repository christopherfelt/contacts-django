from django.test import TestCase
from django.contrib.auth import get_user_model

from contactsapp.models import Contact


class TestModels(TestCase):

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

    def test_contact_creation(self):
        self.assertEqual(f'{self.contact.username.username}', "johnsmith1")
        self.assertEqual(f'{self.contact.name}', "Jane Smith")
        self.assertTrue(self.contact.emergency)