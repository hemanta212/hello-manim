# -*- coding: utf-8 -*-
"""
Backup setup.py for install
"""

import codecs
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.md'), 'r', 'utf-8') as f:
    readme = f.read()

packages = \
['manim.manimlib',
        ]

setup(
    name="manimlib",
    version="1.2.3",
    description='Manim with chanim support',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='hemanta212',
    author_email='sharmahemanta.212@gmail.com',
    url="https://hemanta212.github.io/blogger-cli",
    keywords=["jupyter notebook", "github pages", "blogger"],
    license="MIT",
    packages=packages,
    include_package_data=True,
    python_requires='>=3.5,<4.0',
    project_urls={
        'Bug Reports': 'https://github.com/hemanta212/blogger-cli/issues',
        'Source': 'https://github.com/hemanta212/blogger-cli/',
    }
)
