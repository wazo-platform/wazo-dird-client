# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

import json

from xivo_lib_rest_client import RESTCommand


class PersonalCommand(RESTCommand):

    resource = 'personal'

    def list(self, token=None, **kwargs):
        headers = {'X-Auth-Token': token}
        r = self.session.get(self.base_url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def purge(self, token=None, **kwargs):
        headers = {'X-Auth-Token': token}
        r = self.session.delete(self.base_url, params=kwargs, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def export_csv(self, token=None, **kwargs):
        headers = {'X-Auth-Token': token}
        kwargs['format'] = 'text/csv'
        r = self.session.get(self.base_url, params=kwargs, headers=headers)

        if r.status_code == 200:
            return r.text

        if r.status_code == 204:
            return None

        self.raise_from_response(r)

    def get(self, contact_id, token=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                               contact_id=contact_id)

        headers = {'X-Auth-Token': token}
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def import_csv(self, csv_text, encoding=None, token=None, **kwargs):
        url = '{base_url}/import'.format(base_url=self.base_url)

        content_type = 'text/csv; charset={}'.format(encoding) if encoding else 'text/csv'
        headers = {'Content-Type': content_type,
                   'X-Auth-Token': token}
        r = self.session.post(url, data=csv_text, params=kwargs, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def create(self, contact_infos, token=None, **kwargs):
        headers = {'Content-Type': 'application/json',
                   'X-Auth-Token': token}
        r = self.session.post(self.base_url, data=json.dumps(contact_infos), params=kwargs, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def edit(self, contact_id, contact_infos, token=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                               contact_id=contact_id)

        headers = {'Content-Type': 'application/json',
                   'X-Auth-Token': token}
        r = self.session.put(url, data=json.dumps(contact_infos), params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete(self, contact_id, token=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                               contact_id=contact_id)

        headers = {'X-Auth-Token': token}
        r = self.session.delete(url, params=kwargs, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)
