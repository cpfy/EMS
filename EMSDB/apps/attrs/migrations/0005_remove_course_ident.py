# Generated by Django 3.2.5 on 2021-12-28 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attrs', '0004_auto_20211228_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='ident',
        ),
    ]
