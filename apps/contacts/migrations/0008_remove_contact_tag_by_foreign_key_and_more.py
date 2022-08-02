# Generated by Django 4.0.5 on 2022-07-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_remove_contact_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='tag_by_foreign_key',
        ),
        migrations.AlterField(
            model_name='detailforcontact',
            name='contact_type',
            field=models.CharField(blank=True, choices=[('Phone number', 'Phone number'), ('Linkedin', 'Linkedin'), ('Telegram', 'Telegram'), ('Email', 'Email')], default='Linkedin', help_text='Add details about you Contact', max_length=100, verbose_name='Details'),
        ),
    ]
