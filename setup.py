#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#from nufi import __version__ as version
version = '0.1'

setup(
    name='nufi',
    version=version,
    description='Unix command line filter for processing numeric data',
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    url='https://github.com/lmaurits/nufi',
    license="BSD (3 clause)",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
    scripts=['bin/nufi',],
    packages = ['nufi',],
    requires=['scipy'],
    install_requires=['scipy']

)
