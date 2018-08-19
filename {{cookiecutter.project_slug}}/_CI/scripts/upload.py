#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
from build import build
from library import execute_command

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.upload'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def upload():
    LOGGER.info('Executing build step initially')
    if not build():
        LOGGER.error('Errors caught on building the artifact, bailing out...')
        raise SystemExit(1)
    upload_command = ('twine upload dist/* '
                      '-u pypi-upload '
                      '--skip-existing '
                      '--repository-url https://upload.pypi.org/legacy/')
    LOGGER.info('Trying to upload built artifact...')
    exit_code = execute_command(upload_command)
    success = not exit_code
    if success:
        LOGGER.info('Successfully uploaded artifact! ;)')
    else:
        LOGGER.error('Errors found in uploading artifact! :(')
    raise SystemExit(exit_code)


if __name__ == '__main__':
    upload()
