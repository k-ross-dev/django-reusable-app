# coding=utf-8

from django.conf import settings

# This is an example
DJANGO_REUSABLE_APP_SECRET = settings.SECRET_KEY[::4]
