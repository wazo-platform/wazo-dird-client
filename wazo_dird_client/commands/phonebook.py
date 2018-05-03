# -*- coding: utf-8 -*-
# Copyright (C) 2016 Avencall
# SPDX-License-Identifier: GPL-3.0+

import json

from xivo_lib_rest_client import RESTCommand


class PhonebookCommand(RESTCommand):

    resource = 'tenants'

    def create(self, token=None, tenant=None, phonebook_body=None, **kwargs):
        url = self._phonebook_all_url(tenant)
        headers = self._new_headers(token, content_type='application/json')

        r = self.session.post(url, data=json.dumps(phonebook_body), params=kwargs, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def create_contact(self, token=None, tenant=None, phonebook_id=None, contact_body=None, **kwargs):
        url = self._contact_all_url(tenant, phonebook_id)
        headers = self._new_headers(token, content_type='application/json')

        r = self.session.post(url, data=json.dumps(contact_body), params=kwargs, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def list(self, token=None, tenant=None, **kwargs):
        url = self._phonebook_all_url(tenant)
        headers = self._new_headers(token)
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_contacts(self, token=None, tenant=None, phonebook_id=None, **kwargs):
        url = self._contact_all_url(tenant, phonebook_id)
        headers = self._new_headers(token)

        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete(self, token=None, tenant=None, phonebook_id=None, **kwargs):
        url = self._phonebook_one_url(tenant, phonebook_id)
        headers = self._new_headers(token)

        r = self.session.delete(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def edit(self, token=None, tenant=None, phonebook_id=None, phonebook_body=None, **kwargs):
        url = self._phonebook_one_url(tenant, phonebook_id)
        headers = self._new_headers(token, 'application/json')

        r = self.session.put(url, data=json.dumps(phonebook_body), params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get(self, token=None, tenant=None, phonebook_id=None, **kwargs):
        url = self._phonebook_one_url(tenant, phonebook_id)
        headers = self._new_headers(token)
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get_contact(self, token=None, tenant=None, phonebook_id=None, contact_uuid=None, **kwargs):
        url = self._contact_one_url(tenant, phonebook_id, contact_uuid)
        headers = self._new_headers(token)

        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def edit_contact(self, token=None, tenant=None, phonebook_id=None,
                     contact_uuid=None, contact_body=None, **kwargs):
        url = self._contact_one_url(tenant, phonebook_id, contact_uuid)
        headers = self._new_headers(token, content_type='application/json')

        r = self.session.put(url, data=json.dumps(contact_body), params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_contact(self, token=None, tenant=None, phonebook_id=None, contact_uuid=None, **kwargs):
        url = self._contact_one_url(tenant, phonebook_id, contact_uuid)
        headers = self._new_headers(token)

        r = self.session.delete(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def import_csv(self, tenant=None, phonebook_id=None, csv_text=None, encoding=None, token=None, **kwargs):
        url = self._contact_import_url(tenant, phonebook_id)

        content_type = 'text/csv; charset={}'.format(encoding) if encoding else 'text/csv'
        headers = {'Content-Type': content_type,
                   'X-Auth-Token': token}
        r = self.session.post(url, data=csv_text, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def _contact_all_url(self, tenant, phonebook_id):
        return '{}/{}'.format(self._phonebook_one_url(tenant, phonebook_id), 'contacts')

    def _contact_one_url(self, tenant, phonebook_id, contact_uuid):
        return '{}/{}'.format(self._contact_all_url(tenant, phonebook_id), contact_uuid)

    def _contact_import_url(self, tenant, phonebook_id):
        return '{}/import'.format(self._contact_all_url(tenant, phonebook_id))

    def _phonebook_all_url(self, tenant):
        return '{base_url}/{tenant}/phonebooks'.format(base_url=self.base_url,
                                                       tenant=tenant)

    def _phonebook_one_url(self, tenant, phonebook_id):
        return '{}/{}'.format(self._phonebook_all_url(tenant), phonebook_id)

    @staticmethod
    def _new_headers(token, content_type=None):
        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        if content_type:
            headers['Content-Type'] = content_type
        return headers
