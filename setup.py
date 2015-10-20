from setuptools import setup

_version = '1.0.0'
with open('README.markdown') as file_input:
    readme = file_input.read()

setup(
    # Metadata
    name='django-openedx-geoinfo',
    version=_version,
    license='AGPL-3.0',
    description='TODO: Short description',
    long_description=readme,
    author='stv',
    author_email='stv@stanford.edu',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Framework :: Django :: 1.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],

    # URLs
    url='https://github.com/stvstnfrd/django-openedx-geoinfo',
    download_url='https://github.com/stvstnfrd/django-openedx-geoinfo/tarball/release/v/' + _version,

    # Packages
    packages=[
        'geoinfo',
        'geoinfo.tests',
    ],
    install_requires=[
        'django==1.4.22',
        'django-ipware==1.1.0',
        'logging',
        'pygeoip',
    ],
    tests_require=[
        'coverage',
        'django-nose',
        'mock==1.0.1',
        'pep8',
        'pyflakes',
    ],
    test_suite='geoinfo.tests.run.run_tests',

    # Distribution
    package_dir={
        'geoinfo': 'geoinfo',
    },
    package_data={
        'geoinfo': [
            'data/geoip/*.dat',
        ],
    },
)
