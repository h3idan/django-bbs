from django.conf.urls import patterns, include, url
import os


urlpatterns = patterns('forum.views',

    #url(r'^$', 'index'),
    
    #url(r'^cnhei/(?P<ID>\d+)/$', 'name_id', name='bbs_name_id'),
    
    url(r'^posts/$', 'posts', name='bbs_posts'),
    url(r'^postsadd/$', 'postsadd', name='bbs_postsadd'),
    url(r'^postsdel/(?P<ID>\d+)/$', 'postsdel', name='bbs_postsdel'),
    url(r'^postsmanage/$', 'postsmanage', name='bbs_postsmanage'),
    
    url(r'^subpost/(?P<ID>\d+)/$', 'subpost', name='bbs_subpost'),
    url(r'^replys/(?P<ID>\d+)/$', 'replys', name='bbs_replys'),
    
    url(r'^login/$', 'login', name='bbs_login'),
    url(r'^logout/$', 'logout', name='bbs_logout'),
    
    url(r'^register/$', 'register', name='bbs_register'),
    url(r'^changepwd/$', 'changepwd', name='bbs_changepwd'),
    
    #url(r'^retrievepwd/$', 'retrievepwd', name='bbs_retrievepwd'),
        
)
