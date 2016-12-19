"""
Django settings for gigfinder project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# pylint: disable=unused-import
import authentication
import dj_database_url

LOGIN_REDIRECT_URL = 'home'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'authentication/templates/')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lmdwqn_&9$rn_m)x_khxf%8e5l1gng_^kw9p_zua0o+la#e-1&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1',
                 'pitchccny.herokuapp.com', 'gig-webdev-proj.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'authentication',
    'board.apps.BoardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'floppyforms',
    'django_nose',
    'address',
    'django_s3_storage',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'middleware.DisableCSRF',
)

ROOT_URLCONF = 'gigfinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, "templates", ],
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

WSGI_APPLICATION = 'gigfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# pylint: disable=invalid-name
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# import dj_database_url
# DATABASES['default'] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=authentication,board',
    ]

MEDIA_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), 'media')
MEDIA_URL = '/media/'

#AUTH_PROFILE_MODULE = authentication.UserProfile
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"

# The region to connect to when storing files.
AWS_REGION = "us-east-1"

# The AWS access key used to access the storage buckets.
AWS_ACCESS_KEY_ID = "AKIAIDRNTMEYP4FQCOYA"

# The AWS secret access key used to access the storage buckets.
AWS_SECRET_ACCESS_KEY = "0cQASmEcloAUJAtiL3GXyzt9afbgIsUBz3Yh3nLn"

# The S3 bucket used to store uploaded files.
AWS_S3_BUCKET_NAME = "python-direct-upload"

# The S3 calling format to use to connect to the bucket.
AWS_S3_CALLING_FORMAT = "boto.s3.connection.OrdinaryCallingFormat"

# The host to connect to (only needed if you are using a non-AWS host)
AWS_S3_HOST = ""

# A prefix to add to the start of all uploaded files.
AWS_S3_KEY_PREFIX = ""

# Whether to enable querystring authentication for uploaded files.
AWS_S3_BUCKET_AUTH = True

# The expire time used to access uploaded files.
AWS_S3_MAX_AGE_SECONDS = 60*60  # 1 hour.

# A custom URL prefix to use for public-facing URLs for uploaded files.
AWS_S3_PUBLIC_URL = ""

# Whether to set the storage class of uploaded files to REDUCED_REDUNDANCY.
AWS_S3_REDUCED_REDUNDANCY = False

# A dictionary of additional metadata to set on the uploaded files.
# If the value is a callable, it will be called with the path of the file on S3.
AWS_S3_METADATA = {}

# Whether to enable gzip compression for uploaded files.
AWS_S3_GZIP = True

# The S3 bucket used to store static files.
AWS_S3_BUCKET_NAME_STATIC = ""

# The S3 calling format to use to connect to the static bucket.
AWS_S3_CALLING_FORMAT_STATIC = "boto.s3.connection.OrdinaryCallingFormat"

# The host to connect to for static files (only needed if you are using a non-AWS host)
AWS_S3_HOST_STATIC = ""

# Whether to enable querystring authentication for static files.
AWS_S3_BUCKET_AUTH_STATIC = False

# A prefix to add to the start of all static files.
AWS_S3_KEY_PREFIX_STATIC = ""

# The expire time used to access static files.
AWS_S3_MAX_AGE_SECONDS_STATIC = 60*60*24*365  # 1 year.

# A custom URL prefix to use for public-facing URLs for static files.
AWS_S3_PUBLIC_URL_STATIC = ""

# Whether to set the storage class of static files to REDUCED_REDUNDANCY.
AWS_S3_REDUCED_REDUNDANCY_STATIC = False

# A dictionary of additional metadata to set on the static files.
# If the value is a callable, it will be called with the path of the file on S3.
AWS_S3_METADATA_STATIC = {}

# Whether to enable gzip compression for static files.
AWS_S3_GZIP_STATIC = True
