# Copyright 2020-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base_command import DirdRESTCommand


class GraphQLCommand(DirdRESTCommand):

    resource = 'graphql'

    def query(self, query, token=None, tenant_uuid=None):
        headers = self.build_headers(tenant_uuid, token)
        r = self.session.post(self.base_url, json=query, headers=headers)
        self.raise_from_response(r)
        return r.json()
