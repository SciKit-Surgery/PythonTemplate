# coding=utf-8

"""Hello world tests"""

from unittest import TestCase

from {{ cookiecutter.pkg_name }}.ui.hello_world import hello_world


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        hello_world()
