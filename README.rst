============================================
sphinxjp.themes.revealjs 0.2.0
============================================

reveal.js style presentation theme for Sphinx.

|travis| |coveralls| |downloads| |version| |license|


Output Sample
=============
:output: http://packages.python.org/sphinxjp.themes.revealjs/
:source: http://packages.python.org/sphinxjp.themes.revealjs/_sources/index.txt


Features
========
* provide ``revealjs`` directive for reveal.js presetation slide control.
* provide ``revealjs`` theme for render presetation.


Set up
======
Make environment with pip::

    $ pip install sphinxjp.themes.revealjs

Make environment with easy_install::

    $ easy_install sphinxjp.themes.revealjs


Convert Usage
=============
setup conf.py with::

    extensions = ['sphinxjp.themes.revealjs']
    html_theme = 'revealjs'
    html_use_index = False

and run::

    $ make html

Writing Custom Directives
=============================

revealjs
--------------------

This directive crate a slide section for reveal.js.

::

  .. revealjs:: Heads Up

   reveal.js is a framework for easily creating beautiful presentations using HTML. 
   You'll need a browser with support for CSS 3D transforms to see it in its full glory.


Slides can be nested inside of other slides,

::

  .. revealjs:: 

   .. revealjs:: Vertical Slide1

    vertical slide1 

   .. revealjs:: Vertical Slide2

    vertical slide2

   .. revealjs:: Vertical Slide3

    vertical slide3

You can set various options.

:: 

  # For example, you can write in Markdown syntax to use the data-markdown option.   

  .. revealjs::
     :data-markdown:

     ## Page title

     A paragraph with some text and a [link](http://hakim.se).

Other options

.. list-table::

   * - class
     - Set 'class' attribute to 'section' tag.
   * - noheading
     - 
   * - noheading
     - 
   * - title-heading
     - 
   * - subtitle
     - 
   * - subtitle-heading
     - 
   * - data-markdown
     - 
   * - data-transition
     - 
   * - data-transition-speed
     - 
   * - data-background
     - 
   * - data-background-repeat
     - 
   * - data-transition
     - 
   * - data-state
     - 
   * - data-separator
     - 
   * - data-vertical
     - 

rv_code
---------------------

::

    .. revealjs:: Pretty Code

     .. rv_code::

      function linkify( selector ) {
        if( supports3DTransforms ) {

          var nodes = document.querySelectorAll( selector );

          for( var i = 0, len = nodes.length; i &lt; len; i++ ) {
            var node = nodes[i];

            if( !node.className ) ) {
              node.className += ' roll';
            }
          };
        }
      }


rv_small
---------------------

This directive can be used when writing the text smaller.

::

    .. revealjs:: rv_small smaple

     .. rv_small::

      Created by `tell-k <http://github.com/tell-k>`_ / `@tell-k <http://twitter.com/tell_k>`_

rv_note
---------------------

This directive can be used when creating some notes for presenter. They'll be hidden in your presentation, but you can see them if you open the speaker notes window (hit 's' on your keyboard).

::

    .. revealjs:: Heads Up

     reveal.js is a framework for easily creating beautiful presentations using HTML. You'll need a browser with support for CSS 3D transforms to see it in its full glory.

     .. rv_note::

      Oh hey, these are some notes. They'll be hidden in your presentation, but you can see them if you open the speaker notes window (hit 's' on your keyboard).

Customize Config
=============================

You can change settings in conf.py

::

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

   # Theme (default/blood/beige/moon/night/serif/simple/sky/solarized)
   "theme": "blood",

   # Transition style (default/cube/page/concave/zoom/linear/fade/none)
   "transition": "default",

   # Transition speed (default/fast/slow)
   "transition_speed": "default",

   # Transition style for full page slide backgrounds (default/linear)
   "background_transition": "default",

   # Display the page number of the current slide
   "slide_number": False,

   # Flags if the presentation is running in an embedded mode,
   # i.e. contained within a limited portion of the screen
   "embedded": False,

   # Stop auto-sliding after user input
   "auto_slide_stoppable": True,

   # Hides the address bar on mobile devices
   "hide_address_bar": True,

   # Parallax background image
   # CSS syntax, e.g. "a.jpg"
   "parallax_background_image": 'a.jpg',

   # Parallax background size
   # CSS syntax, e.g. "3000px 2000px"
   "parallax_background_size": '3000px 2000px',

   # Focuses body when page changes visibility to ensure keyboard shortcuts work
   "focus_body_on_page_visibility_change": True,

   # Number of slides away from the current that are visible
   "view_distance": 3,

   # Enable plguin javascript for reveal.js
   "plugin_list": [
     "_static/plugin/leap/leap.js",
     "_static/plugin/multiplex/master.js",
     "_static/plugin/search/search.js",
     "_static/plugin/remotes/remotes.js"
     "_static/plugin/notes-server/client.js",
   ],

  }
 
Multiplexing
--------------------

see also: https://github.com/hakimel/reveal.js#multiplexing

conf.py::

  # set html_theme_options
  "multiplex": {
      "secret": None, # null so the clients do not have control of the master presentation
      "id": '1ea875674b17ca76', # id, obtained from socket.io server
      "url": 'example.com:80' # Location of your socket.io server
  },

  "plugin_list": [
    "//cdnjs.cloudflare.com/ajax/libs/socket.io/0.9.10/socket.io.min.js",
    "_static/plugin/multiplex/master.js",

    # and if you want speaker notes
    "_static/plugin/notes-server/client.js",
  ],

Leap Motion
--------------------

see also: https://github.com/hakimel/reveal.js#leap-motion

conf.py::

  # set html_theme_options
  "leap": {
     "autoCenter": True,
     "gestureDelay": 500,
     "naturalSwipe": False,
     "pointerOpacity": 0.5,
     "pointerColor": '#d80000',
     "pointerSize": 15,
     "pointerTolerance": 120,
  },

  "plugin_list": [
    "_static/plugin/leap/leap.js",
  ],

MathJax
--------------------

see also: https://github.com/hakimel/reveal.js#mathjax

conf.py::

  # set html_theme_options
  "math": {
      "mathjax": 'http://cdn.mathjax.org/mathjax/latest/MathJax.js',
      # See http://docs.mathjax.org/en/latest/config-files.html
      "config": 'TeX-AMS_HTML-full' 
  },

  "plugin_list": [
    "_static/plugin/math/math.js",
  ],

Setting with JS
--------------------------

conf.py::

  # set html_theme_options

  # loading custom js after RevealJs.initialize.
  "customjs": "reveal-configure.js",


Requirement
=============
* Python 2.7 or later
* Sphinx 1.2.x or later.

Using
=============
* Reveal.js 2.6.2
* jQuery 1.10.2

License
=======

* sphinxjp.themes.revealjs Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
* `reveal.js is licensed under the MIT licence <https://github.com/hakimel/reveal.js/blob/master/LICENSE>`_.

See the LICENSE file for specific terms.

.. |travis| image:: https://travis-ci.org/tell-k/sphinxjp.themes.revealjs.svg?branch=master
    :target: https://travis-ci.org/tell-k/sphinxjp.themes.revealjs


.. |coveralls| image:: https://coveralls.io/repos/tell-k/sphinxjp.themes.revealjs/badge.png
    :target: https://coveralls.io/r/tell-k/sphinxjp.themes.revealjs/
    :alt: coveralls.io

.. |downloads| image:: https://pypip.in/d/sphinxjp.themes.revealjs/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.revealjs/
    :alt: downloads

.. |version| image:: https://pypip.in/v/sphinxjp.themes.revealjs/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.revealjs/
    :alt: latest version

.. |license| image:: https://pypip.in/license/sphinxjp.themes.revealjs/badge.png
    :target: http://pypi.python.org/pypi/sphinxjp.themes.revealjs/
    :alt: license
