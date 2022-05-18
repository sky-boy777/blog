from django.db import models
from mdeditor.fields import MDTextField
from db.base_models import BaseModel


class BlogTypeModel(BaseModel):
    """文章分类"""
    type = models.CharField(max_length=100, verbose_name='文章类型')  # 分类：MySQL，python...

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'blog_type'
        verbose_name_plural = '文章类型'


class BlogModel(BaseModel):
    """博客文章模型"""
    title = models.CharField(max_length=254, verbose_name='文章标题')
    content = MDTextField(verbose_name='正文')  # 正文, 富文本格式，渲染前要转换成HTML格式
    browse = models.IntegerField(default=0, verbose_name='阅读量')
    favour = models.IntegerField(default=0, verbose_name='获赞数')
    comment = models.IntegerField(default=0, blank=True, verbose_name='评论数')

    # 逻辑外键
    user = models.ForeignKey('user_app.UserModel',
                             on_delete=models.DO_NOTHING,
                             db_constraint=False,
                             verbose_name='作者')
    blog_type = models.ForeignKey('BlogTypeModel',
                                  on_delete=models.DO_NOTHING,
                                  db_constraint=False,
                                  verbose_name='文章分类')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        verbose_name_plural = '博客'


class BlogCommentModel(BaseModel):
    """文章评论"""
    content = models.CharField(max_length=600, verbose_name='评论内容')
    # 逻辑外键
    user = models.ForeignKey('user_app.UserModel',
                             on_delete=models.DO_NOTHING,
                             db_constraint=False,
                             verbose_name='评论所属用户')
    blog = models.ForeignKey('BlogModel',
                             on_delete=models.DO_NOTHING,
                             db_constraint=False,
                             verbose_name='评论的文章')

    class Meta:
        db_table = 'blog_comment'
        verbose_name_plural = '文章评论'


class BlogFavourModel(models.Model):
    """文章点赞"""
    blog = models.ForeignKey('BlogModel',
                             on_delete=models.DO_NOTHING,
                             db_constraint=False,
                             verbose_name='用户点赞的文章')
    user = models.ForeignKey('user_app.UserModel',
                             on_delete=models.DO_NOTHING,
                             db_constraint=False,
                             verbose_name='点赞的用户')

    class Meta:
        db_table = 'blog_favour'
        verbose_name_plural = '文章评论'
















