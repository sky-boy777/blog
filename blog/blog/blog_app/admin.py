from django.contrib import admin
from .models import *


# Register your models here.
class DuanziAdmin(admin.ModelAdmin):
    '''段子'''
    # 显示的字段
    list_display = ['id', 'text', 'favour']
    # 搜所字段
    search_fields = ['text']
    # 过滤
    # list_filter = ['id']
    list_per_page = 20  # 每页显示条数


class BlogAdmin(admin.ModelAdmin):
    '''博客'''
    list_display = ['bid', 'btitle', 'btime', 'bfavour', 'bbrowse', 'bcomment', 'btext']


class LeaveAMessageAdmin(admin.ModelAdmin):
    '''留言'''
    list_display = ['id', 'content', 'username', 'create_time']
    # 搜所字段
    search_fields = ['username']
    # 过滤
    list_filter = ['username']


class CommentAdmin(admin.ModelAdmin):
    '''文章评论'''
    list_display = ['id', 'content', 'username', 'create_time', 'bid']
    # 搜索字段
    search_fields = ['username', 'bid']
    # 过滤
    list_filter = ['username']


class AboutMeAdmin(admin.ModelAdmin):
    """欢迎信息，关于我，网站底部信息"""
    list_display = ['id', 'title', 'lx', 'jj', 'content']


admin.site.register(Duanzi, DuanziAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(LeaveAMessageModel, LeaveAMessageAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(AboutMeModel, AboutMeAdmin)

