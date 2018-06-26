# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from unittest import TestCase

from {{ cookiecutter.pkg_name }}.ui.{{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name}}


class Test{{ cookiecutter.project_slug }}(TestCase):
    def test_{{cookiecutter.pkg_name}}(self):
        {{cookiecutter.pkg_name}}("Hello world")
