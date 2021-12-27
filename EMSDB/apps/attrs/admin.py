from django.contrib import admin
from .models import Student, Class, Teacher, Admin, Department, Course, Account

# Register your models here.

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Account)
