from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyMusic_Player',
    version='0.0.1',
    description='A GUI Music Player with all the basic functions, which is developed using Tkinter',
    author= 'Kushal Bhavsar',
    url = 'https://github.com/Spidy20/PyMusic_Player',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['music player python', 'music player tkinter', 'music player gui'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['PyMusic_Player'],
    package_dir={'':'src'},
    install_requires = [
        'mutagen',
        'pygame',
        'ttkthemes'
    ]
)
