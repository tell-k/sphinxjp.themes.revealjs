# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.revealjs.directives
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes

from sphinx.util.compat import Directive

from sphinxjp.themes.revealjs import compat

__docformat__ = 'reStrructuredText'


class revealjs(nodes.General, nodes.Element):
    """ node for revealjs """


class rv_code(nodes.General, nodes.Element):
    """ node for revealjs code section """


class rv_small(nodes.General, nodes.Element):
    """ node for revealjs small text section """


class rv_note(nodes.General, nodes.Element):
    """ node for revealjs presentation note """


def heading(argument):
    """ directives choices for heading tag """
    return directives.choice(argument, ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'))


class RevealjsDirective(Directive):
    """ Reveal.JS slide entry  """

    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = False

    option_spec = {
        'id': directives.unchanged,
        'class': directives.class_option,
        'noheading': directives.flag,
        'title-heading': heading,
        'subtitle': directives.unchanged,
        'subtitle-heading': directives.unchanged,
        'data-autoslide': directives.unchanged,
        'data-markdown': directives.unchanged,
        'data-transition': directives.unchanged,
        'data-transition-speed': directives.unchanged,
        'data-background': directives.unchanged,
        'data-background-repeat': directives.unchanged,
        'data-background-size': directives.unchanged,
        'data-background-transition': directives.unchanged,
        'data-state': directives.unchanged,
        'data-separator': directives.unchanged,
        'data-separator-vertical': directives.unchanged,
        'data-separator-notes': directives.unchanged,
        'data-charset': directives.unchanged,
    }

    node_class = revealjs

    def run(self):
        """ build revealjs node """

        set_classes(self.options)

        text = '\n'.join(self.content)
        node = self.node_class(text, **self.options)

        self.add_name(node)

        if "data-markdown" not in self.options:
            self.state.nested_parse(self.content, self.content_offset, node)

        if self.arguments:
            node['title'] = " ".join(self.arguments)

        node['noheading'] = ('noheading' in self.options)

        options_list = (
            'id',
            'title-heading',
            'subtitle-heading',
            'data-autoslide',
            'data-transition',
            'data-transition-speed',
            'data-background',
            'data-background-repeat',
            'data-background-size',
            'data-background-transition',
            'data-state',
            'data-markdown',
            'data-separator',
            'data-separator-vertical',
            'data-separator-notes',
            'data-charset',
        )
        for option in options_list:
            if option in self.options:
                node[option] = self.options.get(option)
        return [node]


class RvSmallDirective(Directive):
    """
    Create small text tag.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    option_spec = {
        'class': directives.class_option,
    }
    node_class = rv_small

    def run(self):
        """ build rv_small node """

        set_classes(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class RvNoteDirective(Directive):
    """
    Directive for a notes tag.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    option_spec = {
        'class': directives.class_option,
    }
    node_class = rv_note

    def run(self):
        """ build rv_note node """
        set_classes(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class RvCodeDirective(Directive):
    """
    Directive for a code block with highlight.js
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    node_class = rv_code

    def run(self):
        """ build rv_code node """
        set_classes(self.options)
        self.assert_has_content()
        node = self.node_class('\n'.join(self.content), **self.options)
        return [node]


def visit_revealjs(self, node):
    """ build start tag for revealjs """
    section_attr = {}
    markdown_headings = {"h1": "#", "h2": "##", "h3": "###",
                         "h4": "####", "h5": "#####", "h6": "######"}

    if node.get("id"):
        section_attr.update({"ids": [node.get("id")]})

    attr_list = (
        'data-autoslide',
        'data-transition',
        'data-transition-speed',
        'data-background',
        'data-background-repeat',
        'data-background-size',
        'data-background-transition',
        'data-state',
        'data-markdown',
        'data-separator',
        'data-separator-vertical',
        'data-separator-notes',
        'data-charset',
    )
    for attr in attr_list:
        if node.get(attr) is not None:
            section_attr.update({attr: node.get(attr)})

    title = None
    if node.get("title") and not node.get('noheading'):
        title = node.get("title")

    title_heading = node.get('title-heading', 'h2')
    subtitle = node.get("subtitle")
    subtitle_heading = node.get('subtitle-heading', 'h3')
    if node.get("data-markdown") is not None:

        title_base = compat.text("%(heading)s %(title)s \n")
        title_text = None
        if title:
            title_text = title_base % dict(
                heading=markdown_headings.get(title_heading),
                title=title
            )

        subtitle_text = None
        if subtitle:
            subtitle_text = title_base % dict(
                heading=markdown_headings.get(subtitle_heading),
                title=subtitle
            )
    else:
        title_base = compat.text("<%(heading)s>%(title)s</%(heading)s>\n")
        title_text = None
        if title:
            title_text = title_base % dict(
                title=title,
                heading=title_heading)

        subtitle_text = None
        if subtitle:
            subtitle_text = title_base % dict(
                title=subtitle,
                heading=subtitle_heading)

    if node.get("data-markdown") is not None:
        self.body.append(self.starttag(node, 'section', **section_attr))
        if node.get("data-markdown") == compat.text(""):
            self.body.append("<script type='text/template'>\n")
            if title_text:
                self.body.append(title_text)
            if subtitle_text:
                self.body.append(subtitle_text)
            self.body.append(node.rawsource)
            self.body.append("</script>\n")
    else:
        self.body.append(self.starttag(node, 'section', **section_attr))
        if title_text:
            self.body.append(title_text)
        if subtitle_text:
            self.body.append(subtitle_text)
        self.set_first_last(node)


def depart_revealjs(self, node=None):
    """ build end tag for revealjs """
    self.body.append('</section>\n')


def visit_rv_code(self, node):
    """ build start tag for rv_code """

    self.body.append(self.starttag(node, 'pre'))
    self.body.append("<code data-trim contenteditable>")
    self.body.append(node.rawsource)


def depart_rv_code(self, node=None):
    """ build end tag for rv_code """

    self.body.append("</code>")
    self.body.append("</pre>\n")


def visit_rv_small(self, node):
    """ build start tag for rv_small """
    self.body.append(self.starttag(node, 'small'))
    self.set_first_last(node)


def depart_rv_small(self, node=None):
    """ build end tag for rv_small"""
    self.body.append("</small>\n")


def visit_rv_note(self, node):
    """ build start tag for rv_note """
    self.body.append(self.starttag(node, 'aside', **{'class': 'notes'}))
    self.set_first_last(node)


def depart_rv_note(self, node=None):
    """ build end tag for rv_note """
    self.body.append("</aside>\n")


def setup(app):
    """Initialize """
    app.info('Initializing RevealJS theme directives')
    app.add_node(revealjs, html=(visit_revealjs, depart_revealjs))
    app.add_node(rv_code, html=(visit_rv_code, depart_rv_code))
    app.add_node(rv_note, html=(visit_rv_note, depart_rv_note))
    app.add_node(rv_small, html=(visit_rv_small, depart_rv_small))
    app.add_directive('revealjs', RevealjsDirective)
    app.add_directive('rv_code', RvCodeDirective)
    app.add_directive('rv_note', RvNoteDirective)
    app.add_directive('rv_small', RvSmallDirective)
    return
