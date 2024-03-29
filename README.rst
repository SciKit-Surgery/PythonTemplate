Python Template
===============================

.. image:: https://github.com/SciKit-Surgery/PythonTemplate/raw/master/project-icon.png
   :height: 128px
   :target: https://github.com/SciKit-Surgery/PythonTemplate
   :alt: Logo

|

.. image:: https://github.com/SciKit-Surgery/PythonTemplate/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/SciKit-Surgery/PythonTemplate/actions
   :alt: GitHub Actions CI status

.. image:: https://img.shields.io/badge/Cite-SciKit--Surgery-informational
   :target: https://doi.org/10.1007/s11548-020-02180-5
   :alt: The SciKit-Surgery paper

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter

Python Template is a Cookiecutter template for creating a python project.
When used with `Cookiecutter`_ Python Template will create a fully working python "Hello world" project with unit tests,
GitHub Actions, linting, PyPi distribution and sphinx documentation.

Authors: Tom Doel, Stephen Thompson, Matt Clarkson, Thomas Dowrick, Mian Ahmad, Miguel Xochicale

Python Template is part of the `SciKit-Surgery`_ software project, developed at the
`Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

Purpose
~~~~~~~
Python Template was developed by the  `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_,
to assist researchers in the development of small but well engineered software components. It has been
widely used in the development of `SciKit-Surgery`_, but can be used as a starting point for any
Python project.
The template supports and encourages well engineered software by helping researchers with
standard software development tasks (`Software Process`_).

How to deliver standard software development tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The table below lists standard development tasks and how the Python Template helps to deliver them.
Paying heed to the following tasks at the earliest stage of development should support the
creation of well defined, maintainable, well documented, and well tested code.

+-------------------------+--------------------------------------------------------------+
|  Task                   |  What the Python Template Does                               |
+=========================+==============================================================+
| Requirements generation | The template creates the file doc/requirements.rst           |
|                         | and populates it with some minimum requirements for all      |
|                         | SciKit-Surgery projects. Instructions and relevant links are |
|                         | provided to encourage the researcher to add more             |
|                         | requirements to the file to describe what the project does,  |
|                         | both before and during development.                          |
+-------------------------+--------------------------------------------------------------+
| Software design         | The Python Template provides a modular framework that        |
|                         | integrates with the wider python ecosystem. Providing a      |
|                         | highly modular environment enables the                       |
|                         | researcher to focus on algorithm development, testing and    |
|                         | publication, with minimal consideration of the wider software|
|                         | design.                                                      |
+-------------------------+--------------------------------------------------------------+
| Managing source code    | Source code versioning and updates is handled by `git`_. The |
| versions and updates    | Python Template supports several git repository providers,   |
+-------------------------+--------------------------------------------------------------+
| Configuring projects    | The Python language is cross platform. The Python            |
| for specific platforms  | Template takes advantage of the `pip`_ package manager to    |
|                         | create modular projects that can be easily installed on      |
|                         | multiple platforms.                                          |
+-------------------------+--------------------------------------------------------------+
| Compilation and linking | By using the python environment, the Python Template avoids  |
|                         | the need for compilation and linking.                        |
+-------------------------+--------------------------------------------------------------+
| Testing the code at     | The Python Platform uses `tox`_ to automate tests (pytest),  |
| run time                | coverage analysis and linting (pylint)                       |
|                         | comes ready with appropriate unit tests to meet the          |
|                         | minimum requirements (see first item). If using GitHub       |
|                         | to host                                                      |
|                         | the code, cross platform continuous integration testing is   |
|                         | set up by default. It is up to the researcher to             |
|                         | write further tests as the code is developed.                |
+-------------------------+--------------------------------------------------------------+
| Verifying the validity  | The validity of output is performed as part of the unit      |
| of output               | testing.                                                     |
+-------------------------+--------------------------------------------------------------+
| Documenting the code    | The Python Template provides a template for code             |
|                         | documentation showing how to write in line documentation.    |
|                         | Documentation can be automatically built using `ReadTheDocs`_|
+-------------------------+--------------------------------------------------------------+
| Tracking and repairing  | Issue tracking is handled by default by the chosen git       |
| bugs                    | repository host.                                             |
+-------------------------+--------------------------------------------------------------+

Whilst every effort has been made to automate tasks where possible, it is up to the researcher consider software
requirements, write documentation, and create unit tests.
Templates for each of these tasks are provided, so after creating your project, please take a little time before you
start coding to think about what you want your software to achieve, and write it down in the file doc/requirements.rst.

How to use
~~~~~~~~~~

1. Install `Cookiecutter`_ package and other requirements using virtual environments (VE) in `conda`_ or `mambaforce`_ by replacing conda with mamba.

::

  conda create -n ssptVE pip -c conda-forge
  conda activate ssptVE
  python -m pip install -e ".[dev]"


2. Test template using `tox` and `pytest`

::

  conda activate ssptVE
  tox

3. Run Cookiecutter with the URL of this template.
Alternatively, you can run it in the same path of this repository if you are developing a new feature for this template.

::

  cookiecutter https://github.com/SciKit-Surgery/PythonTemplate.git
  cookiecutter .

4. Answer the questions to configure your template (press enter to choose defaults), for further details on available answers.
See "List of parameters for cookiecutter" below.

5. Create a local git repository for your new project and commit the files.

::

  cd MyNewProject
  git init
  python -m pip install -e ".[dev]"
  git add .
  git commit -m "Initial commit of My New Project"

Note: make sure you use "git add ." not "git add * " to pick up hidden files like `.gitlab-ci.yml`.

6. Create a new project on GitHub, making sure the URL matches what you set in step 3.

7. Add a remote in order to link your local repository to your GitHub repository and push the files across.
**NOTE**: use the `SSH`_ form of the repository URL for SSH key authentication (so you don't have to enter a username and password).

::

  git remote add origin git@github.com:GITHUB_USERNAME/MyNewProject.git
  git push origin master

8. If using GitHub, and assuming your URLs are all correct, GitHub Actions should automatically
run tests for your project.

9. You can verify your project has been set up correctly by installing and running tox.

::

 cd MyNewProject
 tox
 tox -e lint
 tox -e docs
 cd ..

tox runs several different stages, including pytest for unit tests and pylint for check for PEP8 linting.
These can also be run independently:

::

 python -m pytest
 pylint --rcfile=tests/pylintrc mynewproject

10. Install your package in editable mode and build your package

::

 python -m pip install -e .
 python -m build

10. Take a moment to write some software requirements, and populate the README file with a basic description of
what you want to do, then start coding.


List of parameters for cookiecutter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    project_name          | Name of the project as it will appear in the documentation (can have spaces)   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    project_slug          | Project name as used in the URL; by default project_name with spaces removed   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | The main python package name for your project. By default this is the          |
|   pkg_name               | project_slug converted into lower case. pkg_name should not contain dashes (-) |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | The URL of the git server that will host your code. If you don't want to       |
|  repository_server       | use any of the predefined options, choose any and modify the project_url later |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    full_name             | Your full name, for authorship information, and to suggest your profile name   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | Your personal profile name on GitHub. Or you can                               |
|   repository_profile_name| enter a group name that will be used to construct the repository URL           |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | Choose whether you want your project under your personal profile path or in a  |
|   repository_path        | shared location                                                                |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | The full URL to your project will be constructed from the previous options,    |
|   repository_url         | and is of the form repository_server/repository_path                           |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    open_source_license   | Recommend BSD-3 for internal projects, Apache for external collaborations      |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    copyright_holder      | If you are a member of UCL you should accept the default text                  |
+--------------------------+--------------------------------------------------------------------------------+

For developers
~~~~~~~~~~~~~~
1. Run Cookiecutter with the URL of this template.

::

  cookiecutter .
  cd MyNewProject
  pip install -r requirements-dev.txt
  tox
  tox -e lint
  tox -e docs
  python -m pytest
  pylint --rcfile=tests/pylintrc mynewproject
  python -m pip install -e .
  python -m build

Contributing
~~~~~~~~~~~~

Please see the `contributing guidelines`_.


Useful links
~~~~~~~~~~~~

* `pip`_
* `python`_
* `spinx`_
* `git`_
* `tox`_

Licensing and copyright
-----------------------

Copyright 2017 University College London.
Python Template is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.

.. _`pip`: https://pypi.org/project/pip/
.. _`python`: https://www.python.org/
.. _`spinx`: http://www.sphinx-doc.org/
.. _`git`: https://git-scm.com/
.. _`tox`: https://tox.readthedocs.io/
.. _`SciKit-Surgery`: https://www.github.com/SciKit-Surgery
.. _`Unix Philosophy': https://en.wikipedia.org/wiki/Unix_philosophy
.. _`Software Process`: https://doi.org/10.1109/ISBI.2004.1398621
.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/PythonTemplate/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/PythonTemplate/blob/master/LICENSE
.. _`Cookiecutter`: https://cookiecutter.readthedocs.io
.. _`WEISSLab`: https://weisslab.cs.ucl.ac.uk/
.. _`ReadTheDocs`: https://readthedocs.org/
.. _`mambaforce`: https://github.com/conda-forge/miniforge#install
.. _`conda`: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
.. _`SSH`: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent