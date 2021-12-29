from django.contrib import admin
from .models import Student, Class, Teacher, Admin, Department, Course, Account, CourseTime, Score, OpenCourse, Place

# Register your models here.

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Account)
admin.site.register(CourseTime)
admin.site.register(Score)
admin.site.register(OpenCourse)
admin.site.register(Place)
