# Generated by Django 3.2.5 on 2021-12-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attrs', '0013_auto_20211229_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=10, unique=True, verbose_name='楼号')),
                ('room', models.CharField(max_length=10, verbose_name='教室号')),
            ],
            options={
                'verbose_name': '地点',
                'verbose_name_plural': '地点',
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.FloatField(verbose_name='学分'),
        ),
    ]
