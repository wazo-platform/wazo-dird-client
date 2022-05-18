# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_command import DirdRESTCommand


class StatusCommand(DirdRESTCommand):

    resource = 'status'

    def get(self, tenant_uuid=None):
        headers = self.build_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()
