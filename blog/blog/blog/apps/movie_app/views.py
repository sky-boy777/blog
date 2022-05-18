from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.paginator import Paginator  # 分页
from django.conf import settings
from apps.movie_app.models import *
from utils.check_page_number import check_page_number


class MovieView(View):
    """电影列表页"""
    def get(self, request):
        """电影列表页"""
        sortord = request.GET.get('sortord')  # 获取排序方式，默认是按time排序
        if sortord == 'score':
            movies = MovieModel.objects.filter(is_delete=0).values('id', 'title',
                                                                   'name', 'image',
                                                                   'douban_score', 'IMDb_score'
                                                                   ).order_by('-douban_score', '-IMDb_score')
        else:
            # 查询全部电影
            movies = MovieModel.objects.filter(is_delete=0).values('id', 'title',
                                                                   'name', 'image',
                                                                   'douban_score', 'IMDb_score'
                                                                   ).order_by('-time')
        # 分页
        paginator = Paginator(movies, settings.MOVIE_NUM_PAGES)  # 每页显示条数
        p = request.GET.get('page', 1)  # 获取页码
        page = check_page_number(page=p, paginator=paginator)
        page = check_page_number(page, paginator)  # 校验页码
        pager = paginator.get_page(page)  # 请求的页

        return render(request, 'movie_app/movie.html', {'pager': pager, 'paginator': paginator, 'sortord': sortord})


class MovieDetailView(View):
    """电影详情页"""
    def get(self, request, movie_id):
        # 根据id查询电影
        movie = MovieModel.objects.filter(id=movie_id, is_delete=0).values('title', 'detail').first()
        if movie:
            return render(request, 'movie_app/movie_detail.html', {'movie': movie})
        else:
            return render(request, '404.html')



