# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.client import BaseClient


class DirdClient(BaseClient):

    namespace = 'dird_client.commands'

    def __init__(self, host, port=9489, version='0.1', **kwargs):
        super(DirdClient, self).__init__(host=host, port=port, version=version, **kwargs)
