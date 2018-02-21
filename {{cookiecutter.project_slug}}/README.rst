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

.. image:: https://travis-ci.org/{{ cookiecutter.gitlab_group }}/{{ cookiecutter.project_slug }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.gitlab_group }}/{{ cookiecutter.project_slug }}
    :alt: Travis test status

.. image:: {{ cookiecutter.project_url }}/badges/master/coverage.svg
   :target: {{ cookiecutter.project_url }}/pipelines

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
    :target: http://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



{{ cookiecutter.project_name }} is a python project that does interesting things.

Author: {{ cookiecutter.full_name }}

{{ cookiecutter.project_name }} was developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_ in `University College London (UCL)`_.


Installing
~~~~~~~~~~

::

    pip install {{ cookiecutter.project_slug }}


Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

`Source code repository`_
`Documentation`_


Licensing and copyright
-----------------------

Copyright 2017 University College London.
{{ cookiecutter.project_name }} is released under the {{ cookiecutter.open_source_license }}. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: {{ cookiecutter.project_url }}
.. _`Documentation`: https://{{ cookiecutter.project_slug }}.readthedocs.io
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: {{ cookiecutter.project_url }}/blob/master/CONTRIBUTING.rst
.. _`license file`: {{ cookiecutter.project_url }}/blob/master/LICENSE


.. toctree::
   :maxdepth: 4
   :caption: Contents:
