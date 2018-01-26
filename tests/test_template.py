# coding=utf-8

"""Test the template"""
import os
import subprocess
import shutil
import tempfile
from unittest import TestCase

import sys

from cookiecutter.main import cookiecutter


class TestTemplate(TestCase):
    def test_template(self):
        temp_folder = tempfile.mkdtemp()
        cookiecutter('.', output_dir=temp_folder, no_input=True,
                     overwrite_if_exists=True)
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'],
                           cwd=os.path.join(temp_folder, 'MyNewProject'))
        shutil.rmtree(temp_folder)
