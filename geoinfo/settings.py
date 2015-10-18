import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_nose',
)

MIDDLEWARE_CLASSES = (
    'geoinfo',
)

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'geoip')
GEOIP_PATH = os.path.join(DATA_PATH, 'GeoIP.dat')
GEOIPV6_PATH = os.path.join(DATA_PATH, 'GeoIPv6.dat')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
