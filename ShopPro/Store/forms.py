from django import forms
from django.forms import ValidationError
from Store.models import User


class UserForm(forms.Form):
    username = forms.CharField(max_length = 20,min_length = 6,error_messages={
        "max_length": "用户名超长",
        "min_length": "用户名长度不足",
        "required": "用户名不可以位空"
    })
    password = forms.CharField(max_length = 10,min_length = 6,error_messages={
        "max_length": "密码超长",
        "min_length": "密码长度不足",
        "required": "密码不可以为空"
    })

    def clean_username(self):
        data = self.cleaned_data.get("username")
        user = User.objects.filter(username=data).count()
        if user:
            raise  ValidationError("用户名重复")
        else:
            return data