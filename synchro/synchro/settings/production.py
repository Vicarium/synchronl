from .base import *


#DEBUG = False
#TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
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
