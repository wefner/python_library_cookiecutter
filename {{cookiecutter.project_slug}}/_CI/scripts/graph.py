#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import os
import logging
from bootstrap import bootstrap
from library import execute_command

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.graph'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def graph():
    bootstrap()
    os.chdir('graphs')
    create_graph_command = ('pyreverse '
                            '-o png '
                            '-A '
                            '-f PUB_ONLY '
                            '-p graphs {}').format(os.path.join('..', '{{cookiecutter.project_slug}}'))
    exit_code = execute_command(create_graph_command)
    success = not exit_code
    if success:
        LOGGER.info('Successfully created graph images ;)')
    else:
        LOGGER.error('Errors in creation of graph images found! :(')
    raise SystemExit(exit_code)


if __name__ == '__main__':
    graph()
