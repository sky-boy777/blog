from django.core.mail import send_mail
from blog.settings import EMAIL_HOST_USER
from celery import Celery


# app = Celery(main='celery_tasks_tasks', broker='redis://127.0.0.1/2')


# @app.task
# def send_find_password_mail(email, code, username):
#     """发送重置密码验证码邮件
#     email: 用户邮箱
#     code: 六位数验证码
#     """
#     send_mail(subject='BYC重置密码',
#               message=f'用户名：{username}， 验证码有效时间五分钟：{code}',
#               from_email=EMAIL_HOST_USER,
#               recipient_list=[email]
#               )