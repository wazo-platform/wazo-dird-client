# -*- coding: utf-8 -*-
# Copyright 2014-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_command import DirdRESTCommand


class PersonalCommand(DirdRESTCommand):

    resource = 'personal'

    def list(self, token=None, tenant_uuid=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.get(self.base_url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def purge(self, token=None, tenant_uuid=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.delete(self.base_url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def export_csv(self, token=None, tenant_uuid=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        del headers['Accept']
        kwargs['format'] = 'text/csv'
        r = self.session.get(self.base_url, params=kwargs, headers=headers)

        if r.status_code == 200:
            return r.text

        if r.status_code == 204:
            return None

        self.raise_from_response(r)

    def get(self, contact_id, token=None, tenant_uuid=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                               contact_id=contact_id)
        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def import_csv(self, csv_text, encoding=None, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/import'.format(base_url=self.base_url)
        headers = self.build_headers(tenant_uuid, token)
        content_type = 'text/csv; charset={}'.format(encoding) if encoding else 'text/csv'
        headers['Content-Type'] = content_type
        r = self.session.post(url, data=csv_text, params=kwargs, headers=headers)
        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def create(self, contact_infos, token=None, tenant_uuid=None, **kwargs):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.post(self.base_url, json=contact_infos, params=kwargs, headers=headers)
        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def edit(self, contact_id, contact_infos, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url, contact_id=contact_id)
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.put(url, json=contact_infos, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete(self, contact_id, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url, contact_id=contact_id)
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.delete(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)
