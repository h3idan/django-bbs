# Django settings for bbs project.
# coding:utf-8

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bbs',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'heidan',                  # Not used with sqlite3.
        'HOST':'',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT':'',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../media').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static').replace('\\', '/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),  
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ), 
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ), 
    ('bootstrap',os.path.join(STATIC_ROOT,'bootstrap').replace('\\','/') ), 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '71g6oak=dt+oy9d^^e3n=d_jscl38x$9-@=n!g-_-%9aq_n7t!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bbs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bbs.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../../templates').replace('\\', '/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forum',
    'DjangoUeditor',
    
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


""" ckeditor的设置情况 """
CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), '../../media/ckeditor_up').replace('\\', '/')
CKEDITOR_RESTIRCT_BY_USER = True
#CKEDITOR_UPLOAD_PREFIX = "http://localhost:8080/media/ckeditor_up"                 # 设定media_url 
CKEDITOR_CONFIGS = {
        "default": {
            'toolbar': 'Full',
            'height': 300,
            'width': 850
            },
        "ckeditor_test": {
            'toolbar': 'Basic',
            'uiColor': '#9AB8F3',
            'height': 300,
            'width': 300
            }
        }


""" ueditor 设置情况 """
UEDITOR_SETTINGS={
        "toolbars": {           #定义多个工具栏显示的按钮，允行定义多个
            "name1": [[ 'source', '|','bold', 'italic', 'underline']],
            "name2": []
        },
        "images_upload": {
            "allow_type": "jpg,png",                            #定义允许的上传的图片类型
            "path": "ueditor_up/image_up",                 #定义默认的上传路径
            "max_size": "5000kb"                                #定义允许上传的图片大小, 不可以设置为0
        },
        "files_upload": {
            "allow_type": "zip,rar",   #定义允许的上传的文件类型
            "path": "ueditor_up/file_up",                   #定义默认的上传路径
            "max_size": "5000kb"       #定义允许上传的文件大小，不可以设置为0
        },
        "image_manager": {
            "path": ""         #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
        },
        "scrawl_upload": {
            "path":""           #涂鸦图片默认的上传路径
        }
    }
