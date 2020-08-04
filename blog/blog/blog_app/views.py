from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Duanzi, Blog
from django.core.paginator import Paginator  # 分页
import markdown



# Create your views here.
class IndexView(View):
    '''博客首页'''

    def get(self, request):
        # 反爬措施，请求参数混淆:http://127.0.0.1:8000/blog_detail/?key=88888888&bid=1
        key = '88888888'


        # 1、尝试获取关键字，然后决定查询条件
        keyword = request.GET.get('keyword')  # keyword是字符串类型：None <class 'str'>
        if keyword != 'None' and keyword is not None:
            # 查询数据库
            blogs = Blog.objects.filter(btitle__icontains=keyword)
        else:
            # 查询数据库
            blogs = Blog.objects.all()

        # 2、产生分页器
        paginator = Paginator(blogs, 10)  # 每页显示十条
        # 获取页码
        page = request.GET.get('page', 1)
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'blog_app/index.html', locals())

        # 搜索框提交post请求

    def post(self, request):
        # 1、获取过滤条件，然后查询数据库
        keyword = request.POST.get('keyword')
        if keyword != 'None' and keyword is not None:
            # 查询数据库
            blogs = Blog.objects.filter(btitle__icontains=keyword)
        else:
            # 查询数据库
            blogs = Blog.objects.all()

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

        # # 点赞
        # did = request.GET.get('id')
        # if did != 'None' and did is not None:
        #     try:
        #         d = Duanzi.objects.get(id=did)
        #         d.favour += 1
        #         d.save()
        #         print('ok')
        #     except:
        #         pass

        # 富文本转换成HTML
        duanzi = []
        for i in data:
            i.text = markdown.markdown(i.text)
            duanzi.append(i)

        # 2、产生分页器
        paginator = Paginator(duanzi, 10)  # 每页显示十条
        # 获取页码
        page = request.GET.get('page', 1)
        pager = paginator.get_page(page)  # 请求的页

        # 3、返回
        return render(request, 'blog_app/duanzi.html', locals())

    # 搜索框提交post请求
    def post(self, request):
        # 1、获取过滤条件，然后查询数据库
        keyword = request.POST.get('keyword')
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
        blog.btext = markdown.markdown(blog.btext)  # 富文本转换成HTML

        # 浏览量加一
        blog.bbrowse += 1
        blog.save()
    except:
        msg = '找不到资源了。。。'
        return render(request, 'blog_app/blog_detail.html', locals())

    return render(request, 'blog_app/blog_detail.html', locals())





