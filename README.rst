Python Template
===============================

.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/raw/master/project-icon.png
   :height: 150px
   :width: 150px
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate


.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/badges/master/build.svg
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/pipelines


Python Template is a Cookiecutter template for creating a python project. When used with `Cookiecutter`_. Python Template will create a fully working python "Hello world" project with unit tests, Python 2 and 3 compatibility, GitLab CI, lint and sphinx documentation.

Python template can be used to create projects for CmicLab, WEISSLab, GitHub

How to use
~~~~~~~~~~

1. Install `Cookiecutter`_

::

   pip install cookiecutter


2. Run `Cookiecutter`_ with the URL of this template

::

  cookiecutter https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate.git

4. Answer the questions to configure your template (press enter to choose defaults), for example:

::

  project_name [My New Project]:
  project_slug [MyNewProject]:
  pkg_name [mynewproject]:
  Select repository_server:
  1 - https://weisslab.cs.ucl.ac.uk
  2 - https://cmiclab.cs.ucl.ac.uk
  3 - https://github.com
  4 - https://gitlab.com
  Choose from 1, 2, 3, 4 [1]:
  full_name [Your Name]: Joe Bloggs
  repository_profile_name [JoeBloggs]:
  Select repository_path:
  1 - JoeBloggs/mynewproject
  2 - WEISS/SoftwareRepositories/mynewproject
  Choose from 1, 2 [1]: 1
  project_url [https://weisslab.cs.ucl.ac.uk/JoeBloggs/MyNewProject]:
  Select open_source_license:
  1 - BSD-3 license
  2 - Apache Software License 2.0
  3 - MIT License
  Choose from 1, 2, 3 [1]:
  copyright_holder [University College London]:

Notes:
  * Details of arguments are described below
  * Choose a suitable project name (it can h.
  * The default GitLab group will be your personal namespace. This assumes your username is FirstnameSecondname (if not, you should change this). You should also change this if you want to store your project under a GitLab group (such as CMIC, WEISS, RVM or GIFT-Surg).
  * Modify the URL if you are not putting the prokect on WeissLab
  * For most questions you can chose the defaults.
  * Arguments can also be specified in configuration files — see the `Cookiecutter`_  documentation.


5. (Optional) - you can quickly test it works by creating a virtual environment, then installing and running tox:

::

  cd MyNewProject
  virtualenv mynewprojct_virtualenv
  source mynewprojct_virtualenv/bin/activate
  pip install tox
  tox
  cd ..

6. Create a local git repository for your new project and commit the files. Note that `.gitlab-ci.yml` may be hidden so use `git add .` rather than `git add *` to include it.

::

  cd MyNewProject
  git init
  git add .
  git commit -m "Initial commit of My New Project"


7. Create a new project on WeissLab (or CmicLab, GitHub or your preferred git host), making sure the URL matches

8. Add a remote in order to link your local repository to your WeissLab / CmicLab / GitLab repository and push the files across. NOTE: use the SSH form of the repository URL so you can use SSH key authentication (so you don't have to enter a username and password)

::

  git remote add origin git@weisslab.cs.ucl.ac.uk:JoeBloggs/MyNewProject.git
  git push origin master

9. If using WeissLab, and assuming your URLs are all correct, GitLab CI should automatically build and test your project


List of parameters
~~~~~~~~~~~~~~~~~~

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
|    pkg_name              | The main python package name for your project. By default this is the          |
|                          | project_slug converted into lower case                                         |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|    repository_server     | The URL of the git server that will host your code. If you are don't want to   |
|                          | use any of the predefined options, choose any and modify the project_url later |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    full_name             | Your full name, for authorship information, and to suggest your profile name   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|    repository_profile_name | Your personal profile name on WeissLab/Cmiclab/Gitlab/GitHub. Or you can     |
|                          | enter a group name that will be used to construct the repository URL           |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|    repository_path       | Choose whether you want your project under your personal profile path or in a  |
|                          | shared location                                                                |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|    repository_url        | The full URL to your project will be constructed from the previous options,    |
|                          | and is of the form repository_server/repository_path                           |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    open_source_license   | Recommend BSD-3 for internal projects, Apache for external collaborations      |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    copyright_holder      | If you are a member of UCL you shoud accept the default text                   |
+--------------------------+--------------------------------------------------------------------------------+



Author: Tom Doel

Python Template was developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_ in `University College London (UCL)`_.


Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

`Source code repository`_


Licensing and copyright
-----------------------

Copyright 2017 University College London.
Python Template is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/blob/master/LICENSE
.. _`Cookiecutter`: https://cookiecutter.readthedocs.io

.. toctree::
   :maxdepth: 4
   :caption: Contents:
