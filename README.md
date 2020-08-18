# chess_gif

**[chess_gif](repo-url)** is a python library for easily making GIFs of chess games in `PGN` (Portable Game Notation) format which is the standard plain text format for recording chess games.

## Description
**chess_gif** provides allows users to create highly customizable and optimized GIFs from the PGN files of their chess games. 

## Dependencies

1. [python-chess](python-chess) : python-chess is a pure Python chess library with move generation, move validation and support for common formats. chess_gif uses python-chess for parsing pgn files and also for creating a board represenation of the chess games.

2. [Python Imaging Library](PIL) : Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. 

3. [imageio](imageio) : Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, video, volumetric data, and scientific formats. It is cross-platform, runs on Python 3.5+, and is easy to install. chess_gif is using imageio for creating the GIFs from frames generated using PIL.

4. [pyvips](pyvips) : The module wraps the libvips image processing library. It needs the libvips shared library on your library search path, version 8.2 or later. The library has been utilized in chess_gif for svg rendering.

5. [pygifsicle](pygifsicle): Python package wrapping the gifsicle library for editing and optimizing gifs.

## Credits
* The piece themes used for the repository have been taken from the publicly available themes taken from [lichess.org's](lichess) amazing [repository-lila](lichess-repo).

* [python-chess](python-chess)'s pgn parser made it extremely easy for parsing the PGN files for rendering GIFs.


## License
The repository is licensed under [MIT License](license-url).

## Contributing

1. Fork it (<https://github.com/fork52/chess_gif/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
<!-- [license-image]:https://img.shields.io/github/license/fork52/chess_gif -->
[license-url]:https://github.com/fork52/chess_gif/blob/master/LICENSE
[repo-url]:https://github.com/fork52/chess_gif
[lichess]:https://lichess.org/
[lichess-repo]:https://github.com/ornicar/lila
[python-chess]:https://python-chess.readthedocs.io/en/latest/
[PIL]:https://pypi.org/project/Pillow/
[imageio]:https://github.com/imageio/imageio
[pyvips-install]:https://libvips.github.io/pyvips/README.html#non-conda-install
[pyvips]:https://github.com/libvips/pyvips
[pygifsicle]:https://github.com/LucaCappelletti94/pygifsicle
