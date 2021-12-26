from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@csrf_exempt
def query_student(request):
    return HttpResponse("Stu-查询成功！")

def query_teacher(request):
    return HttpResponse("Tea-查询成功！")