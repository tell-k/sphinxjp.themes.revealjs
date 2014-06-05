# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.revealjs.directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import unittest


class DummyConfig(object):

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, name):
        if name in self.kwargs:
            return self.kwargs.get(name)
        return self

    def nested_parse(self, content, content_offset, node):
        pass

    def warning(self, msg, line):
        return dict(msg=msg, line=line)


class HeadingTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import heading
        return heading

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        self.assertEqual("h1", self._callFUT("h1"))
        self.assertEqual("h2", self._callFUT("h2"))
        self.assertEqual("h3", self._callFUT("h3"))
        self.assertEqual("h4", self._callFUT("h4"))
        self.assertEqual("h5", self._callFUT("h5"))
        self.assertEqual("h6", self._callFUT("h6"))

    def test_value_error(self):
        self.assertRaises(ValueError, self._callFUT, "unknown")


class RevealjsDirectiveTest(unittest.TestCase):

    def _getTargetClass(self):
        from sphinxjp.themes.revealjs.directives import RevealjsDirective
        return RevealjsDirective

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyConfig(self, **kwargs):
        config = dict()
        config.update(kwargs)
        return DummyConfig(**config)

    def _getParams(self, **kwargs):
        params = dict(
            name='dummyname',
            arguments=['tell-k', 'test'],
            options={},
            content="test",
            lineno=1,
            content_offset=1,
            block_text="",
            state="",
            state_machine="",
        )
        params.update(kwargs)
        return params

    def test_it(self):
        directive = self._makeOne(**self._getParams())
        directive.state = self._getDummyConfig()

        nodes = directive.run()
        self.assertEqual(1, len(nodes))
        self.assertEqual('tell-k test', nodes[0]['title'])
        self.assertEqual(False, nodes[0]['noheading'])
        self.assertEqual([], nodes[0]['classes'])

    def test_class_option(self):
        directive = self._makeOne(**self._getParams(options={
            "class": "add-class",
        }))
        directive.state = self._getDummyConfig()
        nodes = directive.run()
        self.assertEqual('add-class', nodes[0]['classes'])

    def test_noheading_option(self):
        directive = self._makeOne(**self._getParams(options={
            "noheading": None,
        }))
        directive.state = self._getDummyConfig()
        nodes = directive.run()
        self.assertEqual(True, nodes[0]['noheading'])

    def test_other_options(self):
        directive = self._makeOne(**self._getParams(options={
            "title-heading": "title-heading",
        }))
        directive.state = self._getDummyConfig()
        nodes = directive.run()
        self.assertEqual("title-heading", nodes[0]['title-heading'])


class RvSmallDirectiveTest(unittest.TestCase):

    def _getTargetClass(self):
        from sphinxjp.themes.revealjs.directives import RvSmallDirective
        return RvSmallDirective

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyConfig(self, **kwargs):
        config = dict()
        config.update(kwargs)
        return DummyConfig(**config)

    def _getParams(self, **kwargs):
        params = dict(
            name='dummyname',
            arguments='',
            options={},
            content="test",
            lineno=1,
            content_offset=1,
            block_text="",
            state="",
            state_machine="",
        )
        params.update(kwargs)
        return params

    def test_it(self):
        directive = self._makeOne(**self._getParams())
        directive.state = self._getDummyConfig()

        nodes = directive.run()
        self.assertEqual(1, len(nodes))
        self.assertEqual([], nodes[0]['classes'])

    def test_class_option(self):
        directive = self._makeOne(**self._getParams(options={
            "class": "add-class",
        }))
        directive.state = self._getDummyConfig()
        nodes = directive.run()
        self.assertEqual('add-class', nodes[0]['classes'])


class RvNoteDirectiveTest(unittest.TestCase):

    def _getTargetClass(self):
        from sphinxjp.themes.revealjs.directives import RvNoteDirective
        return RvNoteDirective

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyConfig(self, **kwargs):
        config = dict()
        config.update(kwargs)
        return DummyConfig(**config)

    def _getParams(self, **kwargs):
        params = dict(
            name='dummyname',
            arguments='',
            options={},
            content="test",
            lineno=1,
            content_offset=1,
            block_text="",
            state="",
            state_machine="",
        )
        params.update(kwargs)
        return params

    def test_it(self):
        directive = self._makeOne(**self._getParams())
        directive.state = self._getDummyConfig()

        nodes = directive.run()
        self.assertEqual(1, len(nodes))
        self.assertEqual([], nodes[0]['classes'])

    def test_class_option(self):
        directive = self._makeOne(**self._getParams(options={
            "class": "add-class",
        }))
        directive.state = self._getDummyConfig()
        nodes = directive.run()
        self.assertEqual('add-class', nodes[0]['classes'])


class RvCodeDirectiveTest(unittest.TestCase):

    def _getTargetClass(self):
        from sphinxjp.themes.revealjs.directives import RvCodeDirective
        return RvCodeDirective

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyConfig(self, **kwargs):
        config = dict()
        config.update(kwargs)
        return DummyConfig(**config)

    def _getParams(self, **kwargs):
        params = dict(
            name='dummyname',
            arguments='',
            options={},
            content="test",
            lineno=1,
            content_offset=1,
            block_text="",
            state="",
            state_machine="",
        )
        params.update(kwargs)
        return params

    def test_it(self):
        directive = self._makeOne(**self._getParams())
        directive.state = self._getDummyConfig()

        nodes = directive.run()
        self.assertEqual(1, len(nodes))


class VisitRevealjsTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import visit_revealjs
        return visit_revealjs

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummyNode(self, *args, **kwargs):

        class DummyNode(object):
            attrs = {
                'id': "id",
                'title': 'title',
                'noheading': False,
                'title-heading': 'h1',
                'subtitle': 'subtitle',
                'subtitle-heading': 'h2',
                'data-markdown': None,
                'data-transition': None,
                'data-background': None,
                'data-background-repeat': None,
                'data-background-size': None,
                'data-background-transition': None,
                'data-state': None,
                'data-separator': None,
                'data-vertical': None,
            }

            def __init__(self, **kwargs):
                self.attrs.update(kwargs)

            def get(self, attr, default=None):
                return self.attrs.get(attr, default)

            @property
            def rawsource(self):
                return "rawsource"

        return DummyNode(**kwargs)

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            fist_last = False

            def __init__(self, body):
                self.body = body

            def starttag(self, node, tag, **kwargs):
                ids = kwargs.pop('ids')
                if ids:
                    kwargs.update({'id': " ".join(ids)})
                attrs = ["{0}='{1}'".format(k, v) for k, v in kwargs.items()]
                attrs.sort()
                return "<{0} {1}>".format(tag, " ".join(attrs))

            def set_first_last(self, node):
                self.first_last = True

        return DummySelf(DummyBody())

    def test_it(self):
        from sphinxjp.themes.revealjs import compat
        dummyself = self._getDummySelf()
        dummynode = self._getDummyNode()

        self._callFUT(dummyself, dummynode)
        self.assertEqual([
            compat.text("<section id='id'>"),
            compat.text('<h1>title</h1>\n'),
            compat.text('<h2>subtitle</h2>\n')
        ], dummyself.body.content)

    def test_markdown(self):
        from sphinxjp.themes.revealjs import compat
        dummyself = self._getDummySelf()
        dummynode = self._getDummyNode(**{"data-markdown": "hoge"})

        self._callFUT(dummyself, dummynode)
        self.assertEqual(["<section data-markdown='hoge' id='id'>"],
                         dummyself.body.content)

        dummyself = self._getDummySelf()
        dummynode = self._getDummyNode(**{"data-markdown": ""})

        self._callFUT(dummyself, dummynode)
        self.assertEqual([
            compat.text("<section data-markdown='' id='id'>"),
            compat.text("<script type='text/template'>\n"),
            compat.text('# title \n'),
            compat.text('## subtitle \n'),
            compat.text('rawsource'),
            compat.text('</script>\n')
        ], dummyself.body.content)


class DepartRevealjsTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import depart_revealjs
        return depart_revealjs

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
        return DummySelf(DummyBody())

    def test_it(self):
        dummyself = self._getDummySelf()
        self._callFUT(dummyself, None)
        self.assertEqual('</section>\n', dummyself.body.content[0])


class VisitRvCodeTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import visit_rv_code
        return visit_rv_code

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummyNode(self, *args, **kwargs):
        class DummyNode(object):
            @property
            def rawsource(self):
                return "rawsource"
        return DummyNode()

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body

            def starttag(self, node, tag):
                try:
                    return "<{0}>".format(tag)
                except ValueError:
                    return "<%s>" % tag

        return DummySelf(DummyBody())

    def test_it(self):
        dummynode = self._getDummyNode()
        dummyself = self._getDummySelf()
        self._callFUT(dummyself, dummynode)
        self.assertEqual(
            '<pre>',
            dummyself.body.content[0]
        )
        self.assertEqual(
            '<code data-trim contenteditable>',
            dummyself.body.content[1]
        )
        self.assertEqual(
            'rawsource',
            dummyself.body.content[2]
        )


class DepartRvCodeTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import depart_rv_code
        return depart_rv_code

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
        return DummySelf(DummyBody())

    def test_it(self):

        dummyself = self._getDummySelf()
        self._callFUT(dummyself, None)
        self.assertEqual(
            '</code>',
            dummyself.body.content[0]
        )
        self.assertEqual(
            '</pre>\n',
            dummyself.body.content[1]
        )


class VisitRvSmallTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import visit_rv_small
        return visit_rv_small

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummyNode(self, *args, **kwargs):
        class DummyNode(object):
            @property
            def rawsource(self):
                return "rawsource"
        return DummyNode()

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
                self.first_last = False

            def starttag(self, node, tag):
                return "<{0}>".format(tag)

            def set_first_last(self, node):
                self.first_last = True

        return DummySelf(DummyBody())

    def test_it(self):
        dummynode = self._getDummyNode()
        dummyself = self._getDummySelf()
        self._callFUT(dummyself, dummynode)
        self.assertEqual(
            '<small>',
            dummyself.body.content[0]
        )
        self.assertTrue(dummyself.first_last)


class DepartRvSmallTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import depart_rv_small
        return depart_rv_small

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
        return DummySelf(DummyBody())

    def test_it(self):

        dummyself = self._getDummySelf()
        self._callFUT(dummyself, None)
        self.assertEqual(
            '</small>\n',
            dummyself.body.content[0]
        )


class VisitRvNoteTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import visit_rv_note
        return visit_rv_note

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummyNode(self, *args, **kwargs):
        class DummyNode(object):
            @property
            def rawsource(self):
                return "rawsource"
        return DummyNode()

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
                self.first_last = False

            def starttag(self, node, tag, **kwargs):
                class_name = kwargs.pop('class')
                return '<{0} class="{1}">'.format(tag, class_name)

            def set_first_last(self, node):
                self.first_last = True

        return DummySelf(DummyBody())

    def test_it(self):
        dummynode = self._getDummyNode()
        dummyself = self._getDummySelf()
        self._callFUT(dummyself, dummynode)
        self.assertEqual(
            '<aside class="notes">',
            dummyself.body.content[0]
        )
        self.assertTrue(dummyself.first_last)


class DepartRvNoteTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import depart_rv_note
        return depart_rv_note

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _getDummySelf(self, *args, **kwargs):
        class DummyBody(object):
            content = []

            def append(self, content):
                self.content.append(content)

        class DummySelf(object):
            def __init__(self, body):
                self.body = body
        return DummySelf(DummyBody())

    def test_it(self):

        dummyself = self._getDummySelf()
        self._callFUT(dummyself, None)
        self.assertEqual(
            '</aside>\n',
            dummyself.body.content[0]
        )


class SetupTest(unittest.TestCase):

    def _getTarget(self):
        from sphinxjp.themes.revealjs.directives import setup
        return setup

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyApp(object):

            nodes = []
            directives = {}

            def info(self, info):
                self.info = info

            def add_node(self, node, html):
                self.nodes.append((node, html))

            def add_directive(self, name, directive):
                self.directives.update({name: directive})

        dummy_app = DummyApp()
        self._callFUT(dummy_app)
        self.assertEqual('Initializing RevealJS theme directives',
                         dummy_app.info)

        from sphinxjp.themes.revealjs import directives as d

        self.assertEqual(d.revealjs, dummy_app.nodes[0][0])
        self.assertEqual((d.visit_revealjs, d.depart_revealjs),
                         dummy_app.nodes[0][1])

        self.assertEqual(d.rv_code, dummy_app.nodes[1][0])
        self.assertEqual((d.visit_rv_code, d.depart_rv_code),
                         dummy_app.nodes[1][1])

        self.assertEqual(d.rv_note, dummy_app.nodes[2][0])
        self.assertEqual((d.visit_rv_note, d.depart_rv_note),
                         dummy_app.nodes[2][1])

        self.assertEqual(d.rv_small, dummy_app.nodes[3][0])
        self.assertEqual((d.visit_rv_small, d.depart_rv_small),
                         dummy_app.nodes[3][1])

        self.assertEqual(d.RevealjsDirective, dummy_app.directives['revealjs'])
        self.assertEqual(d.RvCodeDirective, dummy_app.directives['rv_code'])
        self.assertEqual(d.RvNoteDirective, dummy_app.directives['rv_note'])
        self.assertEqual(d.RvSmallDirective, dummy_app.directives['rv_small'])
