from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from .forms import UserLoginForm, UserRegisterForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User


# Create your views here.

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
                retdata = {
                    'result': False,
                    'id': "",
                    'info': "账号或密码输入有误。请重新输入~"
                }
                return JsonResponse(retdata)

        else:
            retdata = {
                'result': False,
                'id': "",
                'info': "json格式不合法"
            }
            return JsonResponse(retdata)

    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        # return render(request, 'userprofile/login.html', context)
        return HttpResponse("当前用户已登录")

    else:
        retdata = {
            'result': False,
            'id': "",
            'info': "请使用GET或POST请求数据"
        }
        return JsonResponse(retdata)


# 用户退出,实际vue负责管理
def user_logout(request):
    logout(request)
    return redirect("article:article_list")


# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():

            data = user_register_form.cleaned_data

            # create the model to store in db
            User.objects.create(
                username=data['userName'],
                password=data['password']
            )

            retdata = {
                'result': True,
                'info': "注册成功！"
            }

            return JsonResponse(retdata)
        else:
            retdata = {
                'result': False,
                'info': "无效的用户名"
            }
            return JsonResponse(retdata)

    elif request.method == 'GET':
        retdata = {
            'result': False,
            'info': "请求方式有误！请使用POST请求数据"
        }
        return JsonResponse(retdata)

        """user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)"""
    else:
        retdata = {
            'result': True,
            'info': "请使用GET或POST请求数据"
        }
        return JsonResponse(retdata)
