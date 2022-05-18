from django.urls import path
from apps.fun_time_app import views

app_name = 'fun_time_app'

urlpatterns = [
    path('', views.DzView.as_view(), name='dz'),  # 段子
]
