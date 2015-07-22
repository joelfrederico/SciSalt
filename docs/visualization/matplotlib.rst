matplotlib
==========

The :mod:`scisalt.matplotlib` module adds many useful wrappers for `matplotlib <http://matplotlib.org/contents.html>`_ classes and functions. In particular, it adds the color map `viridis <https://github.com/BIDS/colormap/blob/master/option_d.py>`_ as described in a presentation on YouTube, which will become the `new default <http://matplotlib.org/style_changes.html>`_ in `matplotlib <http://matplotlib.org/contents.html>`_:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xAoljeRJ3lU?rel=0" frameborder="0" allowfullscreen></iframe>

.. automodule:: scisalt.matplotlib
   :members:

.. method:: scisalt.matplotlib.tile

   Tile open figures. Finnicky on various OS's, so not imported by default.
