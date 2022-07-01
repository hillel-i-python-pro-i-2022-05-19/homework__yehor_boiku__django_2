# Generated by Django 4.0.5 on 2022-06-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=15, verbose_name='Phone Number'),
        ),
    ]