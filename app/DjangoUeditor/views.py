#!/usr/bin/env python
# coding: utf-8

from django.http import HttpResponse
import settings as USettings
import os
from django.utils import simplejson
from  utils import GenerateRndFilename

try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    def csrf_exempt(fn):
        return fn


def SaveUploadFile(PostFile,FilePath):
    """ 保存上传的文件 """
    try:
        f = open(FilePath, 'wb')
        for chunk in PostFile.chunks():
            f.write(chunk)
    except Exception, E:
        f.close()
        return u"写入文件错误:" + E.message
    f.close()
    return u"SUCCESS"


mimetype = "Application/javascript"
@csrf_exempt
def UploadFile(request,uploadtype,uploadpath):
    """ 上传附件 """
    
    if not request.method == "POST":
        return  HttpResponse(simplejson.dumps( u"{'state:'ERROR'}"), mimetype)
    
    state = "SUCCESS"
    files = request.FILES.get("upfile", None)
    #如果没有提交upfile则返回错误
    if file is None:
        return  HttpResponse(simplejson.dumps(u"{'state:'ERROR'}"), mimetype)
    
    #取得上传的文件的原始名称
    original_name,original_ext = files.name.split('.')
    
    #类型检验
    if uploadtype == "image" or uploadtype == "scrawlbg":
        allow_type = USettings.UEditorSettings["images_upload"]['allow_type']
    else:
        allow_type = USettings.UEditorSettings["files_upload"]['allow_type']
    if not original_ext in allow_type:
        state = u"服务器不允许上传%s类型的文件。" % original_ext
    
    #大小检验
    max_size = USettings.UEditorSettings["images_upload"]['max_size']
    if max_size != 0:
        from utils import FileSize
        MF = FileSize(max_size)
        if files.size > MF.size:
            state = u"上传文件大小不允许超过%s。" % MF.FriendValue
    
    #检测保存路径是否存在,如果不存在则需要创建
    OutputPath = os.path.join(USettings.gSettings.MEDIA_ROOT, os.path.dirname(uploadpath)).replace("\\","/")
    if not os.path.exists(OutputPath):
        os.makedirs(OutputPath)
        
    #要保存的文件名格式使用"原文件名_当前时间.扩展名"
    OutputFile = GenerateRndFilename(files.name)
    
    #所有检测完成后写入文件
    if state == "SUCCESS":
        #保存到文件中
        state = SaveUploadFile(files, os.path.join(OutputPath,OutputFile))
    
    #返回数据
    if uploadtype == "image" or uploadtype == "scrawlbg":
        rInfo={
            'url': OutputFile,    #保存后的文件名称
            'title': request.POST.get("pictitle", files.name),       #文件描述，对图片来说在前端会添加到title属性上
            'original': files.name,     #原始文件名
            'state': state              #上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
        }
    else:
        rInfo={
            'url': OutputFile,          #保存后的文件名称
            'original': files.name,     #原始文件名
            'filetype': original_ext,
            'state': state              #上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
        }
    if uploadtype == "scrawlbg":        #上传涂鸦背景
        return HttpResponse(u"<script>parent.ue_callback('%s','%s');</script>" % (rInfo["url"],rInfo["state"]))
    else:       #上传文件与图片
        return HttpResponse(simplejson.dumps(rInfo), mimetype)


@csrf_exempt
def ImageManager(request, imagepath):
    """ 图片文件管理器 """
    
    if not request.method != "GET": 
        return HttpResponse(simplejson.dumps(u"{'state:'ERROR'}"), mimetype)
    
    #取得动作
    action = request.GET.get("action","get")
    if action == "get":
        TargetPath = os.path.join(USettings.gSettings.MEDIA_ROOT, os.path.dirname(imagepath)).replace("\\","/")
        if not os.path.exists(TargetPath):
            os.makedirs(TargetPath)
        return HttpResponse(ReadDirImageFiles(TargetPath), mimetype)


@csrf_exempt
def ReadDirImageFiles(path):
    """ 遍历所有文件清单 """
    
    files = ""
    dirs = os.listdir(path)
    for f in dirs:
        ext = os.path.splitext(f)[1][1:]
        if ext != "":
            if ext in USettings.UEditorSettings["images_upload"]["allow_type"]:
                if files != "":
                    files += "ue_separate_ue"
                files += f
    return files


def RemoteCatchImage(request, imagepath):
    """抓取远程图片"""

    upfile_url = request.POST.get("upfile", None)
    if upfile_url is None:
        return HttpResponse(simplejson.dumps("{'state:'ERROR'}"), mimetype)
    import urllib
    from urlparse import urlparse

    #读取远程图片文件
    try:
        CatchFile = urllib.urlopen(upfile_url)
    except Exception,E:
        tip = u"抓取图片错误：%s" % E.message
        return HttpResponse(simplejson.dumps("{'tip:'%s'}" % tip), mimetype)

    #取得目标抓取的文件名称
    OutFile = os.path.basename(urlparse(CatchFile.geturl()).path)

    #检查文件类型
    OutFileExt = os.path.splitext(OutFile)[1][1:]
    if not (OutFileExt != "" and OutFileExt in USettings.UEditorSettings['images_upload']['allow_type']):
        tip = u"不允许抓取%s类型的图片错误" % OutFileExt
        return HttpResponse(simplejson.dumps(u"{'tip:'%s'}" % tip), mimetype)

    #将抓取到的文件写入文件
    try:
        f = open(os.path.join(USettings.settings.MEDIA_ROOT, imagepath,OutFile).replace("\\","/"), 'wb')
        f.write(CatchFile.read())
        f.close()
        rInfo = {
            'url': OutFile,                         # 新地址一ue_separate_ue新地址二ue_separate_ue新地址三',
            'srcUrl': upfile_url,                   #原始地址一ue_separate_ue原始地址二ue_separate_ue原始地址三',
            'tip': u'远程图片抓取成功！'            #'状态提示'
        }
        return HttpResponse(simplejson.dumps(rInfo), mimetype)

    except Exception, E:
        tip = u"写入图片文件错误:" % E.message
        return HttpResponse(simplejson.dumps(u"{'tip:'%s'}" % tip), mimetype)


def SearchMovie(request):
    """ 搜索视频 """
    
    Searchkey = request.POST.get("searchKey", None)
    if Searchkey is None:
        return HttpResponse(u"错误！")
    Searchtype = request.POST.get("videoType","")
    import urllib
    Searchkey = urllib.quote(Searchkey.encode("utf8"))
    Searchtype = urllib.quote(Searchtype.encode("utf8"))
    try:
        htmlcontent = urllib.urlopen(u'http://api.tudou.com/v3/gw?method=item.search&appKey=myKey&format=json&kw=%s&pageNo=1&pageSize=20&channelId=%s&inDays=7&media=v&sort=s' % (Searchkey, Searchtype))
        return HttpResponse(htmlcontent)
    except Exception, E:
        return HttpResponse(E.message)


def scrawlUp(request, uploadpath):
    """ 涂鸦功能上传 """
    
    action = request.GET.get("action", "")
    #背景上传
    if action == "tmpImg":
        return UploadFile(request, "scrawlbg", uploadpath)
    else:       #处理涂鸦合成相片上传
        try:
            content = request.POST.get("content", "")
            import base64

            OutputFile = GenerateRndFilename("scrawl.png")
            OutputPath = os.path.join(USettings.gSettings.MEDIA_ROOT, os.path.dirname(uploadpath)).replace("\\","/")
            if not os.path.exists(OutputPath):
                os.makedirs(OutputPath)
            f = open(os.path.join(OutputPath,OutputFile), 'wb')
            f.write(base64.decodestring(content))
            f.close()
            state = "SUCCESS"
        except Exception, E:
            state = "ERROR:"
        rInfo = {
            "url": OutputFile,
            "state": state
        }
        return HttpResponse(simplejson.dumps(rInfo), mimetype)
     
