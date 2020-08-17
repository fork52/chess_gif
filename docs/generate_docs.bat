del /Q chess_gif.rst modules.rst create_frame.rst gif_maker.rst download_data.rst
del /Q "../chess_gif/__init__.py"
sphinx-apidoc --ext-autodoc -o . ../chess_gif/
echo.>"../chess_gif/__init__.py"
make html
