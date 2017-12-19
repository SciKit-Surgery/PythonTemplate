## {{ cookiecutter.project_name }}

The main source code repository for {{ cookiecutter.project_name }} is [WeissLab][repo].

[repo]: {{ cookiecutter.project_url }}

## Submitting bug reports and feature requests

Bug reports and feature requests should be submitted by creating an issue on [WeissLab][issues-link].

[issues-link]: {{ cookiecutter.project_url }}/issues/new


## Submitting merge requests

All merge requests should be submitted via [WeissLab][repo-mr].
Please make sure you have read the following subsections before submitting a merge request.

[repo-mr]: {{ cookiecutter.project_url }}/merge_requests/new


### Python style guide

Please follow the [PEP8 Style Guide for Python Code][pep8].

[pep8]: https://www.python.org/dev/peps/pep-0008/


### Testing your changes

Before submitting a merge request, please make sure your branch passes all
unit tests, by running:

``` sh
cd {{ cookiecutter.project_slug }}/
sh run_tests.sh
```
