from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm, UserChangePwdForm
from .models import Student, Class, Teacher, Admin, Department, Course, Account


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

            print("get username = " + data['userName'])
            print("get password = " + data['password'])
            user = authenticate(username=data['userName'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                retdata = {
                    'result': True,
                    'id': data['userName'],
                    'info': "登录成功！"
                }
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

            inuser = User.objects.filter(username=data['userName'])
            if inuser:
                retdata = createFalseJsonWithInfo("该用户名已被注册！")
                return JsonResponse(retdata)

            else:
                alreadyreg = Account.objects.filter(code=data['studentId'])
                if alreadyreg:
                    retdata = createFalseJsonWithInfo("学生学号已注册！请直接登录")
                    return JsonResponse(retdata)

                else:
                    # create the model to store in db
                    # reg_user = User.objects.create_user(data['userName'],  data['password'])
                    reg_user = User.objects.create(
                        username=data['userName'],
                        password=data['password']
                    )

                    reg_acc = Account.objects.create(
                        user=reg_user,
                        status='a',
                        code=data['studentId'],
                        name=data['realName']
                    )

                    reg_stu = Student.objects.create(
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
    cur_user = request.user

    if user_cpwd_form.is_valid():
        data = user_cpwd_form.cleaned_data
        oldpwd = User.objects.filter(username=data['oldPassword'])
        validuser = authenticate(username=cur_user.username, password=oldpwd)

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


def student_home(request):
    """student_obj = Students.objects.get(admin=request.user.id)

    course_obj = Courses.objects.get(id=student_obj.course_id.id)
    total_subjects = Subjects.objects.filter(course_id=course_obj).count()

    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subjects.objects.filter(course_id=student_obj.course_id)
    for subject in subject_data:
        attendance = Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=True,
                                                                   student_id=student_obj.id).count()
        attendance_absent_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=False,
                                                                  student_id=student_obj.id).count()
        subject_name.append(subject.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

    context = {
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "total_subjects": total_subjects,
        "subject_name": subject_name,
        "data_present": data_present,
        "data_absent": data_absent
    }
    return render(request, "student_template/student_home_template.html", context)"""


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

        stu_data = {
            'realName': account.name,
            'grade': student_obj.student_year,
            'classNum': student_obj.student_class,
            'college': student_obj.student_dept,
            'creditGot': student_obj.student_credit,
            'creditNeed': dept_obj.dept_credit,
            'email': account.code + "@buaa.edu.cn"
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
