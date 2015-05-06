# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for reveal.js'
copyright = u'2014, tell-k'

version = '0.3.0'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.revealjs']
html_theme = 'revealjs'
html_use_index = False

# -- HTML theme options for `revealjs` style ---------------------

html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to "ja"
    'lang': 'ja',

    # The "normal" size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    'width': 960,
    'height': 700,

    # Factor of the display size that should remain empty around the content
    'margin': 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    'min_scale': 0.2,
    'max_scale': 1.0,

    # Display controls in the bottom right corner
    'controls': True,

    # Display a presentation progress bar
    'progress': True,

    # Push each slide change to the browser history
    'history': True,

    # Enable keyboard shortcuts for navigation
    'keyboard': True,

    # Enable the slide overview mode
    'overview': True,

    # Vertical centring of slides
    'center': True,

    # Enables touch navigation on devices with touch input
    'touch': True,

    # Loop the presentation
    'loop': False,

    # Change the presentation direction to be RTL
    'rtl': False,

    # Turns fragments on and off globally
    'fragments': True,

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    'auto_slide': 0,

    # Enable slide navigation via mouse wheel
    'mouse_wheel': False,

    # Apply a 3D roll to links on hover
    'rolling_links': True,

    # Opens links in an iframe preview overlay
    'preview_links': False,

    # Theme (black/white/league/beige/sky/night/serif/simple/solarized)
    'theme': 'black',

    # Transition style (default(=convex)/none/fade/slide/concave/zoom)
    'transition': 'default',

    # Transition speed (default/fast/slow)
    'transition_speed': 'default',

    # Transition style for full page slide backgrounds
    # (default(=convex)/none/fade/slide/concave/zoom)
    'background_transition': 'default',

    # Display the page number of the current slide
    'slide_number': False,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    'embedded': False,

    # Stop auto-sliding after user input
    'auto_slide_stoppable': True,

    # Hides the address bar on mobile devices
    'hide_address_bar': True,

    # Parallax background image
    # CSS syntax, e.g. "a.jpg"
    # "parallax_background_image": '_static/bg.jpg',

    # Parallax background size
    # CSS syntax, e.g. "3000px 2000px"
    # "parallax_background_size": '2000px 900px',

    # Focuses body when page changes visibility
    # to ensure keyboard shortcuts work
    'focus_body_on_page_visibility_change': True,

    # Number of slides away from the current that are visible
    'view_distance': 3,

    # Enable plguin javascript for reveal.js
    # "plugin_list": [
    #  "_static/plugin/search/search.js",
    #  "_static/plugin/remotes/remotes.js"
    # ],

    # config for Multiplexing
    # "multiplex": {
    #   # None so the clients do not have control of the master presentation
    #   "secret": None,
    #   "id": '1ea875674b17ca76', # id, obtained from socket.io server
    #   "url": 'example.com:80' # Location of your socket.io server
    # },

    # config for Leap Motion
    # "leap": {
    #    "autoCenter": True,
    #    "gestureDelay": 500,
    #    "naturalSwipe": False,
    #    "pointerOpacity": 0.5,
    #    "pointerColor": '#d80000',
    #    "pointerSize": 15,
    #    "pointerTolerance": 120,
    # },

    # config for MathJax
    # "math": {
    #     "mathjax": 'http://cdn.mathjax.org/mathjax/latest/MathJax.js',
    #     # See http://docs.mathjax.org/en/latest/config-files.html
    #     "config": 'TeX-AMS_HTML-full'
    # },

    # loading custom js after RevealJs.initialize.
    # "customjs": "mysettings.js",
}

html_static_path = ['_static']
