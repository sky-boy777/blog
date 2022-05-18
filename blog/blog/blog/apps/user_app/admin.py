from django.contrib import admin
from apps.user_app.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """用户信息"""
    list_display = ['username', 'avatar', 'email', 'last_login',
                    'is_superuser', 'is_active',
                    'is_delete', 'create_time', 'update_time', 'id']

    # 只读字段
    readonly_fields = ["password", 'create_time', 'update_time', 'last_login', 'date_joined']


# admin.site.unregister(UserModel)
admin.site.register(UserModel, UserAdmin)
