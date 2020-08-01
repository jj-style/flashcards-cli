import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flashcards-cli",
    version="1.0.0",
    description="Learn a set of flashcards",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jj-style/flashcards-cli",
    author="JJ Style",
    author_email="style.jj@protonmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "flashcards-cli=__main__:main",
        ]
    },
)