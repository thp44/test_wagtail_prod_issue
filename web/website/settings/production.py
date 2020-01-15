from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*uk2h3w0r4wy1gsx(xpy62#tf3mfe41(*!y4ztuat#0kk3@g$(' #os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'NO').lower() in ('on', 'true', 'y', 'yes')

# TODO FIX ALLOWED HOST TO IP
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
