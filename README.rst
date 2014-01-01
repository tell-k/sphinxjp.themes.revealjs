============================================
sphinxjp.themes.revealjs 0.1.1
============================================

reveal.js style presentation theme for Sphinx.

.. image:: https://drone.io/github.com/tell-k/sphinxjp.themes.revealjs/status.png
   :target: https://drone.io/github.com/tell-k/sphinxjp.themes.revealjs

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

     reveal.js is a framework for easily creating beautiful presentations using HTML. You'll need a browser with support for CSS 3D transforms to see it in its full glory.


Slides can be nested inside of other slides,

::

    .. revealjs:: 

     .. revealjs:: Vertical Slide1

      vertical slide1 

     .. revealjs:: Vertical Slide2

      vertical slide2

     .. revealjs:: Vertical Slide3

      vertical slide3


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


Requirement
=============
* Python 2.7 or later
* Sphinx 1.2.x or later.

Using
=============
* Reveal.js
* jQuery 1.10.2

License
=======

* sphinxjp.themes.revealjs Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
* `reveal.js is licensed under the MIT licence <https://github.com/hakimel/reveal.js/blob/master/LICENSE>`_.

See the LICENSE file for specific terms.

