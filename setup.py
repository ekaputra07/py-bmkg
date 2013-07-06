#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "py-bmkg",
    version = "0.1.0",
    url = 'https://github.com/ekaputra07/py-bmkg',
    description = 'A Python wrapper for accessing earth quake, climate data of Indonesia based on BMKG (http://data.bmkg.go.id/).',
    license = 'MIT License',
    author = 'Eka Putra',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

