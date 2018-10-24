# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo

# Unittest style test case
from unittest import TestCase

class Test{{ cookiecutter.pkg_name }}(TestCase):
    def test_using_unittest_{{ cookiecutter.pkg_name }}(self):
        return_value = run_demo(True, "Hello world")
        self.assertTrue(return_value)


# Pytest style

def test_using_pytest_{{ cookiecutter.pkg_name }}():
    assert run_demo(True, "Hello World") == True

