#!/usr/bin/env python3
# from distutils.core import setup

from setuptools import setup, find_packages

# here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()


setup(
   name='foo',
   version='1.0',
   license='MIT',
   keywords='foo very useful module',
   description='Python Distribution Utilities',
   author='testingry',
   author_email='testingry@gmail.com',
   url='https://github.com/',
   packages=find_packages(exclude=['*test', 'doc']),
   entry_points={
        "console_scripts": [
            'foo=foo.main:main'
        ]
    }
)

