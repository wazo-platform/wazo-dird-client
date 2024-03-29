# Copyright 2019-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_source_command import SourceCommand


class Command(SourceCommand):
    resource = 'backends/personal/sources'
