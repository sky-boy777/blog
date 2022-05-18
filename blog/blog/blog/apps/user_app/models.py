from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_models import BaseModel


class UserModel(AbstractUser, BaseModel):
    """扩展auth_user"""
    avatar = models.ImageField(upload_to='avatar/',  # 默认上传到media/avatar/
                               default='avatar/default.jpg',
                               verbose_name='用户头像'
                               )
    # 邮箱唯一，用来邮箱登录
    email = models.EmailField(blank=True, unique=True, max_length=254, verbose_name='邮箱地址')

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户信息'










