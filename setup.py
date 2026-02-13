#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-munigeo',
    version='0.2.89+voltti.1',
    packages=['munigeo'],
    include_package_data=True,
    license='BSD License',
    description='A Django app for processing municipality-related geospatial data.',
    long_description=README,
    url='https://github.com/City-of-Helsinki/django-munigeo',
    author='Juha Yrjölä',
    author_email='juha.yrjola@iki.fi',
    install_requires=[
        'Django>=4.2',
        'requests',
        'django_mptt>=0.18.0',
        'django_modeltranslation',
        'six',
        'pyyaml',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
