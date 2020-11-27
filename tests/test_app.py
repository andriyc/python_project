import os
import sys
import unittest
import tests.tests_context

from app import project_properties


class AppTests(unittest.TestCase):
    @staticmethod
    def test_if_debug_mode():
        assert not project_properties.is_true('APP', 'DEBUG_MODE'), 'Deploy in debug mode is permitted!!!'


if __name__ == '__main__':
    unittest.main()
