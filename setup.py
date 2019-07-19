#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-19 18:52
# @Author  : weihuchao
import os

import setuptools


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setuptools.setup(
    name="django_utils",
    version="0.0.1",
    python_requires="==2.7",
    author="weihuchao",
    author_email="weihuchao@gmail.com",
    description="django 1.9.9 utils",
    long_description=read('README.md'),
    url="https://github.com/weihuchao/django_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 0.0.1 ',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)
