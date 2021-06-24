#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
__author__ = 'bigfish'
REQUIRED = [
    'randstr==0.1.2',
    'envoy==0.0.3',
    'PyGObject~=3.36'
]

setup(
    name='pydebtutorial',
    version='0.0.1',
    install_requires=REQUIRED,
    description='Simple Package(Example) for packaging python to Debian',
    author='bigfish',
    author_email='thebigfish@foxmail.com',
    license='GNU',
    url='https://github.com/',
    packages=['pydebtutorial'],
    entry_points={
        'console_scripts': [
            'pydebt=pydebtutorial.main:main',
        ]
    },
)
