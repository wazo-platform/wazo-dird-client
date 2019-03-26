# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand

class DisplaysCommand(RESTCommand):

    resource = 'displays'
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    _ro_headers = {'Accept': 'application/json'}

    def create(self, body, tenant_uuid=None):
        headers = dict(self._rw_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        r = self.session.post(self.base_url, json=body, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, display_uuid, tenant_uuid=None):
        headers = dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = '/'.join([self.base_url, display_uuid])
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def edit(self, display_uuid, body, tenant_uuid=None):
        headers = dict(self._rw_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = '/'.join([self.base_url, display_uuid])
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)

    def get(self, display_uuid, tenant_uuid=None):
        headers = dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = '/'.join([self.base_url, display_uuid])
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, **kwargs):
        headers = dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        self.raise_from_response(r)
        return r.json()
