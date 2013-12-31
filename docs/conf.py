# -*- coding: utf-8 -*-
#
# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for reveal.js'
copyright = u'2013, tell-k'

version = '0.1.1'

# -- Options for HTML output ---------------------------------------------------

extensions = ['sphinxjp.themes.revealjs']
html_theme = 'revealjs'
html_use_index = False

# -- HTML theme options for `revealjs` style -------------------------------------

html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to "ja"
    "lang": "ja",

    # The "normal" size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    "width": 960,
    "height": 700,

    # Factor of the display size that should remain empty around the content
    "margin": 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    "min_scale": 0.2,
    "max_scale": 1.0,

    # Display controls in the bottom right corner
    "controls": True,

    # Display a presentation progress bar
    "progress": True,

    # Push each slide change to the browser history
    "history": True,

    # Enable keyboard shortcuts for navigation
    "keyboard": True,

    # Enable the slide overview mode
    "overview": True,

    # Vertical centring of slides
    "center": True,

    # Enables touch navigation on devices with touch input
    "touch": True,

    # Loop the presentation
    "loop": False,

    # Change the presentation direction to be RTL
    "rtl": False,

    # Turns fragments on and off globally
    "fragments": True,

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    "auto_slide": 0,

    # Enable slide navigation via mouse wheel
    "mouse_wheel": False,

    # Apply a 3D roll to links on hover
    "rolling_links": True,

    # Opens links in an iframe preview overlay
    "preview_links": False,

    # Theme (default/beige/moon/night/serif/simple/sky/solarized)
    "theme": "default",

    # Transition style (default/cube/page/concave/zoom/linear/fade/none)
    "transition": "default",

    # Transition speed (default/fast/slow)
    "transition_speed": "default",

    # Transition style for full page slide backgrounds (default/linear)
    "background_transition": "default",

    # Enable plguin javascript for reveal.js
    "plugin_list": ["search/search.js", "remotes/remotes.js"],

}
