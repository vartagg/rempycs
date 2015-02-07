#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

version = "1.0"

description = (
    'Simple Python .pyc files remover.'
)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = read('README.rst')

setup(
    name='rempycs',
    version='1.0',
    description=description,
    long_description=long_description,
    author='Vladimir Chub',
    author_email='vartagg@users.noreply.github.com',
    url='https://github.com/vartagg/rempycs',
    packages=[
        'rempycs',
    ],
    package_dir={'rempycs':
                 'rempycs'},
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='rempycs,pyc,pycs',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points = {
        'console_scripts': [
            'rempycs = rempycs:main'
        ],
    }
)
