"""
Django settings for BoardSetting project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import load_dotenv, find_dotenv  # Переменная окружения для хранения токенов

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

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

    # Список пользовательских приложений, создается разработчиком
    # Плоские страницы
    'django.contrib.sites',  # Косвенно влияет на работу flatpages и allauth
    'django.contrib.flatpages',  # Плоская страница - это объект с URL, заголовком и содержанием. Используется для
    # одноразовых, специальных страниц, таких как страницы «About» или «Privacy Policy», которые хранятся в базе
    # данных, но для которых не надо разрабатывать собственное приложение Django
    'fpages',  # Приложение добавляющее во flatpages возможность включения комментариев
    'ckeditor',
    'ckeditor_uploader',
    'django_filters',  # Приложение для подключения фильтров
    'bootstrap4',

    # Подключение приложений из "allauth"
    'allauth',  # Обязательное приложение allauth
    'allauth.account',  # Обязательное приложение allauth
    'allauth.socialaccount',  # Обязательное приложение allauth
    'allauth.socialaccount.providers.yandex',  # Необходимо для реализации регистрации через провайдер "Yandex"

    'BoardApp.apps.BoardappConfig',  # Основное приложение сайта
    'accounts.apps.AccountsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Список пользовательских middleware, создается разработчиком
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',  # Middleware для работы с flatpages
]

SITE_ID = 1  # Идентификатор (целое число) текущего сайта в таблице базы данных django_site. Может использоваться
# приложениями для связывания своих данных с определенными сайтами и, таким образом, для управления контентом
# нескольких сайтов в единой базе данных. Влияет на работу flatpages
SITE_URL = 'http://127.0.0.1:8000'

ROOT_URLCONF = 'BoardSetting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'accounts', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',  # контекстный процессор, нужен для allauth.
            ],
        },
    },
]

# Добавляем бэкенды аутентификации:
AUTHENTICATION_BACKENDS = [
    # Необходимо войти в систему под именем пользователя в админке Django, независимо от `allauth`:
    'django.contrib.auth.backends.ModelBackend',  # Встроенный бэкенд Django, реализующий аутентификацию по username
    # Специальные методы аутентификации `allauth`, такие, как вход по электронной почте:
    'allauth.account.auth_backends.AuthenticationBackend',  # Бэкенд аутентификации, предоставленный пакетом allauth:
    # нам нужно «включить» аутентификацию как по username, так и специфичную по email или сервис-провайдеру.
]

WSGI_APPLICATION = 'BoardSetting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Настройка STATICFILES_DIRS указывает каталоги, которые проверяются на наличие статических файлов.
STATICFILES_DIRS = []

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'height': 600,
        'toolbar': 'Custom',
        'extraPlugins': ','.join([
            'codesnippet',
            # 'youtube'
        ]),
        'toolbar_Custom': [
            [
                'Bold',
                'Italic',
                'Underline'
            ],
            [
                'Font',
                'FontSize',
                'TextColor',
                'BGColor'
            ],
            [
                'NumberedList',
                'BulletedList',
                '-',
                'Outdent',
                'Indent',
                '-',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock'
            ],
            [
                'Link',
                'Unlink'
            ],
            [
                'RemoveFormat',
                'Source',
                'CodeSnippet',
                'Image',
                'Youtube'
            ]
        ],

    },

}

CKEDITOR_UPLOAD_PATH = 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/accounts/profile"
LOGOUT_REDIRECT_URL = reverse_lazy('board_list')

ACCOUNT_EMAIL_REQUIRED = True  # Регистрация по электронной почте обязательно
ACCOUNT_UNIQUE_EMAIL = True  # Регистрация по уникальной электронной почте
ACCOUNT_USERNAME_REQUIRED = True  # Регистрация по username обязательна
ACCOUNT_AUTHENTICATION_METHOD = 'username'  # Аутентификация по username
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Не пускать пользователя на сайт до момента подтверждения почты;
# optional — сообщение о подтверждении почты будет отправлено, но пользователь может
# залогиниться на сайте без подтверждения почты;
# 'none' Верификация электронной почты отсутствует
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # Позволит избежать дополнительного входа и активирует аккаунт сразу, как только
# мы перейдём по ссылке
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3  # Хранит количество дней, когда доступна ссылка на подтверждение
# регистрации.

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

EMAIL_SUBJECT_PREFIX = 'Hello!'
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'