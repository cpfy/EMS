# /userprofile/forms.py

# 引入表单类
import datetime

from django import forms
# 引入 User 模型
from django.contrib.auth.models import User


# 登录表单，继承了 forms.Form 类
class UserLoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField()
    userType = forms.CharField()


# 注册用户表单
class UserRegisterForm(forms.Form):
    # 复写 User 的密码

    studentId = forms.CharField()
    userName = forms.CharField()
    password = forms.CharField()
    realName = forms.CharField()

    # password = forms.CharField()
    # password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查，验证密码是否一致
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")


# 修改密码表单
class UserChangePwdForm(forms.Form):
    oldPassword = forms.CharField()
    newPassword = forms.CharField()


# 修改username表单
class UserChangeUsernameForm(forms.Form):
    newUserName = forms.CharField()


# 修改username表单
class UserChangeEmailForm(forms.Form):
    newEmail = forms.CharField()


# 事务申请表单
class UserExemptionForm(forms.Form):
    applyType = forms.CharField()  # 申请类型：免听or免修or缓考or补考
    courseName = forms.CharField()  # 课程名
    courseCollege = forms.CharField()  # 开课院系
    teacher = forms.CharField()  # 任课教师
    courseId = forms.CharField()  # 课程编号
    applyReason = forms.CharField()  # 申请理由


# 选课申请表单
class CourseIdForm(forms.Form):
    courseId = forms.CharField()


# 空教师查询表单
class DateForm(forms.Form):
    #date = forms.DateField(input_formats=['%m %d %Y'], initial=datetime.date.today())
    date = forms.CharField()


# 评教
class EvaluateCourseForm(forms.Form):
    courseId = forms.CharField()
    #mark = forms.IntegerField()
    mark = forms.CharField()


# 课程信息更改
class ChangeCourseInfoForm(forms.Form):
    #id = forms.CharField()
    name = forms.CharField()
    college = forms.IntegerField()
    capacity = forms.IntegerField()  # 课程容量
    category = forms.CharField()  # 课程类别
    credit = forms.IntegerField()  # 课程学分


# 课程信息创建
class CreateCourseForm(forms.Form):
    # courseId = forms.CharField()
    name = forms.CharField()
    college = forms.IntegerField()
    capacity = forms.IntegerField()  # 课程容量
    category = forms.CharField()  # 课程类别
    credit = forms.IntegerField()  # 课程学分


# 选课过滤
class FilterCourseForm(forms.Form):
    filter = forms.BooleanField(required=False)
