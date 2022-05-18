from django.db import models
from db.base_models import BaseModel
from mdeditor.fields import MDTextField


# Create your models here.
class BYCInfoModel(BaseModel):
    """欢迎信息，关于我，网站底部信息"""
    content = MDTextField(null=True, verbose_name='首页简介')
    bottom = MDTextField(null=True, verbose_name='网站底部标题')  # 网站底部，富文本
    about_me = MDTextField(verbose_name='关于我')  # 富文本格式，渲染前要转换成HTML格式，longText类型

    class Meta:
        db_table = 'byc_info'
        verbose_name_plural = '欢迎信息，关于我，网站底部信息'


class HomePlateModel(BaseModel):
    """首页主体板块"""
    image = models.ImageField(upload_to='home_plate/', verbose_name='首页板块封面')
    # 图片不能显示时，显示的文字
    title = models.CharField(max_length=32, verbose_name='板块标题')
    url = models.URLField(verbose_name='板块url')
    index = models.PositiveSmallIntegerField(verbose_name='排序号')

    class Meta:
        db_table = 'home_plate'
        verbose_name_plural = '首页板块'


class LeaveAMessageModel(BaseModel):
    """网站留言"""
    content = models.CharField(max_length=600, verbose_name='留言内容')

    # 逻辑外键，多对一，删除一那方，多一方什么都不做，需要手动编写逻辑保持数据一致性、完整性
    user = models.ForeignKey('user_app.UserModel', on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = 'leave_a_message'
        verbose_name_plural = '网站留言'
