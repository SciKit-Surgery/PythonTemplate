#!/usr/bin/python
#  -*- coding: utf-8 -*-
"""{{ cookiecutter.project_slug }}"""

import sys
import argparse

from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name }}
from {{ cookiecutter.pkg_name }} import __version__


def main(args=None):
    """Entry point for {{ cookiecutter.project_name }} application"""

    parser = argparse.ArgumentParser(description='{{ cookiecutter.project_name }}')

    parser.add_argument("-t", "--text",
                        required=False,
                        default="This is {{ cookiecutter.project_name }}",
                        type=str,
                        help="Text to display")
    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='{{ cookiecutter.project_name }} version ' + friendly_version_string)

    args = parser.parse_args(args)

    {{ cookiecutter.pkg_name }}(args.text)


if __name__ == "__main__" and not __package__:
    # To allow the package's main function to be executed without the -m switch,
    # i.e. "python {{ cookiecutter.pkg_name }}", we have to explicitly set the
    # module name and append the parent directory to the sys.path (see PEP 366)
    import os.path as path
    __package__ = "{{ cookiecutter.pkg_name }}"  # pylint: disable=redefined-builtin
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(__file__)))

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
