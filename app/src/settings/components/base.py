from typing import Tuple

from decouple import Csv

from src.settings.components import config, BASE_DIR

SECRET_KEY = config('SECRET_KEY')

DEBUG = config("DEBUG", False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default=config('DOMAIN'))

DJANGO_APPS: Tuple[str, ...] = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',  # for robots
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

PROJECT_APPS: Tuple[str, ...] = (
    'apps.account.apps.AccountConfig',
    'apps.core.apps.CoreConfig',
    'apps.balance.apps.BalanceConfig',
)

THIRD_PARTY_APPS: Tuple[str, ...] = (
    'corsheaders',
    'bootstrap5',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE: Tuple[str, ...] = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'src.urls'

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT", cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    }
}

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        BASE_DIR.joinpath('templates')
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'apps.core.context_processors.global_context',
        ],
    },
}]

WSGI_APPLICATION = 'src.wsgi.application'
# Channels
# ASGI_APPLICATION = 'src.asgi.application'


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

AUTH_USER_MODEL = 'account.Account'
AUTHENTICATION_BACKENDS = (

    "django.contrib.auth.backends.ModelBackend",
)

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')  # сбор всей статики в одну директорию для вебсервера nginx
STATICFILES_DIRS = [
    BASE_DIR.joinpath("static"),  # указываем где еще может находиться статика помимо app/static/app/css/example.css
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

SITE_ID = 1  # for robots

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PROJECT_NAME = config('PROJECT_NAME')

# REDIS_HOST = config("REDIS_HOST")
# REDIS_PORT = config("REDIS_PORT", cast=int, default=6379)

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
