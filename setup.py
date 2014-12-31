# -*- coding: utf-8 -*-
import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

version = '0.2.2'


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

requires = [
    "setuptools",
    "Sphinx",
]

tests_require = [
    "pytest-cov",
    "pytest",
    "mock",
]

long_description = '\n'.join([
    open(os.path.join("src", "README.txt")).read(),
    open(os.path.join("src", "AUTHORS.txt")).read(),
    open(os.path.join("src", "HISTORY.txt")).read(),
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
    packages=find_packages('src'),
    package_dir={'': 'src'},
    cmdclass={'test': PyTest},
    install_requires=requires,
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
