from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from .models import Student, Class, Teacher, Admin, Department, Course, Account


# Create your views here.

@csrf_exempt
def query_student(request):
    return HttpResponse("Stu-查询成功！")


def query_teacher(request):
    return HttpResponse("Tea-查询成功！")


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
            'email':current_user.email
        }
        retdata.update(admin_data)

        return JsonResponse(retdata)
