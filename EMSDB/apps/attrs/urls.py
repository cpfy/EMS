from django.urls import path
from . import views

app_name = 'attrs'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),

    # 用户退出
    path('logout/', views.user_logout, name='logout'),

    # 用户注册
    path('register/', views.user_register, name='register'),

    # 个人信息查询
    path('info/', views.get_user_info, name='info'),

]
