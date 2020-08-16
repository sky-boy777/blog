from django.contrib import admin
from .models import *

# Register your models here.
class DuanziAdmin(admin.ModelAdmin):
    '''段子'''
    # 显示的字段
    list_display = ['id', 'text']
    # 搜所字段
    search_fields = ['text']
    # 过滤
    # list_filter = ['id']
    list_per_page = 20  # 每页显示10条


class BlogAdmin(admin.ModelAdmin):
    list_display = ['bid', 'btitle', 'btext', 'btime', 'bfavour', 'bbrowse', 'bcomment']


class LeaveAMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'username', 'create_time']
    # 搜所字段
    search_fields = ['username']
    # 过滤
    list_filter = ['username']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'username', 'create_time', 'bid']
    # 搜所字段
    search_fields = ['username', 'bid']
    # 过滤
    list_filter = ['username']


admin.site.register(Duanzi, DuanziAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(LeaveAMessageModel, LeaveAMessageAdmin)
admin.site.register(CommentModel, CommentAdmin)


