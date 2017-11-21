Python Library Template
=======================

Cookiecutter template for a Python library script. 


Remember, when creating a library with this template, to:

 * If you add more packages (subdirectories) than the one you create your project for, add them to the packages in setup.py
 * Write **tests** for you software and put them in tests/
 * **Document** your project.
  * Write inline documentation to describe your classes and methods
  * Populate the readme (./README.rst)
  * Write (a) usage example(s) (./USAGE.rst)
  * Write proper installation instructions (./INSTALLATION.rst)
  * Keep a (global) changelog in ./HISTORY.rst


Development Requirements
------------------------

These utilities / libraries are needed to start developing on with this template.

 * curl
 * make
 * cookiecutter
 * virtualwrapper
 * sphinx
 * setuptools


Development Workflow
--------------------

This template needs to be interpolated with the required variables. This is done through cookiecutter.

    $ cookiecutter python_library_cookiecutter
    
This will produce a wizard that will walk through all the required fields and once all questions are answered there will be a project directory in the current directory.

The workflow (after one has initialized git on the project which is out of the scope of this) supports the following steps

 * lint
 * test
 * build
 * document
 * upload
 * graph
 
These actions are supported out of the box by the corresponding scripts under _CI/scripts directory with sane defaults based on best practices.
The following aliases will be very handy on bash

    $ alias _bootstrap='_CI/scripts/bootstrap'
    $ alias _lint='_CI/scripts/lint'
    $ alias _test='_CI/scripts/test'
    $ alias _build='_CI/scripts/build'
    $ alias _upload='_CI/scripts/upload'
    $ alias _document='_CI/scripts/document'
    $ alias _tag='_CI/scripts/tag'
    $ alias _graph='_CI/scripts/graph'
    
The bootstrap script creates a .{{cookiecutter.project_slug}} directory inside the project directory hosting the virtual environment.
It is called by all other scripts before they do anything. So one could simple start by calling _lint and that would set up everything before it tried to actually lint the project

Once the code is ready to be delivered the _tag script should be called accepting one of three arguments, patch, minor, major following the semantic versioning scheme.
So for the initial delivery one would call

    $ _tag minor
    
which would bump the version of the project to 0.1.0 tag it in git and do a push.


So the full workflow after git is initialized is:

 * repeat as necessary (of course it could be test - code - lint :) )
   * code
   * lint 
   * test
 * commit and push
 * develop more through the code-lint-test cycle
 * tag (with the appropriate argument)
 * build
 * upload (if you want to host your package in pypi)
 * document (of course this could be run at any point)


Important Information
=====================

This template assumes some stuff about the structure of the project.
So when building a package out of this **do not** simple call

    $ python setup.py sdist bdist_egg
    
**as this will produce an unusable artifact with files missing.** 
Instead use the provided build and upload scripts that create all the necessary files in the artifact.