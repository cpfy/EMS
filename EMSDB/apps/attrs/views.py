from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse

from django.db import models

from .forms import *
from .models import Student, Class, Teacher, Admin, Department, Course, Account, CourseTime, Score, OpenCourse, Score, \
    Place, Exam

import random
import string

from django.conf import settings


# Create your views here.

# 登录相关 #

def user_login(request):
    # print(request.POST)

    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_login_form = UserLoginForm(data=request.POST)

    if not user_login_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    # .cleaned_data 清洗出合法数据
    data = user_login_form.cleaned_data
    # 检验账号、密码是否正确匹配数据库中的某个用户

    myusername = data['userName']
    mypassword = data['password']
    myusertype = data['userType']

    print("get username = " + myusername)
    print("get password = " + mypassword)
    # print("userType = " + data['userType'])

    user = authenticate(username=myusername, password=mypassword)

    if not user:
        retdata = createFalseJsonWithIdAndInfo("账号或密码输入有误。请重新输入~")
        return JsonResponse(retdata)

    account = Account.objects.get(user=user)
    if (checkUserTypeIsFit(account.status, myusertype)):
        # 将用户数据保存在 session 中，即实现了登录动作
        login(request, user)

        # request.session['username'] = user.username
        # request.session.modified = True

        settings.FAKEUSERID = user.id

        print(settings.FAKEUSERID)

        print("登录成功！当前用户：", request.user.username)

        # session_id = request.session.session_key
        # print("s id: ", session_id)

        retdata = {
            'result': True,
            'id': myusername,
            'info': "登录成功！",
            # 'session_id': session_id,
        }

        return JsonResponse(retdata)

    else:
        retdata = createFalseJsonWithIdAndInfo("账号类型有误。请重新选择~")
        return JsonResponse(retdata)


# 用户退出,实际vue负责管理
def user_logout(request):
    logout(request)
    return JsonResponse({})


# 用户注册
def user_register(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    user_register_form = UserRegisterForm(data=request.POST)
    if not user_register_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = user_register_form.cleaned_data
    myusername = data['userName']
    mypassword = data['password']
    mystuid = data['studentId']
    myrealname = data['realName']

    inuser = User.objects.filter(username=myusername)
    if inuser:
        retdata = createFalseJsonWithInfo("该用户名已被注册！")
        return JsonResponse(retdata)

    alreadyreg = Account.objects.filter(code=mystuid)
    if alreadyreg:
        retdata = createFalseJsonWithInfo("学生学号已注册！请直接登录")
        return JsonResponse(retdata)

    # create the model to store in db
    reg_user = User.objects.create_user(
        myusername,
        mystuid + "@buaa.edu.cn",
        mypassword
    )

    newacc = Account.objects.create(
        user=reg_user,
        status='a',
        code=mystuid,
        name=myrealname
    )

    Student.objects.create(
        id=newacc,
        dept=Department.objects.order_by('?').first(),
        student_class=Class.objects.order_by('?').first(),
        # inyear=,
        # age=,
        home=getRandomProvince(),
        # credit
    )

    retdata = {
        'result': True,
        'info': "注册成功！"
    }
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
# @login_required
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
# @login_required
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
# @login_required
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


# 获取个人info
# @login_required
def get_user_info(request):
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)

    type = account.status  # 用户类型

    print("type = ", type)

    retdata = {
        'userType': getUserTypeStr(type),
        'userName': user.username,
        'id': account.code,
    }

    if (type == "a"):
        curStudent = Student.objects.get(id=account)

        if not user.email:
            myemail = account.code + "@buaa.edu.cn"
        else:
            myemail = user.email

        stu_data = {
            'realName': account.name,
            'grade': curStudent.inyear,
            'classNum': curStudent.student_class.id,
            'college': curStudent.dept.name,
            'creditGot': curStudent.credit,
            'creditNeed': curStudent.dept.fullcredit,
            'email': myemail
        }
        retdata.update(stu_data)

        return JsonResponse(retdata)

    elif (type == "b"):
        curTeacher = Teacher.objects.get(id=account)
        # dept_obj = curTeacher.dept

        if not user.email:
            myemail = account.code + "@buaa.edu.cn"
        else:
            myemail = user.email

        teacher_data = {
            'realName': account.name,
            'age': curTeacher.age,
            'phone': curTeacher.telephone,
            'college': curTeacher.dept.name,
            'email': myemail
        }
        retdata.update(teacher_data)

        return JsonResponse(retdata)

    elif (type == "c"):
        if not user.email:
            myemail = account.code + "@buaa.edu.cn"
        else:
            myemail = user.email

        admin_data = {
            'email': myemail
        }
        retdata.update(admin_data)

        return JsonResponse(retdata)


#####  课程相关操作  #####

# 获取可选课程
# #@login_required
def get_course_list(request):
    """user_id = settings.FAKEUSERID
    print("userid=", user_id)"""

    print(request.POST)
    print(request)

    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    course_filter_form = FilterCourseForm(data=request.POST)

    if not course_filter_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = course_filter_form.cleaned_data
    filter = data['filter']

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)

    # courses_list = Course.objects.filter()
    courses_list = Course.objects.all()

    resultList = []
    allchoose = Score.objects.filter(student=student)

    for course in courses_list:
        """thisteacher = course.courseTeacher
        if thisteacher is None:
            teacherstr = "待定"
        else:
            teacherstr = thisteacher

        # selected = Score.objects.filter(course=course, student=student)
        ifselected = Score.objects.filter(course=course, student=student)
        selected = ifselected is None"""

        if (filter):
            mayConflict = allchoose.filter(opencourse__course__time=course.time)
            if mayConflict:
                print("当前课程冲突：", str(course))
                continue

        openc = OpenCourse.objects.get(course=course)
        if openc.teacher is None:
            teacherstr = "待定"
        else:
            teacherstr = openc.teacher.id.name

        chooseThis = Score.objects.filter(opencourse=openc, student=student)
        # print("openc = ",openc.__str__(), "; stu = ",student.__str__())

        if chooseThis:
            selected = True
        else:
            selected = False
        # print("if selected = ",)

        capacitystr = str(course.capacity - course.count) + "/" + str(course.capacity)

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
        for x in data.values():
            print(x)
        resultList.append(data)

    retdata = {
        'resultList': resultList
    }
    return JsonResponse(retdata)


# select课程
# @login_required
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

    course = Course.objects.get(code=courseId)
    if not course:
        retdata = createFalseJsonWithInfo("该课程不存在！请重新检查")
        return JsonResponse(retdata)

    openc = OpenCourse.objects.get(course=course)
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)

    Score.objects.create(opencourse=openc, student=student)
    course.count += 1

    retdata = {
        'result': True,
        'info': "选课成功！"
    }
    return JsonResponse(retdata)


# 获取已选课程
# @login_required
def get_course_selected(request):
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)

    selected_courses_list = Score.objects.filter(student=student)
    resultList = []

    for sc in selected_courses_list:
        # openc = OpenCourse.objects.get(course=select_course)
        openc = sc.opencourse
        c = openc.course

        if openc.teacher is None:
            teacherstr = "待定"
        else:
            teacherstr = openc.teacher.id.name

        capacitystr = str(c.capacity - c.count) + "/" + str(c.capacity)

        data = {
            "courseId": c.code,
            "courseName": c.name,
            "courseCategory": c.type,
            "courseCollege": str(c.dept),
            "courseTeacher": teacherstr,
            "time": str(c.time),
            "credit": c.credit,
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
# @login_required
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

    course = Course.objects.get(code=courseId)
    if not course:
        retdata = createFalseJsonWithInfo("该课程不存在！请重新检查")
        return JsonResponse(retdata)

    openc = OpenCourse.objects.get(course=course)
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
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


#####  信息查询相关操作  #####
# 课表
# @login_required
def get_stu_schedule(request):
    if (request.method != "GET"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用GET请求数据")
        return JsonResponse(retdata)

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)
    mycourseSC = Score.objects.filter(student=student)
    # mycourse = OpenCourse.objects.filter(mycourseSC.opencourse)

    # print(mycourse)

    schedule = []

    for i in range(16):
        weekschedule = []
        week = i + 1

        # 本周课程
        weekcourse = mycourseSC.filter(opencourse__course__time__startweek__lte=week).filter(
            opencourse__course__time__startweek__gte=week - models.F('opencourse__course__time__duringweek'))

        for j in range(6):
            # 1,2节
            timestr = str(2 * j + 1) + "," + str(2 * j + 2) + "节"

            # 示例：编译技术 锌小子 (一)215
            onesect = {
                'time': timestr,
                'Monday': '',
                'Tuesday': '',
                'Wednesday': '',
                'Thursday': '',
                'Friday': '',
                'Saturday': '',
                'Sunday': ''
            }

            sectweekcourse = weekcourse.filter(opencourse__course__time__startsection__lte=2 * j).filter(
                opencourse__course__time__startsection__gte=2 * j + 1 - models.F(
                    'opencourse__course__time__duringsection'))

            if sectweekcourse:
                for c in sectweekcourse:
                    if not c.opencourse.course.place:
                        placestr = "待定"
                    else:
                        placestr = str(c.opencourse.course.place)

                    course_str = str(c.opencourse.course.name) + " " \
                                 + str(c.opencourse.teacher.id.name) + " " + placestr

                    weekstr = convertWeeknumToEng(int(c.opencourse.course.time.weekday))
                    onesect[weekstr] = course_str
                    print("Set weekstr: ", course_str)

                    weekschedule.append(onesect)

        schedule.append(weekschedule)

    retdata = {
        'schedule': schedule,
    }
    return JsonResponse(retdata)


# 推荐课表
# @login_required
def get_stu_schedule_recommend(request):
    if (request.method != "GET"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用GET请求数据")
        return JsonResponse(retdata)

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)
    mycourseSC = Score.objects.filter(student=student)
    mycourse = mycourseSC.opencourse

    print(mycourse)

    schedule = []

    for i in range(16):
        weekschedule = []
        week = i + 1

        # 本周课程
        weekcourse = mycourse.filter(course__time__startweek__lte=week).filter(
            course__time__startweek__gte=week - models.F('course__time__duringweek'))

        for j in range(6):
            # 1,2节
            timestr = str(2 * j + 1) + "," + str(2 * j + 2) + "节"

            # 示例：编译技术 锌小子 (一)215
            onesect = {
                'time': timestr,
                'Monday': '',
                'Tuesday': '',
                'Wednesday': '',
                'Thursday': '',
                'Friday': '',
                'Saturday': '',
                'Sunday': ''
            }

            sectweekcourse = weekcourse.filter(course__time__startsection__lte=2 * j).filter(
                course__time__startsection__gte=2 * j + 1 - models.F('course__time__duringsection'))

            if sectweekcourse:
                for c in sectweekcourse:
                    course_str = str(c.course.name) + " " \
                                 + str(c.teacher.id.name) + " " \
                                 + str(c.course.place)

                    weekstr = convertWeeknumToEng(int(c.course.time.week))
                    onesect[weekstr] = course_str
                    print("Set weekstr: ", course_str)

                    weekschedule.append(onesect)

        schedule.append(weekschedule)

    retdata = {
        'schedule': schedule,
    }
    return JsonResponse(retdata)
    return JsonResponse(retdata)


# 教师课表
# @login_required
def get_teacher_schedule(request):
    if (request.method != "GET"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用GET请求数据")
        return JsonResponse(retdata)

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    teacher = Teacher.objects.get(id=account)
    mycourseOP = OpenCourse.objects.filter(teacher=teacher)

    print(mycourseOP)

    schedule = []

    for i in range(16):
        weekschedule = []
        week = i + 1

        # 本周课程
        weekcourse = mycourseOP.filter(course__time__startweek__lte=week).filter(
            course__time__startweek__gte=week - models.F('course__time__duringweek'))

        for j in range(6):
            # 1,2节
            timestr = str(2 * j + 1) + "," + str(2 * j + 2) + "节"

            # 示例：编译技术 锌小子 (一)215
            onesect = {
                'time': timestr,
                'Monday': '',
                'Tuesday': '',
                'Wednesday': '',
                'Thursday': '',
                'Friday': '',
                'Saturday': '',
                'Sunday': ''
            }

            sectweekcourse = weekcourse.filter(course__time__startsection__lte=2 * j).filter(
                course__time__startsection__gte=2 * j + 1 - models.F('course__time__duringsection'))

            if sectweekcourse:
                for c in sectweekcourse:
                    course_str = str(c.course.name) + " " \
                                 + str(c.teacher.id.name) + " " \
                                 + str(c.course.place)

                    weekstr = convertWeeknumToEng(int(c.course.time.week))
                    onesect[weekstr] = course_str
                    print("Set weekstr: ", course_str)

                    weekschedule.append(onesect)

        schedule.append(weekschedule)

    retdata = {
        'schedule': schedule,
    }
    return JsonResponse(retdata)


# 空教室
# @login_required
def get_empty_room(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    date_form = DateForm(data=request.POST)

    if not date_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    # 与数据库中匹配的星期
    data = date_form.cleaned_data
    search_date = data['date']
    weeknum = search_date.weekday() + 1

    roomInfo = []

    spare = ['空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲', '空闲']
    places = Place.objects.all()
    for place in places:
        conflict = Course.objects.filter(time__weekday=weeknum, place=place)
        # 有冲突
        if conflict:
            for conf in conflict:
                start = conf.time.startsection
                during = conf.time.duringsection
                for i in range(start - 1, start + during - 1):
                    spare[i] = "占用"

        roomitem = {
            "room": str(place),
            "c": spare
        }
        roomInfo.append(roomitem)

    retdata = {
        'roomInfo': roomInfo,
    }
    return JsonResponse(retdata)


# 考表
# @login_required
def get_stu_exam(request):
    if (request.method != "GET"):
        retdata = createVoidListWithInfo("请求方式有误！请使用GET请求数据")
        return JsonResponse(retdata)

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)
    mycourseSC = Score.objects.filter(student=student)
    mycourse = mycourseSC.opencourse.course
    myexam = Exam.objects.filter(course=mycourse)

    resultList = []

    if myexam:
        for item in myexam:
            if item.course.teacher is None:
                teacherstr = "待定"
            else:
                teacherstr = item.course.teacher.id.name

            # capacitystr = str(item.course.capacity - item.course.count) + "/" + str(item.course.capacity)

            data = {
                "courseId": item.course.code,
                "courseName": item.course.name,
                "courseCategory": item.course.type,
                "courseCollege": str(item.course.dept),
                "courseTeacher": teacherstr,
                "time": str(item.time),
                "location": str(item.place),
            }
            resultList.append(data)

    retdata = {
        'resultList': resultList,
    }

    return JsonResponse(retdata)


#####  事务相关操作  #####

# 学生事务申请
# @login_required
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


##### 教学评价 #####
# 进入页面需要信息
# @login_required
def get_evaluate_list(request):
    if (request.method != "GET"):
        retdata = createVoidListWithInfo("请求方式有误！请使用GET请求数据")
        return JsonResponse(retdata)

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    student = Student.objects.get(id=account)
    courseSC = Score.objects.filter(student=student)

    resultList = []

    if courseSC:
        for item in courseSC:
            if item.course.teacher is None:
                teacherstr = "待定"
            else:
                teacherstr = item.opencourse.course.teacher.id.name

            data = {
                "courseId": item.opencourse.course.code,
                "courseName": item.opencourse.course.name,
                "courseCategory": item.opencourse.course.type,
                "mark": item.mark,
                "credit": item.opencourse.course.credit,
                "courseTeacher": teacherstr,
                "evaluated": item.eval,
            }
            resultList.append(data)

    retdata = {
        'resultList': resultList,
    }
    return JsonResponse(retdata)


# 进行评价时信息交流
# @login_required
def evaluate_course(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    course_eval_form = EvaluateCourseForm(data=request.POST)

    if course_eval_form.is_valid():
        data = course_eval_form.cleaned_data
        cid = data['courseId']
        mark = data['mark']

        user = User.objects.get(pk=settings.FAKEUSERID)
        account = Account.objects.get(user=user)
        student = Student.objects.get(id=account)
        mysc = Score.objects.get(student=student, course__code=cid)

        if not mysc:
            retdata = createFalseJsonWithInfo("请核对学生与课程信息后重新尝试！")
            return JsonResponse(retdata)

        mysc.mark = mark
        retdata = {
            'result': True,
            'info': '评价成功！'
        }
        return JsonResponse(retdata)

    else:
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)


##### 教师操作 #####
# 得到对应教师所开课程信息
# @login_required
def get_course(request):
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    teacher = Teacher.objects.get(id=account)
    mycourseOP = OpenCourse.objects.filter(teacher=teacher)

    courseInfo = []

    if mycourseOP:
        for openc in mycourseOP:
            data = {
                "courseId": openc.course.code,
                "courseName": openc.course.name,
            }
            # for x in data.values():
            # print(x)
            courseInfo.append(data)

    retdata = {
        'courseInfo': courseInfo,
    }
    return JsonResponse(retdata)


# 查看某课程学生信息
# @login_required
def get_course_stuinfo(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    courseid_form = CourseIdForm(data=request.POST)

    if not courseid_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = courseid_form.cleaned_data
    cid = data['courseId']
    mySC = Score.objects.filter(opencourse__course__code=cid)

    if not mySC:
        retdata = createFalseJsonWithInfo("该课程当前无学生选课")
        return JsonResponse(retdata)

    studentInfo = []

    for sc in mySC:
        if sc.grade == 0:
            gradestr = "待录入"
        else:
            gradestr = sc.grade

        data = {
            'studentId': sc.student.id.code,
            'studentName': sc.student.id.name,
            'class': str(sc.student.student_class.id),
            'grade': gradestr,
            'college': str(sc.student.dept),
            'email': sc.student.id.user.email,
        }
        studentInfo.append(data)

    retdata = {
        "studentInfo": studentInfo,
    }
    return JsonResponse(retdata)


# 获取成绩
# @login_required
def get_course_of_score(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    courseid_form = CourseIdForm(data=request.POST)

    if not courseid_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = courseid_form.cleaned_data
    cid = data['courseId']
    myOP = OpenCourse.objects.filter(course__code=cid)

    scoreInfos = []

    for opc in myOP:
        data = {
            'courseId': opc.course.code,
            'courseName': opc.course,
            'recorded': opc.recorded,
        }
        scoreInfos.append(data)

    retdata = {
        "scoreInfos": scoreInfos,
    }
    return JsonResponse(retdata)


# 导入成绩
# @login_required
def import_grade_file(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    courseid_form = CourseIdForm(data=request.POST)

    if not courseid_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = courseid_form.cleaned_data
    # cid = data['courseId']
    # mySC = Score.objects, filter(opencourse__course__code=cid)

    retdata = {
        'result': True,
        'info': "成绩导入成功！"
    }
    return JsonResponse(retdata)


# 得到对应教师所开课程detail信息
# @login_required
def get_course_detail(request):
    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    teacher = Teacher.objects.get(id=account)
    mycourseOP = OpenCourse.objects.filter(teacher=teacher)

    resultList = []

    if mycourseOP:
        for openc in mycourseOP:
            data = {
                'id': openc.course.code,
                'name': openc.course.name,
                'capacity': openc.course.capacity,
                'college': str(openc.course.dept),
                'credit': openc.course.credit,
                'category': openc.course.type,
            }
            # for x in data.values():
            # print(x)
            resultList.append(data)

    retdata = {
        'resultList': resultList,
    }

    return JsonResponse(retdata)


# 修改课程信息
# @login_required
def change_course_info(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    create_course_form = ChangeCourseForm(data=request.POST)

    if not create_course_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = create_course_form.cleaned_data
    cid = data['id']
    name = data['name']
    college = data['college']
    capacity = data['capacity']
    category = data[' category']
    credit = data['credit']

    destc = Course.objects.get(courseId=cid)

    if not destc:
        retdata = createFalseJsonWithInfo("该课程不存在")
        return JsonResponse(retdata)

    destdept = Department.objects.get(name=college)

    if not destdept:
        retdata = createFalseJsonWithInfo("学院不存在")
        return JsonResponse(retdata)

    destc.name = name
    destc.dept = destdept
    destc.capacity = capacity
    destc.type = getCategoryType(category)
    destc.credit = credit
    destc.save()

    retdata = {
        'result': True,
        'info': "课程信息修改成功！"
    }
    return JsonResponse(retdata)


# 添加课程信息
# @login_required
def add_course(request):
    if (request.method != "POST"):
        retdata = createFalseJsonWithInfo("请求方式有误！请使用POST请求数据")
        return JsonResponse(retdata)

    create_course_form = ChangeCourseForm(data=request.POST)

    if not create_course_form.is_valid():
        retdata = createFalseJsonWithInfo("json格式有误")
        return JsonResponse(retdata)

    data = create_course_form.cleaned_data
    name = data['name']
    college = data['college']
    capacity = data['capacity']
    category = data['category']
    credit = data['credit']

    # 随机：MyModel.objects.order_by('?').first()

    destdept = Department.objects.get(name=college)

    if not destdept:
        retdata = createFalseJsonWithInfo("学院不存在")
        return JsonResponse(retdata)

    # Random+不重复 课程号
    randomcodestr = generateRandCourseCode()
    while (Course.objects.filter(courseId=randomcodestr)):
        randomcodestr = generateRandCourseCode()

    newc = Course.objects.create(
        code=randomcodestr,
        name=name,
        # pred =
        type=getCategoryType(category),
        credit=credit,
        time=CourseTime.objects.order_by('?').first(),
        place=Place.objects.order_by('?').first(),
        # semi =
        dept=destdept,
        capacity=capacity,
        # count = 0,
    )

    user = User.objects.get(pk=settings.FAKEUSERID)
    account = Account.objects.get(user=user)
    teacher = Teacher.objects.get(id=account)
    OpenCourse.objects.create(
        course=newc,
        teacher=teacher
    )

    retdata = {
        'result': True,
        'info': '添加课程成功',
        'id': randomcodestr,
    }
    return JsonResponse(retdata)


##### 通知类 #####

def send_notice(request):
    retdata = {
        'result': True,
        'info': "消息发送成功！"
    }
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


def convertWeeknumToEng(num):
    dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }
    return dict.get(num)


def createVoidListWithInfo(str):
    print("请求方式错误！请使用GET")
    retdata = {
        'resultList': [],
        'info': str
    }
    return retdata


# 生成随机课程码
def generateRandCourseCode():
    # printing lowercase
    letters = string.ascii_lowercase
    digits = string.digits
    str1 = ''.join(random.choice(letters) for i in range(1))
    str2 = str1.join(random.choice(digits) for i in range(2))
    return str2


# category对应码
def getCategoryType(str):
    dict = {
        '必修': 'a',
        '选修': 'b',
        '限修': 'c',
        '任修': 'd',
    }
    return dict.get(str)


# 随机省份（学生create时）
def getRandomProvince():
    province = [
        '司隶',
        '徐州',
        '青州',
        '豫州',
        '冀州',
        '并州',
        '幽州',
        '兖州',
        '凉州',
        '益州',
        '荆州',
        '扬州',
        '交州',
    ]
    return random.choice(province)


# usertype
def getUserTypeStr(str):
    if (str == 'a'):
        return "学生"
    elif (str == 'b'):
        return "教师"
    elif (str == 'c'):
        return "管理员"
