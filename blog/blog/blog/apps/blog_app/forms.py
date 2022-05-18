from django import forms
from captcha.fields import CaptchaField  # 图形验证码


# 留言表单验证
class BlogCommentForm(forms.Form):
    content = forms.CharField(required=True, error_messages={
        'required': '还未输入内容',
    })




