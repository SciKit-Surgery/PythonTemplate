#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys

from {{ cookiecutter.pkg_name }} import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
