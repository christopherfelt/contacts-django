import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Contact(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = PhoneNumberField()
    emergency = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    


    
