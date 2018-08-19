#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
import os
from time import sleep

# this needs to be imported first as it manipulates the path
from bootstrap import bootstrap
from library import (open_file,
                     clean_up,
                     execute_command,
                     save_requirements)

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.test'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def test():
    bootstrap()
    clean_up('test-output')
    os.mkdir('test-output')
    exit_code = execute_command('pipenv lock')
    success = not exit_code
    if success:
        LOGGER.info('Successfully locked dependencies ;)')
    else:
        LOGGER.error('Could not lock dependencies, quiting... :(')
        raise SystemExit(1)
    save_requirements()
    exit_code = execute_command('tox')
    success = not exit_code
    if success:
        open_file(os.path.join('test-output', 'coverage', 'index.html'))
        sleep(0.5)
        open_file(os.path.join('test-output', 'nosetests.html'))
        LOGGER.info('No testing errors found! ;)')
    else:
        LOGGER.error('Testing errors found! :(')
    raise SystemExit(exit_code)


if __name__ == '__main__':
    test()
