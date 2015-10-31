# coding: utf-8
"""
Configure settings for the djangoapp
"""
import os


PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'geoip')
GEOIP_PATH = os.path.join(DATA_PATH, 'GeoIP.dat')
GEOIPV6_PATH = os.path.join(DATA_PATH, 'GeoIPv6.dat')
MIDDLEWARE_CLASSES = (
    'geoinfo',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_nose',
)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SECRET_KEY = 'This cannot be empty.'
