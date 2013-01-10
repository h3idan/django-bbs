# coding: utf-8

from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import models
import forms
import time


def index(request):
    
    after_range_num = 5     # 当前页前显示5页
    bevor_range_num = 4     # 当前页后显示4页

    try:        # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    info = models.Subject.objects.all()     
    paginator = Paginator(info, 4)      # 设置页面显示帖子的数量
    
    try:
        posts_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        posts_list = paginator.page(1)
    
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num : page + bevor_range_num]
    else:
        page_range = paginator.page_range[0 : int(page) + bevor_range_num]

    return render_to_response('content.html',locals())


def postsForm(request):
    ''' 发帖表单处理 '''
    if request.method == "POST":
        form = forms.PostsForm(request.POST)
        postdata = True

    else:
        form = forms.PostsForm()
        postdata = False
    return form, postdata

def posts(request):
    ''' 帖子内容处理，发帖成功重定向 '''
    form,postdata = postsForm(request)
    if postdata:
        if form.is_valid():
            title = request.POST.get('title', '')
            detail = request.POST.get('details', '')
            
            author = request.session['username']
            the_author = models.MyUser.objects.get(username=author)
            name = models.Subject(title=title, details = detail, user = the_author)
            name.save() 
    return HttpResponseRedirect('/')

def postsadd(request):
    '''发帖'''
    form, postdata = postsForm(request)    
    
    return render_to_response('postsadd.html', locals())


def postsdel(request, ID):
    '''删除帖子'''
    email = request.session['email']
    
    posts = models.Subject.objects.get(id=ID)
    
    if email == posts.user.email:
        posts.delete()

    return HttpResponseRedirect('/bbs/postsmanage/')


def postsmanage(request):
    '''帖子管理'''
    posts = models.Subject.objects.all()
    after_range_num = 5     # 当前页前显示5页
    bevor_range_num = 4     # 当前页后显示4页

    try:        # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    
    paginator = Paginator(posts, 4)      # 设置页面显示帖子的数量
    
    try:
        posts_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        posts_list = paginator.page(1)
    
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num : page + bevor_range_num]
    else:
        page_range = paginator.page_range[0 : int(page) + bevor_range_num]
    
    return render_to_response('postsmanage.html',locals())


def subpostForm(request):
    '''评论表单处理'''
    if request.method == "POST":
        form = forms.SubpostForm(request.POST)
        postdata = True
    else:
        form = forms.SubpostForm()
        postdata = False
    return form, postdata

def subpost(request, ID):
    ''' 评论内容处理 '''
    form,postdata = subpostForm(request)
    if postdata:
        if form.is_valid():
            reply = request.POST.get('comments', '')     # 从request得到comments的内容
            posts = models.Subject.objects.get(id=ID)       
            
            try:
                username = request.session['username']
            except:
                return render_to_response('fail_rep.html')
            else:
                user = models.MyUser.objects.get(username=username)

                rep = models.Reply(title=reply, details=reply, user=user)
                rep.save()
                posts.reply.add(rep)
                posts.save()
    return HttpResponseRedirect('/bbs/replys/'+ID+'/')

def replys(request,ID):
    '''回复'''
    
    nameid = models.Subject.objects.get(id=ID)      # 查找这个id的帖子
    replys = nameid.reply.all()                     # 查找所有帖子的回复
    
    after_range_num = 5     # 当前页前显示5页
    bevor_range_num = 4     # 当前页后显示4页

    try:        # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    
    paginator = Paginator(replys, 4)      # 设置页面显示帖子的数量
    
    try:
        posts_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        posts_list = paginator.page(1)
    
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num : page + bevor_range_num]
    else:
        page_range = paginator.page_range[0 : int(page) + bevor_range_num]
    
    form, postdata = subpostForm(request)

    return render_to_response('subpost.html', locals())


def login(request):
    '''登录'''
    email = request.POST.get('email', '')
    userpasswd = request.POST.get('passwd', '')
    
    if email:
        try:
            user = models.MyUser.objects.get(email=email)
        except:
            return render_to_response('fail_login.html')
        else:
            if email == user.email and userpasswd == user.userpassword:
                request.session['email'] = email 
                request.session['username'] = user.username 
                return HttpResponseRedirect('/')
            else:
                return render_to_response('fail_login.html')
    else:
        return render_to_response('fail_login.html')


def logout(request):
    '''登出'''
    del request.session['username']
    return HttpResponseRedirect('/')


def register(request):
    '''用户注册'''
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        
        if form.is_valid():
            name = request.POST.get('username','')
            password1 = request.POST.get('password1','')
            password2 = request.POST.get('password2','')
            email = request.POST.get('email','')
            
            if password1 == password2:
                user = models.MyUser(username = name, userpassword = password1, email = email)
                user.save()
                return render_to_response('success_reg.html')
            else:
                return render_to_response('fail_reg.html')
    else:
        
        form = forms.UserForm()
    return render_to_response('registers.html', locals())


def changepwd(request):
    '''更改密码'''
    if request.method == 'POST':
        form = forms.ChangePwd(request.POST)
        
        if form.is_valid():
            email = request.POST.get('email','')
            oldpassword = request.POST.get('oldpassword', '')
            password1 = request.POST.get('password1','')
            password2 = request.POST.get('password2','')
            
            author = request.session['username']
            user = models.MyUser.objects.get(email=email)
            
            if email == user.email:
                if oldpassword == user.userpassword:
                    if password1 == password2:
                        user.delete()
                        user = models.MyUser(username = author, userpassword = password1, email = email)
                        user.save()
                        return HttpResponse('修改成功！')
                    else:
                        return HttpResponse('您输入的两次密码不一致!!')
                else:
                    return HttpResponse('原密码不正确！')
            else:
                return HttpResponse('您输入的邮箱不存在！')
    else:
        form = forms.ChangePwd()

    return render_to_response('changepwd.html', locals())



