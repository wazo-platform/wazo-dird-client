# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import RESTCommand


class BackendsCommand(RESTCommand):

    resource = 'backends'
    _ro_headers = {'Accept': 'application/json'}

    def list(self, token=None, **kwargs):
        r = self.session.get(self.base_url, params=kwargs, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()
