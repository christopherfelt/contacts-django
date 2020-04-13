from django.forms import ModelForm

from .models import Contact


class AddContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'number', 'emergency']
