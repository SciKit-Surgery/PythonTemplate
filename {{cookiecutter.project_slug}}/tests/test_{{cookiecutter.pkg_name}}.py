# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from unittest import TestCase

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo


class Test{{ cookiecutter.project_slug }}(TestCase):
    def test_{{ cookiecutter.pkg_name }}(self):
        run_demo(True, "Hello world")
