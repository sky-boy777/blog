from django.db import models
from mdeditor.fields import MDTextField


class Duanzi(models.Model):
    """ 段子模型 """
    id = models.AutoField(primary_key=True)
    text = MDTextField(blank=True, null=True, verbose_name='段子')  # 内容
    favour = models.PositiveIntegerField(default=0, verbose_name='获赞数')   # 点赞数,只能是正整数或0

    class Meta:
        managed = False
        db_table = 'duanzi'
        verbose_name_plural = '搞笑段子'


class Blog(models.Model):
    """ 博客文章模型 """
    bid = models.AutoField(primary_key=True, verbose_name='文章id')
    btitle = models.CharField(max_length=254, verbose_name='标题')      # 标题
    btext = MDTextField(verbose_name='正文')  # 正文, 富文本格式，渲染前要转换成HTML格式
    btime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')   # 发布时间
    bfavour = models.PositiveIntegerField(default=0, verbose_name='获赞数')   # 点赞数
    bbrowse = models.PositiveIntegerField(default=0, verbose_name='浏览数')   # 浏览数
    bcomment = models.IntegerField(default=0, blank=True, null=True, verbose_name='评论数')  # 评论数

    class Meta:
        db_table = 'blog'
        verbose_name_plural = '博客'


class LeaveAMessageModel(models.Model):
    """ 留言表 """
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=False, verbose_name='内容')  # 留言内容
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')  # 留言创建时间
    username = models.CharField(max_length=30, verbose_name='用户')  # 谁留的言

    class Meta:
        db_table = 'leave_a_message'
        verbose_name_plural = '留言'


class CommentModel(models.Model):
    """ 文章评论 """
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=False, verbose_name='内容')  # 内容
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')  # 创建时间
    username = models.CharField(max_length=30, verbose_name='用户')  # 谁的评论
    bid = models.IntegerField(verbose_name='文章id')  # 文章id

    class Meta:
        db_table = 'blog_comment'
        verbose_name_plural = '文章评论'










