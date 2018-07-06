#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_command_line import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
