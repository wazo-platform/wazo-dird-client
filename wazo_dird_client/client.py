# -*- coding: utf-8 -*-
# Copyright 2015-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient


class DirdClient(BaseClient):

    namespace = 'wazo_dird_client.commands'

    def __init__(self, host, port=443, prefix='/api/dird', version='0.1', **kwargs):
        super(DirdClient, self).__init__(
            host=host, port=port, prefix=prefix, version=version, **kwargs
        )
