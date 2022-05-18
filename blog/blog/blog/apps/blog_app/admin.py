from django.contrib import admin
from apps.blog_app.models import *


# Register your models here.
@admin.register(BlogTypeModel)
class BlogTypeAdmin(admin.ModelAdmin):
    """博客类型"""
    list_display = ['type', 'id', 'is_delete', 'create_time', 'update_time']
    # 只读字段
    readonly_fields = ['create_time', 'update_time']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    """博客"""
    list_display = ['title', 'id', 'user', 'blog_type', 'favour',
                    'browse', 'comment', 'is_delete', 'create_time',
                    'update_time'
                    ]
    # 只读字段
    readonly_fields = ['create_time', 'update_time', 'favour', 'browse', 'comment']


@admin.register(BlogCommentModel)
class BlogCommentAdmin(admin.ModelAdmin):
    """文章评论"""
    list_display = ['id', 'content', 'user', 'blog', 'is_delete', 'create_time', 'update_time']
    # 搜索字段
    search_fields = ['user', 'id']
    # 过滤
    list_filter = ['blog']
    # 只读字段
    readonly_fields = ['content', 'user', 'blog', 'create_time', 'update_time']


# admin.site.register(BlogTypeModel, BlogTypeAdmin)
# admin.site.register(BlogModel, BlogAdmin)
# admin.site.register(BlogCommentModel, BlogCommentAdmin)


