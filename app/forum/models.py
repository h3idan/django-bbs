# coding: utf-8

from django.db import models
from DjangoUeditor.models import UEditorField

class MyUser(models.Model):
    username = models.CharField(max_length=50)
    userpassword = models.CharField(max_length=20)
    images = models.ImageField(upload_to='./heads/', blank=True) #头像
    email = models.EmailField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True) # 注册时间
    def __unicode__(self):
        return self.username

class Reply(models.Model):
    title = models.CharField(max_length=50)
    details = UEditorField(verbose_name=u'内容')    # 回复的内容
    datetime = models.DateTimeField(auto_now_add=True)   # 回复的时间
    user = models.ForeignKey(MyUser)    # 回复的作者
    def __unicode__(self):
        return self.title
    
class Subject(models.Model):
    title = models.CharField(max_length=50)     
    details = UEditorField(verbose_name=u'内容')    # 帖子的内容
    datetime = models.DateTimeField(auto_now_add=True)  # 发帖时间
    reply = models.ManyToManyField(Reply)  # 帖子的回复
    user = models.ForeignKey(MyUser)  # 发帖的作者
    def __unicode__(self):
        return self.title


