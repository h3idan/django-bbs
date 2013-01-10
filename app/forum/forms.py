# coding: utf-8

from django import forms
from DjangoUeditor.forms import UEditorField


class UserForm(forms.Form):
    
    username = forms.CharField(label=u'用户名', max_length=30)
    email = forms.EmailField(label=u'邮箱')
    password1 = forms.CharField(label=u'密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label=u'确认密码', widget=forms.PasswordInput())
    
class ChangePwd(forms.Form):
    
    email = forms.EmailField(label=u'邮箱')
    oldpassword = forms.CharField(label=u'旧密码', widget=forms.PasswordInput())
    password1 = forms.CharField(label=u'新密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label=u'确认密码', widget=forms.PasswordInput())
    
class PostsForm(forms.Form):
    title = forms.CharField(label=u'标题', max_length=30)
    details = UEditorField(label=u'内容')

class SubpostForm(forms.Form):
    comments = UEditorField(label=u'回复')
