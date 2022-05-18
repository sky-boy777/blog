from django import forms
from django.core.cache import cache
from captcha.fields import CaptchaField  # 图形验证码
import re


# 注册验证
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, error_messages={
        'max_length': '用户名不能超过30个字符',
        'required': '用户名不能为空'
    })

    password = forms.CharField(min_length=6, required=True, error_messages={
        'min_length': '密码最小长度6位',
        'required': '密码不能为空',
    })

    captcha = CaptchaField()  # 验证码字段

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            raise ValueError('邮箱格式不正确')
        return email


# 登录验证
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, error_messages={
        'max_length': '用户名不能超过30个字符',
        'required': '用户名不能为空'
    })

    password = forms.CharField(min_length=6, required=True, error_messages={
        'min_length': '密码最小长度6位',
        'required': '密码不能为空',
    })

    captcha = CaptchaField()  # 验证码字段


# 修改密码表单验证
class PasswordForm(forms.Form):
    old_password = forms.CharField(required=True, error_messages={
        'required': '请输入旧密码',
    })
    new_password = forms.CharField(min_length=6, required=True, error_messages={
        'min_length': '密码最小长度6位',
        'required': '新密码不能为空',
    })


class FindPasswordForm(forms.Form):
    """找回密码表单验证"""
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空'})
    verification_code = forms.CharField(required=True, error_messages={'required': '验证码不能为空'})
    captcha = CaptchaField()  # 图片验证码字段

    # 验证邮箱格式
    def clean_email(self):
        """验证邮箱格式"""
        email = self.cleaned_data.get('email')
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            raise forms.ValidationError('邮箱格式不正确')
        return email

    def clean_verification_code(self):
        """验证邮箱验证码"""
        email = self.cleaned_data.get('email')
        verification_code = self.cleaned_data.get('verification_code')
        cache_verification_code = cache.get('find_password_' + email)
        if verification_code != cache_verification_code:
            raise forms.ValidationError('验证码错误')
        return verification_code


# 留言表单验证
class LeaveAMessageForm(forms.Form):
    content = forms.CharField(required=True, error_messages={
        'required': '还没输入，咩都某拒',
    })

    captcha = CaptchaField()  # 验证码字段



