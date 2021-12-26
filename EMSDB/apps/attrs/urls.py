from django.urls import path
from . import views

app_name = 'attrs'

urlpatterns = [
    # 学生查询
    path('student/', views.query_student, name='student'),

    # 教师查询
    path('teacher/', views.query_teacher, name='teacher'),
]
