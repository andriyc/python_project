import unittest
from app import app


def test_app():
    assert app.index() == 'CD to DEV is working well !!!'

