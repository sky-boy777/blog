from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # 注册
    path('active/', views.active, name='active'),  # 激活账号
    path('login/', views.LoginView.as_view(), name='login'),  # 登录
    path('send_find_password_email/', views.SendFindPasswordEmail.as_view(), name='send_find_password_email'),  # 发送重置密码邮件
    path('find_password/', views.FindPassword.as_view(), name='find_password'),  # 找回密码
    path('logout/', views.user_logout, name='logout'),  # 退出登录
    path('change_password/', views.change_password, name='change_password'),  # 修改密码
]
