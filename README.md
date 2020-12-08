# chess_gif : Convert chess PGNs to GIFs

**[chess_gif][repo-url] is a python library for easily making GIFs of chess games in `PGN` (Portable Game Notation) format which is the standard plain text format for recording chess games. chess_gif allows users to create highly customizable and optimized GIFs from the PGN files of their chess games.**

<p align="center">
  <a href="https://github.com/fork52/chess_gif/blob/master/LICENSE">
      <img alt="MIT License" src="https://img.shields.io/github/license/fork52/chess_gif?style=for-the-badge" />
  </a>
  <a href="https://github.com/fork52/chess_gif">
      <img alt="Code-Size" src="https://img.shields.io/github/repo-size/fork52/chess_gif?color=orange&style=for-the-badge" />
  </a>
  <a href="https://chess-gif.readthedocs.io/en/latest/?badge=latest">
      <img alt="Documentation" src="https://readthedocs.org/projects/chess-gif/badge/?version=latest&style=for-the-badge" />
  </a>
  <a href="https://pepy.tech/project/chess-gif">
      <img alt="Downloads" src="https://pepy.tech/badge/chess-gif" />
  </a>
  
</p>

<!--
[![MIT License][license-img]][license-url]
[![Code size][codesize-img]][repo-url]
[![Documentation Status](https://readthedocs.org/projects/chess-gif/badge/?version=latest)](https://chess-gif.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/chess-gif)](https://pepy.tech/project/chess-gif)
-->

## Installation

You can install chess_gif from [PyPI][pypi-link].

```
pip install chess_gif
```

**chess_gif** requires [pyvips][pyvips] and [pygifsicle][pygifsicle] as its dependencies:

1. Windows users need to download the pyvip's binaries and add `vips-dev-x.y\bin` to their `PATH` variable for its installation. You can download the binaries by [clicking here][pyvips-bin]. Linux and macOS users need not worry about this and can simply skip this step. For further details, refer [pyvip's installation guide][pyvips-install].

2. While running the installation, on MacOS the setup will automatically install gifsicle using [Brew](https://brew.sh/).  

   On Linux you will need to install gifsicle using apt-get as follows:

       sudo apt-get install gifsicle 

   On Windows you will need to download and install the [appropriate port of the library][gifsicle-port] for your OS. Add the path to `gifsicle.exe` file to your `PATH` variable.


## Documentation
Check out the documentation: [chess_gif docs](https://chess-gif.readthedocs.io)

## Usage Example

This is how a sample PGN file looks like. 

```
[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6
23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5
hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5
35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6
Nf2 42. g4 Bd3 43. Re6 1/2-1/2
```

Save this text in a file with .pgn extension.

Run the following code to create a GIF !

```python3 
    >>> from chess_gif.gif_maker import Gifmaker
    >>> obj = Gifmaker(pgn_file_path, h_margin = 20 , v_margin = 80 )
    >>> obj.make_gif('chess_game.gif')
```

The GIF should be generated in your current working directory.

<p align="center">
<img src="https://github.com/fork52/chess_gif/blob/master/docs/chess_game.gif" 
width="55%" height="55%">
</p>


## Dependencies

1. [python-chess][python-chess] : python-chess is a pure Python chess library with move generation, move validation and support for common formats. chess_gif uses python-chess for parsing pgn files and also for creating a board represenation of the chess games.

2. [Python Imaging Library][PIL] : Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. 

3. [imageio][imageio] : Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, video, volumetric data, and scientific formats. It is cross-platform, runs on Python 3.5+, and is easy to install. chess_gif is using imageio for creating the GIFs from frames generated using PIL.

4. [pyvips][pyvips] : The module wraps the libvips image processing library. It needs the libvips shared library on your library search path, version 8.2 or later. The library has been utilized in chess_gif for svg rendering.

5. [pygifsicle][pygifsicle]: Python package wrapping the gifsicle library for editing and optimizing gifs.

## Credits
* The piece themes used for the repository have been taken from the publicly available themes taken from [lichess.org's][lichess] amazing [repository-lila][lichess-repo].

* [python-chess's][python-chess] pgn parser made it extremely easy for parsing the PGN files for rendering GIFs.


## License
The repository is licensed under [MIT License][license-url] .

## Contributing

1. Fork it (<https://github.com/fork52/chess_gif/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[imageio]:https://github.com/imageio/imageio
[license-url]:https://github.com/fork52/chess_gif/blob/master/LICENSE
[license-img]:https://img.shields.io/github/license/fork52/chess_gif
[repo-url]:https://github.com/fork52/chess_gif
[lichess]:https://lichess.org/
[lichess-repo]:https://github.com/ornicar/lila
[python-chess]:https://python-chess.readthedocs.io/en/latest
[PIL]:https://pypi.org/project/Pillow/
[pyvips-install]:https://libvips.github.io/pyvips/README.html#non-conda-install
[pyvips]:https://github.com/libvips/pyvips
[pyvips-bin]:https://libvips.github.io/libvips/install.html
[pygifsicle]:https://github.com/LucaCappelletti94/pygifsicle
[gifsicle-port]:https://eternallybored.org/misc/gifsicle/
[pypi-link]:https://pypi.org/project/chess-gif/
[codesize-img]:https://img.shields.io/github/repo-size/fork52/chess_gif?color=orange

