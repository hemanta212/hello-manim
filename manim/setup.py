#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manimlib',
 'manimlib.animation',
 'manimlib.camera',
 'manimlib.chanimlib',
 'manimlib.container',
 'manimlib.for_3b1b_videos',
 'manimlib.mobject',
 'manimlib.mobject.svg',
 'manimlib.mobject.types',
 'manimlib.once_useful_constructs',
 'manimlib.scene',
 'manimlib.utils']

package_data = \
{'': ['*'], 'manimlib': ['files/*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'colour>=0.1.5,<0.2.0',
 'numpy>=1.19.4,<2.0.0',
 'opencv-python>=4.4.0.46,<5.0.0.0',
 'pillow>=8.0.1,<9.0.0',
 'progressbar>=2.5,<3.0',
 'pycairo>=1.20.0,<2.0.0',
 'pydub>=0.24.1,<0.25.0',
 'pygments>=2.7.3,<3.0.0',
 'scipy>=1.5.4,<2.0.0',
 'tqdm>=4.54.1,<5.0.0']

entry_points = \
{'console_scripts': ['manim = manimlib:main']}

setup_kwargs = {
    'name': 'manimlib',
    'version': '0.1.13',
    'description': 'Manim with chanim support',
    'long_description': None,
    'author': 'hemanta212',
    'author_email': 'sharmahemanta.212@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
    'setup_requires': ['pbr'],
    'pbr': True,

}


setup(**setup_kwargs)
