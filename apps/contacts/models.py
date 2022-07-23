from django.core.validators import MaxLengthValidator
from django.db import models

from django.db.models import Field


class TagsChoices(models.TextChoices):
    FAMILY = 'family', '#family'
    FRIEND = 'friend', '#friend'
    WORK = 'work', '#work'


class SomeTag(models.Model):
    tag = models.CharField('Tag', help_text='Some tag for your contact', max_length=200)

    def __str__(self) -> str:
        return f'{self.tag}'

    __repr__ = __str__


class Contact(models.Model):
    contact_name = models.CharField('Contact Name',
                                    help_text='It is name of human',
                                    max_length=20,
                                    default='Vasya')
    # phone_number = models.PositiveIntegerField('Phone Number', help_text='Phone number must start "380"')

    birthday = models.CharField('Day of birth', max_length=20, default='01/01/99')

    tags = models.CharField(
        'Tags', max_length=100,
        help_text='Tags dor you Contact',
        choices=TagsChoices.choices,
        default=TagsChoices.WORK,
        blank=True,
    )

    tag_by_foreign_key = models.ForeignKey(
        SomeTag,
        related_name='tag_by_foreign_key',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    tag_by_many_to_many = models.ManyToManyField(
        SomeTag,
        related_name='tag_by_many_to_many',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact_name}'

    __repr__ = __str__


class Tags(models.Model):
    tag = models.CharField('Tag',
                           max_length=50,
                           help_text='Tag for your contact')

    def __str__(self) -> str:
        return f'{self.tag}'

    __repr__ = __str__


class DetailForContact(models.Model):
    PHONE_NUMBER = 'APN'
    LINKEDIN = 'LinIn'
    TELEGRAM = 'TG'
    EMAIL = 'EMAIL'
    DETAIL_IN_CONTACT_CHOICES = [
        (PHONE_NUMBER, 'Phone number'),
        (LINKEDIN, 'Linkedin'),
        (TELEGRAM, 'Telegram'),
        (EMAIL, 'Email'),
    ]
    contact_type = models.CharField(
        'Details',
        max_length=100,
        help_text='Add details about you Contact',
        choices=DETAIL_IN_CONTACT_CHOICES,
        default=LINKEDIN,
        blank=True,
    )
    detail_for_contact_type = models.CharField(
        'Detail for contact type',
        max_length=20,
        default='@example')

    detail = models.ForeignKey(
        to=Contact,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
