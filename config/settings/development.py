from .base import *

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.str("DEBUG")

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", default='').split(" ")

LOCAL_APPS = [

]

THIRD_PARTY_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


def get_type_databases(type_db: str = 'postgres') -> tuple:
    databases = {
        'postgres': {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': env.str("DB_NAME", default='postgres'),
                'USER': env.str("DB_USER", default='postgres'),
                'PASSWORD': env.str("DB_PASSWORD", default='postgres'),
                'HOST': env.str("DB_HOST", default='localhost'),
                'PORT': env.str("DB_PORT", default=5432),
            }
        },
        'sqlite': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    }
    return databases[type_db]


DATABASES = get_type_databases()
