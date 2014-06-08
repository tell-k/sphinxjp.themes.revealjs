# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.2.0'
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
    "Programming Language :: Python :: 3",
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
    package_data={'': ['buildout.cfg']},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'sphinx',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'flake8', 'mock', 'coverage'],
    extras_require=dict(test=['nose', 'flake8', 'mock', 'coverage']),
    entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.revealjs:template_path

        [sphinx_directives]
        setup = sphinxjp.themes.revealjs:setup
    """,
    zip_safe=False
)
