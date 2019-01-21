# coding=utf-8
"""
Setup for {{ cookiecutter.project_name }}
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='{{ cookiecutter.project_name }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='{{ cookiecutter.project_description }}',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='{{ cookiecutter.project_url }}',
    author='{{ cookiecutter.full_name }}',
    author_email='YOUR-EMAIL@ucl.ac.uk',
    license='{{ cookiecutter.open_source_license }}',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

{% if cookiecutter.open_source_license == 'BSD-3 license' %}
        'License :: OSI Approved :: BSD License',
{% elif cookiecutter.open_source_license == 'Apache Software License 2.0' %}
       'License :: OSI Approved :: Apache Software License',
{% elif cookiecutter.open_source_license == 'GNU General Public License v3' %}
       'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
{% endif %}

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
    ],

    entry_points={
        'console_scripts': [
            '{{ cookiecutter.pkg_name }}={{ cookiecutter.pkg_name }}.__main__:main',
        ],
    },
)
