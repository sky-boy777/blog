from django.contrib import admin
from apps.movie_app.models import *


# Register your models here.
@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    """ 电影 """
    list_display = ['title', 'name', 'is_delete', 'create_time', 'update_time']

    # 只读字段
    readonly_fields = ['douban_score', 'IMDb_score', 'create_time', 'update_time']

    # 搜索字段
    search_fields = ['title']