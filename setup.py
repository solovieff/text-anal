# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="tubetone",
    version="0.1.2",
    description="Library to process youtube videos texts and analyze results.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solovieff/text-anal",
    author="Andrey Solovieff",
    author_email="solovieff.nnov@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Analysts",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["numpy", "pytube", "youtube_transcript_api", "pymorphy2", "pymongo[srv]", "dostoevsky"],
    entry_points={
        "console_scripts": [
            "tubetone=tubetone.__main__:main",
        ]
    },

)
