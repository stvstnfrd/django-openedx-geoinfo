#!/usr/bin/env python
"""
Manage.py file for XBlock
"""
import os
import sys

from django.core.management import execute_from_command_line

PROJECT_ROOT = os.path.dirname(__file__)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoinfo.settings')
    sys.path.insert(0, PROJECT_ROOT)
    execute_from_command_line(sys.argv)
