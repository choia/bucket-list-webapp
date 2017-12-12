from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

# Be sure to update this to proper host URL!
ALLOWED_HOSTS = ['*',]

INSTALLED_APPS += ['storages', ]