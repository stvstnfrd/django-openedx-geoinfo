# coding: utf-8
"""
Setup package
"""
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand

_version = '1.0.0'
with open('README.markdown') as file_input:
    readme = file_input.read()


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

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
    download_url='https://github.com/stvstnfrd/django-openedx-geoinfo/tarball/release/version/' + _version,
    # Packages
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={
        '': 'src',
        'geoinfo': 'src/geoinfo',
    },
    install_requires=[
        # geoinfo
        'django>=1.4',
        'django-ipware==1.1.0',
        'logging',
        'pygeoip',
        # Test dependencies installed as tests are included inside the
        # packages. This enables you to monkey-patch the library and its
        # tests, instead of forking the entire package.
        'coverage',
        'django-nose>=1.4',
        'mock==1.0.1',
        'tox',
    ],
    tests_require=[
    ],
    cmdclass={
        'test': Tox,
    },
)
