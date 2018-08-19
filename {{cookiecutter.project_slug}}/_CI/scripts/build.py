#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
import os
import shutil

from bootstrap import bootstrap
from configuration import BUILD_REQUIRED_FILES
from library import execute_command, clean_up, save_requirements

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.build'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def build():
    bootstrap()
    clean_up(('build', 'dist'))
    exit_code = execute_command('pipenv lock')
    success = not exit_code
    if success:
        LOGGER.info('Successfully created lock file ;)')
    else:
        LOGGER.error('Errors creating lock file! :(')
        raise SystemExit(1)
    save_requirements()
    for file in BUILD_REQUIRED_FILES:
        shutil.copy(file, os.path.join('{{cookiecutter.project_slug}}', file))
    exit_code = execute_command('python setup.py sdist bdist_egg')
    success = not exit_code
    if success:
        LOGGER.info('Successfully built artifact ;)')
    else:
        LOGGER.error('Errors building artifact! :(')
    clean_up([os.path.join('{{cookiecutter.project_slug}}', file)
              for file in BUILD_REQUIRED_FILES])
    return success


if __name__ == '__main__':
    raise SystemExit(not build())
