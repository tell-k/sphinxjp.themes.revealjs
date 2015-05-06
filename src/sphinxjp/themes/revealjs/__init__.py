# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.revealjs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

from os import path
from sphinxjp.themes.revealjs import directives

__version__ = '0.3.0'

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates')


def get_path():
    """entry-point for sphinx  theme."""
    return template_path


def setup(app):
    """entry-point for sphinx  directive."""
    directives.setup(app)
