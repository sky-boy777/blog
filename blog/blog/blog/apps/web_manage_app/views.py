from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.paginator import Paginator  # 分页
from django.conf import settings
from apps.web_manage_app.models import *
from apps.user_app.models import UserModel
import markdown
from apps.user_app.forms import LeaveAMessageForm  # 表单验证
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from utils.check_page_number import check_page_number


def index(request):
    """主页"""
    try:
        info = BYCInfoModel.objects.values('content', 'bottom').first()
        # 简介转换为html格式字符串
        if info:
            info['content'] = markdown.markdown(info.get('content'))
    except:
        info = None
    # 板块，按序号排序
    try:
        home_plates = HomePlateModel.objects.values('image', 'title', 'url').order_by('index')
    except:
        home_plates = None
    return render(request, 'web_manage_app/index.html', {'info': info, 'home_plates': home_plates})


def about_me(request):
    """关于我"""
    try:
        about = BYCInfoModel.objects.values('about_me').order_by('-id').first()
        about['about_me'] = markdown.markdown(about.get('about_me'))  # 转换为html格式字符串
    except:
        about = None
    return render(request, 'web_manage_app/about.html', {'about': about})


def leave_a_message_view(request):
    """留言板"""
    # get请求
    # 生成验证码
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)

    # 查询所有留言
    data = LeaveAMessageModel.objects.filter(is_delete=0).order_by('-id')
    if data:
        # 分页
        paginator = Paginator(data, settings.NUM_PAGES)
        # 获取页码
        p = request.GET.get('page', 1)
        page = check_page_number(page=p, paginator=paginator)
        pager = paginator.get_page(page)  # 请求的页

    if request.method == 'POST':
        form = LeaveAMessageForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            user_id = request.user.id if request.user.is_authenticated else -1
            try:
                leave_a_message = LeaveAMessageModel(content=content, user_id=user_id)
                leave_a_message.save()
                # 保存后重定向get请求，重写查询数据库，可用ajax优化
                return redirect(reverse('web_manage_app:leave_a_message'))
            except:
                msg = '出错了'
                return redirect(reverse('web_manage_app:leave_a_message'), locals())
    return render(request, 'web_manage_app/leave_a_message.html', locals())











