from django.contrib import admin
from apps.web_manage_app.models import *


# Register your models here.
class BYCInfoAdmin(admin.ModelAdmin):
    """欢迎信息，关于我，网站底部信息"""
    list_display = ['id', 'content', 'bottom', 'about_me', 'is_delete', 'create_time', 'update_time']
    # 只读字段
    readonly_fields = ['create_time', 'update_time']


@admin.register(HomePlateModel)
class HomePlateAdmin(admin.ModelAdmin):
    """首页板块"""
    list_display = ('title', 'image', 'url', 'index', 'is_delete', 'create_time', 'update_time')
    # 只读字段
    readonly_fields = ['create_time', 'update_time']


class LeaveAMessageAdmin(admin.ModelAdmin):
    """网站留言"""
    list_display = ['id', 'content', 'user_id', 'is_delete', 'create_time', 'update_time']
    # 只读字段
    readonly_fields = ['user_id', 'create_time', 'update_time']
    # 搜所字段
    search_fields = ['content']
    # 过滤
    list_filter = ['is_delete']


admin.site.register(LeaveAMessageModel, LeaveAMessageAdmin)
admin.site.register(BYCInfoModel, BYCInfoAdmin)
