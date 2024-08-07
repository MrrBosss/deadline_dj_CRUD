from .settings import *
from .settings import env

DEBUG=True

MEDIA_ROOT = "/var/www/deadline.itlink.uz/media"
STATIC_ROOT = "/var/www/deadline.itlink.uz/static"
SPECTACULAR_SETTINGS["SERVERS"] = [  # noqa: F405
    {"url": "https://deadline.itlink.uz", "description": "Deadline server"},
]
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["deadline.itlink.uz"])
MEDIA_URL="/media/"
