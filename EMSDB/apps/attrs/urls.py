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

    # 个人信息查询
    path('info/', views.get_user_info, name='info'),

    # 改密码,信息
    path('passwordChange/', views.change_pwd, name='passwordChange'),
    path('changeUsername/', views.change_username, name='changeUsername'),
    path('changeEmail/', views.change_email, name='changeEmail'),

    # 课程相关
    path('course/getCourse', views.get_course_list, name='course_list'),
    path('course/selectCourse', views.select_course, name='select_course'),
    path('course/getCourseSelected', views.get_course_selected, name='getCourseSelected'),
    path('course/unselectCourse', views.unselect_course, name='unselect_course'),

    # 事务
    path('task/exemptionApply/', views.exemption_apply, name='exemptionApply'),

]
