# coding=utf-8

"""Runs after project generation to provide additional configuration steps."""

import os

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_top_level_files():
    file_names = ["{{ cookiecutter.pkg_name }}.py",
                  os.path.join("{{ cookiecutter.pkg_name }}", "__main__.py")]

    for file_name in file_names:
        os.remove(file_name)

def main():

    if "{{ cookiecutter.pkg_runnable }}".lower() == "n":
        remove_top_level_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
