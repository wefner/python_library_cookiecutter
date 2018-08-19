#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    pfile = Project().parsed_pipfile
    requirements = convert_deps_to_pip(pfile['packages'], r=False)
    test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
except ImportError:
    # get the requirements from the requirements.txt
    requirements = [line.strip()
                    for line in open('requirements.txt').readlines()
                    if line.strip() and not line.startswith('#')]
    # get the test requirements from the test_requirements.txt
    test_requirements = [line.strip()
                         for line in
                         open('dev-requirements.txt').readlines()
                         if line.strip() and not line.startswith('#')]

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

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
version = open('.VERSION').read()
{% set DEVELOPMENT_STATUS = ["Planning",
                             "Pre-Alpha",
                             "Alpha",
                             "Beta",
                             "Production/Stable",
                             "Mature",
                             "Inactive"] %}

setup(
    name='''{{ cookiecutter.project_slug }}''',
    version=version,
    description='''{{ cookiecutter.project_short_description }}''',
    long_description=readme + '\n\n' + history,
    author='''{{ cookiecutter.full_name }}''',
    author_email='''{{ cookiecutter.email }}''',
    url='''{{ cookiecutter.git_url }}''',
    packages=find_packages(where='.', exclude=('tests', 'hooks')),
    package_dir={'''{{ cookiecutter.project_slug }}''':
                 '''{{ cookiecutter.project_slug }}'''},
    include_package_data=True,
    install_requires=requirements,
    license='{{ cookiecutter.license }}',
    zip_safe=False,
    keywords='''{{ cookiecutter.project_slug }}{% for tag in cookiecutter.tags.split(',') %} {{ tag|trim }}{% endfor %}''',
    classifiers=[
        'Development Status :: {{ DEVELOPMENT_STATUS.index(cookiecutter.development_status) + 1 }} - {{ cookiecutter.development_status }}',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {{ cookiecutter.license }} License',
        'Natural Language :: English',
        {% for version in cookiecutter.compatible_versions.split(',') -%}
            'Programming Language :: Python :: {{ version|trim }}',
        {% endfor -%}
    ],
    test_suite='tests',
    tests_require=test_requirements,
    data_files=[('', BUILD_REQUIRED_FILES),
                ]
)
