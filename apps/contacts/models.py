from django.core.validators import MaxLengthValidator
from django.db import models


class Contact(models.Model):
    contact_name = models.CharField('Contact Name', help_text='It is name of human', max_length=20)
    phone_number = models.PositiveIntegerField('Phone Number')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)