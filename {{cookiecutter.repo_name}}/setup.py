#!/usr/bin/python
import os
import sys

from setuptools import setup, find_packages
from pip.req import parse_requirements


assert sys.version_info.major == 3, "Only Python 3 is supported"


def _pt(name):
    return os.path.join(os.path.dirname(__file__), name)


def _read(name):
    with open(_pt(name)) as fil:
        return fil.read()


def _get_version():
    return _read("CHANGES").split("\n")[0].split()[0]


def _get_requirements():
    req_f = _pt("requirements.txt")
    if os.path.exists(req_f):
        return [str(ir.req) for ir in parse_requirements(req_f, session=False)]
    else:
        return []


setup(
    name="{{cookiecutter.repo_name}}",
    provides=["{{cookiecutter.python_name}}"],
    install_requires=_get_requirements(),
    version=_get_version(),
    packages=find_packages(exclude=["tests"]),
    include_package_data=True
)
