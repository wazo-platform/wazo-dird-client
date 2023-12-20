#!/usr/bin/env python3
# Copyright 2014-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='wazo_dird_client',
    version='0.1',
    description='a simple client library for the wazo-dird HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_dird_client.commands': [
            'backends = wazo_dird_client.commands.backends:BackendsCommand',
            'conference_source = wazo_dird_client.commands.conference_source:Command',
            'config = wazo_dird_client.commands.config:ConfigCommand',
            'csv_source = wazo_dird_client.commands.csv_source:Command',
            'csv_ws_source = wazo_dird_client.commands.csv_ws_source:Command',
            'directories = wazo_dird_client.commands.directories:DirectoriesCommand',
            'displays = wazo_dird_client.commands.displays:DisplaysCommand',
            'graphql = wazo_dird_client.commands.graphql:GraphQLCommand',
            'ldap_source = wazo_dird_client.commands.ldap_source:Command',
            'personal = wazo_dird_client.commands.personal:PersonalCommand',
            'phonebook = wazo_dird_client.commands.phonebook:PhonebookCommand',
            (
                'phonebook_deprecated = wazo_dird_client.commands.phonebook_deprecated:'
                'DeprecatedPhonebookCommand'
            ),
            'wazo_source = wazo_dird_client.commands.wazo_source:Command',
            'personal_source = wazo_dird_client.commands.personal_source:Command',
            'phonebook_source = wazo_dird_client.commands.phonebook_source:Command',
            'profiles = wazo_dird_client.commands.profiles:ProfilesCommand',
            'sources = wazo_dird_client.commands.sources:SourcesCommand',
            'status = wazo_dird_client.commands.status:StatusCommand',
        ],
    },
)
