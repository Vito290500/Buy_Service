# Generated by Django 4.2.1 on 2023-10-16 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allservice', '0002_remove_user_profile_country_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_authentification',
        ),
    ]
