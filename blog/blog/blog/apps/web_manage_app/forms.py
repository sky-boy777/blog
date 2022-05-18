from django import forms
from captcha.fields import CaptchaField  # 图形验证码


# 留言表单验证
class LeaveAMessageForm(forms.Form):
    content = forms.CharField(required=True, error_messages={
        'required': '还没输入，咩都某拒',
    })

    captcha = CaptchaField()  # 验证码字段



