{{ cookiecutter.project_name }}
===============================

.. image:: {{ cookiecutter.project_url }}/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: {{ cookiecutter.project_url }}
   :alt: Logo

.. image:: {{ cookiecutter.project_url }}/badges/master/build.svg
   :target: {{ cookiecutter.project_url }}/pipelines
   :alt: GitLab-CI test status

.. image:: {{ cookiecutter.project_url }}/badges/master/coverage.svg
    :target: {{ cookiecutter.project_url }}/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
    :target: http://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: {{ cookiecutter.full_name }}

{{ cookiecutter.project_name }} is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

{{ cookiecutter.project_name }} is tested on Python 3.8 but should support other modern Python versions.

{{ cookiecutter.project_name }} is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python {{cookiecutter.pkg_name}}.py 5 8
    python {{cookiecutter.pkg_name}}.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone {{ cookiecutter.project_url }}


Create virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can create a mamba virtual environment using

::

    mamba create -n {{ cookiecutter.project_name }}VE python=3.8 pip -c conda-forge
    mamba activate {{ cookiecutter.project_name }}VE
    pip install -r requirements-dev.txt

Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pylint --rcfile=tests/pylintrc {{cookiecutter.pkg_name}}


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+{{ cookiecutter.project_url }}



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright {% now 'local', '%Y' %} {{ cookiecutter.copyright_holder }}.
{{ cookiecutter.project_name }} is released under the {{ cookiecutter.open_source_license }}. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: {{ cookiecutter.project_url }}
.. _`Documentation`: https://{{ cookiecutter.project_slug }}.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/SciKit-Surgery
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: {{ cookiecutter.project_url }}/blob/master/CONTRIBUTING.rst
.. _`license file`: {{ cookiecutter.project_url }}/blob/master/LICENSE