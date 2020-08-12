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

# debug=False时的静态文件配置，真正部署的时候，静态文件一般放在web服务器（例：nginx），先在本地收集静态文件，然后推送到服务器
# from django.conf.urls import url
# from django.views import static


urlpatterns = [
    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('houtaiguanli666/', admin.site.urls),  # 后台管理:byc_admin, qq1314, 嗯，谁都不认识的后台管理路径
    path('mdeditor/', include('mdeditor.urls')),  # 富文本
    path('captcha/', include('captcha.urls')),  # 图形验证码
    path('', include('blog_app.urls', namespace='blog_app')),  # 首页模块
    path('user/', include('user_app.urls', namespace='user_app')),  # 用户模块
]


# 富文本配置
if settings.DEBUG:
    # 静态文件 (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
