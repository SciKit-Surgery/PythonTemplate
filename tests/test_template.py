# coding=utf-8

"""Test the template"""
import shutil
import tempfile
from unittest import TestCase

from cookiecutter.main import cookiecutter


class TestTemplate(TestCase):
    def test_template(self):
        temp_folder = tempfile.mkdtemp()
        cookiecutter('.', output_dir=temp_folder, no_input=True,
                     overwrite_if_exists=True)
        shutil.rmtree(temp_folder)
