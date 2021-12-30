# Generated by Django 3.2.5 on 2021-12-28 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attrs', '0006_auto_20211228_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['code'], 'verbose_name': '账户', 'verbose_name_plural': '账户'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['id'], 'verbose_name': '班级', 'verbose_name_plural': '班级'},
        ),
        migrations.AlterModelOptions(
            name='coursetime',
            options={'ordering': ['weekday', 'startsection'], 'verbose_name': '课程时间', 'verbose_name_plural': '课程时间'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['dept_id'], 'verbose_name': '院系', 'verbose_name_plural': '院系'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': [], 'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
        migrations.AddField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(default=100, verbose_name='总容量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='cur_capacity',
            field=models.IntegerField(default=0, verbose_name='当前人数'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.IntegerField(default=6, verbose_name='开课学院'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='brief',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseStudent',
            field=models.ManyToManyField(blank=True, to='attrs.Student', verbose_name='课程学生'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseTeacher',
            field=models.ManyToManyField(blank=True, to='attrs.Teacher', verbose_name='课程教师'),
        ),
        migrations.AlterField(
            model_name='course',
            name='pred',
            field=models.ForeignKey(blank=True, max_length=15, null=True, on_delete=django.db.models.deletion.CASCADE, to='attrs.course', verbose_name='先修课'),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attrs.coursetime', verbose_name='课程时间'),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_leader',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='系主任'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attrs.class', verbose_name='班级号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attrs.department', verbose_name='学院号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_home',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_inyear',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attrs.department', verbose_name='学院号'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_email',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='联系电话'),
        ),
    ]
