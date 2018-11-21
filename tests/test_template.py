# coding=utf-8

"""Test the template"""
import os
import subprocess
import shutil
import tempfile

import sys

from cookiecutter.main import cookiecutter


def test_template():
    temp_folder = tempfile.mkdtemp()
    cookiecutter('.', output_dir=temp_folder, no_input=True,
                    overwrite_if_exists=True)
    return_code = subprocess.call([sys.executable, '-m', 'pytest'],
                        cwd=os.path.join(temp_folder, 'MyNewProject'))
    shutil.rmtree(temp_folder)
    assert not return_code
