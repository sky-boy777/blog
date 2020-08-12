from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # 首页
    path('duanzi/', views.DuanziView.as_view(), name='duanzi'),  # 段子
    path('about/', views.aboutme, name='about'),   # 关于我
    path('blog_detail/', views.blog_detail, name='blog_detail'),   # 博客详情页
    path('leave_a_message/', views.LeaveAMessageView.as_view(), name='leave_a_message'),  # 留言板
]
