# Generated by Django 3.2.5 on 2022-01-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attrs', '0021_auto_20220102_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['course__code'], 'verbose_name': '考试表', 'verbose_name_plural': '考试表'},
        ),
    ]
