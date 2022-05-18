import re
import random
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from django.http import JsonResponse
from django.core.cache import cache  # 缓存
from django.core.mail import send_mail  # 发送邮件
from itsdangerous import TimedJSONWebSignatureSerializer  # 生成token
from itsdangerous import SignatureExpired  # token超时发生的异常
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required  # 路由保护
from django.conf import settings  # 从settings.py里导入
from apps.user_app.models import UserModel
from apps.user_app.forms import RegisterForm, LoginForm, PasswordForm, FindPasswordForm
from utils.send_mail import send_find_password_mail
# 验证码的东西
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


class RegisterView(View):
    """用户注册"""
    def get(self, request):
        # 验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        # 已登录的用户不能访问注册页码跟登录页面
        if request.user.is_authenticated:
            return redirect(reverse('blog_app:index'))
        return render(request, 'user_app/register.html', locals())

    def post(self, request):
        # 验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # 验证表单
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 判断用户名是否已存在
            if len(UserModel.objects.filter(username=username)) > 0:
                username_error = '用户名已存在'
                return render(request, 'user_app/register.html', locals())
            # 判断邮箱是否已存在
            if len(UserModel.objects.filter(email=email)) > 0:
                email_error = '该邮箱已被注册'
                return render(request, 'user_app/register.html', locals())
            try:
                # 注册，create_user会把密码加密
                user = UserModel.objects.create_user(username=username, password=password, email=email)
                user.is_active = 0  # 未激活激的用户
                user.save()
            except:
                error = '注册出错，请联系管理员'
                return render(request, 'user_app/register.html', locals())

            # 发送激活邮件
            # 1、生成加密token
            serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 86400)  # 有效期一天
            info = {'id': user.id}  # 要加密的字典
            token = serializer.dumps(info)  # 加密，生成token
            token = token.decode('utf-8')  # 生成的token默认是byte类型，需要解码

            # 2、邮件模板,域名或主机名
            html = """<h1>%s,欢迎注册</h1> 点击下面链接激活账号(24小时后过期)<br> 
                        <a href="%s/user/active/?token=%s">%s/user/active/?token=%s</a>""" \
                   % (username, settings.HOST_URL, token, settings.HOST_URL, token)
            # 2、发送邮件
            send_mail('BYC账号激活', '', settings.EMAIL_HOST_USER, [email], html_message=html)
            return redirect(reverse('user_app:login'))
        # 表单验证失败，返回错误信息
        return render(request, 'user_app/register.html', locals(), {'form': form})


def active(request):
    """激活账号"""
    uid = None

    # 查看token是否过期
    try:
        serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, 86400)
        token = request.GET.get('token')
        info = serializer.loads(token)  # 解密，加密的时候是字典，解密的时候还是字典
        uid = info.get('id')
    except SignatureExpired as e:  # token过期的错误SignatureExpired
        try:
            user = UserModel.objects.get(pk=uid)  # 删除账号，让用户重新注册
            user.delete()
        except:
            pass
        return HttpResponse('激活链接已过期，请重新注册')

    # 查看用户是否存在
    user = UserModel.objects.filter(pk=uid).first()  # 在数据库里查找用户，找不到则表示用户不存在
    if not user:
        return HttpResponse('<h1>用户不存在,前往<a href="' + settings.HOST_URL + '/user/register">注册</a></h1>')
    # 激活用户
    try:
        if user.is_active == 1:
            return render(request, 'user_app/active.html')
        user.is_active = 1
        user.save()
        return render(request, 'user_app/active.html')
    except:
        return HttpResponse('激活失败，请联系管理员: 1251779123@qq.com')


class LoginView(View):
    """用户登录"""
    def get(self, request):
        """渲染登录页面"""
        # 生成验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        # 已登录的用户不能访问注册页码跟登录页面
        if request.user.is_authenticated:
            return redirect(reverse('web_manage_app:index'))
        return render(request, 'user_app/login.html', {'hashkey': hashkey, 'image_url': image_url})

    def post(self, request):
        """处理表单数据"""
        # 生成验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        # 获取表单数据
        data = request.POST.dict()
        username = data.get('username', '')
        password = data.get('password', '')

        # 验证表单
        form = LoginForm(request.POST)
        if form.is_valid():
            # 用户验证，如果用户名和密码正确，返回user对象，否则返回None
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('web_manage_app:index'))
            else:
                error = '用户名或密码错误'
                password = ''
                return render(request, 'user_app/login.html', locals())
        else:
            return render(request, 'user_app/login.html', locals(), {'form': form})


class SendFindPasswordEmail(View):
    """发送重置密码邮件"""
    def post(self, request):
        # 一个空字典，code=0表示未发送邮件，1为已发送，需要前端判断，然后发送按钮倒计时
        data = {}
        # 接收数据
        email = request.POST.get('email')
        # 验证邮箱
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            data = {'code': 0, 'msg': '邮箱格式错误'}
            return JsonResponse(data=data)
        # 是否已经发送过验证码
        if cache.get('find_password_'+email):
            data = {'code': 0, 'msg': '此邮箱已发送过验证码，请五分钟后再重试'}
            return JsonResponse(data=data)
        # 验证用户
        user = UserModel.objects.filter(email=email, is_active=1).first()
        if not user:
            data = {'code': 0, 'msg': '邮箱未注册'}
            return JsonResponse(data=data)
        # 生成邮箱验证码
        code = ''
        choice_str = '1234567890'
        for i in range(6):
            code += random.choice(choice_str)
        # 验证码放入缓存，key为email，有效时间五分钟
        try:
            cache.set('find_password_'+email, code, 300)
        except:
            data = {'code': 0, 'msg': '验证码缓存出错'}
            return JsonResponse(data=data)
        # 发送邮件
        send_find_password_mail(email=email, code=code, username=user.username)
        data = {'code': 1, 'msg': '邮件发送成功'}
        return JsonResponse(data=data)


class FindPassword(View):
    """重置密码"""
    def get(self, request):
        """渲染表单"""
        default_password = settings.DEFAULT_PASSWORD
        # 生成验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        # 已登录的用户不能访问注册页码跟登录页面
        if request.user.is_authenticated:
            return redirect(reverse('web_manage_app:index'))
        return render(request, 'user_app/find_password.html', locals())

    def post(self, request):
        """处理邮箱找回密码"""
        default_password = settings.DEFAULT_PASSWORD
        # 生成图片验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        # 接收数据
        email = request.POST.get('email', '')
        verification_code = request.POST.get('verification_code', '')
        # 表单验证
        form = FindPasswordForm(request.POST)
        if form.is_valid():
            # 重置密码
            user = UserModel.objects.filter(email=email).first()
            if user:
                try:
                    user.set_password(default_password)
                    user.save()  # 保存
                    msg = '重置密码成功！'
                except:
                    error = '重置密码失败！'
            else:
                error = '用户不存在！'
        return render(request, 'user_app/find_password.html', locals())


# 路由保护
@login_required(login_url='user_app:login')
def change_password(request):
    """修改密码"""
    if request.method == 'POST':
        form = PasswordForm(request.POST)  # 表单验证
        if form.is_valid():
            username = request.user.username
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')

            # 用户验证，如果当前登录的用户名和表单输入的旧密码密码正确，则返回user对象，否则返回None
            user = authenticate(request, username=username, password=old_password)
            if user:
                try:
                    user = UserModel.objects.get(pk=request.user.id)  # 获取得用户实例对象
                    user.set_password(new_password)  # 修改密码
                    user.save()  # 保存
                    return redirect(reverse('user_app:login'))
                except:
                    return render(request, 'user_app/change_password.html', {'error': '出错了'})
            else:
                return render(request, 'user_app/change_password.html', {'msg': '密码不正确'})
        else:
            return render(request, 'user_app/change_password.html', {'form': form})
    # GET请求
    return render(request, 'user_app/change_password.html')


@login_required(login_url='user_app:login')
def user_logout(request):
    """退出登录"""
    logout(request)
    return redirect(reverse('web_manage_app:index'))



