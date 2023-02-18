from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        # 获取POST请求中提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 调用Django的authenticate函数进行身份验证
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 如果身份验证成功，则调用Django的login函数将用户登录
            login(request, user)
            return redirect('home')
        else:
            # 如果身份验证失败，则返回登录表单和错误消息
            error_message = '用户名或密码不正确'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # 如果是GET请求，则返回登录表单
        return render(request, 'login.html')