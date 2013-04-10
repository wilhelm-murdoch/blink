#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from version import __version__

setup(
    name='blink',
    version=__version__,
    description='Create jQuery-like events for your Python app.',
    author='Wilhelm Murdoch',
    author_email='wilhelm.murdoch@gmail.com',
    url='http://www.thedrunkenepic.com/',
    packages=find_packages(exclude=['tests']),
    setup_requires=[
        'nose==1.1.2',
        'yanc==0.2.3'
    ]
)