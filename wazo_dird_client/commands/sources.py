# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class SourcesCommand(RESTCommand):

    resource = 'sources'
    _ro_headers = {'Accept': 'application/json'}

    def list(self, tenant_uuid=None, **kwargs):
        headers = dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        self.raise_from_response(r)
        return r.json()
