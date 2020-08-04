from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),  # 登录
    path('register/', views.RegisterView.as_view(), name='register'),  # 注册
    path('active/', views.active, name='active'),  # 激活账号
    path('logout/', views.userlogout, name='logout'),  # 退出登录
]
