"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('django_admin666/', admin.site.urls, name='django_admin'),  # 嗯，谁都不认识的后台管理路径
    path('mdeditor/', include('mdeditor.urls')),  # 富文本
    path('movies/search/', include('haystack.urls')),  # 全文检索，地址为form表单的action
    path('captcha/', include('captcha.urls')),  # 图形验证码
    path('user/', include('user_app.urls', namespace='user_app')),  # 用户模块
    path('blog/', include('blog_app.urls', namespace='blog_app')),  # 博客模块
    path('movies/', include('movie_app.urls', namespace='movie_app')),  # 电影模块
    path('fun_time/', include('fun_time_app.urls', namespace='fun_time_app')),  # 开心一刻模块
    path('', include('web_manage_app.urls', namespace='web_manage_app')),  # 首页，网站前台管理
]


# 开发环境media配置，部署上线时同静态文件一起在nginx里面配置
if settings.DEBUG:
    # 静态文件 (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
