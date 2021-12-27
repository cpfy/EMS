from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    TYPE = (
        ('a', '学生'),
        ('b', '老师'),
        ('c', '管理员')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    status = models.CharField(choices=TYPE, verbose_name='身份', max_length=1, default='a')
    code = models.CharField(verbose_name='学号/工号', max_length=10, unique=True)
    name = models.CharField(verbose_name='姓名', max_length=5)

    class Meta:
        verbose_name = '账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.user.__str__())


class Student(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    # 与学院多对一
    student_dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        null=True
    )

    # 与班级多对一
    student_class = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        verbose_name="班级号",
        null=True
    )
    student_inyear = models.CharField(max_length=5)
    student_age = models.IntegerField(default=0);
    student_home = models.CharField(max_length=15)

    # studentAddress = models.CharField(max_length=128, verbose_name="宿舍地址", null=True)
    student_credit = models.IntegerField(default=0, verbose_name="已修学分")

    class Meta:
        verbose_name = "学生"  # 模型名称
        verbose_name_plural = verbose_name  # 模型复数


class Teacher(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    # 与学院多对一
    teacher_dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        null=True
    )

    teacher_age = models.IntegerField(default=0);
    teacher_email = models.CharField(verbose_name='邮箱', max_length=30, null=True)
    telephone = models.CharField(verbose_name='联系电话', max_length=11, unique=True, null=True)

    # brief = models.TextField(verbose_name="简介", null=True)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name


class Admin(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(verbose_name='院系名', max_length=10, null=True)
    dept_leader = models.CharField(verbose_name='系主任', max_length=10, null=True)

    # 学院培养方案所需学分
    dept_credit = models.IntegerField(default=150, verbose_name="所需学分")

    class Meta:
        verbose_name = "院系"
        verbose_name_plural = verbose_name


class Class(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    brief = models.TextField(verbose_name="简介", null=True)

    # classesTeacher = models.ManyToManyField(Teacher)
    # classesCourse = models.ManyToManyField(Course)

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = verbose_name


class Course(models.Model):
    TYPE = (
        ('a', '必修'),
        ('b', '选修'),
        ('c', '限修'),
        ('d', '任修')
    )
    code = models.CharField(max_length=15, verbose_name="课程码", primary_key=True, unique=True)
    name = models.CharField(max_length=10, verbose_name="课程名称", unique=True)
    pred = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        max_length=15,
        null=True
    )
    type = models.CharField(choices=TYPE, verbose_name='课程类别', max_length=1, default='a')
    ident = models.CharField(max_length=10)  # 课程性质
    credit = models.IntegerField(verbose_name="学分")

    courseStudent = models.ManyToManyField(Student, verbose_name="课程学生")
    courseTeacher = models.ManyToManyField(Teacher, verbose_name="课程教师")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name
