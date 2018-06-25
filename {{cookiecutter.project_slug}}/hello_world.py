#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys

from {{cookiecutter.pkg_name}}.ui.hello_world import hello_world


def main(args=None):
    """Entry point for Hello World application"""

    parser = argparse.ArgumentParser(description='Hello world demo')

    parser.add_argument("-t", "--text", required=False, default=None,
                        type=str
                        help="Text to display")
    version_string = get_version_string()
    parser.add_argument(
        "-v", "--version",
        action='version',
        version=version_string)

    args = parser.parse_args(args)

    hello_world(args.text)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
