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