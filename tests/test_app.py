import unittest
import app

class AppTestClass(unittest.TestCase):
    def test_app(self):
        assert app.index() == 'CD to DEV is working well !!!'