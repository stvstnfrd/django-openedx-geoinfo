#!/usr/bin/env python
# coding: utf-8
"""
Run Django Test with Python setuptools test command
REFERENCE:
    http://gremu.net/blog/2010/enable-setuppy-test-your-django-apps/
"""
import os
import sys


def run_tests(apps=None, verbosity=1, interactive=False):
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'geoinfo.settings'
    if django.VERSION >= (1, 7):
        django.setup()
    from django.conf import settings
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner(
        verbosity=verbosity,
        interactive=interactive,
        failfast=False,
    )
    if apps:
        app_tests = [x.strip() for x in apps if x]
    else:
        app_tests = [
            'geoinfo',
        ]
    failures = test_runner.run_tests(app_tests)
    sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()
