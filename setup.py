from setuptools import setup, find_packages

setup(
    name='Python Template',
    version='0.1',
    description='Python Template',
    url='https://https://github.com/SciKit-Surgery/PythonTemplate',
    author='Tom Doel',
    author_email='s.thompson@ucl.ac.uk',
    license='BSD-3 license',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    )
)
