from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .myForm import RegisterForm, LoginForm
from django.core.mail import send_mail  # 发送邮件
from itsdangerous import TimedJSONWebSignatureSerializer  # 生成token
from itsdangerous import SignatureExpired  # token超时发生的异常
from django.contrib.auth import authenticate, logout, login
from django.conf import settings  # 从settings.py里导入
import time


class RegisterView(View):
    '''用户注册'''
    def get(self, request):
        # 已登录的用户不能访问注册页码跟登录页面
        if request.user.is_authenticated:
            return redirect(reverse('blog_app:index'))
        return render(request, 'user_app/register.html')

    def post(self, request):
        # 验证表单
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 获取数据
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            try:
                # 注册，标为未激活状态,create_user会把密码加密
                user = User.objects.create_user(username=username, password=password, email=email)
                user.is_active = 0  # 改为未激活激的用户
                user.save()
            except:
                return render(request, 'user_app/register.html', {'msg': '用户名已存在'})

            # 发送激活邮件
            if user:
                # 生成加密token                                            超时时间（秒）
                serializer = TimedJSONWebSignatureSerializer('SECRET_KEY', 86400)  # 一天
                info = {'id': user.id}  # 要加密的字典
                token = serializer.dumps(info)  # 加密，生成token
                token = token.decode('utf-8')  # 生成的token默认是byte类型，需要解码

                # 邮件模板                                                                                                                                  域名或主机名
                html = '<h1>%s,欢迎注册</h1> 点击下面链接激活账号(24小时后过期)<br> <a href="%s/user/active/?token=%s">%s/user/active/?token=%s</a>' % (username, settings.HOST_URL, token, settings.HOST_URL, token)

                # 发送邮件
                send_mail('BYC账号激活', '', '1251779123@qq.com', [email], html_message=html)
            return redirect(reverse('user_app:login'))
        else:
            # 表单验证失败，返回错误信息
            return render(request, 'user_app/register.html', {'form': form})


def active(request):
    '''激活账号'''
    try:
        serializer = TimedJSONWebSignatureSerializer('SECRET_KEY', 86400)
        token = request.GET.get('token')
        info = serializer.loads(token)  # 解密，加密的时候是字典，解密的时候还是字典
        uid = info.get('id')
    except SignatureExpired as e:  # token过期的错误SignatureExpired
        user = User.objects.get(pk=uid)  # 删除账号，让用户重新注册
        user.delete()
        return HttpResponse('激活链接过期，请重新注册')
    try:
        user = User.objects.get(pk=uid)  # 在数据库里查找用户，找不到则表示用户不存在
    except:
        return HttpResponse('用户不存在，请重新注册')

    # 将用户标记为激活
    user.is_active = 1
    user.save()
    print(serializer.loads(token))

    # return render(request, 'user_app/active.html')
    return redirect(reverse('blog_app:index'))


class LoginView(View):
    '''用户登录'''
    def get(self, request):
        # 已登录的用户不能访问注册页码跟登录页面
        if request.user.is_authenticated:
            return redirect(reverse('blog_app:index'))
        return render(request, 'user_app/login.html')

    def post(self, request):

        # 验证表单
        form = LoginForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            username = data.get('username')
            password = data.get('password')
            # 用户验证，如果用户名和密码正确，返回user对象，否则返回None
            user = authenticate(request, username=username, password=password)
            if user:
                    login(request, user)
                    return redirect(reverse('blog_app:index'))
            return render(request, 'user_app/login.html', {'msg': '用户名或密码不正确'})
        else:
            return render(request, 'user_app/login.html', {'form': form})


def userlogout(request):
    '''退出登录'''
    logout(request)
    return redirect(reverse('blog_app:index'))



