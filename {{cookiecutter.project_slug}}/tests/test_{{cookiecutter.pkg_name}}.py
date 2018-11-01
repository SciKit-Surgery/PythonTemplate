# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo

# Pytest style

def test_using_pytest_{{ cookiecutter.pkg_name }}():
    assert run_demo(True, "Hello World") == True

