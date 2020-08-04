from django import forms
import re

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, error_messages={
        'max_length': '用户名不能超过30个字符',
        'required': '用户名不能为空'
    })

    password = forms.CharField(min_length=6, required=True, error_messages={
        'min_length': '密码最小长度6位',
        'required': '密码不能为空',
    })

    def clean_email(self):
        emial = self.cleaned_data.get('emial')
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", emial) is None:
            raise ValueError('邮箱格式不正确')
        return emial


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, error_messages={
        'max_length': '用户名不能超过30个字符',
        'required': '用户名不能为空'
    })

    password = forms.CharField(min_length=6, required=True, error_messages={
        'min_length': '密码最小长度6位',
        'required': '密码不能为空',
    })



