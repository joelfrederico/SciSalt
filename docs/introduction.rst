.. _introduction:

Introduction
============

This is the documentation for a Python package designed to make scientific data analysis easier. The main objective is to create a collection of interconnected methods frequently needed to visualize and analyze data using Numpy, Scipy, Matplotlib, and PyQt.

Prerequisites
-------------

Python 3
^^^^^^^^

:mod:`scisalt` works with Python 3 and up, which should be installed via apt-get on \*nix, `Macports <https://www.macports.org/>`_ on Apple machines, or downloaded from https://www.python.org/downloads/.

HDF5 and h5py
^^^^^^^^^^^^^

While technically :mod:`scisalt` only depends on `h5py <http://www.h5py.org/>`_, :mod:`h5py` depends on `HDF5 <https://www.hdfgroup.org/HDF5/>`_. :mod:`h5py` can be installed via `pip <https://pypi.python.org/pypi/pip>`_::

        pip install h5py

However, `HDF5 <https://www.hdfgroup.org/HDF5/>`_ may need to be installed at the system level via apt-get or `Macports <https://www.macports.org/>`_.

It is possible to download or compile `HDF5 <https://www.hdfgroup.org/HDF5/>`_ and `h5py <http://www.h5py.org/>`_ from source::

* https://www.hdfgroup.org/HDF5/release/obtain5.html
* https://pypi.python.org/pypi/h5py

NumPy
^^^^^

:mod:`scisalt` depends on `NumPy <http://www.numpy.org/>`_ to manipulate data. `NumPy <http://www.numpy.org/>`_ has dependencies such as BLAS, LAPACK, and ATLAS, which makes downloading building form source is difficult. Installation via apt-get or `Macports <https://www.macports.org/>`_ is highly recommended in order to handle these dependencies. It is possible to `download <http://www.scipy.org/scipylib/download.html>`_ or to `build from source <http://www.scipy.org/scipylib/building/index.html#building>`_.

PyQt4
^^^^^

:mod:`scisalt` requires `PyQt4 <http://www.riverbankcomputing.com/software/pyqt/download>`_, which has dependencies of its own. Installation via apt-get or `Macports <https://www.macports.org/>`_ is highly recommended in order to handle these dependencies.

It is possible, although difficult, to `install from source <http://pyqt.sourceforge.net/Docs/PyQt4/installation.html>`_, including dependencies. If you would like to run on a \*nix machine without access to apt-get, you may have to compile from source. It is possible to `build against Qt 5 <http://pyqt.sourceforge.net/Docs/PyQt4/qt_v5.html>`_.

Installation
------------

There are a few ways to install :mod:`scisalt`. If you are unsure or want something more reliable (and also updated less frequently), install from PyPI.

.. _from-pypi:

From PyPI
^^^^^^^^^

You can install the most recent `SciSalt version <https://pypi.python.org/pypi/scisalt>`_ using `pip <https://pypi.python.org/pypi/pip>`_::

        sudo pip install scisalt

This will install :mod:`scisalt` in your Python installation’s site-packages directory.

The PyPI site is found at https://pypi.python.org/pypi/scisalt.

From the tarball release
^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the most recent tarball from the `download page <https://pypi.python.org/pypi/scisalt>`_
#. Unpack the tarball
#. ``sudo python setup.py install``

*Note that you have to have setuptools installed.*

This will install :mod:`scisalt` into your Python installation’s site-packages directory.

Installing the development version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install `git <https://git-scm.com/>`_ (available through Linux's apt-get and `Macports <https://www.macports.org/>`_ as well)
#. ``git clone git@github.com:joelfrederico/SciSalt.git``
#. ``cd SciSalt``
#. ``python setup.py develop``

*Note that you have to have setuptools installed.*
