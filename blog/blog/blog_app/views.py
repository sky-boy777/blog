from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Duanzi, Blog, LeaveAMessageModel, CommentModel
from django.core.paginator import Paginator  # 分页
import markdown
from user_app.myForm import LeaveAMessageForm  # 表单验证
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.views.decorators.cache import cache_page  # 页面缓存
from django.utils.decorators import method_decorator  # 将函数装饰器转换为方法装饰器
import random


def welcome(request):
    '''欢迎页'''
    return render(request, 'blog_app/welcome.html')


class IndexView(View):
    '''博客首页'''
    def get(self, request):
        # 请求参数混淆:http://127.0.0.1:8000/blog_detail/?key=88888888&bid=1
        key = '88888888'


        # 1、尝试获取关键字，然后决定查询条件
        keyword = request.GET.get('keyword')  # keyword是字符串类型：None <class 'str'>
        # print(keyword, type(keyword))
        if keyword != 'None' and keyword is not None:
            # 查询数据库
            blogs = Blog.objects.filter(btitle__icontains=keyword).order_by('-btime')
        else:
            # 查询数据库
            blogs = Blog.objects.all().order_by('-btime')  # 按时间降序

        # 2、产生分页器
        paginator = Paginator(blogs, 20)  # 每页显示十条
        # 获取页码
        page = request.GET.get('page', 1)
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'blog_app/index.html', locals())

        # 搜索框提交post请求
    def post(self, request):
        # 1、获取过滤条件，然后查询数据库
        keyword = request.POST.get('keyword')
        if keyword != '' and keyword is not None:
            # 查询数据库
            blogs = Blog.objects.filter(btitle__icontains=keyword).order_by('-btime')
        else:
            # blogs = Blog.objects.all()
            return redirect(reverse('blog_app:index'))

        # 2、分页
        paginator = Paginator(blogs, 20)
        pager = paginator.page(1)

        # 3、返回
        return render(request, 'blog_app/index.html', locals())


class DuanziView(View):
    '''段子'''
    def get(self, request):
        # 1、尝试获取关键字，然后决定查询条件
        keyword = request.GET.get('keyword')  # keyword是字符串类型：None <class 'str'>
        if keyword != 'None' and keyword is not None:
            # 查询数据库
            data = Duanzi.objects.filter(text__icontains=keyword)
        else:
            # 查询数据库
            data = Duanzi.objects.all()

        # 富文本转换成HTML
        duanzi = []
        for i in data:
            i.text = markdown.markdown(i.text)
            duanzi.append(i)

        # 2、产生分页器
        paginator = Paginator(duanzi, 20)  # 每页显示十条
        # 获取页码
        page = request.GET.get('page', 1)
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'blog_app/duanzi.html', locals())

    # 搜索框提交post请求
    def post(self, request):
        # 1、获取过滤条件，然后查询数据库
        keyword = request.POST.get('keyword')
        if keyword != '' and keyword is not None:
            # 查询数据库
            data = Duanzi.objects.filter(text__icontains=keyword)
        else:
            # keyword为空则重定向到duanz.html
            return redirect(reverse('blog_app:duanzi'))

        # 富文本转换成HTML
        duanzi = []
        for i in data:
            i.text = markdown.markdown(i.text)
            duanzi.append(i)
        # 2、分页
        paginator = Paginator(duanzi, 20)
        pager = paginator.page(1)

        # 3、返回
        return render(request, 'blog_app/duanzi.html', locals())


def aboutme(request):
    '''关于我'''
    return render(request, 'blog_app/about.html')


class LeaveAMessageView(View):
    '''留言板'''
    def get(self, request):
        '''查询数据库并渲染'''
        # 验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        leave_a_messages = LeaveAMessageModel.objects.all().order_by('-create_time')
        return render(request, 'blog_app/leave_a_message.html', locals())

    def post(self, request):
        '''接收数据并保存'''
        # 验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        leave_a_messages = LeaveAMessageModel.objects.all().order_by('-create_time')
        form = LeaveAMessageForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            username = request.user.username if request.user.is_authenticated else '匿名用户'
            try:
                leave_a_message = LeaveAMessageModel()
                leave_a_message.content = content
                leave_a_message.username = username
                leave_a_message.save()
            except:
                return render(request, 'blog_app/leave_a_message.html', locals(), {'msg': '出错了'})
            return render(request, 'blog_app/leave_a_message.html', locals())
        else:
            return render(request, 'blog_app/leave_a_message.html', locals(), {'form': form})


def blog_detail(request):
    '''博客详情页'''
    bid = request.GET.get('bid')  # 获取文章id
    # post
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if len(content) == 0:
            msg = '请输入内容'
        else:
            try:
                # 保存评论
                username = request.user.username if request.user.is_authenticated else '匿名用户'
                comment = CommentModel(content=content, username=username, bid=bid)
                comment.save()
            except:
                return redirect(reverse('blog_app:blog_detail'))

    # get
    try:
        blog = Blog.objects.get(bid=bid)  # 根据文章id查询一条数据
        comments = CommentModel.objects.filter(bid=bid).order_by('-create_time')  # 文章的全部评论
        # blog.btext = markdown.markdown(blog.btext)  # 富文本转换成HTML

        blog.btext = markdown.markdown(blog.btext, extensions=[  # 扩展参考官方：https://python-markdown.github.io/extensions/
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            # 'markdown.extensions.abbr',
            # 'markdown.extensions.smarty',
                                                    ])
        # 尝试获取session值，如果session值不等于本片文章的id，则浏览量加1
        # 然后使用本片文章id设置session值，使用了str函数，并设置过期时间
        if request.session.get(str(blog.btext)) != blog.btext:
            # 浏览量加一
            blog.bbrowse += 1
            blog.save()
            request.session[str(blog.btext)] = blog.btext
            request.session.set_expiry(0)  # 全部session过期时间，关闭浏览器
    except:
        msg = '找不到资源了。。。'
        return render(request, 'blog_app/blog_detail.html', locals())
    return render(request, 'blog_app/blog_detail.html', locals())





