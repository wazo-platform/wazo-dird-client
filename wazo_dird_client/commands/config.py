# -*- coding: utf-8 -*-
# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.command import DirdCommand


class ConfigCommand(DirdCommand):

    resource = 'config'

    def get(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def patch(self, config_patch):
        headers = self._get_headers()
        r = self.session.patch(self.base_url, headers=headers, json=config_patch)
        self.raise_from_response(r)
        return r.json()
