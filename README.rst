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

Purpose
~~~~~~~
Python Template is part of SNAPPY, a collection of software
developed by the Wellcome EPSRC Centre for Surgical Sciences and Interventions. 
SNAPPY is being developed to support faster translation of advanced surgical 
research from the bench to the bed side. SNAPPY does this by supporting and
encouraging the development of small but well engineered software components that 
can;
* be used and developed during early stage research, and;
* easily be built into high quality clinical applications that can be production ready in less than 2 years.

SNAPPY supports and encourages well engineered software by helping researchers with
standard software development tasks (from <link to VTK thing>). The table below 
lists 9 standard development tasks and how the Python Template helps to deliver them. 
Paying heed to the following tasks at the earliest stage of development should support the
creation of well defined, maintainable, well documented, and well tested code. 

+-------------------------+--------------------------------------------------------------+
|  Task                   |  What the Python Template Does                               |
+-------------------------+--------------------------------------------------------------+
| Requirements generation | The template creates the file doc/requirements.rst           |
|                         | and populates it with some minimum requirements for all      | 
|                         | SNAPPY projects. Instructions and relevant links are provided|
|                         | to encourage the researcher to add more requirements to the  |
|                         | file to describe what the project does, both before and      |
|                         | during development.                                          | 
+-------------------------+--------------------------------------------------------------+
| Software design         | The Python Template provides a modular framework that        |
|                         | integrates with the wider SNAPPY ecosystem. Many of the      |
|                         | important software design decisions have been made by the    |
|                         | SNAPPY development team. By providing a highly modular       |
|                         | environment the researcher can focus on algorithm            |
|                         | development, with minimal consideration of the wider software|
|                         | design.                                                      |
+-------------------------+--------------------------------------------------------------+
| managing source code    | Source code versioning and updates is handled by git. The    |
| versions and updates    | Python Template supports several git repository providers,   |
|                         | allowing the researcher to choose an appropriate one.        |
+-------------------------+--------------------------------------------------------------+
| configuring projects    | The Python environment is cross platform. The Python         |
| for specific platforms  | Template takes advantage of the pip Package manager to       | 
|                         | create modular projects that can be easily installed on      |
|                         | multiple platforms.                                          |
+-------------------------+--------------------------------------------------------------+
| compilation and linking | By using the python environment, the Python Template avoids  |
|                         | the need for compilation and linking.                        |
+-------------------------+--------------------------------------------------------------+
| testing the code at     | The Python Platform provides unit testing using tox, and     |
| run time                | comes ready with appropriate unit tests to meet the          |
|                         | minimum requirements (see above). If using WEISSlab to host  |
|                         | the code cross platform continuous integration testing is    |
|                         | set up by default. It is up to the user to                   |
|                         | write further tests as the code is developed, by providing   |
|                         | a ready made template for unit tests, this should be easy.   |
+-------------------------+--------------------------------------------------------------+
| verifying the validity  | The validity of output is performed as part of the unit      |
| of output               | testing (above).                                             |
+-------------------------+--------------------------------------------------------------+
| documenting the code    | The Python Template provides a template for code             |
|                         | documentation showing how to write documentation for         |
|                         | functions using spinx? It is up to the user to write         |
|                         | further documentation as the code is developed.              |
+-------------------------+--------------------------------------------------------------+
| tracking and repairing  | Issue tracking is handled by default by the chosen git       |
| bugs                    | repository host.                                             |
+-------------------------+--------------------------------------------------------------+

Whilst every effort has been made to automate tasks where possible, it is up to the researcher consider software requirements, write documentation, and sensible unit tests. Templates for each of these tasks are provided, so after creating your project, see below please take a little time before you start coding to think about what you want your software to achieve, and write it down in the file doc/requirements.rst.

How to use
~~~~~~~~~~

1. Install `Cookiecutter`_

::

   pip install cookiecutter


2. Run `Cookiecutter`_ with the URL of this template

::

  cookiecutter https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate.git

4. Answer the questions to configure your template (press enter to choose defaults), for further details on available answers see "List of Parameters" below. 

5. Create a local git repository for your new project and commit the files. 

::

  cd MyNewProject
  git init
  git add .  
  git commit -m "Initial commit of My New Project"

Note: make sure you use "git add ." not "git add * " to pick up hidden files like `.gitlab-ci.yml`.

6. Create a new project on WeissLab (or CmicLab, GitHub or your preferred git host), making sure the URL matches

7. Add a remote in order to link your local repository to your WeissLab / CmicLab / GitLab repository and push the files across. NOTE: use the SSH form of the repository URL so you can use SSH key authentication (so you don't have to enter a username and password)

::

  git remote add origin git@weisslab.cs.ucl.ac.uk:JoeBloggs/MyNewProject.git
  git push origin master

8. You can quickly test it works by creating a virtual environment, then installing and running tox:

::

  cd MyNewProject
  virtualenv mynewprojct_virtualenv
  source mynewprojct_virtualenv/bin/activate
  pip install tox
  tox
  cd ..


9. If using WeissLab, and assuming your URLs are all correct, GitLab CI should automatically build and test your project

10. Take a moment to enter some requirements, then start coding.


List of parameters
~~~~~~~~~~~~~~~~~~

::

Notes:
  * Details of arguments are described below
  * Choose a suitable project name (it can h.
  * The default GitLab group will be your personal namespace. This assumes your username is FirstnameSecondname (if not, you should change this). You should also change this if you want to store your project under a GitLab group (such as CMIC, WEISS, RVM or GIFT-Surg).
  * Modify the URL if you are not putting the prokect on WeissLab
  * For most questions you can chose the defaults.
  * Arguments can also be specified in configuration files — see the `Cookiecutter`_  documentation.
=======
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

Author: Tom Doel
=======

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

.. _`The WEISS Software Manifsesto - Check it out`: https://weisslab.cs.ucl.ac.uk/WEISS/_manifesto
.. _`Software Process`: https://doi.org/10.1109/ISBI.2004.1398621
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
