#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# File: {{cookiecutter.repo_name}}.py
"""
Main module file

Put your classes here
"""

import logging

__author__ = '''{{cookiecutter.full_name}} <{{cookiecutter.email}}>'''
__docformat__ = 'plaintext'
__date__ = '''{{cookiecutter.release_date}}'''

# This is the main prefix used for logging
LOGGER_BASENAME = '''{{cookiecutter.repo_name}}'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())
