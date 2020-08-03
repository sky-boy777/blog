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
    list_per_page = 10  # 每页显示10条


class BlogAdmin(admin.ModelAdmin):
    list_display = ['bid', 'btitle', 'btext', 'btime', 'bfavour', 'bbrowse', 'bcomment']


admin.site.register(Duanzi, DuanziAdmin)
admin.site.register(Blog, BlogAdmin)

