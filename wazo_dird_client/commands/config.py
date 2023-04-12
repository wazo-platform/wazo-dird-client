# Copyright 2022-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.command import DirdCommand


class ConfigCommand(DirdCommand):
    resource = 'config'

    def get(self, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()
