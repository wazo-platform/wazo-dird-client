#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_dird_client',
    version='0.1',

    description='a simple client library for the wazo-dird HTTP interface',

    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'dird_client.commands': [
            'directories = wazo_dird_client.commands.directories:DirectoriesCommand',
            'personal = wazo_dird_client.commands.personal:PersonalCommand',
            'phonebook = wazo_dird_client.commands.phonebook:PhonebookCommand',
        ],
    }
)
