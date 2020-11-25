import unittest
import app


def test_app():
    assert app.index() == 'CI/CD to DEV is working well !!! Powered by Jenkins!!!'

