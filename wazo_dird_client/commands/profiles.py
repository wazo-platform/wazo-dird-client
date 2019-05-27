# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers import DirdRESTCommand


class ProfilesCommand(DirdRESTCommand):

    resource = 'profiles'

    def create(self, body, tenant_uuid=None, token=None):
        headers = self.build_rw_headers(tenant_uuid, token)
        r = self.session.post(self.base_url, json=body, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, profile_uuid, tenant_uuid=None, token=None):
        headers = self.build_ro_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, profile_uuid])
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def edit(self, profile_uuid, body, tenant_uuid=None, token=None):
        headers = self.build_rw_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, profile_uuid])
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)

    def get(self, profile_uuid, tenant_uuid=None, token=None):
        headers = self.build_ro_headers(tenant_uuid, token)
        url = '/'.join([self.base_url, profile_uuid])
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, token=None, **kwargs):
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        self.raise_from_response(r)
        return r.json()
