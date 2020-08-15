"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@!sl@4-enq!9()7=$2&4v4fcrkvpw#j!^o7j)#glt-wei@zj9q'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发模式为True，上线后改为False
DEBUG = True

ALLOWED_HOSTS = ['*']

# 账号激活链接主机名，将来换成域名
HOST_URL = 'http://127.0.0.1:8000'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册app
    'blog_app',
    # 富文本
    'mdeditor',
    # 图形验证码
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 加载模板文件
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',  # 数据库名字
        'USER': 'root',  # 用户名
        'PASSWORD': 'root',  # 密码
        'HOST': '127.0.0.1',  # 数据库地址
        'PORT': 3306,  # 端口号
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 改成False，使数据库时间跟本地时间一样（默认是格林尼治时间）
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# 静态文件路径（css，js）
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 部署上线的时候使用来收集静态文件
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 发送邮件
EMAIL_FROM = 'BYC账号激活<bycwql@163.com>'   # 收件人看到的发送者名称，没有默认是EMAIL_HOST_USER
# 必须
EMAIL_HOST = 'smtp.163.com'  # smtp服务的邮箱服务器， 如果是 163 改成 smtp.163.com
EMAIL_HOST_USER = 'bycwql@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'JBRHBAFRQNGZTPHP'  # 开启SMTP后的客户端授权码
# EMAIL_PORT = 465

# 缓存，不配置默认使用本地内存缓存
# 数据库缓存配置，然后python manage.py createcachetable生成缓存表
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 缓存表的名字
        'LOCATION': 'blog_cache_table'
    }
}
# redis做缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',  # redis地址（无密码），后面表示使用第二个数据库
#         # 'LOCATION': 'redis://密码@192.168.1.101:6379/2',  # redis地址（有密码），后面表示使用第二个数据库
#     }
# }

# 富文本图片上传的位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

# 图像验证码配置
CAPTCHA_FONT_SIZE = 22  # 字体大小（默认22）
CAPTCHA_IMAGE_SIZE = (80, 30)  # 图片大小（宽高）
CAPTCHA_TIMEOUT = 5  # 每一分钟生成一个验证码
CAPTCHA_LENGTH = 4  # 验证码上面的字符个数
CAPTCHA_OUTPUT_FORMAT = u'%(image)s %(hidden_field)s %(text_field)s'  # 输出格式
CAPTCHA_NOISE_FUNCTIONS = (
                            # 'captcha.helpers.noise_arcs',  # 弧线
                           'captcha.helpers.noise_dots',  #
                            'captcha.helpers.noise_null',  # 无
                           )   # 干扰的东西
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 随机字符串


