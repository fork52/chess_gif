del /Q chess_gif.rst modules.rst create_frame.rst gif_maker.rst download_data.rst
REM del /Q "../chess_gif/__init__.py"
sphinx-apidoc --ext-autodoc -o . ../chess_gif/
REM echo.>"../chess_gif/__init__.py"
make html
