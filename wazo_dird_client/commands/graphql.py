# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base_command import DirdRESTCommand


class GraphQLCommand(DirdRESTCommand):
    def query(self, query, tenant_uuid, token):
        headers = self.build_rw_headers(tenant_uuid, token)
        url = self._client.url('graphql')
        r = self.session.post(url, json=query, headers=headers)
        self.raise_from_response(r)
        return r.json()
