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

from xivo_lib_rest_client import RESTCommand


class DirectoriesCommand(RESTCommand):

    resource = 'directories'

    def lookup(self, profile, token=None, **kwargs):
        url = '{base_url}/lookup/{profile}'.format(base_url=self.base_url,
                                                   profile=profile)
        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def headers(self, profile, token=None, **kwargs):
        url = '{base_url}/lookup/{profile}/headers'.format(base_url=self.base_url,
                                                           profile=profile)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def favorites(self, profile, token=None, **kwargs):
        url = '{base_url}/favorites/{profile}'.format(base_url=self.base_url,
                                                      profile=profile)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def new_favorite(self, directory, contact, token=None, **kwargs):
        url = '{base_url}/favorites/{directory}/{contact}'.format(base_url=self.base_url,
                                                                  directory=directory,
                                                                  contact=contact)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.put(url, params=kwargs, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def remove_favorite(self, directory, contact, token=None, **kwargs):
        url = '{base_url}/favorites/{directory}/{contact}'.format(base_url=self.base_url,
                                                                  directory=directory,
                                                                  contact=contact)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.delete(url, params=kwargs, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)
