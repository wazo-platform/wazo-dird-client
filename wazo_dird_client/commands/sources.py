# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_command import DirdRESTCommand


class SourcesCommand(DirdRESTCommand):

    resource = 'sources'

    def list(self, tenant_uuid=None, token=None, **kwargs):
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        self.raise_from_response(r)
        return r.json()
