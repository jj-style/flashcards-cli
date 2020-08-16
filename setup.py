import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flashcards_cli",
    version="1.3.8",
    description="Learn a set of flashcards",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jj-style/flashcards-cli",
    author="JJ Style",
    author_email="style.jj@protonmail.com",
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["flashcards_cli"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "flashcards_cli=flashcards_cli.__main__:main",
        ]
    },
)