#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
test_{{ cookiecutter.repo_name }}
----------------------------------
Tests for `{{ cookiecutter.repo_name }}` module.
"""

from betamax.fixtures import unittest


class Test{{ cookiecutter.repo_name|capitalize }}(unittest.BetamaxTestCase):

    def setUp(self):
        """
        Test set up

        This is where you can setup things that you use throughout the tests. This method is called before every test.
        """
        pass

    def tearDown(self):
        """
        Test tear down

        This is where you should tear down what you've setup in setUp before. This method is called after every test.
        """
        pass
