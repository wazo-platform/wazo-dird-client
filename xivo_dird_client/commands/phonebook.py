# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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

    def list(self, token=None, tenant=None, **kwargs):
        url = self._phonebook_all_url(tenant)
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

    def _phonebook_all_url(self, tenant):
        return '{base_url}/{tenant}/phonebooks'.format(base_url=self.base_url,
                                                       tenant=tenant)

    def _phonebook_one_url(self, tenant, phonebook_id):
        return '{base_url}/{tenant}/phonebooks/{phonebook_id}'.format(base_url=self.base_url,
                                                                      tenant=tenant,
                                                                      phonebook_id=phonebook_id)

    @staticmethod
    def _new_headers(token, content_type=None):
        headers = {'X-Auth-Token': token}
        if content_type:
            headers['Content-Type'] = content_type
        return headers
