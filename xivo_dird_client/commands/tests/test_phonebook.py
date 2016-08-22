# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
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

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from hamcrest import assert_that, equal_to, none
from mock import sentinel as s

from ..phonebook import PhonebookCommand


class TestPhonebookContact(RESTCommandTestCase):

    Command = PhonebookCommand

    def setUp(self):
        super(TestPhonebookContact, self).setUp()
        self.tenant = 'atenant'
        self.phonebook_id = 42

    def test_create(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})
        contact_body = {'firstname': 'Foo', 'lastname': 'Bar'}

        result = self.command.create_contact(tenant=self.tenant,
                                             phonebook_id=self.phonebook_id,
                                             token=s.token, contact_body=contact_body)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}/contacts'.format(base_url=self.base_url,
                                                                              tenant=self.tenant,
                                                                              phonebook_id=self.phonebook_id)
        self.session.post.assert_called_once_with(
            url,
            data=json.dumps(contact_body),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_create_when_not_201(self):
        self.session.post.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.create,
                                   phonebook_body={},
                                   tenant=self.tenant,
                                   token=s.token)

    def test_list(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list_contacts(tenant=self.tenant,
                                            token=s.token,
                                            phonebook_id=self.phonebook_id)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}/contacts'.format(base_url=self.base_url,
                                                                              tenant=self.tenant,
                                                                              phonebook_id=self.phonebook_id)
        self.session.get.assert_called_once_with(url, params={}, headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_list_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.list_contacts, token=s.token,
                                   tenant=self.tenant, phonebook_id=self.phonebook_id)

    def test_get(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get_contact(token=s.token,
                                          tenant=self.tenant,
                                          phonebook_id=self.phonebook_id,
                                          contact_uuid=s.contact_uuid)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}/contacts/{contact_uuid}'
        url = url.format(base_url=self.base_url,
                         tenant=self.tenant,
                         phonebook_id=self.phonebook_id,
                         contact_uuid=s.contact_uuid)
        self.session.get.assert_called_once_with(url, params={}, headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.get_contact,
                                   token=s.token,
                                   tenant=self.tenant,
                                   phonebook_id=self.phonebook_id,
                                   contact_uuid=s.contact_uuid)

    def test_edit(self):
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})
        body = {'firstname': 'test'}

        result = self.command.edit_contact(tenant=self.tenant,
                                           phonebook_id=self.phonebook_id,
                                           contact_uuid=s.contact_uuid,
                                           contact_body=body,
                                           token=s.token)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}/contacts/{contact_uuid}'
        url = url.format(base_url=self.base_url,
                         tenant=self.tenant,
                         phonebook_id=self.phonebook_id,
                         contact_uuid=s.contact_uuid)

        self.session.put.assert_called_once_with(
            url,
            data=json.dumps(body),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_edit_when_not_200(self):
        self.session.put.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.edit_contact)

    def test_delete(self):
        self.session.delete.return_value = self.new_response(204)

        result = self.command.delete_contact(tenant=self.tenant,
                                             phonebook_id=self.phonebook_id,
                                             contact_uuid=s.contact_uuid,
                                             token=s.token)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}/contacts/{contact_uuid}'
        url = url.format(base_url=self.base_url,
                         tenant=self.tenant,
                         phonebook_id=self.phonebook_id,
                         contact_uuid=s.contact_uuid)
        self.session.delete.assert_called_once_with(
            url,
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_delete_when_not_204(self):
        self.session.delete.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.delete, token=s.token, tenant=s.tenant,
                                   phonebook_id=s.phonebook_id)


class TestPhonebook(RESTCommandTestCase):

    Command = PhonebookCommand

    def test_create(self):
        self.session.post.return_value = self.new_response(201, json={'return': 'value'})
        phonebook_body = {'name': 'main', 'description': 'The main phonebook'}
        tenant = 'mytenant'

        result = self.command.create(tenant=tenant, token=s.token, phonebook_body=phonebook_body)

        url = '{base_url}/mytenant/phonebooks'.format(base_url=self.base_url)
        self.session.post.assert_called_once_with(
            url,
            data=json.dumps(phonebook_body),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_create_when_not_201(self):
        self.session.post.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.create, phonebook_body={'name': 'main'},
                                   tenant='thetenant', token=s.token)

    def test_list_phonebook(self):
        tenant = 'mytenant'
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.list(tenant=tenant, token=s.token)

        url = '{base_url}/mytenant/phonebooks'.format(base_url=self.base_url)
        self._assert_get(url=url, token=s.token)
        assert_that(result, equal_to({'return': 'value'}))

    def test_list_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.list, s.token, 'mytenant')

    def test_get(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        tenant, phonebook_id = 'atenant', 42

        result = self.command.get(token=s.token, tenant=tenant, phonebook_id=phonebook_id)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}'.format(base_url=self.base_url,
                                                                     tenant=tenant,
                                                                     phonebook_id=phonebook_id)
        self._assert_get(url, s.token)
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_when_not_200(self):
        self.session.get.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.get, token=s.token, tenant='mytenant', phonebook_id=42)

    def test_edit(self):
        self.session.put.return_value = self.new_response(200, json={'return': 'value'})
        tenant = 'thetenant'
        phonebook_id = 'my_contact_id'
        body = {'name': 'test'}

        result = self.command.edit(tenant=tenant, phonebook_id=phonebook_id,
                                   phonebook_body=body, token=s.token)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}'.format(base_url=self.base_url,
                                                                     tenant=tenant,
                                                                     phonebook_id=phonebook_id)
        self.session.put.assert_called_once_with(
            url,
            data=json.dumps(body),
            params={},
            headers={'X-Auth-Token': s.token,
                     'Content-Type': 'application/json'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_edit_when_not_200(self):
        self.session.put.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.edit, tenant=s.tenant, phonebook_body={}, token=s.token)

    def test_delete(self):
        self.session.delete.return_value = self.new_response(204)
        phonebook_id, tenant = 'my_phonebook_id', 'zetenant'

        result = self.command.delete(tenant=tenant, phonebook_id=phonebook_id, token=s.token)

        url = '{base_url}/{tenant}/phonebooks/{phonebook_id}'.format(base_url=self.base_url,
                                                                     tenant=tenant,
                                                                     phonebook_id=phonebook_id)
        self.session.delete.assert_called_once_with(
            url,
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_delete_when_not_204(self):
        self.session.delete.return_value = self.new_response(401)

        self.assertRaisesHTTPError(self.command.delete, token=s.token, tenant=s.tenant,
                                   phonebook_id=s.phonebook_id)

    def _assert_get(self, url, token):
        self.session.get.assert_called_once_with(
            url, params={}, headers={'X-Auth-Token': token})
