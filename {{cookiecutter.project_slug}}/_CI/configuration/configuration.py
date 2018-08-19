import os
import json

current_file_path = os.path.dirname(os.path.abspath(__file__))
files_path = os.path.abspath(os.path.join(current_file_path, '..', 'files'))

LOGGING_LEVEL = json.loads(open(os.path.join(files_path,
                                           'logging_level.json'), 'r' ).read()).get('level').upper()
ENVIRONMENT_VARIABLES = json.loads(open(os.path.join(files_path,
                                                     'environment_variables.json'), 'r' ).read())
PREREQUISITES = json.loads(open(os.path.join(files_path,
                                           'prerequisites.json'), 'r' ).read())

BUILD_REQUIRED_FILES = ('.VERSION',
                        'LICENSE',
                        'AUTHORS.rst',
                        'CONTRIBUTING.rst',
                        'HISTORY.rst',
                        'README.rst',
                        'USAGE.rst',
                        'Pipfile',
                        'Pipfile.lock',
                        'requirements.txt',
                        'dev-requirements.txt')

LOGGERS_TO_DISABLE = ['sh.command',
                      'sh.command.process',
                      'sh.command.process.streamreader',
                      'sh.streamreader',
                      'sh.stream_bufferer']
