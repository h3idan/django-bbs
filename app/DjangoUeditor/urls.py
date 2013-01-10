#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns, url
from DjangoUeditor.views import UploadFile,ImageManager,RemoteCatchImage,SearchMovie,scrawlUp

urlpatterns = patterns('',
    url(r'^ImageUp/(?P<uploadpath>.*)', UploadFile, {'uploadtype':'image'}),
    url(r'^FileUp/(?P<uploadpath>.*)', UploadFile, {'uploadtype':'file'}),
    url(r'^scrawlUp/(?P<uploadpath>.*)$', scrawlUp),
    url(r'^ImageManager/(?P<imagepath>.*)$', ImageManager),
    url(r'^RemoteCatchImage/(?P<imagepath>.*)$', RemoteCatchImage),
    url(r'^SearchMovie/$', SearchMovie),
)
 
