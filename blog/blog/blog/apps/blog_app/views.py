from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.paginator import Paginator  # 分页
from django.core.cache import cache  # 缓存
from django.db.models import F, Count
from django.db import transaction
from django.conf import settings
import markdown
from apps.blog_app.forms import BlogCommentForm  # 文章评论表单验证类
from apps.blog_app.models import *
from utils.check_page_number import check_page_number


class BlogView(View):
    """博客列表页"""
    def get(self, request):
        """查询所有文章，分页展示"""
        # 1、查询所有文章
        type_id = request.GET.get('type_id', '')
        try:
            type_id = int(type_id)  # 按类型查询文章
            blogs = BlogModel.objects.filter(is_delete=0, blog_type=type_id).order_by('-id')  # 按时间降序
        except:
            blogs = BlogModel.objects.filter(is_delete=0).order_by('-id')  # 按时间降

        # 2、产生分页器
        paginator = Paginator(blogs, settings.NUM_PAGES)  # 每页显示条目数
        p = request.GET.get('page', 1)  # 获取页码
        page = check_page_number(page=p, paginator=paginator)
        pager = paginator.get_page(page)  # 请求的页

        # 文章按类型分组
        blog_type = BlogModel.objects.values('blog_type', 'blog_type__type', 'blog_type__id').annotate(Count('blog_type'))

        # 3、返回
        return render(request, 'blog_app/blog.html', locals())


class BlogDetailView(View):
    """博客详情页"""
    def get(self, request):
        """显示文章详情，文章评论"""
        bid = request.GET.get('bid')  # 获取文章id
        error = request.GET.get('error')  # post请求后会重定向，并带上error参数
        if bid and bid.isdigit():
            # 1、根据id查询文章
            blog = BlogModel.objects.filter(id=bid).first()
            if blog:
                # 文章浏览量: +1
                key = request.META['REMOTE_ADDR'] + str(blog.id)  # 缓存键：用户ip + 文章id
                if not cache.get(key):
                    try:
                        blog.browse += 1
                        blog.save()
                        cache.set(key, 1, 300)  # 缓存过期时间5分钟
                    except:
                        pass
            # 文章内容转换为html字符串
            blog.content = markdown.markdown(blog.content,
                                             extensions=[
                                                 # 扩展参考官方：https://python-markdown.github.io/extensions/
                                                 'markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc'])

            # 2、查询文章所属评论，然后分页
            comments = BlogCommentModel.objects.filter(is_delete=0, blog_id=bid).order_by('-id')  # 文章的全部评论
            if comments:
                pager = None
                paginator = Paginator(comments, settings.NUM_PAGES)
                p = request.GET.get('page', 1)
                page = check_page_number(page=p, paginator=paginator)
                pager = paginator.get_page(page)  # 请求的页
        return render(request, 'blog_app/blog_detail.html', locals())

    def post(self, request):
        """post请求，处理提交的评论"""
        bid = request.POST.get('bid')  # 获取文章id
        error = ''
        if request.user.is_authenticated:
            content = request.POST.get('content','').strip()  # 获取评论内容，去除两边空格
            if content:
                # 创建一条评论
                comment = BlogCommentModel(content=content,
                                           user_id=request.user.id,
                                           blog_id=bid)
                blog_item = BlogModel.objects.filter(id=bid).first()
                if blog_item:
                    try:
                        # 显示开启事务，需要两张表一起修改，保持数据完整
                        with transaction.atomic():
                            BlogModel.objects.filter(id=bid).update(comment=F('comment') + 1)  # 文章评论数 +1
                            comment.save()  # 保存评论
                    except:
                        error = '评论保存失败'
                else:
                    error = '找不到对应的文章'
            else:
                error = '请输入内容'
        else:
            error = '请先登录'
        return redirect(f'/blog/blog_detail/?bid={bid}&error={error}#comment_list')












