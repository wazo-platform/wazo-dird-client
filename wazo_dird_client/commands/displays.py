# Copyright 2019-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_command import DirdRESTCommand


class DisplaysCommand(DirdRESTCommand):
    resource = 'displays'

    def create(self, body, tenant_uuid=None, token=None):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.post(self.base_url, json=body, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, display_uuid, tenant_uuid=None, token=None):
        headers = self.build_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, display_uuid])
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def edit(self, display_uuid, body, tenant_uuid=None, token=None):
        headers = self.build_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, display_uuid])
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)

    def get(self, display_uuid, tenant_uuid=None, token=None):
        headers = self.build_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, display_uuid])
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, token=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        self.raise_from_response(r)
        return r.json()
