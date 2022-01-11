from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
    dept = models.ForeignKey(
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
    inyear = models.CharField(verbose_name="入学年份", max_length=5, default=2021)
    age = models.IntegerField(verbose_name="年龄", default=18)
    home = models.CharField(verbose_name="家乡", max_length=15, null=True, blank=True)

    # studentAddress = models.CharField(max_length=128, verbose_name="宿舍地址", null=True)
    credit = models.IntegerField(default=0, verbose_name="已修学分")

    """courses = models.ManyToManyField(
        "Course",
        verbose_name="已选课程",
        blank=True,
    )"""

    def __str__(self):
        return self.id.__str__()

    class Meta:
        verbose_name = "学生"  # 模型名称
        verbose_name_plural = verbose_name  # 模型复数
        ordering = ['id__code']


class Teacher(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    # 与学院多对一
    dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="学院号",
        null=True,
        blank=True
    )

    age = models.IntegerField(default=0)

    # teacher_email = models.CharField(verbose_name='邮箱', max_length=30, null=True, blank=True)
    # Account已经包含

    telephone = models.CharField(verbose_name='联系电话', max_length=11, unique=True, null=True, blank=True)

    # brief = models.TextField(verbose_name="简介", null=True)

    """courses = models.ManyToManyField(
        "Course",
        verbose_name="开设课程",
        blank=True,
    )"""

    def __str__(self):
        return self.id.__str__()

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
        ordering = ['id__code']




class Admin(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name


class Department(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='院系名', max_length=10, null=True)
    leader = models.CharField(verbose_name='系主任', max_length=10, null=True, blank=True)

    # 学院培养方案所需学分
    fullcredit = models.IntegerField(default=150, verbose_name="所需学分")

    def __str__(self):
        return str(self.no) + "-" + str(self.name)

    class Meta:
        verbose_name = "院系"
        verbose_name_plural = verbose_name
        ordering = ['no']


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
    duringsection = models.IntegerField(verbose_name="持续节数")

    def __str__(self):
        dbstr = "周" + self.convertToHanz(self.weekday) \
                + "第" + str(self.startsection) + "-" + str(self.startsection + self.duringsection - 1) + "节[" \
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


class Place(models.Model):
    building = models.CharField(max_length=10, verbose_name="楼号")
    room = models.CharField(max_length=10, verbose_name="教室号")

    def __str__(self):
        return self.building.__str__() + self.room.__str__()

    class Meta:
        verbose_name = "地点"
        verbose_name_plural = verbose_name
        ordering = ['building']


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
    credit = models.FloatField(verbose_name="学分")

    time = models.ForeignKey(
        "CourseTime",
        on_delete=models.CASCADE,
        verbose_name="课程时间",
        null=True,
        blank=True
    )

    place = models.ForeignKey(
        "Place",
        on_delete=models.CASCADE,
        verbose_name="课程地点",
        null=True,
        blank=True,
    )

    semi = models.IntegerField(verbose_name="课程学年", default=2021)

    dept = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="开课学院",
    )

    capacity = models.IntegerField(verbose_name="总容量")
    count = models.IntegerField(verbose_name="当前人数", default=0)

    # courseTeacher = models.ManyToManyField(Teacher, verbose_name="课程教师", blank=True)
    # courseStudent = models.ManyToManyField(Student, verbose_name="课程学生", blank=True)

    def __str__(self):
        return self.code + "-" + self.name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name
        ordering = ['code']


class OpenCourse(models.Model):  # 开课表
    # 课号
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name="m",
    )

    # 工号
    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.CASCADE
    )

    # semester = models.CharField(max_length=20, blank=True)  # 学期
    # course_time = models.CharField(max_length=20)  # 上课时间

    record = models.BooleanField(verbose_name="录入状态", default=False)

    def __str__(self):
        return self.course.__str__() + "(" + self.teacher.__str__() + ")"

    class Meta:
        # unique_together = ("course", "teacher", "semester")
        # db_table = "OpenTable"
        verbose_name = "开课表"
        verbose_name_plural = verbose_name
        ordering = ['course__code']


class Score(models.Model):  # 选课表
    # 开设课程号
    opencourse = models.ForeignKey(
        "OpenCourse",
        on_delete=models.CASCADE
    )

    # 学号
    student = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        blank=True
    )

    score = models.FloatField(verbose_name="最终成绩", default=0)

    mark = models.FloatField(verbose_name="评教分数", default=0)
    eval = models.BooleanField(verbose_name="是否评价", default=False)

    def __str__(self):
        return self.opencourse.__str__() + "——" + self.student.__str__()

    class Meta:
        verbose_name = "选课表SC"
        verbose_name_plural = verbose_name


class Exam(models.Model):
    # 课号
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name="考试课程",
    )

    # 工号
    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.CASCADE,
        verbose_name="监考教师",
    )

    time = models.DateTimeField()
    place = models.ForeignKey(
        "Place",
        on_delete=models.CASCADE,
        verbose_name="考试地点",
    )

    def __str__(self):
        return self.course.__str__()

    class Meta:
        verbose_name = "考试表"
        verbose_name_plural = verbose_name
        ordering = ['course__code']


class Message(models.Model):
    time = models.DateTimeField(verbose_name="发布时间", default=timezone.now)

    class Meta:
        verbose_name = "通知信息"
        verbose_name_plural = verbose_name
