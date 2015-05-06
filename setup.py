# -*- coding: utf-8 -*-
import sys
import os
import re

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

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

here = os.path.dirname(__file__)

version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'src', 'sphinxjp',
                              'themes', 'revealjs', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)

install_requires = [
    "setuptools",
    "Sphinx",
]

tests_require = [
    "pytest-cov",
    "pytest",
    "mock",
]

long_description = '\n'.join([
    open(os.path.join(here, "src", "README.txt")).read(),
    open(os.path.join(here, "src", "AUTHORS.txt")).read(),
    open(os.path.join(here, "src", "HISTORY.txt")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Framework :: Sphinx",
    "Framework :: Sphinx :: Extension",
    "Framework :: Sphinx :: Theme",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

description = 'A sphinx theme for generate reveal.js presentation. #sphinxjp'

setup(
    name='sphinxjp.themes.revealjs',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme', 'presentation'],
    author='tell-k',
    author_email='ffk2005 at gmail dot com',
    url='https://github.com/tell-k/sphinxjp.themes.revealjs',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src', exclude=["tests"]),
    package_dir={'': 'src'},
    cmdclass={'test': PyTest},
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.revealjs:template_path

        [sphinx_directives]
        setup = sphinxjp.themes.revealjs:setup
    """,
    zip_safe=False
)
