"""
Django settings for mointaineer project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from mountaineer.core.utils import settings as utils


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_MODULE = os.path.dirname(os.path.abspath(__file__))
CORE_MODULE = os.path.dirname(SETTINGS_MODULE)

# These last three are mostly useful for development
MODULE_ROOT = os.path.dirname(CORE_MODULE)
BASE_DIR = MODULE_ROOT
PROJECT_ROOT = os.path.dirname(MODULE_ROOT)
HOME = utils.get_env('HOME')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = utils.get_env('MNTNR_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'mountaineer.core',
    'rest_framework',
    'rest_framework_swagger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mountaineer.core.urls.root'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mountaineer.core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mountaineer',
        'USER': utils.get_env('MNTNR_POSTGRES_USER'),
        'PASSWORD': utils.get_env('MNTNR_POSTGRES_PASSWORD'),
        'HOST': utils.get_env('MNTNR_POSTGRES_HOST'),
        'PORT': utils.get_env('MNTNR_POSTGRES_PORT')
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(HOME, 'var', 'mountaineer', 'media')
STATIC_ROOT = os.path.join(HOME, 'share', 'mountaineer', 'static')

LOG_DIR = utils.get_log_dir()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
      'verbose': {
          'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
          'datefmt' : "%d/%b/%Y %H:%M:%S"
      },
      'simple': {
          'format': '%(levelname)s %(message)s'
      },
    },
    'handlers': {
      'file': {
          'level': 'DEBUG',
          'class': 'logging.handlers.RotatingFileHandler',
          'filename': os.path.join(LOG_DIR, 'mountaineer.log'),
          'maxBytes': 1024 * 1024 * 5,  # 5MiB
          'backupCount': 5,
          'formatter': 'verbose'
      },
    },
    'loggers': {
      'django': {
          'handlers': ['file'],
          'propagate': True,
          'level': 'DEBUG',
      },
      'mountaineer': {
          'handlers': ['file'],
          'level': 'DEBUG',
      },
    }
}

CORS_ORIGIN_WHITELIST = [
    'localhost:3000',
]