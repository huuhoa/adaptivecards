#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Huu Hoa NGUYEN",
    author_email='huuhoa@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Author adaptive cards in pure python",
    install_requires=requirements,
    license="MIT License",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='adaptivecards',
    name='adaptivecards',
    packages=find_packages(include=['adaptivecards']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/huuhoa/adaptivecards',
    version='0.3.0',
    zip_safe=False,
)

