# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_dird_client.commands.helpers.base_command import DirdRESTCommand


class DirectoriesCommand(DirdRESTCommand):

    resource = 'directories'

    def lookup(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/lookup/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def lookup_user(self, profile, xivo_user_uuid, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/lookup/{profile}/{xivo_user_uuid}'.format(
            base_url=self.base_url,
            profile=profile,
            xivo_user_uuid=xivo_user_uuid,
        )
        headers = self.build_ro_headers(tenant_uuid, token)
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
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def headers(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/lookup/{profile}/headers'.format(base_url=self.base_url, profile=profile)
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def favorites(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/favorites/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self.build_ro_headers(tenant_uuid, token)
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
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.put(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def remove_favorite(self, directory, contact, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/favorites/{directory}/{contact}'.format(
            base_url=self.base_url,
            directory=directory,
            contact=contact,
        )
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.delete(url, params=kwargs, headers=headers)
        if r.status_code != 204:
            self.raise_from_response(r)

    def personal(self, profile, token=None, tenant_uuid=None, **kwargs):
        url = '{base_url}/personal/{profile}'.format(base_url=self.base_url, profile=profile)
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(url, params=kwargs, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_sources(self, profile, token=None, tenant_uuid=None, **list_params):
        url = '{base_url}/{profile}/sources'.format(
            base_url=self.base_url,
            profile=profile,
        )
        headers = self.build_ro_headers(tenant_uuid, token)
        r = self.session.get(url, params=list_params, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
