# coding=utf-8

"""Removes top-level __main__.py and {{ cookiecutter.project_slug }}.py if not needed."""

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_top_level_files():
    file_names = [os.path.join("{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.py"),
                  os.path.join("{{ cookiecutter.project_slug }}", "__main__.py")]
    for file_name in file_names:
        os.remove(file_name)

def main():

    if "{{ cookiecutter.project_runnable }}".lower() == "n":
        remove_top_level_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
