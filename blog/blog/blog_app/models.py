from django.db import models
from mdeditor.fields import MDTextField

class Duanzi(models.Model):
    '''段子模型'''
    # id
    id = models.AutoField(primary_key=True)
    # 内容
    text = MDTextField(blank=True, null=True, verbose_name='段子')
    # 点赞数
    favour = models.IntegerField(default=0, null=True, verbose_name='获赞数')

    class Meta:
        managed = False
        db_table = 'duanzi'


class Blog(models.Model):
    '''博客文章模型'''
    bid = models.AutoField(primary_key=True, verbose_name='文章id')
    # 标题
    btitle = models.CharField(max_length=254, verbose_name='标题')
    # 正文, 富文本格式，渲染前要转换成HTML格式
    btext = MDTextField(verbose_name='正文')
    # 发布时间
    btime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # 点赞数
    bfavour = models.IntegerField(default=0, blank=True, null=True, verbose_name='获赞数')
    # 浏览数
    bbrowse = models.IntegerField(default=0, blank=True, null=True, verbose_name='浏览数')
    # 评论数
    bcomment = models.IntegerField(default=0, blank=True, null=True, verbose_name='评论数')

    class Meta:
        db_table = 'blog'






