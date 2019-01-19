# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_dird_client.commands.helpers.base_source_command import SourceCommand


class Command(SourceCommand):

    resource = 'backends/phonebook/sources'
