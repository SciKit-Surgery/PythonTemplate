# coding=utf-8

"""
scikit-surgery test to check that `requirements.txt vs `setup.py` or `requirements.txt` vs `pytproject.toml`
specify the same dependencies
"""
import pytest
import glob


@pytest.mark.skipif(not glob.glob('setup.py') == 'setup.py', reason="there is no setup.py")
def test_requirements_vs_setup():
    """
    Test that the requirements.txt matches setup.py
    """

    with open("setup.py", "r", encoding='us-ascii') as file_to_read:
        searchlines = file_to_read.readlines()

    install_line = -1
    for i, line in enumerate(searchlines):
        if "install_requires" in line:
            install_line = i
            break

    end_line = -1
    for i, line in enumerate(searchlines[install_line:]):
        if "]" in line:
            end_line = install_line + i
            break

    setup_reqs = []

    for line in searchlines[install_line + 1: end_line]:
        req = line.replace(',', '').replace("'", "")
        req = req.replace(' ', '').replace('\n', '')
        setup_reqs.append(req)

    with open("requirements.txt", "r", encoding='us-ascii') as file_to_read:
        searchlines = file_to_read.readlines()

    reqs = []
    for line in searchlines:
        if "#" not in line:
            reqs.append(line.replace('\n', ''))

    for setup_req in setup_reqs:
        assert setup_req in reqs

    for req in reqs:
        assert req in setup_reqs
