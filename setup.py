from setuptools import setup, find_packages

setup(
    name='Python Template',
    version='0.1',
    description='Python Template',
    url='https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareArchitecture/PythonTemplate',
    author='Tom Doel',
    author_email='t.doel@ucl.ac.uk',
    license='BSD license',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    )
)
