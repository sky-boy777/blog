from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Duanzi, Blog
from django.core.paginator import Paginator  # 分页
import markdown
from django.views.decorators.cache import cache_page  # 页面缓存
from django.utils.decorators import method_decorator  # 将函数装饰器转换为方法装饰器
import random


class IndexView(View):
    '''博客首页'''
    def get(self, request):
        # 反爬措施，请求参数混淆:http://127.0.0.1:8000/blog_detail/?key=88888888&bid=1
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
        paginator = Paginator(blogs, 7)  # 每页显示十条
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
        paginator = Paginator(blogs, 10)
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
        paginator = Paginator(duanzi, 7)  # 每页显示十条
        # 获取页码
        page = request.GET.get('page', 1)
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'blog_app/duanzi.html', locals())

    # 搜索框提交post请求
    def post(self, request):
        # 1、获取过滤条件，然后查询数据库
        keyword = request.POST.get('keyword')
        print(keyword, type(keyword))
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
        paginator = Paginator(duanzi, 10)
        pager = paginator.page(1)

        # 3、返回
        return render(request, 'blog_app/duanzi.html', locals())


def aboutme(request):
    '''关于我'''
    return render(request, 'blog_app/about.html')


def blog_detail(request):
    '''博客详情页'''
    bid = request.GET.get('bid')  # 获取文字id
    try:
        blog = Blog.objects.get(bid=bid)  # 根据文字id查询一条数据
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





