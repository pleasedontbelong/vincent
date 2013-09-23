from .base import *

SESSION_COOKIE_NAME = 'b_sessionid'

RAVEN_CONFIG = {
    'dsn': 'http://57492f38501440048d5db984779a5359:ff4dae3ee12044afae6a02dd30026181@logging.sem.io/20'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

PARENT_HOST = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
