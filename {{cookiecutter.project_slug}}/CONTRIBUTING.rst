.. highlight:: shell

===============================================
Contributing to {{ cookiecutter.project_name }}
===============================================

We welcome contributions to {{ cookiecutter.project_name }}.


Reporting bugs and feature requests
-----------------------------------

Please create a new issue on {{ cookiecutter.project_url }}/issues/new

When reporting a bug, please include:
* The version of {{ cookiecutter.project_name }} you are using
* Your OS version (for example Windows 10 64-bit, macOS High Sierra, Ubuntu 16.04)
* Detailed steps to reproduce the bug.




Fixing bugs or implement features
---------------------------------

The easiest way to contribute is to follow these guidelines:

1. Look through the issues on {{ cookiecutter.project_url }}/issues and assign the relevant issue to yourself. If there is not an existing issue that covers your work, please create one: {{ cookiecutter.project_url }}/issues/new
2. Fork the repository: {{ cookiecutter.project_url }}/forks/new
3. Create a branch for your changes. The branch name should start with the issue number, followed by hyphen separated words describing the issue. For example: 1-update-contribution-guidelines
4. Make your changes following the coding guidelines below.
5. Commit and push your changes to your fork. The commit message should start with `Issue #<issue number>`, for example: "Issue #1: Fixed typo". Commit in small, related chunks. Review each commit and explain its purpose in the commit message.
6. Submit a merge request: {{ cookiecutter.project_url }}/merge_requests/new



Coding guidelines
-----------------

1. Please follow PEP8 guidelines https://www.python.org/dev/peps/pep-0008/
2. Create a python virtual environment (virtualenv) for development
3. Make sure that pylint passes. You may disable specific warnings within the code where it is reasonable to do so
4. Add unit tests for new and modified code
5. Make sure all existing and new tests pass
6. Make sure all docstrings have been added
7. Make sure all dependencies have been added to requirements
8. Make sure your code works for all required versions of Python
9. Make sure your code works for all required operating systems

