# Generated by Django 3.2.5 on 2021-12-29 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attrs', '0012_auto_20211229_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='cur_capacity',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='open',
            new_name='opencourse',
        ),
    ]