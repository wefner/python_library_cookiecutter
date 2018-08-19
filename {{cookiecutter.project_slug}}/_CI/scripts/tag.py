#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import argparse
import logging
from bootstrap import bootstrap
from gitwrapperlib import Git
from library import bump


# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.tag'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


def check_branch():
    git = Git()
    if not git.get_current_branch() == 'master':
        print("Tagging is only supported on master, you should not tag a branch, exiting!")
        raise SystemExit(1)


def push():
    git = Git()
    current_version = open('.VERSION', 'r').read()
    git.commit('Set version to {}'.format(current_version), '.VERSION')
    git.tag(current_version)
    git.push()
    git.push('origin', current_version)


def get_arguments():
    parser = argparse.ArgumentParser(description='Handles bumping of the artifact version')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--major', help='Bump the major version', action='store_true')
    group.add_argument('--minor', help='Bump the minor version', action='store_true')
    group.add_argument('--patch', help='Bump the patch version', action='store_true')
    args = parser.parse_args()
    return args


def tag():
    bootstrap()
    args = get_arguments()
    check_branch()
    if args.major:
        bump('major')
    elif args.minor:
        bump('minor')
    elif args.patch:
        bump('patch')
    else:
        bump()
        raise SystemExit(0)
    push()


if __name__ == '__main__':
    tag()
