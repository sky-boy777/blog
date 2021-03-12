from django.db import models
from mdeditor.fields import MDTextField

class Duanzi(models.Model):
    '''段子模型'''
    # id
    id = models.AutoField(primary_key=True)
    # 内容
    text = MDTextField(blank=True, null=True, verbose_name='段子')
    # 点赞数,只能是正整数或0
    favour = models.PositiveIntegerField(default=0, verbose_name='获赞数')

    class Meta:
        managed = False
        db_table = 'duanzi'
        verbose_name_plural = '搞笑段子'



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
    bfavour = models.PositiveIntegerField(default=0, verbose_name='获赞数')
    # 浏览数
    bbrowse = models.PositiveIntegerField(default=0, verbose_name='浏览数')
    # 评论数
    bcomment = models.IntegerField(default=0, blank=True, null=True, verbose_name='评论数')

    class Meta:
        db_table = 'blog'
        verbose_name_plural = '博客'


class LeaveAMessageModel(models.Model):
    '''留言表'''
    id = models.AutoField(primary_key=True)
    # 留言内容
    content = models.TextField(null=False, verbose_name='内容')
    # 留言创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    # 谁留的言
    username = models.CharField(max_length=30, verbose_name='用户')

    class Meta:
        db_table = 'leave_a_message'
        verbose_name_plural = '留言'


class CommentModel(models.Model):
    '''文章评论'''
    id = models.AutoField(primary_key=True)
    # 内容
    content = models.TextField(null=False, verbose_name='内容')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    # 谁的评论
    username = models.CharField(max_length=30, verbose_name='用户')
    # 文章id
    bid = models.IntegerField(verbose_name='文章id')

    class Meta:
        db_table = 'blog_comment'
        verbose_name_plural = '文章评论'










