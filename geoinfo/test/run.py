#!/usr/bin/env python
# coding: utf-8
"""
Run Django Test with Python setuptools test command
REFERENCE:
    http://gremu.net/blog/2010/enable-setuppy-test-your-django-apps/
"""
import os
import sys


def run_tests():
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'geoinfo.settings'
    if hasattr(django, 'setup'):
        django.setup()
    from django.conf import settings
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner(
        verbosity=1,
        interactive=False,
        failfast=False,
    )
    failures = test_runner.run_tests([])
    sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()
