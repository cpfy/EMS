from django.urls import path
from . import views

app_name = 'attrs'

urlpatterns = [
    # 个人信息查询
    path('info/', views.get_user_info, name='userinfo'),

]
