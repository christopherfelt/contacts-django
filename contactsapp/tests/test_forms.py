from django.test import TestCase

from contactsapp.forms import ContactForm


class TestForms(TestCase):

    def test_contact_form(self):
        form_data = {
            'name': 'Joesph Smith',
            'number': '2345677878',
            'emergency': True}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
