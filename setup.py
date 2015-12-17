#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from os import path

setup(
    name='streamsMt',
    version = '0.1.0',
    description = 'Multithreaded stream oriented message processing.',

    author = 'Markus Peröbner',
    author_email = 'markus.peroebner@gmail.com',

    packages = find_packages(),
)
