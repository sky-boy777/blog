import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ('SECRET_KEY')
SECRET_KEY = '@!sl@4-enq!9()7=$2&4v4fcrkvpw#j!^o7j)#glt-wei@zj9q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 调试模式
ALLOWED_HOSTS = ['*']  # 允许访问白名单，*代表全部
HOST_URL = 'http://127.0.0.1:8000'  # 邮箱激活主机名，或域名

# apps前导目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',                   # 全文检索框架
    'apps.blog_app',              # 博客模块
    'apps.user_app',              # 用户模块
    'apps.web_manage_app',        # 网站页面管理模块
    'apps.fun_time_app',          # 开心一刻模块
    'apps.movie_app',             # 电影模块
    'mdeditor',                   # 富文本
    'captcha',                    # 图像验证码
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

# 扩展auth_user
AUTH_USER_MODEL = 'user_app.UserModel'

# 全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',  # 搜索引擎
        'ENGINE': 'utils.haystack_analyzer.whoosh_cn_backend.WhooshEngine',  # 使用自定义whoosh_cn_backend
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),  # 索引文件路径
    }
}
# 数据变动时自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 默认每页条目
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 8

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# 缓存配置，使用redis做缓存,session缓存，https://pypi.org/project/django-redis/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # redis地址（无密码），后面表示使用第3个数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "1qaz@WSX",  # 或者这样设置密码
        }
    }
}
# session缓存配置
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


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
# 静态文件路径配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 用户上传文件路径配置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 部署上线的时候使用来收集静态文件
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 发送邮件配置
EMAIL_FROM = 'BYC账号激活<bycwql@163.com>'   # 收件人看到的发送者名称，没有默认是EMAIL_HOST_USER
EMAIL_HOST = 'smtp.163.com'  # smtp服务的邮箱服务器， 如果是 163 改成 smtp.163.com
EMAIL_HOST_USER = 'bycwql@163.com'  # 应用发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'xxx'  # 开启SMTP后的客户端授权码
EMAIL_USE_SSL = True
EMAIL_PORT = 465  # SMTP端口需要SSL

# 图像验证码配置
CAPTCHA_FONT_SIZE = 42  # 字体大小（默认22）
CAPTCHA_IMAGE_SIZE = (150, 43)  # 图片大小（宽高）
CAPTCHA_TIMEOUT = 5  # 有效时间5分钟
CAPTCHA_LENGTH = 4  # 验证码上面的字符个数
CAPTCHA_OUTPUT_FORMAT = u'%(image)s %(hidden_field)s %(text_field)s'  # 输出格式
CAPTCHA_NOISE_FUNCTIONS = (
                            'captcha.helpers.noise_arcs',  # 弧线
                            'captcha.helpers.noise_dots',  #
                            'captcha.helpers.noise_null',  # 无
                           )   # 干扰的东西
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 随机字符串

# 分页配置
NUM_PAGES = 20  # 分页默认条目数
MOVIE_NUM_PAGES = 8  # 电影每页8条

# 默认密码
DEFAULT_PASSWORD = 'byc1234'




