import glob
import os
import pep8
from pylint import epylint as lint
import unittest


class TestCodeFormat(unittest.TestCase):

    def test_pylint(self):
        # root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
        # lint(root)
        # lint.py_run('/home/stv/src/edx/django-openedx-geoinfo/geoinfo/', True)
        # lint.py_run(
        #     '/Users/stv/src/edx/openedx-django-middleware-geoinfo/geoinfo/*',
        #     True,
        # )
        args = [
            os.path.join(__file__, os.pardir, os.pardir),
        ]
        targets = [os.path.abspath(arg) for arg in args]

        for target in targets:
            if not os.path.exists(target):
                try:
                    # Is target a module?
                    x = __import__(args[0], locals(), globals(), [], -1)
                    target = sys.modules[args[0]].__path__[0]
                except:
                    pass

            if not os.path.exists(target):
                raise parser.error(
                    "The specified target (%r) does not exist" \
                        % target
                )

            path = target
            while True:
                flag = False
                for django_file in ('manage.py', 'models.py', 'urls.py'):
                    if os.path.exists(os.path.join(path, django_file)):
                        sys.path.insert(0, os.path.dirname(path))
                        flag = True
                        break
                if flag:
                    break

                path = os.path.dirname(path)

                if path == '/':
                    raise parser.error(
                        "The specified target (%r) does not appear to be part of a " \
                        "Django application" % target
                    )

        try:
            import django
        except ImportError:
            print >>sys.stderr, "E: Cannot import `django' module, exiting.."
            return 1

        linter = lint.PyLinter()
        # linter.set_option('reports', options.report)
        # linter.set_option('output-format', options.outputformat)

        # if options.pylint:
        #     checkers.initialize(linter)
        #     for msg in ('C0111', 'C0301'):
        #         linter.disable(msg)

        # AstCheckers.register(linter)

        # if options.errors:
        #    linter.set_option('disable-msg-cat', 'WCRI')
        #    linter.set_option('reports', False)
        #    linter.set_option('persistent', False)

        linter.check(targets)

        return linter.msg_status

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
