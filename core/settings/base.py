import os
import dj_database_url
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY',)

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'rolepermissions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'secret',
    'jobs',
    'django_icons',
    'tailwind',
    'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DATABASE_URL = config('POSTGRES_DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    # fallback para desenvolvimento local (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'jobs.Enterprise'

DJANGO_ICONS = {
    "ICONS": {
        "login": {"name": "fa-duotone fa-solid fa-right-to-bracket"},
        "logout": {"name": "fa-solid fa-arrow-right-from-bracket"},
        "delete": {"name": "fa-solid fa-trash"},
        "edit": {"name": "fa-solid fa-pen-to-square"},
        "home": {"name": "fa-solid fa-house"},
        "happy": {"name": "fa-regular fa-face-smile-beam"},
        "arow_right": {"name": "fa-solid fa-right-long"},
        "arow_left": {"name": "fa-solid fa-left-long"},
        "plus": {"name": "fa-solid fa-plus"},
        "eye": {"name": "fa-solid fa-eye"},
    },
}

ROLEPERMISSIONS_MODULE = "core.roles"

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1",]
