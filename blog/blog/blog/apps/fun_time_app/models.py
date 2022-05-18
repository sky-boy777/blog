from django.db import models
from db.base_models import BaseModel
from mdeditor.fields import MDTextField


# Create your models here.
class DzModel(BaseModel):
    """段子模型"""
    content = MDTextField(blank=True, verbose_name='内容')  # 富文本
    # 逻辑外键，
    user = models.ForeignKey('user_app.UserModel',
                             on_delete=models.DO_NOTHING,  # 非级联删除
                             db_constraint=False,  # 不在真实数据库创建外键
                             verbose_name='作者')

    class Meta:
        # managed = False
        db_table = 'fun_time_dz'
        verbose_name_plural = '搞笑段子'
