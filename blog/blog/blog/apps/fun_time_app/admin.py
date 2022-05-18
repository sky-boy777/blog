from django.contrib import admin
from apps.fun_time_app.models import *


# Register your models here.
class DzAdmin(admin.ModelAdmin):
    """段子"""
    # 显示的字段
    list_display = ['id', 'content', 'user_id', 'is_delete', 'create_time', 'update_time']

    # 只读字段
    readonly_fields = ['create_time', 'update_time',]
    search_fields = ['content']   # 搜索字段
    list_filter = ['is_delete']   # 过滤
    list_per_page = 20  # 每页显示条数


admin.site.register(DzModel, DzAdmin)
