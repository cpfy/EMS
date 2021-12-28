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

    def __str__(self):
        return self.code + "-" + self.name

    class Meta:
        verbose_name = '账户'
        verbose_name_plural = verbose_name
        ordering = ['code']


class Student(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    # 与学院多对一
    student_dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        null=True,
        blank=True
    )

    # 与班级多对一
    student_class = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        verbose_name="班级号",
        null=True,
        blank=True
    )
    student_inyear = models.CharField(max_length=5, null=True, blank=True)
    student_age = models.IntegerField(default=0);
    student_home = models.CharField(max_length=15, null=True, blank=True)

    # studentAddress = models.CharField(max_length=128, verbose_name="宿舍地址", null=True)
    student_credit = models.IntegerField(default=0, verbose_name="已修学分")

    def __str__(self):
        return self.id.__str__()

    class Meta:
        verbose_name = "学生"  # 模型名称
        verbose_name_plural = verbose_name  # 模型复数
        ordering = []


class Teacher(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    # 与学院多对一
    teacher_dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        null=True,
        blank=True
    )

    teacher_age = models.IntegerField(default=0);
    teacher_email = models.CharField(verbose_name='邮箱', max_length=30, null=True, blank=True)
    telephone = models.CharField(verbose_name='联系电话', max_length=11, unique=True, null=True, blank=True)

    # brief = models.TextField(verbose_name="简介", null=True)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id.__str__()


class Admin(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(verbose_name='院系名', max_length=10, null=True)
    dept_leader = models.CharField(verbose_name='系主任', max_length=10, null=True, blank=True)

    # 学院培养方案所需学分
    dept_credit = models.IntegerField(default=150, verbose_name="所需学分")

    def __str__(self):
        return str(self.dept_id) + "-" + self.dept_name

    class Meta:
        verbose_name = "院系"
        verbose_name_plural = verbose_name
        ordering = ['dept_id']


class Class(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    brief = models.TextField(verbose_name="简介", null=True, blank=True)

    # classesTeacher = models.ManyToManyField(Teacher)
    # classesCourse = models.ManyToManyField(Course)

    def __str__(self):
        return self.id + "小班"

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = verbose_name
        ordering = ['id']


class CourseTime(models.Model):
    startweek = models.IntegerField(verbose_name="开始周数")
    duringweek = models.IntegerField(verbose_name="持续周数")
    weekday = models.IntegerField(verbose_name="星期")
    startsection = models.IntegerField(verbose_name="开始节数")
    durinsection = models.IntegerField(verbose_name="持续节数")

    def __str__(self):
        dbstr = "周" + self.convertToHanz(self.weekday) \
                + "第" + str(self.startsection) + "-" + str(self.startsection + self.durinsection - 1) + "节[" \
                + str(self.startweek) + "-" + str(self.startweek + self.duringweek - 1) + "周]"
        return dbstr

    def convertToHanz(self, num):
        dict = {
            1: "一",
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            7: "日",
        }
        return dict.get(num)

    class Meta:
        verbose_name = "课程时间"
        verbose_name_plural = verbose_name
        ordering = ['weekday', 'startsection']


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
        verbose_name="先修课",
        max_length=15,
        null=True,
        blank=True
    )
    type = models.CharField(choices=TYPE, verbose_name='课程类别', max_length=1, default='a')
    credit = models.IntegerField(verbose_name="学分")
    # time = models.OneToOneField(CourseTime, on_delete=models.CASCADE, blank=True)

    time = models.ForeignKey(
        "CourseTime",
        on_delete=models.CASCADE,
        verbose_name="课程时间",
        null=True,
        blank=True
    )

    dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="开课学院",
    )

    #dept = models.IntegerField(verbose_name="开课学院")

    courseTeacher = models.ManyToManyField(Teacher, verbose_name="课程教师", blank=True)
    courseStudent = models.ManyToManyField(Student, verbose_name="课程学生", blank=True)

    capacity = models.IntegerField(verbose_name="总容量")
    cur_capacity = models.IntegerField(verbose_name="当前人数", default=0)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code + "-" + self.name
