# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
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


class PrivatesCommand(RESTCommand):

    resource = 'privates'

    def list(self, token=None, **kwargs):
        url = '{base_url}'.format(base_url=self.base_url)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def create(self, contact_infos, token=None, **kwargs):
        url = '{base_url}'.format(base_url=self.base_url)

        headers = {'Content-Type': 'application/json'}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.post(url, data=json.dumps(contact_infos), params=kwargs, headers=headers)

        if r.status_code != 201:
            self.raise_from_response(r)

        return r.json()

    def delete(self, contact_id, token=None, **kwargs):
        url = '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                               contact_id=contact_id)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.delete(url, params=kwargs, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)
