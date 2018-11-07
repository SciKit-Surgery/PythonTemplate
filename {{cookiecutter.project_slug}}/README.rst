{{ cookiecutter.project_name }}
===============================

.. image:: {{ cookiecutter.project_url }}/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: {{ cookiecutter.project_url }}

.. image:: {{ cookiecutter.project_url }}/badges/master/build.svg
   :target: {{ cookiecutter.project_url }}/pipelines
   :alt: GitLab-CI test status

.. image:: {{ cookiecutter.project_url }}/badges/master/coverage.svg
    :target: {{ cookiecutter.project_url }}/commits/master
    :alt: Test coverage

.. image:: https://travis-ci.org/{{ cookiecutter.repository_path }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.repository_path }}
    :alt: Travis test status

.. image:: {{ cookiecutter.project_url }}/badges/master/coverage.svg
   :target: {{ cookiecutter.project_url }}/pipelines

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
    :target: http://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



{{ cookiecutter.project_name }} is a python project that does interesting things. 

Author: {{ cookiecutter.full_name }}

{{ cookiecutter.project_name }} is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

Design Considerations
---------------------

(edit as appropriate once project is created)

1. Python only
2. As few dependencies as possible. Try to stick to standard scipy packages like numpy and pandas.
3. Discuss extra dependencies with the team and maybe the outcome will be to create a new separate package, where you can be more specific and more modular.
4. Unit test well, using pytest, with good coverage.
5. All errors as exceptions rather than return codes.

Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+{{ cookiecutter.project_url }}


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone {{ cookiecutter.project_url }}


Running the tests
^^^^^^^^^^^^^^^^^

You can run the unit tests by installing and running tox:

::

    pip install tox
    tox

Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

`Source code repository`_
`Documentation`_


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
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: {{ cookiecutter.project_url }}/blob/master/CONTRIBUTING.rst
.. _`license file`: {{ cookiecutter.project_url }}/blob/master/LICENSE


.. toctree::
   :maxdepth: 4
   :caption: Contents:
