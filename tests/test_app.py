import unittest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app


def test_app():
    assert app.index() == 'CI/CD to DEV is working well !!! Powered by Jenkins!!!'
