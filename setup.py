from setuptools import setup


setup(
    name='django-openedx-geoinfo',
    version='1.0.0',
    description='TODO: Short description',
    long_description='TODO: Long description',
    author='stv',
    author_email='stv@stanford.edu',
    url='https://github.com/Stanford-Online/django-openedx-geoinfo',
    license='AGPL-3.0',
    packages=[
        'geoinfo',
    ],
    install_requires=[
        'django==1.4.22',
        'django-ipware==1.1.0',
        'django-nose',
        'logging',
        'mock==1.0.1',
        'pygeoip',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
