qt
==

PyQt4 is a class for creating GUI elements such as buttons, user input, and file dialog boxes. They can be embedded in a custom interface generated via Qt Creator. They are generally difficult to work with; `Matplotlib widgets <http://matplotlib.org/api/widgets_api.html>`_ are recommended over the PyQt4 interface where possible.

Opening GUI Elements
--------------------

.. class:: scisalt.qt.ButtonMsg(maintext, buttons, title=None, infotext=None)

   Base class :class:`PyQt4.QtGui.QMessageBox`

   A convenience function for creating a multi-buttion dialog box:

   * *title*: Title of dialog box
   * *maintext*: Prompt for user
   * *infotext*: Further information for user
   * *buttons*: Array of strings for buttons

   .. attribute:: clicked
      
      Returns the index of the clicked button.

   .. attribute:: clickedArray

      Returns a boolean array of which button was clicked

   .. method:: clickedButton

      Returns the button clicked.

   .. attribute:: clickedItem

      Returns the string of the clicked button.

.. class:: scisalt.qt.getDouble(title='', text='Double number:', **kwargs)

   Base class :class:`PyQt4.QtGui.QWidget`

   A convenience class for accessing :class:`PyQt4.QtGui.QInputDialog.getDouble(title, text, **kwargs)`

.. function:: scisalt.qt.getExistingDirectory(*args, **kwargs)

   A convenience function for :meth:`PyQt4.QtGui.QFileDialog.getExistingDirectory`

   Returns a string of the directory the user selects. Raises an :exc:`IOError` exception if a directory is not chosen.

   *\*args*, *\*\*kwargs* passed through to :meth:`PyQt4.QtGui.QFileDialog.getExistingDirectory`.

.. function:: scisalt.qt.getOpenFileName(*args, **kwargs)

   A convenience function for :meth:`PyQt4.QtGui.QFileDialog.getOpenFileName`

   Returns a string of the file the user selects. Raises an :exc:`IOError` exception if a file is not chosen.

   *\*args*, *\*\*kwargs* passed through to :meth:`PyQt4.QtGui.QFileDialog.getOpenFileName`.

Helper Objects
--------------

.. function:: scisalt.qt.get_app(argv=sys.argv)

   Tries to get the current :class:`PyQt4.QtGui.Qapplication` instance. If it fails, creates one. This is due to the fact that :mod:`PyQt4` it is only possible to create one :class:`PyQt4.QtGui.Qapplication` instance to be created per Python execution, or Python will crash.

.. class:: scisalt.qt.Rectangle(x, y, width, height, axes=None, alpha=0.5, fill=True)

   A convenience class for specifying and accessing an instance of :class:`matplotlib.patches.Rectangle((x, y), width, height, facecolor='w', edgecolor='r', alpha=alpha, fill=fill, axes=axes)`.

   .. attribute:: patch

      The :class:`matplotlib.patches.Rectangle`

   .. method:: get_height()

      Get the height in y

   .. method:: get_width()

      Get the width in x

   .. method:: get_x()

      Get the smaller x coordinate

   .. method:: get_y()

      Get the smaller y coordinate

   .. method:: get_xy()

      Get the smaller coordinates :code:`(x, y)`

   .. method:: set_xy()

      Set the smaller coordinates :code:`(x, y)`

   .. method:: set_height()

      Set the height in y

   .. method:: set_width()

      Set the width in x

   .. attribute:: x0

      The smaller x coordinate

   .. attribute:: x1

      The larger x coordinate

   .. attribute:: y0

      The smaller y coordinate

   .. attribute:: y1

      The larger y coordinate

