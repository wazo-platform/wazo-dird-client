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

from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import is_
from hamcrest import none
from mock import sentinel as s

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..personal import PersonalCommand


class TestPersonal(RESTCommandTestCase):

    Command = PersonalCommand

    def test_list(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list(token=s.token)

        self.session.get.assert_called_once_with(
            self.base_url,
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_purge(self):
        self.session.delete.return_value = self.new_response(204)

        result = self.command.purge(token=s.token)

        self.session.delete.assert_called_once_with(
            self.base_url,
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_list_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.list, s.token)

    def test_export_csv(self):
        csv = 'firstname\r\nAlice'
        self.session.get.return_value = self.new_response(200, body=csv)

        result = self.command.export_csv(token=s.token)

        self.session.get.assert_called_once_with(
            self.base_url,
            params={'format': 'text/csv'},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to(csv))

    def test_export_csv_when_empty(self):
        self.session.get.return_value = self.new_response(204)

        result = self.command.export_csv(token=s.token)

        assert_that(result, is_(none()))

    def test_export_csv_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.export_csv, s.token)

    def test_get(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})
        contact_id = 'my_contact_id'

        result = self.command.get(contact_id, token=s.token)

        self.session.get.assert_called_once_with(
            '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                             contact_id=contact_id),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.get, 'my_contact_id', s.token)

    def test_import_csv(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})
        csv = 'firstname,lastname\ndaniel,martini'

        result = self.command.import_csv(csv, encoding='cp1252', token=s.token)

        self.session.post.assert_called_once_with(
            '{base_url}/import'.format(base_url=self.base_url),
            data=csv,
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'text/csv; charset=cp1252'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_import_csv_when_not_201(self):
        self.session.post.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.import_csv, 'firstname,lastname\ndaniel,martini')

    def test_create(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})
        contact = {'firstname': 'Alice'}

        result = self.command.create(contact, token=s.token)

        self.session.post.assert_called_once_with(
            self.base_url,
            data=json.dumps(contact),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_create_when_not_201(self):
        self.session.post.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.create, {'firstname': 'Alice'}, s.token)

    def test_edit(self):
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})
        contact_id = 'my_contact_id'
        contact = {'firstname': 'Alice'}

        result = self.command.edit(contact_id, contact, token=s.token)

        self.session.put.assert_called_once_with(
            '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                             contact_id=contact_id),
            data=json.dumps(contact),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_edit_when_not_200(self):
        self.session.put.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.edit, 'my_contact_id', {'firstname': 'Alice'}, s.token)

    def test_delete(self):
        self.session.delete.return_value = self.new_response(204)
        contact_id = 'my_contact_id'

        result = self.command.delete(contact_id, token=s.token)

        self.session.delete.assert_called_once_with(
            '{base_url}/{contact_id}'.format(base_url=self.base_url,
                                             contact_id=contact_id),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_delete_when_not_201(self):
        self.session.delete.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.delete, {'firstname': 'Alice'}, s.token)