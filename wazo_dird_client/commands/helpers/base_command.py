# -*- coding: utf-8 -*-
# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class DirdRESTCommand(RESTCommand):
    def build_headers(self, tenant_uuid=None, token=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        return self._build_headers(headers, token)

    # Keep only for compatibility with external plugins
    build_rw_headers = build_headers
    build_ro_headers = build_headers

    def _build_headers(self, headers, token):
        if token:
            headers['X-Auth-Token'] = token
        return headers
