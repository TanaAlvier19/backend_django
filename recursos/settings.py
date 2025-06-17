from pathlib import Path
from corsheaders.defaults import default_headers
from datetime import timedelta
from cryptography.fernet import Fernet
import os

import dj_database_url
from django.conf import ENVIRONMENT_VARIABLE
FACIAL_ENCRYPTION_KEY = Fernet.generate_key()  # Guardar em variável de ambiente
FACE_RECOGNITION_TOLERANCE = 0.4
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']


SITE_NAME = "Test Django Next.js"

DOMAIN = 'localhost:3000'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_email',   # envio de OTP por e‑mail
    'app',
    'app1',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',

]
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dconggyoi',
    'API_KEY': '777815344477198',
    'API_SECRET': 'DdyMhcmHxMHQWwugPMQ9ckdiS1k',
}

# Configurações do Gmail

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tanaalvier@gmail.com'
EMAIL_HOST_PASSWORD = 'jxzz xpxs tdup nzuq'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'recursos.urls' 
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
    'Content-Type',
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# settings.py
CORS_ALLOW_CREDENTIALS = True
WSGI_APPLICATION = 'recursos.wsgi.application'
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}
    

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_PERMISSION_CLASSES':[
      'rest_framework.permissions.IsAuthenticated',

    ],
  
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
        'user': '100/hour',
    },
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your-secret-key',  # Substitua com sua chave secreta
    'AUTH_HEADER_TYPES': ('Bearer',),
}
# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "auth/password/reset-password-confirmation/?uid={uid}&token={token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {},
}
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
# https://docs.djangoproject.com/en/5.2/topics/i18n/
AUTH_USER_MODEL='app.Funcionario'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

CORS_ALLOW_ALL_ORIGINS = True
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE    = 'None'
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://avd-ydux.onrender.com']  # URL do frontend
REST_AUTH={
    'USE_JWT':True,
    'JWT_AUTH_COOKIE':'djangojwtauth_cookie',
    'JWT_AUTH_REFRESH_COOKIE':'djangojwtauth_refresh_cookie'
}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = "staticfiles"
# Para servir arquivos estáticos corretamente
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
