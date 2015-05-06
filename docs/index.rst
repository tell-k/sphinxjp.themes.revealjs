=================================================
sphinxjp.themes.revealjs
=================================================

.. revealjs:: sphinxjp.themes.revealjs
 :title-heading: h2
 :subtitle: REVEAL.JS presentation style theme for Sphinx
 :subtitle-heading: h3

 .. rv_small::

  Created by `tell-k <http://github.com/tell-k>`_ / `@tell-k <http://twitter.com/tell_k>`_

.. revealjs:: Heads Up

 reveal.js is a framework for easily creating beautiful presentations using HTML. You'll need a browser with support for CSS 3D transforms to see it in its full glory.

 .. rv_note::

  Oh hey, these are some notes. They'll be hidden in your presentation, but you can see them if you open the speaker notes window (hit 's' on your keyboard).

.. revealjs::

 .. revealjs:: Vertical Slides

  Slides can be nested inside of other slides,
  try pressing |down_link|.

  .. image:: images/arrow.png
   :target: ""
   :class: navigate-down

  .. |down_link| raw:: html

   <a href="#" class="navigate-down">down</a>

 .. revealjs:: Basement Level 1

  Press down or up to navigate.

 .. revealjs:: Basement Level 2

  Cornify

  .. image:: images/cornify.gif
   :target: http://cornify.com
   :width: 280
   :height: 326

 .. revealjs:: Basement Level 3

  That's it, time to go back up.

  .. raw:: html

   <a href="#/2" class="image">
   <img width="178" height="238" src="/_images/arrow.png" alt="Up arrow" style="-webkit-transform: rotate(180deg);">
   </a>

.. revealjs:: Slides

 Not a coder? No problem. There's a fully-featured visual editor for authoring these, try it out at `http://slid.es <http://slid.es>`_.

.. revealjs:: Point of View

 Press **ESC** to enter the slide overview.

 Hold down alt and click on any element to zoom in on it using `zoom.js <http://lab.hakim.se/zoom-js>`_. Alt + click anywhere to zoom back out.

.. revealjs:: Works in Mobile Safari

 Try it out! You can swipe through the slides and pinch your way to the overview.

.. revealjs:: Marvelous Unordered List

 * No order here
 * Or here
 * Or here
 * Or here

.. revealjs:: Fantastic Ordered List

 #. One is smaller than...
 #. Two is smaller than...
 #. Three!

.. revealjs:: Tabular Tables

 .. list-table::
   :header-rows: 1

   * - Item
     - Value
     - Quantity
   * - Apple
     - $1
     - 7
   * - Lemonade
     - $2
     - 18
   * - Bread
     - $3
     - 2

.. revealjs:: Markdown support
 :data-markdown:

 For those of you who like that sort of thing. Instructions and a bit more info available [here](https://github.com/hakimel/reveal.js#markdown).

 ```
 .. revealjs:: Markdown support
  :data-markdown:

  For those of you who like that sort of thing. Instructions and a bit
  more info available[here](https://github.com/hakimel/reveal.js#markdown).
 ```

.. revealjs:: External Markdown
 :data-markdown: _static/external.md
 :data-separator: ^\n\n\n
 :data-separator-vertical: ^\n\n
 :data-separator-notes: ^Speaker:


.. revealjs:: Transition Styles
 :id: transitions

 You can select from different transitions, like:

 `Convex <?transition=convex#/transitions>`_ -
 `None <?transition=none#/transitions>`_ -
 `Fade <?transition=fade#/transitions>`_ -
 `Slide <?transition=slide#/transitions>`_ -
 `Concave <?transition=concave#/transitions>`_ -
 `Zoom <?transition=zoom#/transitions>`_ -

.. revealjs:: Themes
 :id: themes

 reveal.js comes with a few themes built in:

 .. raw:: html

   <!-- Hacks to swap themes after the page has loaded. Not flexible and only intended for the reveal.js demo deck. -->
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/black.css'); return false;">Black (default)</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/white.css'); return false;">White</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/league.css'); return false;">League</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/sky.css'); return false;">Sky</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/beige.css'); return false;">Beige</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/simple.css'); return false;">Simple</a> <br>
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/serif.css'); return false;">Serif</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/night.css'); return false;">Night</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/moon.css'); return false;">Moon</a> -
   <a href="#" onclick="document.getElementById('theme').setAttribute('href','_static/css/theme/solarized.css'); return false;">Solarized</a>


.. revealjs:: Global State

 Set :code:`data-state: "something"` on a slide and :code:`"something"`
 will be added as a class to the document element when the slide is open. This lets you
 apply broader style changes, like switching the background.

.. revealjs:: Custom Events
 :data-state: customevent

 Additionally custom events can be triggered on a per slide basis by binding to the :code:`data-state` name.

 .. rv_code::

  Reveal.addEventListener( 'customevent', function() {
    console.log( '"customevent" has fired' );
  });

.. revealjs::

 .. revealjs:: Slide Backgrounds
  :data-background: #007777

  Set :code:`data-background: #007777` on a slide to change the full page background to the given color. All CSS color formats are supported.

  .. image:: images/arrow.png
   :target: "#"
   :class: image navigate-down
   :width: 178
   :height: 238
   :alt: "Down arrow"


 .. revealjs:: Image Backgrounds
  :data-background: _images/arrow.png

  .. rv_code::

   .. revealjs::
    :data-background: image.png;

 .. revealjs:: Repeated Image Backgrounds
  :data-background: _images/arrow.png
  :data-background-repeat: repeat
  :data-background-size: 100px

  .. rv_code::

   .. revealjs::
    :data-background: image.png
    :data-background-repeat: repeat
    :data-background-size: 100px

.. revealjs:: Background Transitions
 :data-transition: linear
 :data-background: #4d7e65
 :data-background-transition: slide

 Pass reveal.js the :code:`backgroundTransition: 'slide'` config argument to make backgrounds slide rather than fade.

.. revealjs:: Background Transition Override
 :data-transition: linear
 :data-background: #8c4738
 :data-background-transition: slide

 You can override background transitions per slide by using :code:`data-background-transition: slide`.

.. revealjs:: Clever Quotes

 These guys come in two forms, inline: |quote_text| and block:

 |blockquote_text|

 .. |quote_text| raw:: html

  <q cite="http://searchservervirtualization.techtarget.com/definition/Our-Favorite-Technology-Quotations">
   &ldquo;The nice thing about standards is that there are so many to choose from&rdquo;</q>

 .. |blockquote_text| raw:: html

  <blockquote cite="http://searchservervirtualization.techtarget.com/definition/Our-Favorite-Technology-Quotations">
  &ldquo;For years there has been a theory that millions of monkeys typing at random on millions of typewriters would
  reproduce the entire works of Shakespeare. The Internet has proven this theory to be untrue.&rdquo;
  </blockquote>

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

 Courtesy of `highlight.js <http://softwaremaniacs.org/soft/highlight/en/description/>`_.


.. revealjs:: Intergalactic Interconnections

 You can link between slides internally, `like this <#/2/3>`_.

.. revealjs::

 .. revealjs:: Fragmented Views

  .. rst-class:: fragment

   Hit the next arrow...

  .. raw:: html

   <ol>
   <li class="fragment"><code>any type</code></li>
   <li class="fragment"><em>of view</em></li>
   <li class="fragment"><strong>fragments</strong></li>
   </ol>

  .. rv_note::

   This slide has fragments which are also stepped through in the notes window.

 .. revealjs:: Fragment Styles

  There's a few styles of fragments, like:

  .. rst-class:: fragment grow

   grow

  .. rst-class:: fragment shrink

   shrink

  .. rst-class:: fragment roll-in

   roll-in

  .. rst-class:: fragment fade-out

   fade-out

  .. rst-class:: fragment highlight-red

   highlight-red

  .. rst-class:: fragment highlight-green

   highlight-green

  .. rst-class:: fragment highlight-blue

   highlight-blue

.. revealjs:: Spectacular image!

 .. image:: images/meny.png
  :target: http://lab.hakim.se/meny/
  :width: 320
  :height: 299
  :alt: Meny

.. revealjs:: Export to PDF

 Presentations can be `exported to PDF <https://github.com/hakimel/reveal.js#pdf-export>`_, below is an example that's been uploaded to SlideShare.

 .. raw::html

  <iframe id="slideshare" src="http://www.slideshare.net/slideshow/embed_code/13872948" width="455" height="356" style="margin:0;overflow:hidden;border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen> </iframe>
  <script>
  document.getElementById('slideshare').attributeName = 'allowfullscreen';
  </script>

.. revealjs:: Take a Moment

 Press b or period on your keyboard to enter the 'paused' mode. This mode is helpful when you want to take distracting slides off the screen during a presentation.

.. revealjs:: Stellar Links

 * `Try the online editor <http://slid.es>`_
 * `Reveal.js Source code on GitHub <https://github.com/hakimel/reveal.js>`_
 * `sphinxjp.themes.revealjs Source code on GitHub <https://github.com/hakimel/reveal.js>`_

.. revealjs:: THE END
 :title-heading: h2
 :subtitle-heading: h3
 :subtitle: BY tell-k
