# coding=utf-8

"""{{ cookiecutter.project_name }} tests"""

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo

import six

# Pytest style

def test_using_pytest_{{ cookiecutter.pkg_name }}():
    console = True
    assert run_demo(console, "Hello World") == True

# Disable this test if root.mainloop is uncommented in
# run_demo()
def test_using_pytest_cookienewwithgitinit_withTK():
    try:
        import tkinter
        try:
            console=False
            assert run_demo(console, "Hello World") == True
        except tkinter.TclError:
            six.print_("Got TCL error, probably no DISPLAY set, that's OK.")
            assert True
        except:
            six.print_("Got another error (not TCL), that's not OK.")
            assert False

    except ModuleNotFoundError:
        six.print_("Got import error on tkinter, please check your python installation")
        #we're not trying to test whether we have tkinter so this is ok
        assert True
    except:
        assert False

