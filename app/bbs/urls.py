from django.conf.urls import patterns, include, url
import os
from bbs import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^bbs/', include('bbs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    
    url(r'^$', 'forum.views.index'),
    url(r'^bbs/', include('forum.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

)


urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)


urlpatterns += patterns('',

    url(r'^css/(?P<path>.*)','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__), './templates/css').replace('\\', '/')}),
    url(r'^js/(?P<path>.*)','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__), './templates/js').replace('\\', '/')}),
    url(r'^images/(?P<path>.*)','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__), './templates/images').replace('\\', '/')}),

        
)



