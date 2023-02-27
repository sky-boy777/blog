from django.db import models
from db.base_models import BaseModel


# Create your models here.
class MovieBannerModel(BaseModel):
    """电影海报轮播图"""
    image = models.URLField(verbose_name='图片url')
    # 排序号

    class Meta:
        db_table = 'movie_banner'
        verbose_name_plural = '电影轮播图'


class MovieModel(BaseModel):
    """电影模型"""
    title = models.CharField(max_length=255, verbose_name='标题')
    name = models.CharField(max_length=255, verbose_name='电影名')
    time = models.DateTimeField(verbose_name='电影天堂发布此电影时间')
    image = models.CharField(max_length=255, null=True, verbose_name='电影封面')
    detail = models.TextField(verbose_name='电影详情')  # html格式
    url = models.URLField(null=True, verbose_name='原电影url')
    douban_score = models.DecimalField(max_digits=2, decimal_places=1, default=-1, verbose_name='豆瓣评分')
    IMDb_score = models.DecimalField(max_digits=2, decimal_places=1, default=-1, verbose_name='IMDb评分')

    class Meta:
        db_table = 'movie'
        verbose_name_plural = '电影'



