# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class DirdRESTCommand(RESTCommand):

    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    _ro_headers = {'Accept': 'application/json'}

    def build_ro_headers(self, tenant_uuid, token):
        return self._build_headers(dict(self._ro_headers), tenant_uuid, token)

    def build_rw_headers(self, tenant_uuid, token):
        return self._build_headers(dict(self._rw_headers), tenant_uuid, token)

    def _build_headers(self, headers, tenant_uuid, token):
        if token:
            headers['X-Auth-Token'] = token

        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        return headers
