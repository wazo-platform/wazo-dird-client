# -*- coding: utf-8 -*-
# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class BackendsCommand(RESTCommand):

    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    resource = 'backends'

    def create_source(self, backend, body, tenant_uuid=None):
        url = self._build_base_url(backend)

        headers = dict(self._rw_headers)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        r = self.session.post(url, headers=headers, json=body)
        self.raise_from_response(r)

        return r.json()

    def delete_source(self, backend, source_uuid):
        url = self._build_url(backend, source_uuid)

        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def edit_source(self, backend, source_uuid, body):
        url = self._build_url(backend, source_uuid)

        r = self.session.put(url, headers=self._rw_headers, json=body)
        self.raise_from_response(r)

    def get_source(self, backend, source_uuid):
        url = self._build_url(backend, source_uuid)

        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)

        return r.json()

    def list(self, token=None, **kwargs):
        r = self.session.get(self.base_url, params=kwargs, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def list_sources(self, backend, **kwargs):
        url = self._build_base_url(backend)

        r = self.session.get(url, headers=self._ro_headers, params=kwargs)
        self.raise_from_response(r)

        return r.json()

    def list_contacts_from_source(self, backend, source_uuid, tenant_uuid=None, **kwargs):
        url = self._build_url(backend, source_uuid, 'contacts')
        header = self._ro_headers

        if tenant_uuid:
            header['Wazo-Tenant'] = tenant_uuid


        r = self.session.get(url, headers=headers, params=kwargs)
        self.raise_from_response(r)

        return r.json()

    def _build_base_url(self, backend):
        return '/'.join([self.base_url, backend, 'sources'])

    def _build_url(self, backend, source_uuid, *args):
        return '/'.join([self.base_url, backend, 'sources', source_uuid] + list(args))
