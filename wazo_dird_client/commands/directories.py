# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

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

    def reverse(self, profile, xivo_user_uuid, token=None, **kwargs):
        url = '{base_url}/reverse/{profile}/{xivo_user_uuid}'.format(base_url=self.base_url,
                                                                     profile=profile,
                                                                     xivo_user_uuid=xivo_user_uuid)
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

    def personal(self, profile, token=None, **kwargs):
        url = '{base_url}/personal/{profile}'.format(base_url=self.base_url,
                                                     profile=profile)

        headers = {}
        if token:
            headers['X-Auth-Token'] = token
        r = self.session.get(url, params=kwargs, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
