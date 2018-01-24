"""
Django settings for mainproj project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$d@68n&#3#vra&64=(tjdfjz4rxska^w0!6^sueq)b45!*)bs%'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
# SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# CSRF_COOKIE_SECURE= True
SESSION_COOKIE_DOMAIN = None
# SESSION_COOKIE_SECURE= True

SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
SECURE_CONTENT_TYPE_NOSNIFF = True

CONN_MAX_AGE= None

# CSRF_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = [
]


# Application definition

INSTALLED_APPS = (
    #django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    'registration',
    'fontawesome',
    'profiles',
    #my apps
    'cali',
    'mainproj',
    'connect',
    # 'joins',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'mainproj.middleware.ReferMiddleware',
)
X_FRAME_OPTIONS = 'DENY'




ROOT_URLCONF = 'mainproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mainproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': 'califuse_startup',
        # 'USER': 'califuse_Ryan',
        # 'HOST': 'localhost',
        # 'PASSWORD': 'georgia23',
        # 'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
#This is a test 1
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHARE_URL = "http://127.0.0.1:8000/?ref="

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #'/var/www/static/',
]




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mainproj/media')

AUTH_PROFILE_MODULE = "mainproj.UserProfile"

CRISPY_TEMPLATE_PACK = 'bootstrap3'


#Django registration redux settings
ACCOUNT_ACTIVATION_DAYS = 365
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/' #Change to '/Profile/' to redirect login to profile page

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'my@gmail.com'
EMAIL_HOST_PASSWORD = 'my_emails_password'

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
#
# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.califuse.com'
# Email_HOST_USER = 'contact@califuse.com'
# EMAIL_HOST_PASSWORD = 'Georgia23'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = True
