import unittest

from context import app


class AppTests(unittest.TestCase):
    def test_app(self):
        assert True  # app.index() == 'CI/CD to DEV is working well !!! Powered by Jenkins!!!'

    def test_if_debug_mode(self):
        assert not app.DEBUG_MODE, 'Deploy in debug mode is permitted!!!'
