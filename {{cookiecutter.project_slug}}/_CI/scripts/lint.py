#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
from bootstrap import bootstrap
from library import execute_command

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.lint'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def lint():
    bootstrap()
    exit_code = execute_command('prospector -DFM')
    success = not exit_code
    if success:
        LOGGER.info('No linting errors found! ;)')
    else:
        LOGGER.error('Linting errors found! :(')
    raise SystemExit(exit_code)


if __name__ == '__main__':
    lint()
