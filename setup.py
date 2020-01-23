#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import versioneer


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering",
]

cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": PyTest})

setup(
    name="mrrt.utils",
    namespace_package=["mrrt"],
    cmdclass=cmdclass,
    version=versioneer.get_version(),
    description="MRI-related utilities implemented in Python",
    author="Gregory Lee",
    author_email="grlee77@gmail.com",
    url="https://github.com/mritools/mrrt.utils",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">= 3.6",
)
