# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class DirectoriesCommand(RESTCommand):

    resource = 'directories'

    def lookup(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/lookup/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def reverse(self, profile, xivo_user_uuid, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/reverse/{profile}/{xivo_user_uuid}'.format(
            base_url=self.base_url,
            profile=profile,
            xivo_user_uuid=xivo_user_uuid,
        )
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def headers(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/lookup/{profile}/headers'.format(base_url=self.base_url, profile=profile)
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def favorites(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/favorites/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def new_favorite(self, directory, contact, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/favorites/{directory}/{contact}'.format(
            base_url=self.base_url,
            directory=directory,
            contact=contact,
        )
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.put(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def remove_favorite(self, directory, contact, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/favorites/{directory}/{contact}'.format(
            base_url=self.base_url,
            directory=directory,
            contact=contact,
        )
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.delete(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def personal(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/personal/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self._build_headers(token, tenant_uuid)

        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def _build_headers(self, token, tenant_uuid):
        headers = {'Accept': 'application/json'}
        if token:
            headers['X-Auth-Token'] = token

        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        return headers
