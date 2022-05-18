from django.urls import path
from apps.web_manage_app import views

app_name = 'web_manage_app'

urlpatterns = [
    path('about/', views.about_me, name='about'),   # 关于我
    path('leave_a_message/', views.leave_a_message_view, name='leave_a_message'),  # 留言板
    path('', views.index, name='index')  # 主页，放到最后匹配
]
