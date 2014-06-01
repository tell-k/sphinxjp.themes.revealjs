# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.reveals
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import mock
import unittest


class GetPathTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs import get_path
        return get_path

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from sphinxjp.themes import revealjs
        self.assertEqual(revealjs.template_path, self._callFUT())


class SetupTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs import setup
        return setup

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        dummy_app = "dummy_app"

        with mock.patch('sphinxjp.themes.revealjs.directives.setup',
                        return_value=True, autospec=True) as mock_func:

            self._callFUT(dummy_app)
            mock_func.assert_called_with(dummy_app)
