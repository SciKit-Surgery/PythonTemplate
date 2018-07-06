# coding=utf-8

"""Command line processing"""


import argparse
from {{ cookiecutter.pkg_name }} import __version__
from {{ cookiecutter.pkg_name }}.ui.{{ cookiecutter.pkg_name }}_demo import run_demo


def main(args=None):
    """Entry point for {{ cookiecutter.project_name }} application"""

    parser = argparse.ArgumentParser(description='{{ cookiecutter.project_name }}')

    parser.add_argument("-t", "--text",
                        required=False,
                        default="This is {{ cookiecutter.project_name }}",
                        type=str,
                        help="Text to display")

    parser.add_argument("--console", required=False,
                        action='store_true',
                        help="If set, {{ cookiecutter.project_name }} will not bring up a graphical user "
                             "interface")ß

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='{{ cookiecutter.project_name }} version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_demo(args.console, args.text)
