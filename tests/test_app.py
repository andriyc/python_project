import os
import sys
import unittest
from tests import context
import app
from app import project_properties


class AppTests(unittest.TestCase):
    @staticmethod
    def test_if_debug_mode():
        assert not project_properties.is_true('APP', 'DEBUG_MODE'), 'Deploy in debug mode is permitted!!!'


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    unittest.main()
