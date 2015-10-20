import glob
import os
import pep8
import unittest


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
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
