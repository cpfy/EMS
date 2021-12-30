from django.urls import path
from . import views

app_name = 'attrs'

urlpatterns = [
    # 用户登录,退出,注册
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    # 登录状态
    path('status/', views.check_status, name='status'),

    # 个人信息查询,改密码,信息
    path('my/info/', views.get_user_info, name='info'),
    path('my/passwordChange/', views.change_pwd, name='passwordChange'),
    path('my/changeUsername/', views.change_username, name='changeUsername'),
    path('my/changeEmail/', views.change_email, name='changeEmail'),

    # 管理员消息
    path('notice_Send/', views.send_notice, name='notice_Send'),

    # 课程相关
    path('course/getCourse/', views.get_course_list, name='course_list'),
    path('course/selectCourse/', views.select_course, name='select_course'),
    path('course/getCourseSelected/', views.get_course_selected, name='getCourseSelected'),
    path('course/unselectCourse/', views.unselect_course, name='unselect_course'),

    # 事务
    path('task/exemptionApply/', views.exemption_apply, name='exemptionApply'),

    # 信息查询
    path('info/Student_Schedule/', views.get_stu_schedule, name='Student_Schedule'),
    path('info/Student_ScheduleRecommend/', views.get_stu_schedule_recommend, name='Student_ScheduleRecommend'),
    path('info/Teacher_Schedule/', views.get_teacher_schedule, name='Teacher_Schedule'),
    path('info/getExamSchedule/', views.get_stu_exam, name='getExamSchedule'),
    path('info/getEmptyRoom/', views.get_empty_room, name='getEmptyRoom'),

    # 教学评价
    path('eva/getEvaInfo/', views.get_evaluate_list, name='getEvaInfo'),
    path('eva/evaluateCourse/', views.evaluate_course, name='evaluateCourse'),

    # 教师课程管理
    path('t/getCourse/', views.get_course, name='getCourse'),
    path('t/getStudentInfo/', views.get_course_stuinfo, name='getStudentInfo'),
    path('t/getCourseOfScore/', views.get_course_of_score, name='getCourseOfScore'),
    path('t/importGrade/', views.import_grade_file, name='importGrade'),

]
