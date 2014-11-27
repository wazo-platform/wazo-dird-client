# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
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

from ..directories import DirectoriesCommand
from hamcrest import assert_that
from hamcrest import equal_to
from xivo_lib_rest_client.tests.command import HTTPCommandTestCase


class TestDirectories(HTTPCommandTestCase):

    Command = DirectoriesCommand

    def test_lookup(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.lookup(profile='default', term='Alice')

        self.session.get.assert_called_once_with(
            '{base_url}/lookup/default'.format(base_url=self.base_url),
            params={'term': 'Alice'})
        assert_that(result, equal_to({'return': 'value'}))

    def test_lookup_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.headers, profile='my_profile')

    def test_headers(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.headers(profile='default')

        self.session.get.assert_called_once_with(
            '{base_url}/lookup/default/headers'.format(base_url=self.base_url),
            params={})
        assert_that(result, equal_to({'return': 'value'}))

    def test_headers_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.headers, profile='my_profile')
