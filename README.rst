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

3. Answer the questions to configure your template, or press enter to choose defaults. See the List Of Parameters section for more details.


4. Create a local git repository for your new project and commit the files. Use `git add .` rather than `git add *` to include files which are hidden by default.

::

  cd MyNewProject
  git init
  git add .
  git commit -m "Initial commit of My New Project"
  
Syncing to WeissLab
~~~~~~~~~~~~~~~~~~

1. Create a new project on WeissLab (or CmicLab, GitHub or your preferred git host), making sure the URL matches

2. Add a remote in order to link your local repository to your WeissLab / CmicLab / GitLab repository and push the files across. NOTE: use the SSH form of the repository URL so you can use SSH key authentication (so you don't have to enter a username and password)

::

  git remote add origin git@weisslab.cs.ucl.ac.uk:WEISS/SoftwareRepositories/newprojectname.git
  git push origin master

3. If using WeissLab, and assuming your URLs are all correct, GitLab CI should automatically build and test your project

Testing
~~~~~~~

You can quickly test if it has worked by installing and running tox. It is recommended to use a virtual environment:

::

  cd MyNewProject
  virtualenv mynewprojct_virtualenv
  source mynewprojct_virtualenv/bin/activate
  pip install tox
  tox
  cd ..


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
|                          | The main python package name for your project. By default this is the          |
|   pkg_name               | project_slug converted into lower case                                         |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | The URL of the git server that will host your code. If you are don't want to   |
|  repository_server       | use any of the predefined options, choose any and modify the project_url later |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    full_name             | Your full name, for authorship information, and to suggest your profile name   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          | Your personal profile name on WeissLab/Cmiclab/Gitlab/GitHub. Or you can       |
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
|    copyright_holder      | If you are a member of UCL you shoud accept the default text                   |
+--------------------------+--------------------------------------------------------------------------------+


Python Template was developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_ in `University College London (UCL)`_.


Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^


Licensing and copyright
-----------------------

Copyright 2017 University College London.
Python Template is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate/blob/master/LICENSE
.. _`Cookiecutter`: https://cookiecutter.readthedocs.io

.. toctree::
   :maxdepth: 4
   :caption: Contents:
