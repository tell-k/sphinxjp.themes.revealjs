# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.revealjs.compat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import sys
text = str if sys.version_info >= (3, 0) else unicode  # NOQA
