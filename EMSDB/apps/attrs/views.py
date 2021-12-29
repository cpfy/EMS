from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .forms import *
from .models import Student, Class, Teacher, Admin, Department, Course, Account, CourseTime, Score, OpenCourse, Score


# Create your views here.

# 登录相关 #

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        # print("POST=",request.POST)

        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象

            myusername = data['userName']
            mypassword = data['password']
            myusertype = data['userType']

            print("get username = " + myusername)
            print("get password = " + mypassword)
            # print("userType = " + data['userType'])

            user = authenticate(username=myusername, password=mypassword)
            if user:
                account = Account.objects.get(user=user)
                if (checkUserTypeIsFit(account.status, myusertype)):
                    # 将用户数据保存在 session 中，即实现了登录动作
                    login(request, user)
                    retdata = {
                        'result': True,
                        'id': myusername,
                        'info': "登录成功！"
                    }
                    return JsonResponse(retdata)

                else:
                    retdata = createFalseJsonWithIdAndInfo("账号类型有误。请重新选择~")
                    return JsonResponse(retdata)

            else:
                retdata = createFalseJsonWithIdAndInfo("账号或密码输入有误。请重新输入~")
                return JsonResponse(retdata)

        else:
            retdata = createFalseJsonWithIdAndInfo("json格式不合法")
            return JsonResponse(retdata)

    else:
        retdata = createFalseJsonWithIdAndInfo("请使用POST请求数据")
        return JsonResponse(retdata)


# 用户退出,实际vue负责管理
def user_logout(request):
    logout(request)
    return redirect("article:article_list")


# 用户注册
def user_register(request):
    if request.method == 'POST':
        print(request.POST)

        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():

            data = user_register_form.cleaned_data
            myusername = data['userName']
            mypassword = data['password']
            mystuid = data['studentId']
            myrealname = data['realName']

            inuser = User.objects.filter(username=myusername)
            if inuser:
                retdata = createFalseJsonWithInfo("该用户名已被注册！")
                return JsonResponse(retdata)

            else:
                alreadyreg = Account.objects.filter(code=mystuid)
                if alreadyreg:
                    retdata = createFalseJsonWithInfo("学生学号已注册！请直接登录")
                    return JsonResponse(retdata)

                else:
                    # create the model to store in db
                    reg_user = User.objects.create_user(myusername, mystuid + "@buaa.edu.cn", mypassword)

                    """reg_user = User.objects.create(
                        username=myusername,
                        password=mypassword,
                        email=mystuid + "@buaa.edu.cn"
                    )"""

                    reg_acc = Account.objects.create(
                        user=reg_user,
                        status='a',
                        code=mystuid,
                        name=myrealname
                    )

                    Student.objects.create(
                        id=reg_acc
                    )

                    retdata = {
                        'result': True,
                        'info': "注册成功！"
                    }

                    return JsonResponse(retdata)
        else:
            retdata = createFalseJsonWithInfo("无效的json格式")
            return JsonResponse(retdata)

    else:
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)


# 获取账户用户状态
def check_status(request):
    if not request.user.is_authenticated:
        retdata = createFalseJsonWithInfo("当前用户未登录")
        return JsonResponse(retdata)
    else:
        current_user = request.user
        account = Account.objects.get(user=current_user)
        type = account.status  # 用户类型

        if (type == "a"):
            usertypestr = "学生"
        elif (type == "b"):
            usertypestr = "教师"
        elif (type == "c"):
            usertypestr = "管理员"

        retdata = {
            "result": True,
            "id": account.code,
            "userType": usertypestr,
            "userName": account.name
        }

        return JsonResponse(retdata)


# 改密码
def change_pwd(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_cpwd_form = UserChangePwdForm(data=request.POST)
    owner = request.user

    if user_cpwd_form.is_valid():
        data = user_cpwd_form.cleaned_data
        oldpwd = User.objects.filter(username=data['oldPassword'])
        validuser = authenticate(username=owner.username, password=oldpwd)

        if validuser is None:
            retdata = createFalseJsonWithInfo("原密码不正确！请重新输入")
            return JsonResponse(retdata)

        else:
            validuser.set_password(data['newPassword'])
            validuser.save()

            retdata = {
                'result': True,
                'info': "修改密码成功！"
            }
            return JsonResponse(retdata)
    else:
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)


# 改username
def change_username(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_cuname_form = UserChangeUsernameForm(data=request.POST)

    if not user_cuname_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = user_cuname_form.cleaned_data
    inname = User.objects.filter(username=data['newUserName'])

    if inname:
        retdata = createFalseJsonWithInfo("该用户名已被使用！请重新输入")
        return JsonResponse(retdata)

    else:
        owner = request.user
        owner.username = data['newUserName']
        owner.save()

        retdata = {
            'result': True,
            'info': "修改用户名成功！"
        }
        return JsonResponse(retdata)


# 改email
def change_email(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_cemail_form = UserChangeEmailForm(data=request.POST)

    if not user_cemail_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = user_cemail_form.cleaned_data
    inemail = User.objects.filter(username=data['newEmail'])

    if inemail:
        retdata = createFalseJsonWithInfo("该Email已被使用！请重新输入")
        return JsonResponse(retdata)

    else:
        owner = request.user
        owner.email = data['newEmail']
        owner.save()

        retdata = {
            'result': True,
            'info': "修改邮箱成功！"
        }
        return JsonResponse(retdata)


def get_user_info(request):
    current_user = request.user
    account = Account.objects.get(user=current_user)
    type = account.status  # 用户类型

    print(type)

    retdata = {
        'userType': type,
        'userName': current_user.username,
        'id': account.code,
    }

    if (type == "a"):
        student_obj = Student.objects.get(id=account)
        dept_obj = Department.objects.get(dept_id=student_obj.student_dept)

        if (current_user.email is None):
            myemail = account.code + "@buaa.edu.cn"
        else:
            myemail = current_user.email

        stu_data = {
            'realName': account.name,
            'grade': student_obj.student_year,
            'classNum': student_obj.student_class,
            'college': student_obj.student_dept,
            'creditGot': student_obj.student_credit,
            'creditNeed': dept_obj.dept_credit,
            'email': myemail
        }
        retdata.update(stu_data)

        return JsonResponse(retdata)

    elif (type == "b"):
        teacher_obj = Teacher.objects.get(id=account)
        dept_obj = Department.objects.get(teacher_obj.teacher_dept)

        teacher_data = {
            'realName': account.name,
            'age': teacher_obj.teacher_age,
            'phone': teacher_obj.student_class,
            'college': dept_obj.dept_name,
            'email': teacher_obj.teacher_email
        }
        retdata.update(teacher_data)

        return JsonResponse(retdata)

    elif (type == "c"):
        admin_data = {
            'email': current_user.email
        }
        retdata.update(admin_data)

        return JsonResponse(retdata)


#####  课程相关操作  #####

# 获取可选课程
def get_course_list(request):
    resultList = []

    account = Account.objects.get(user=request.user)
    student = Student.objects.get(id=account)

    # courses_list = Course.objects.filter()
    courses_list = Course.objects.all()

    for course in courses_list:
        """thisteacher = course.courseTeacher
        if thisteacher is None:
            teacherstr = "待定"
        else:
            teacherstr = thisteacher

        # selected = Score.objects.filter(course=course, student=student)
        ifselected = Score.objects.filter(course=course, student=student)
        selected = ifselected is None"""

        openc = OpenCourse.objects.get(course=course)
        if openc.teacher is None:
            teacherstr = "待定"
        else:
            teacherstr = openc.teacher.id.name

        ifselected = Score.objects.filter(opencourse=openc, student=student)
        selected = ifselected is None

        capacitystr = course.count + "/" + course.capacity

        data = {
            "courseId": course.code,
            "courseName": course.name,
            "courseCategory": course.type,
            "courseCollege": str(course.dept),
            "courseTeacher": teacherstr,
            "time": str(course.time),
            "credit": course.credit,
            "capacity": capacitystr,
            "selected": selected
        }
        # for x in data.values():
        # print(x)
        resultList.append(data)

    retdata = {
        'resultList': resultList
    }
    return JsonResponse(retdata)


# select课程
def select_course(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_selectc_form = CourseIdForm(data=request.POST)

    if not user_selectc_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = user_selectc_form.cleaned_data
    courseId = data['courseId']

    course = Course.objects.filter(code=courseId)
    if not course:
        retdata = createFalseJsonWithInfo("该课程不存在！请重新检查")
        return JsonResponse(retdata)

    openc = OpenCourse.objects.get(course=course)
    account = Account.objects.get(user=request.user)
    student = Student.objects.get(id=account)

    Score.objects.create(opencourse=openc, student=student)
    course.count += 1

    retdata = {
        'result': True,
        'info': "选课成功！"
    }
    return JsonResponse(retdata)


# 获取已选课程
def get_course_selected(request):
    account = Account.objects.get(user=request.user)
    student = Student.objects.get(id=account)

    selected_courses_list = Score.objects.filter(student=student)
    resultList = []

    for select_course in selected_courses_list:
        openc = OpenCourse.objects.get(course=select_course)
        if openc.teacher is None:
            teacherstr = "待定"
        else:
            teacherstr = openc.teacher.id.name

        capacitystr = select_course.count + "/" + select_course.capacity

        data = {
            "courseId": select_course.code,
            "courseName": select_course.name,
            "courseCategory": select_course.type,
            "courseCollege": str(select_course.dept),
            "courseTeacher": teacherstr,
            "time": str(select_course.time),
            "credit": select_course.credit,
            "capacity": capacitystr,
        }
        for x in data.values():
            print(x)
        resultList.append(data)

    retdata = {
        'resultList': resultList
    }
    return JsonResponse(retdata)


# 退选课程
def unselect_course(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_courseid_form = CourseIdForm(data=request.POST)

    if not user_courseid_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = user_courseid_form.cleaned_data
    courseId = data['courseId']

    course = Course.objects.filter(code=courseId)
    if not course:
        retdata = createFalseJsonWithInfo("该课程不存在！请重新检查")
        return JsonResponse(retdata)

    openc = OpenCourse.objects.get(course=course)
    account = Account.objects.get(user=request.user)
    student = Student.objects.get(id=account)

    sc = Score.objects.get(opencourse=openc, student=student)

    if not sc:
        retdata = createFalseJsonWithInfo("您已退选该课程！请勿重复退选")
        return JsonResponse(retdata)

    sc.delete()
    course.count -= 1

    retdata = {
        'result': True,
        'info': "退课成功！"
    }
    return JsonResponse(retdata)


#####  事务相关操作  #####

# 学生事务申请
def exemption_apply(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    exemption_form = UserExemptionForm(data=request.POST)

    if not exemption_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = exemption_form.cleaned_data
    # applyType = data['applyType']  #免听or免修or缓考or补考
    courseName = data['courseName']
    courseCollege = data['courseCollege']
    teacher = data['teacher']
    courseId = data['courseId']
    # applyReason = data['applyReason']

    retdata = {}
    return JsonResponse(retdata)


##### 辅助用函数 #####

def createFalseJsonWithIdAndInfo(str):
    retdata = {
        'result': False,
        'id': '',
        'info': str
    }
    return retdata


def createFalseJsonWithInfo(str):
    retdata = {
        'result': False,
        'info': str
    }
    return retdata


def checkUserTypeIsFit(status, typestr):
    print(status, typestr)

    if (status == 'a'):
        return typestr == '学生'
    elif (status == 'b'):
        return typestr == '教师'
    elif (status == 'c'):
        return typestr == '管理员'
    else:
        # print("Unknown Type!")
        return False
