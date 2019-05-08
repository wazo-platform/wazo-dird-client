#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_dird_client',
    version='0.1',

    description='a simple client library for the wazo-dird HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'dird_client.commands': [
            'backends = wazo_dird_client.commands.backends:BackendsCommand',
            'conference_source = wazo_dird_client.commands.conference_source:Command',
            'csv_source = wazo_dird_client.commands.csv_source:Command',
            'csv_ws_source = wazo_dird_client.commands.csv_ws_source:Command',
            'directories = wazo_dird_client.commands.directories:DirectoriesCommand',
            'displays = wazo_dird_client.commands.displays:DisplaysCommand',
            'ldap_source = wazo_dird_client.commands.ldap_source:Command',
            'personal = wazo_dird_client.commands.personal:PersonalCommand',
            'phonebook = wazo_dird_client.commands.phonebook:PhonebookCommand',
            'wazo_source = wazo_dird_client.commands.wazo_source:Command',
            'personal_source = wazo_dird_client.commands.personal_source:Command',
            'phonebook_source = wazo_dird_client.commands.phonebook_source:Command',
            'profiles = wazo_dird_client.commands.profiles:ProfilesCommand',
            'sources = wazo_dird_client.commands.sources:SourcesCommand',
            'status = wazo_dird_client.commands.status:StatusCommand',
        ],
    }
)
