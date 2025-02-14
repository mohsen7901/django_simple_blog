
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='test')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
COMPRESS_ENABLED = config('COMPRESS_ENABLED', default=False, cast=bool)

if DEBUG:
    ALLOWED_HOSTS = [
    '127.0.0.1'
    ]
else:
    ALLOWED_HOSTS = ['*']


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE', default = 'django.db.backends.mysql'),
            'NAME': config('DB_NAME', default = 'db.myqsl'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE', default= 'django.db.backends.mysql'),
            'NAME': config('DB_NAME', default= 'db.myqsl'),
            'USER': config('DB_USER', default= 'username'),
            'PASSWORD': config('DB_PASSWORD', default = 'password'),
            'HOST': config('DB_HOST', default= 'localhost'),
            'PORT': config('DB_PORT', default= '3306'),
            "OPTIONS": {
                'init_command': config('DB_INIT_COMMAND')
            },
        }
    }

# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'blog',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'debug_toolbar',
    'django_summernote',
    'captcha',
    'accounts',
    'django.contrib.humanize',
    'compressor',
]

if COMPRESS_ENABLED:
    INSTALLED_APPS += 'AppDirectoriesFinder'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Iran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_ROOT = BASE_DIR / 'media'
    STATICFILES_DIRS = [
        BASE_DIR / "statics",
    ]
else:
    STATIC_ROOT = "/home/mfathali/static"
    MEDIA_ROOT = "/home/mfathali/media"
    STATICFILES_DIRS = [
        BASE_DIR / "statics",
        BASE_DIR / "static",
    ]

if COMPRESS_ENABLED:
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        'compressor.finders.CompressorFinder'
    )

# Sites
if DEBUG:
    SITE_ID = 2
else:
    SITE_ID = 3


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


INTERNAL_IPS = [
    "127.0.0.1",
]

# Summernote configs
SUMMERNOTE_THEME = 'bs4'

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        # 'width': '100%',
        'height': '480px',

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    }
}

# Captcha configs
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTHENTICATION_BACKENDS = ['accounts.backends.EmailOrUsernameModelBackend']

# email configs
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default='True')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# robots
ROBOTS_USE_HOST = config('ROBOTS_USE_HOST', default=True, cast=bool)
ROBOTS_USE_SITEMAP = config('ROBOTS_USE_SITEMAP', default=True, cast=bool)

# show admin page
ADMIN_ENABLED = config('ADMIN_ENABLED', default=False, cast=bool)
