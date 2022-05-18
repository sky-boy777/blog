from django.urls import path
from apps.blog_app import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),  # 博客列表页
    path('blog_detail/', views.BlogDetailView.as_view(), name='blog_detail'),  # 博客详情页
]
