from django.urls import path
from apps.movie_app import views

app_name = 'movie_app'

urlpatterns = [
    path('', views.MovieView.as_view(), name='movies'),  # 电影首页
    path('<int:movie_id>/', views.MovieDetailView.as_view(), name='movie_detail'),  # 电影详情页
]
