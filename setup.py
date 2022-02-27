import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess_gif", 
    version="0.0.3",
    author="Mrunank Mistry",
    author_email="mrunankmistry52@gmail.com",
    description="A package for creating GIFs of chess game from PGN files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fork52/PGN-to-GIF",
    packages=setuptools.find_packages(),
    install_requires=[
          'python-chess', 'pyvips' ,'imageio', 'pygifsicle', 'Pillow'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.10.0', 
    include_package_data = True,
    zip_safe = False,
    keywords = ['Chess GIF','PGN']

)