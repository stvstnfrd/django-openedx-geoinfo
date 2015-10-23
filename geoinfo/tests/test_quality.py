# coding: utf-8
import glob
import os
import sys
import unittest

import pep8
import pyflakes.scripts.pyflakes as flakes


class TestCodeFormat(unittest.TestCase):

    def test_pyflakes(self):
        root = os.path.join(__file__, os.pardir)
        path = os.path.abspath(os.path.sep.join([
            __file__,
            os.pardir,
            os.pardir,
            os.pardir,
            '**',
            '*.py'
        ]))
        modules = ['geoinfo']
        dirs = (os.path.join(*d) for d in (m.split('.') for m in modules))
        warns = 0
        for dir in dirs:
            for filename in os.listdir(dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    warns += flakes.checkPath(os.path.join(dir, filename))
        if warns > 0:
            print(
                "Audit finished with total %d warnings" % warns
            )  # pragma: no cover
            raise Exception(warns)  # pragma: no cover

    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide()
        root = os.path.join(__file__, os.pardir)
        path = os.path.abspath(os.path.sep.join([
            __file__,
            os.pardir,
            os.pardir,
            '**',
            '*.py'
        ]))
        files = glob.glob(path)
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors,
            0,
            'Found code style errors (and warnings).',
        )
