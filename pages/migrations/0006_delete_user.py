# Generated by Django 4.1.4 on 2023-02-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
