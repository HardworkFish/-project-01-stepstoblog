
"""
Django settings for eden_cats_blog project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=0dnupswsjy%ip$4f4&$02-e7uh-9+w595dsc@r$0v9)i)y298'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True
# ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = [
#     '127.0.0.1',  # Allow domain and subdomains
#     'localhost',  # Also allow FQDN and subdomains
# ]
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.blog',  # blog 应用
    # 'django_summernote',  # 富文本应用
    'haystack',  # 搜索应用
    'mdeditor',  # Markdown 应用
    # 'mptt',  # 树存储结构目录应用
    'ckeditor',
    'ckeditor_uploader',
    'mptt',
    'apps.easy_comment',
    'notifications',
    'apps.online_status',
    # 'django.contrib.auth',
    'django.contrib.sites',
    'allauth', # 用户注册与登录
    'allauth.account', # 用户注册与登录
    'allauth.socialaccount', # 用户注册与登录

    # 下面是第三方账号相关的，比如weibo和github
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.gitlab',
    'crispy_forms',
    'imagekit',
    'apps.message',
]
# 使用bootstrap3的样式，前端需要引入相应的css
CRISPY_TEMPLATE_PACK = 'bootstrap3'




# django-allauth相关设置
AUTHENTICATION_BACKENDS = (
# django admin所使用的用户登录与django-allauth无关
    'django.contrib.auth.backends.ModelBackend',

# `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 前面我们app里添加了django.contrib.sites,需要设置SITE_ID
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/'

# 默认情况下不发邮件通知,开启邮件通知功能后，只有当用户不在线的情况下，才会发邮件。
SEND_NOTIFICATION_EMAIL = False  # 不开启邮件通知
# Email setting
# SMTP服务器，使用sendclound的服务
EMAIL_HOST = 'smtp587.sendcloud.net'
EMAIL_HOST_USER = 'TRsky_STMP_Mail'
EMAIL_HOST_PASSWORD = '*********'
EMAIL_PORT = 587

# 是否使用了SSL 或者TLS
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = True
# 默认发件人，默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = 'TRsky <noreply@mail.trskycooik.com>'


COMMENT_ENTRY_MODEL = 'blog.article' # 格式是 app_name+model_name
AUTH_USER_MODEL = 'blog.User'     # 格式是 app_name+model_name
ADMINS = (('TRsky', '625310581@qq.com'),)  # 网站管理员


# 邮件通知
# SEND_NOTIFICATION_EMAIL = True   # 开启邮件通知
# SMTP设置
# EMAIL_HOST = ''
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT =
# EMAIL_USE_SSL =


#ckeditor setup
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        # 编辑器的宽高请根据你的页面自行设置
        'width': '1030px',
        'height': '150px',
        'image_previewText': ' ',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Format', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Blockquote', 'CodeSnippet'],
            ['Image', 'Link', 'Unlink'],
        ],
        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'prism', 'widget', 'lineutils', ]),
    }
}
# 不允许非图片文件上传，默认为True
CKEDITOR_ALLOW_NONIMAGE_FILES = False
# 限制用户查看上传图片的权限， 只能看自己传的图片
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_RESTRICT_BY_DATE = True
# 在编辑器里浏览上传的图片时，图片会以路径分组，日期排序
CKEDITOR_BROWSE_SHOW_DIRS = True


# 搜索
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 主题
JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# 静态文件放置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'apps.online_status.middleware.OnlineStatusMiddleware',
]

# USER_ONLINE_TIMEOUT = 600

ROOT_URLCONF = 'eden_cats_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eden_cats_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edencatsdb',
        'USER': 'root',
        'PASSWORD': 'mymysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

PAGE_NUM = 3  # 每页显示 3 篇文章

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = 'static'  # debug=False
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     os.path.join(BASE_DIR, "recommend", "static"),
# ]

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

# 纯文本设置为富文本

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 富文本编辑器设置
# SUMMERNOTE_CONFIG = {
#     Using SummernoteWidget - iframe mode
    # 'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    # 'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # 'styleWithSpan': False,

    # Change editor size
    # 'width': '80%',
    # 'height': '480',
    #
    # Use proper language setting automatically (default)
    # 'lang': 'zh-CN',

    # }

# Markdown django-mdeditor
# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_URL = '/media/'


# Markdown 语法设置
MDEDITOR_CONFIGS = {
    'default': {
        'width': '90%',
        'heigth': 1000,  # markdown 编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase",
                    "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code",
                    "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],
        'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF",
                                 "png", "PNG", "bmp", "BMP", "webp", "WEBP"],
        'image_floder': 'editor',
        'theme': 'default',  # dark / default
        'preview_theme': 'default',  # dark / default
        'editor_theme': 'default',  # pastel-on-dark / default
        'toolbar_autofixed': True,
        'search_replace': True,
        'emoji': True,
        'tex': True,
        'flow_chart': True,
        'sequence': True
    }
}