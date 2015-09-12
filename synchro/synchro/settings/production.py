from .base import *


DEBUG = True
#TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'synchroproject',
        'USER': 'synchrops',
        'PASSWORD': 'nuzansulfentalokfodvinvuldovahnok',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

SECRET_KEY = os.environ['IS_PRODUCTION']

try:
    from .local import *
except ImportError:
    pass
