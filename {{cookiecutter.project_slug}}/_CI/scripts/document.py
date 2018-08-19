#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import os
import logging
import shutil
from bootstrap import bootstrap
from library import open_file, clean_up, execute_command

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.document'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def document():
    bootstrap()
    clean_up(('_build',
              os.path.join('docs', '_build'),
              os.path.join('docs', 'test_docs.rst'),
              os.path.join('docs', 'modules.rst')))
    exit_code = execute_command('make -C docs html')
    success = not exit_code
    if success:
        shutil.move(os.path.join('docs', '_build'), '_build')
        path = os.path.join('_build', 'html', 'index.html')
        open_file(path)
        LOGGER.info('Successfully built documentation ;)')
    else:
        LOGGER.error('Documentation creation errors found! :(')
    raise SystemExit(exit_code)


if __name__ == '__main__':
    document()
