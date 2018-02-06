Python Template
===============================

.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate/raw/master/project-icon.png
   :height: 150px
   :width: 150px
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate


.. image:: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate/badges/master/build.svg
   :target: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate/pipelines


Python Template is a Cookiecutter template for creating a python project. When used with `Cookiecutter`_. Python Template will create a fully working python "Hello world" project with unit tests, Python 2 and 3 compatibility, GitLab CI, lint and sphinx documentation.

Python template can be used to create projects for CmicLab, WEISSLab, GitHub

How to use
~~~~~~~~~~

1. Install `Cookiecutter`_

::

   pip install cookiecutter


2. Run `Cookiecutter`_ with the URL of this template

::

  cookiecutter https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate.git

4. Answer the questions to configure your template (press enter to choose defaults), for example:

::

  project_name [My New Project]:
  full_name [Your Name]: Joe Bloggs
  gitlab_group [JoeBloggs]:
  project_slug [MyNewProject]:
  project_url [https://weisslab.cs.ucl.ac.uk/JoeBloggs/MyNewProject]:
  pkg_name [mynewproject]:
  Select open_source_license:
  1 - BSD-3 license
  2 - Apache Software License 2.0
  Choose from 1, 2 [1]:

Notes:
  * Details of arguments are described below
  * Choose a suitable project name (it can h.
  * The default GitLab group will be your personal namespace. This assumes your username is FirstnameSecondname (if not, you should change this). You should also change this if you want to store your project under a GitLab group (such as CMIC, WEISS, RVM or GIFT-Surg).
  * Modify the URL if you are not putting the prokect on WeissLab
  * For most questions you can chose the defaults.
  * Arguments can also be specified in configuration files — see the `Cookiecutter`_  documentation.


5. Create a local git repository for your new project and commit the files. Note that `.gitlab-ci.yml` may be hidden so use `git add .` rather than `git add *` to include it.

::

  cd MyNewProject
  git init
  git add .
  git commit -m "Initial commit of My New Project"


6. Create a new project on WeissLab (or CmicLab, GitHub or your preferred git host), making sure the URL matches

7. Add a remote in order to link your local repository to your WeissLab / CmicLab / GitLab repository and push the files across. NOTE: use the SSH form of the repository URL so you can use SSH key authentication (so you don't have to enter a username and password)

::

  git remote add origin git@weisslab.cs.ucl.ac.uk:JoeBloggs/MyNewProject.git
  git push origin master

8. If using WeissLab, and assuming your URLs are all correct, GitLab CI should automatically build and test your project


List of parameters
~~~~~~~~~~~~~~~~~~

+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    project_name          | Name of the project as it will appear in the documentation (can have spaces)   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    full_name             | Your full name, for authorship information                                     |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    gitlab_group          | The group on WeissLab where you want to store the project - only affects the   |
|                          | URL. By default this will be full_name with the spaces removed                 |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    project_slug          | Project name as used in the URL; by default project_name with spaces removed   |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    pkg_name              | The main python package name for your project. By default this is the          |
|                          | project_slug converted into lower case                                         |
+--------------------------+--------------------------------------------------------------------------------+
| ::                       |                                                                                |
|                          |                                                                                |
|    open_source_license   | Recommend BSD-3 for internal projects, Apache for external collaborations      |
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
.. _`source code repository`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate/blob/master/LICENSE
.. _`Cookiecutter`: https://cookiecutter.readthedocs.io

.. toctree::
   :maxdepth: 4
   :caption: Contents:
