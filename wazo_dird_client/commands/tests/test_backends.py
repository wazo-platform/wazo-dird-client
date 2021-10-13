# -*- coding: utf-8 -*-
# Copyright 2019-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, equal_to

from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..backends import BackendsCommand


class TestBackends(RESTCommandTestCase):

    Command = BackendsCommand

    def test_list_contacts_from_source(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_contacts_from_source(
            backend='wazo', source_uuid='source-uuid', uuids=['uuid1', 'uuid2']
        )

        self.session.get.assert_called_once_with(
            'backends/wazo/sources/source-uuid/contacts',
            params={'uuid': 'uuid1,uuid2'},
            headers={'Accept': 'application/json'},
        )
        assert_that(result, equal_to({'return': 'value'}))
