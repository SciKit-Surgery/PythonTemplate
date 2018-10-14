# coding=utf-8

"""Runs after project generation to provide additional configuration steps."""

import os

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_non_module_files():

    file_names = ["{{ cookiecutter.pkg_name }}.py",
                  os.path.join("{{ cookiecutter.pkg_name }}", "__main__.py"),
                  os.path.join("{{ cookiecutter.pkg_name }}", "ui", "{{ cookiecutter.pkg_name }}_command_line.py"),
                  os.path.join("{{ cookiecutter.pkg_name }}", "ui", "{{ cookiecutter.pkg_name }}_demo.py")
                 ]

    for file_name in file_names:
        os.remove(file_name)


def main():

    if "{{ cookiecutter.modules_only }}".lower() == "y":
        remove_non_module_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
