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

from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import none
from mock import sentinel as s

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..directories import DirectoriesCommand


class TestDirectories(RESTCommandTestCase):

    Command = DirectoriesCommand

    def test_lookup(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.lookup(profile='default', term='Alice', token=s.token)

        self.session.get.assert_called_once_with(
            '{base_url}/lookup/default'.format(base_url=self.base_url),
            params={'term': 'Alice'},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_lookup_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.headers, profile='my_profile')

    def test_headers(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.headers(profile='default', token=s.token)

        self.session.get.assert_called_once_with(
            '{base_url}/lookup/default/headers'.format(base_url=self.base_url),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_headers_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.headers, profile='my_profile')

    def test_favorites(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.favorites(profile='default', token=s.token)

        self.session.get.assert_called_once_with(
            '{base_url}/favorites/default'.format(base_url=self.base_url),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_favorites_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.favorites, profile='my_profile')

    def test_new_favorite(self):
        self.session.put.return_value = self.new_response(204)

        result = self.command.new_favorite('my_directory', 'my_contact', token=s.token)

        self.session.put.assert_called_once_with(
            '{base_url}/favorites/my_directory/my_contact'.format(base_url=self.base_url),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_new_favorite_when_not_204(self):
        self.session.put.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.new_favorite, 'my_directory', 'my_contact')

    def test_remove_favorite(self):
        self.session.delete.return_value = self.new_response(204)

        result = self.command.remove_favorite('my_directory', 'my_contact', token=s.token)

        self.session.delete.assert_called_once_with(
            '{base_url}/favorites/my_directory/my_contact'.format(base_url=self.base_url),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, none())

    def test_remove_favorite_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.remove_favorite, 'my_directory', 'my_contact')

    def test_personal(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.personal(profile='default', token=s.token)

        self.session.get.assert_called_once_with(
            '{base_url}/personal/default'.format(base_url=self.base_url),
            params={},
            headers={'X-Auth-Token': s.token})
        assert_that(result, equal_to({'return': 'value'}))

    def test_personal_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.personal, profile='my_profile')
