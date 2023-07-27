# coding=utf-8

"""Test the template"""
import os
import shutil
import subprocess
import sys
import tempfile
from cookiecutter.main import cookiecutter


def test_template_tests():
    temp_folder = tempfile.mkdtemp()
    cookiecutter('.', output_dir=temp_folder, no_input=True, overwrite_if_exists=True)
    return_code = subprocess.call([sys.executable, '-m', 'pytest', '-v'], cwd=os.path.join(temp_folder, 'MyNewProject'))
    shutil.rmtree(temp_folder)
    assert not return_code
