.. chess_gif documentation master file, created by
   sphinx-quickstart on Sun Aug 16 15:47:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to chess_gif's documentation!
=====================================

**chess_gif** is a python library for easily making GIFs of chess games in ``PGN`` (Portable Game Notation) 
format which is the standard plain text format for recording chess games.

**chess_gif** provides allows users to create highly customizable and optimized GIFs from the
``PGN`` files of your chess games.

Installation
------------

You can install chess_gif from `PyPI`_.

::

   pip install chess_gif

**chess_gif** requires `pyvips`_ and `pygifsicle`_ as its dependencies:

1. Windows users need to download the pyvip’s binaries and add
   ``vips-dev-x.y\bin`` to their ``PATH`` variable for its installation.
   You can download the binaries by `clicking here`_. Linux and macOS
   users need not worry about this and can simply skip this step. For
   further details, refer `pyvip’s installation guide`_.

2. While running the installation, on MacOS the setup will automatically
   install gifsicle using `Brew`_.

   On Linux you will need to install gifsicle using apt-get as follows:

   ::

      sudo apt-get install gifsicle 

   On Windows you will need to download and install the `appropriate
   port of the library`_ for your OS. Add the path to ``gifsicle.exe``
   file to your ``PATH`` variable.

.. _PyPI: https://pypi.org/project/chess-gif/
.. _pyvips: https://github.com/libvips/pyvips
.. _pygifsicle: https://libvips.github.io/libvips/install.html
.. _clicking here: https://libvips.github.io/libvips/install.html
.. _pyvip’s installation guide: https://libvips.github.io/pyvips/README.html#non-conda-install
.. _Brew: https://brew.sh/
.. _appropriate port of the library: https://eternallybored.org/misc/gifsicle/


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   modules

.. ..automodule:: gifmaker:
..    :members:
..    :undoc-members:
..    :show-inheritance:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
