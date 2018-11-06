# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo

import six
import tkinte

# Pytest style

def test_using_pytest_{{ cookiecutter.pkg_name }}():
    console = True
    assert run_demo(console, "Hello World") == True

def test_using_pytest_cookienewwithgitinit_withTK():
    try:
        console=False
        assert run_demo(console, "Hello World") == True
    except tkinter.TclError:
        six.print_("Got TCL error, probably no DISPLAY set, that's OK.")
        assert True
    except:
        six.print_("Got another error (not TCL), that's not OK.")
        assert False

